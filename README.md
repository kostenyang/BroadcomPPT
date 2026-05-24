# BroadcomPPT — VMware by Broadcom 簡報技能套件

本 Repo 存放 Kosten Yang 專屬的 Claude Skill 套件，用於快速產生 Broadcom VCF 技術簡報。

## 官方範本

請將以下兩個範本 `.pptx` 上傳至本 Repo 根目錄：

- `VCF_5_2_Master_Technical_-_BC04.pptx` — VCF 5.2 深度技術範本
- `APJ__Tech__Upgrade_Pathways_to_VCF_9_1-Slides.pptx` — VCF 9.1 升級路徑範本

## Skill 套件

| Skill | 說明 | 適用情境 |
|-------|------|---------|
| `broadcom-ppt-base` | 共用基礎 (顏色/字體/Layout) | 所有垂直 skill 共用 |
| `vcf-semiconductor` | 半導體/晶圓廠 | TSMC、聯發科、VSMC、OA/MES |
| `vcf-financial` | 金融業 | CTBC、國泰世華、中信、富邦 |
| `vcf-telecom` | 電信/VCSP | CHT、OpenStack 遷移、VCD |
| `vcf-hybrid-cloud` | 混合雲/多站點 | GCVE、HCX、內雲/外雲/公雲 |
| `vcf-ai` | AI 基礎架構 | Private AI、GPU、VKS、GenAI |

## 目錄結構

```
BroadcomPPT/
├── skills/              # Skill 原始檔 (SKILL.md)
│   ├── broadcom-ppt-base/
│   ├── vcf-semiconductor/
│   ├── vcf-financial/
│   ├── vcf-telecom/
│   ├── vcf-hybrid-cloud/
│   └── vcf-ai/
└── skills-pkg/          # 打包好的 .skill 安裝檔
    ├── broadcom-ppt-base.skill
    ├── vcf-semiconductor.skill
    ├── vcf-financial.skill
    ├── vcf-telecom.skill
    ├── vcf-hybrid-cloud.skill
    └── vcf-ai.skill
```

## 使用方式

下載 `skills-pkg/` 下的 `.skill` 檔，安裝到 Claude 後即可使用。

觸發範例：
- 「幫我做一份給 CTBC 的 VCF 升級提案」→ `vcf-financial`
- 「CHT OpenStack 遷移簡報」→ `vcf-telecom`
- 「VSMC 半導體客戶架構提案」→ `vcf-semiconductor`
- 「混合雲 GCVE + HCX 簡報」→ `vcf-hybrid-cloud`
- 「Private AI 基礎架構簡報」→ `vcf-ai`
