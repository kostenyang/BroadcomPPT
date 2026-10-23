---
name: vcf-edge
description: Create Broadcom VMware Cloud Foundation (VCF) Edge presentation decks for distributed edge, retail, manufacturing, healthcare, logistics, and edge-AI customers. Trigger whenever the user wants a presentation, proposal, or slide deck about VCF Edge, edge computing, 邊緣運算, 分散式站點, retail/門市, factory/工廠, ROBO (remote office / branch office), edge AI inference, thin edge / single-node / two-node edge, autonomous edge operations, ZTP (zero touch provisioning), VKS at the edge, GitOps/Argo CD edge fleet, NVMe memory tiering, or scaling thousands of edge sites. Also trigger for 邊緣站點大規模部署, air-gapped/disconnected edge, edge GPU/SLM inference (llama.cpp), or any customer running infrastructure outside the core datacenter. Always use the official VCF Edge Customer Presentation template — never create from scratch.
---

# VCF Edge Presentation Skill

Read `broadcom-ppt-base` SKILL.md first for template specs, colors, fonts, and editing workflow.
Location: `/home/claude/broadcom-ppt-skills/broadcom-ppt-base/SKILL.md`

> **⚡ 預設底版**：邊緣主題永遠先用官方 `VCF_Edge_Customer_Presentation.pptx` (42 slides, 白底, VCF Edge 9.1)。
> 若使用者要的是純升級路徑或一般 VCF 平台主題，可改用 `Getting_Started_with_VCF_9_1__Upgrade_Paths__and_What_to_Expect.pptx`。
> 只有使用者明確說「用 5.2 Master」時才改用 97MB 大檔。
> **所有 content slides 以白底 (#FFFFFF) 為主。**

Download base from GitHub:
`https://raw.githubusercontent.com/kostenyang/BroadcomPPT/main/VCF_Edge_Customer_Presentation.pptx`

---

## Industry Context — Why Edge Now

Edge has shifted from a niche topic to a board-level business imperative:
- **50%** of enterprise AI inference workloads will be processed locally on endpoints or edge nodes by 2030 (IDC, Dec 2025).
- **$380 Billion** expected worldwide spending on edge solutions by 2028 (IDC Worldwide Edge Spending Guide, Feb 2026).
- Edge is where data is **created and consumed** — factories, stores, hospitals, substations, logistics hubs — too much latency and bandwidth cost to round-trip everything to the core.

The edge is fundamentally different from the datacenter, and that drives every design choice in the deck:
- **Limited Footprint** — 1U/2U, no raised floor, often a closet or shop floor
- **Lack of Local IT** — no admins on site; everything must be remote / zero-touch
- **Privacy & Security** — physically exposed sites, regulated data staying local
- **Scale (Sites)** — hundreds to thousands of locations, not hundreds of VMs
- **Limited / Unstable Network** — intermittent WAN, must keep running when disconnected

Customer requirements that follow from this:
Consistent infrastructure core-to-edge · Autonomous edge operations · Security & HA · Resilient to network instability · Cloud-native readiness · Cost efficiency.

Typical Taiwan / APJ edge customers:
- **Retail / 零售**: 超商、連鎖門市、量販 — 1000s of stores, POS + loss prevention + in-store AI
- **Manufacturing / 製造**: 工廠 OT/IT 融合, virtual PLC, MES, machine vision (參考 Audi smart factory)
- **Healthcare / 醫療**: 醫院/診所連鎖, imaging at the edge, 2000+ distributed locations
- **Logistics / 物流 & Transportation**: 倉儲、配送中心、port/airport
- **Energy / 能源**: substations, renewable sites, remote monitoring

---

## The Product — VCF Edge 9.1

**Positioning line**: *Scalable Autonomous Edge Platform — AI-Ready Edge. Autonomous Operations. Built-In Security.*

Three pillars (use as section structure):
1. **AI-Ready Edge** — Run VMs, containers, and AI workloads on a single unified platform.
2. **Autonomous Edge Operations** — Operate thousands of edge sites on one platform with zero-touch and lifecycle automation.
3. **Secure and Resilient Edge** — Built-in security & compliance with continuous, resilient operations across every edge site.

Right-sized edge — **1, 2, 3+ nodes to scale** (all patterns require ≥100ms latency tolerance and ≥10 Mbps bandwidth):
- **Single Node**: Minimal footprint — vSphere + VKS on one host
- **Two Node**: HA with vSAN + witness appliance
- **Multi-Cluster (3+ Nodes)**: Full scale-out edge clusters

---

## Recommended Deck Structure

The official template already follows this flow (42 slides). Trim to the customer; keep this skeleton.

### Standard Edge Customer Pitch
1. **Title** — VMware Cloud Foundation Edge — Overview
2. **Agenda** — Edge Opportunity · Today's Challenges · VCF Edge Overview · Use Cases & Customer Stories · Packaging & Licensing
3. **Section: The Edge Opportunity** — IDC stats (50% AI inference at edge by 2030; $380B by 2028)
4. **Section: Today's Challenges** — Limited footprint / no local IT / privacy & security / scale / limited network → customer requirements
5. **Section: VCF Edge Overview**
   - Right-sized edge (1/2/3+ nodes)
   - VCF Edge 9.1 three pillars
   - Day 0 / Day 1 — ZTP infrastructure provisioning & registration
   - NVMe Memory Tiering (lower cost at the edge)
   - VKS (vSphere Kubernetes Service) — CNCF conformant
   - GitOps / Argo CD fleet management across 1000s of sites
   - Edge AI — GPU placement, CPU-based SLM inference (llama.cpp)
   - Operations — real-time observability, desired-state config management, non-disruptive live patching
6. **Section: Use Cases & Customer Stories** — industry use cases + Audi / Healthcare / Retail stories
7. **Section: Packaging & Licensing** — VCF Edge core-based licensing, vSAN rules, license override
8. **Closing** — Key outcomes: Scale, Speed, Efficiency, Real-Time Intelligence

### Edge-AI Focused Pitch
1. Title · 2. The Edge AI Opportunity (50% inference at edge) · 3. AI workload challenges at the edge · 4. VCF Edge unified platform (VM + container + AI) · 5. Advanced GPU management & intelligent placement · 6. CPU-based SLM inference with llama.cpp (no GPU) · 7. VKS for production AI apps · 8. Customer story · 9. Closing

### Retail / Manufacturing Fleet-at-Scale Pitch
1. Title · 2. Scaling 1000s of sites as one platform · 3. Thin edge (single host) topology · 4. Zero-touch provisioning (ZTP) · 5. GitOps continuous delivery (Argo CD) · 6. Desired-state config + live patching · 7. Customer story (Retail 1000+ stores / Audi smart factory) · 8. Closing

---

## Key Messages for Edge

| Customer Pain at the Edge | VCF Edge Answer |
|---------------------------|-----------------|
| 站點太多、沒有現場 IT | Zero Touch Provisioning (ZTP) + autonomous operations, manage 1000s from one platform |
| 機房空間/預算受限 | Right-sized 1/2/3+ node; NVMe memory tiering cuts infra cost up to ~40% |
| 網路不穩/斷線 | Resilient disconnected operations; air-gapped Workload Domain per site |
| VM + 容器 + AI 各自為政 | Single unified platform runs VMs, containers, and AI workloads together |
| 需要在地 AI 推論 | Edge GPU passthrough/vGPU placement + CPU-based SLM inference (llama.cpp) |
| 上千站點組態漂移 | Desired-state configuration management enforces consistency, eliminates drift |
| 升級/修補要停機 | Non-disruptive ESX live patching — up to ~80% of patches with no reboot |
| 看不到分散站點狀態 | Real-time observability across all edge sites from a centralized view (lower MTTR) |
| K8s 部署複雜 | VKS — CNCF-conformant clusters on demand in minutes (K8s 1.35, Cluster API) |
| 跨站點部署不一致 | GitOps with Argo CD — desired state in customer Git repo, consistent core-to-edge |

---

## Edge Topologies (Appendix detail)

Four reference topologies — pick by scale, network, and isolation needs:

| Topology | When | Key traits |
|----------|------|-----------|
| **Single VCF Instance (VMs + Containers)** | Limited sites, low management overhead | Edge clusters are part of the central Management Domain; full VCF functionality, minimal mgmt resources; optional NSX at edge |
| **Thin Edge (Single Host)** | Many small sites | Dedicated Supervisor per site, 1 Control Plane VM; guest VKS clusters; scales 1-host → multi-host without re-platforming |
| **Two-Node HA** | Need local HA, small footprint | vSAN + witness appliance for availability on two hosts |
| **Air-Gapped / Disconnected** | Critical infrastructure, no/intermittent WAN | Each site is its own Workload Domain (WD) with all components local; independent LCM; self-contained while disconnected |

Topology diagram building blocks: **VCF Ops · vCenter · ESX Host(s) · vSphere Namespace · VKS (Supervisor + guest clusters) · Argo CD · vSAN**. For connected models show the central VCF Ops/vCenter managing remote edge sites; for air-gapped show each site self-contained.

---

## Day 0 / Day 1 — Zero Touch Provisioning

- **Day 0 — Infrastructure Provisioning & Registration**: Pre-configuration → vCenter & ZTP setup → host registration with no on-site IT.
- **Day 1 — Workload Enablement**: Enable VKS / namespaces, attach to GitOps, push desired-state workloads.
Emphasize that ZTP is what makes thousands-of-sites economically viable — ship hardware, power on, it self-registers.

---

## Edge AI Talking Points

- **Unified runtime for distributed edge AI** — VMs, containers, and AI on one platform; improved vGPU placement with automatic migration; GPU passthrough; GPU reservations for capacity planning; cluster-level power utilization metrics.
- **CPU-based inference with llama.cpp** — run quantized **Small Language Models (SLMs)** on CPUs, no GPU required. Lowers cost, increases deployment flexibility, and preserves GPUs for large-scale training/inference. Strong fit for retail/branch sites that can't justify a GPU per location.
- **VKS for production AI** — CNCF-conformant K8s for modern apps + AI: lower TCO, faster time-to-value, enterprise security & compliance, reduced skills gap.

---

## Operations Story (the autonomous-edge proof points)

| Capability | One-liner | Benefit |
|-----------|-----------|---------|
| Real-Time Observability | Continuous telemetry across all edge sites, centralized view | Detect issues instantly, lower MTTR & downtime |
| Configuration Management — Desired State | Continuously monitor, detect, and enforce config across vCenters/clusters | Eliminate drift; every site matches the standard |
| Non-Disruptive Live Patching | ESX live patching on TPM-enabled hosts, no reboot | Up to ~80% of patches with near-zero downtime; patch remotely |
| GitOps Continuous Delivery | Argo CD reconciles desired state from customer Git repo | Consistent workload deployment & LCM across 1000s of sites |

---

## Customer Stories (ready to drop in)

- **Audi (Manufacturing)** — Premium car maker (Audi Group incl. Bentley, Lamborghini, Ducati). Deployed Edge Cloud for Production on VCF to virtualize factory workloads; introduced safety-certified **virtual PLCs** on standardized factory hardware. Theme: smart factories transforming the auto industry.
- **Large Healthcare System (Healthcare, North America)** — Serves 85%+ of its state's population, **2,100+ statewide locations**. Challenge: managing IT across thousands of remote healthcare sites with HA for essential services. Theme: scaling edge infrastructure across a wide geography.
- **Global Retailer (Retail, North America)** — **1,000+ brick-and-mortar stores** worldwide. Needed a low-cost, lightweight, modern edge solution at extreme scale, with robust security and resiliency, operated as one unified, automated platform. Theme: technical parity across all stores.

Match the story to the customer's vertical; lead with the one that mirrors their profile.

---

## Packaging & Licensing Notes

- **VCF Edge** is licensed on **VCF Edge cores**; sizing is per-core at the edge sites.
- **vSAN in VCF Edge** can only be used on VCF Edge cores and **cannot be combined with non-VCF-Edge vSAN** — buy additional VCF Edge cores to expand.
- **(NEW in 9.1)** VCF Edge **decouples the Edge license from the managing vCenter** — remote hosts can use a **VCF Edge license override** even when connected to a non-Edge vCenter.
- VKS is included in the platform; position the advanced services catalog (Ops, security, K8s) as part of the VCF Edge value, not add-on cost.
Always confirm current SKU/core math with the latest Broadcom price book before quoting — do not invent numbers.

---

## Slide Color Recommendation

Use **Aqua / Teal** as the primary edge theme (matches the official deck):
- Primary: `#007A86` (Teal) — platform, core message
- Supporting: `#0193C2` (Sky Blue) — distributed sites, connectivity
- AI / GPU highlight: `#6C4B8F` (Plum) or `#EDB516` (Gold) — edge-AI sections
- Success metrics / outcomes: `#61A00A` (Green)
- Dark section headers: Navy `#1B1E35`

---

## Speaker Notes Guidelines (中文)

- 開場：用 IDC 數據建立急迫性 — 「到 2030 年一半的企業 AI 推論會在邊緣執行，2028 年邊緣市場 $380B」。先談商機，再談痛點。
- 痛點章節：強調邊緣「不是小型資料中心」— 沒有現場 IT、站點上千、網路會斷，這三點決定一切設計。
- Overview：用「1/2/3+ node 右尺寸」破除「邊緣一定要犧牲功能」的迷思 — 單節點也是完整 VCF。
- ZTP：強調這是上千站點能成立的經濟前提 — 出貨、開機、自動註冊，不派人。
- VKS / GitOps：強調 VKS 是原生 K8s (1.35, Cluster API)，Argo CD 讓「一個 Git repo 管全網站點」。
- 邊緣 AI：對沒有 GPU 預算的門市，主打 llama.cpp 的 CPU 推論；有 GPU 的場景才談 vGPU placement。
- 維運三招：observability + desired-state config + live patching = 自主邊緣，少停機、零漂移。
- 客戶故事：挑與客戶同產業的那一個先講 (製造→Audi、零售→Global Retailer、醫療→Healthcare)。
- 授權：9.1 的 license override 是新賣點 — 遠端主機不再被 vCenter 綁死。
- 結尾：四個關鍵成果 — Scale、Speed、Efficiency、Real-Time Intelligence。建議 PoC：選 1 個代表性站點做單節點 + VKS + GitOps 驗證。
