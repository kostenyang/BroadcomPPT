---
name: lab-env
description: Lab 環境事實的單一來源 — 主機、IP、FQDN、DNS、憑證來源該去哪裡查、怎麼驗、怎麼帶進工作狀態。務必在下列情況觸發：(1) 任何 lab 環境的部署 / 組態 / 升級 / 除錯任務開始前（VCF、vCenter、NSX、vSAN、ESXi、SDDC Manager、VCF Installer、VCF Operations、VCF Automation）；(2) 需要用到任何 lab 的主機名 / IP / FQDN / VLAN / 網段 / port group / datastore 名稱；(3) 使用者提到 lab、實驗室、測試環境、POC 環境、demo 環境、nested 環境、我的環境、那台 vCenter；(4) 要寫任何含環境資訊的交付文件、組態檔、IP 規劃表、firewall port table；(5) 部署失敗要查原因，特別是憑證 / bring-up / 註冊類錯誤。核心規則：絕不憑印象填 IP 或 FQDN — 查不到就停下來問。
---

# Lab Environment — 環境事實的單一來源

## 最重要的一條（其他都可以忘，這條不行）

> **絕不憑印象填 IP / FQDN / 主機名 / 網段。查不到就停下來問使用者。**

理由不是潔癖：

- 使用者有**多套** lab，環境之間長得很像，記錯一碼不會報錯，會靜默跑到錯的機器上
- lab 資料會變（重建、換網段、搬站台），對話裡或舊 session 印象中的值是過期的
- 這些值會被抄進**客戶交付文件**（IP 規劃表、firewall port table、as-built）。編出來的 IP 進到交付物是最貴的一種錯

「我記得上次是 10.x.x.x」＝ 已經錯了。停下來問。

---

## 這個 skill 不存任何環境資料

本 skill 只定義**怎麼讀、怎麼驗、怎麼帶進工作狀態**。實際的主機清單住在檔案裡：

| 檔案 | 內容 | 進版控？ |
|---|---|---|
| `lab-info.md` | 主機清單、IP、角色、版本、網段、VLAN、datastore、**憑證的來源指標** | ✅ 可以 |
| `dns-records.md` | 正解 / 反解記錄、DNS server、search domain | ✅ 可以 |
| credential 本體 | 密碼、API key、license key | ❌ **絕不**進版控、絕不進 skill、絕不進對話 |

範本在 `assets/lab-info.md`、`assets/dns-records.md`。

原因：skill 是**全域**的（`~/.claude/skills/`），lab 是**每套環境不同**的。把 IP 寫進 SKILL.md，等於讓 A 環境的資料污染 B 專案，而且改一次要動 skill 庫。

---

## 模式一：READ（動任何 lab 之前）

1. **找 `lab-info.md`**，依序：專案根目錄 → `dev-docs/` → 使用者慣用位置。
2. **讀 `dns-records.md`**。
3. **抄進 `dev-docs/context.md` 的「關鍵資源」表**（銜接 `session-state` skill）—— 只抄這次任務**真的會用到**的那幾筆，不要整份貼。壓縮後這張表會留下，原始檔不必重讀。
4. **檔案不存在 → 停。** 跟使用者要，不要自己編、不要從舊 session 印象填、不要用 `192.168.1.x` 這種佔位值繼續往下做。

抄進 `context.md` 的格式：

```
| 項目 | 值 | 來源 |
|---|---|---|
| vCenter FQDN | vcsa01.lab.local | lab-info.md |
| NSX Manager VIP | 10.x.x.x | lab-info.md |
| vCenter 帳密 | 見 lab-info.md（不抄值） | — |
```

---

## 模式二：PREFLIGHT（VCF 部署 / 升級動手前）

**DNS 正反解一致 + NTP 同步 —— 這兩個是 VCF 部署失敗的頭號原因**，而且症狀會誤導人。

VMCA 憑證安裝失敗、SDDC Manager bring-up 失敗、元件註冊失敗，第一直覺都是去查憑證或服務本身，實際 root cause 往往是 DNS 反解缺一筆或 NTP 偏移。**先排除這兩個再往下查**，可以省掉數小時。

```bash
bash scripts/preflight.sh <hosts-file>
```

或手動，每台都要正反解對得起來：

```bash
nslookup vcsa01.lab.local        # 正解 → IP
nslookup 10.x.x.x                # 反解 → 必須回到同一個 FQDN
ntpq -p                          # 或 chronyc sources / w32tm /query /status
```

判讀：

| 現象 | 意義 |
|---|---|
| 正解通、反解無回應或指到別的名字 | ❌ 擋 VCF，先修 DNS |
| FQDN 大小寫或 domain 與 `lab-info.md` 不一致 | ❌ 擋 VCF |
| NTP offset 過大或 unsynchronised | ❌ 擋憑證流程 |

**不要**因為「ping 得到」就判定 DNS 沒問題 —— ping 只驗正解。

---

## 模式三：CONFIRM（破壞性操作之前）

重建、刪 cluster、改網路、重啟服務、套用組態之前，**先講出你要動的是哪一台**，讓使用者有機會攔：

```
即將在 <vCenter FQDN / cluster 名稱> 執行 <動作>，影響 <對象>。
來源：lab-info.md 第 N 列。確認？
```

lab 之間長得像，這一步是唯一擋得住「動到另一套環境」的機制。

---

## Credential 邊界

- `lab-info.md` 只寫**憑證來源指標**（例：`vCenter 帳密：見 1Password / lab-secrets，不在此檔`），不寫值
- 狀態檔（`context.md` / `plan.md` / `tasks.md`）**絕不**寫入 credential
- 要求使用者貼密碼進對話之前先想：有沒有別的辦法（ssh key、已存在的 session、他自己執行）
- 交付文件裡的憑證欄位一律留空或寫「另行提供」

---

## 反模式

- **憑印象填 IP** —— 本 skill 存在的唯一理由。
- **整份 `lab-info.md` 貼進對話** —— 只抄用得到的幾筆進 `context.md`，其餘用 `rg` 精準查。
- **用佔位 IP 繼續做** —— `192.168.1.10` 會活到交付文件裡。
- **跳過 preflight 直接部署** —— 然後花三小時查憑證，root cause 是反解少一筆。
- **把環境資料寫進 SKILL.md** —— 全域 skill 污染所有專案。
- **只驗正解就宣告 DNS 沒問題**。
