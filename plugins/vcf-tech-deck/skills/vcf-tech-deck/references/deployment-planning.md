# Deployment planning deck recipe

Use this recipe when the user asks for a VCF 9.1 deployment planning deck (資源 / IP / FQDN / 網段 / 防火牆規劃 / DNS / NTP / 部署前檢查).

## Audience

Infra engineers, PMO, network/DNS owners, customer's IT planning team. Tone: technical and prescriptive. The deck is a working document, not a sales pitch.

## Length

30–45 slides typical. Customer-specific Greenfield builds can go to 50+ if you include per-domain detail.

## Required deliverable structure

Six chapters with section headers. Drop slides from the 150-slide template that fit each chapter, then add customer-specific content slides.

```
Cover (template slide 1)
Agenda (template slide 78 reskinned as agenda)
Chapter 01 — Platform overview                      (section header from slide 4)
Chapter 02 — Components inventory                   (section header from slide 4 or 7)
Chapter 03 — Resource planning (Compute/Memory/Storage)
Chapter 04 — IP & network planning (VLAN/Subnet/IP Pool)
Chapter 05 — FQDN & DNS planning
Chapter 06 — Pre-deployment checklist
Closing (template slide 150)
```

## Slide picks from the 150-slide template

Use these slides as starting points. Replace text with customer-specific values.

| Chapter | Pick from template | Why |
|---|---|---|
| Cover | 1 | Plum cover |
| Agenda | 78 (Resources / Agenda layout) | Already has 6-bullet structure |
| Ch 01 — Section header | 4 | Plum section header |
| Ch 01 — VCF Overview | 5 (Private Cloud Constructs) | One-page VCF stack visual |
| Ch 01 — Architecture hierarchy | 6 (Private Cloud Constructs — Title Only) | Re-skin as "Cluster → WLD → Instance → Fleet" |
| Ch 01 — Deployment paths | 11, 12 (Deploy new fleets, Existing components) | 4-path comparison |
| Ch 02 — Section header | 7 (Section Header – Plum) | |
| Ch 02 — Components | 13 (Integrated Planning & Preparation) | Component inventory table reskin |
| Ch 03 — Section header | 21 (Section Header – Plum) | "Storage" header — reskin as "Resource" |
| Ch 03 — Resource summary | 25 (Diagram with Content on R) | One-page resource summary diagram |
| Ch 03 — SDDC & vCenter sizing | 26 (Diagram with Content on R) | Table layout |
| Ch 03 — NSX sizing | 27 (Diagram with Content on R) | |
| Ch 03 — vSAN ESA storage | 28 (Diagram with Content on R) | Bring vSAN ESA in here |
| Ch 04 — Section header | 34 (Section Header – Plum) | "Network" header |
| Ch 04 — VLAN overview | 37 (VCF with Physical Networking) | Re-skin as VLAN list |
| Ch 04 — Subnet example | 22 (Title with Subtitle) | Re-skin as customer mgmt subnet |
| Ch 04 — vMotion/vSAN/TEP | 38 (NSX Virtual Networking) | Re-skin with VMK pool table |
| Ch 04 — Edge Uplink & BGP | 43 (Configure external connectivity) | |
| Ch 04 — IP pool worksheet | 45 (Virtual Network Supporting VPC) | Re-skin as IP Pool table |
| Ch 05 — Section header | 49 (Section Header – Plum) | "Modernize" — reskin as "FQDN & DNS" |
| Ch 05 — DNS requirements | 60 (Centralized Certificate Mgmt) | Re-skin as DNS forward/reverse |
| Ch 05 — Full FQDN list | 13 (Integrated Planning — table layout) | Table reskin for FQDN list |
| Ch 06 — Section header | 56 (Section Header – Plum) | "Manage" — reskin as "Pre-deployment" |
| Ch 06 — DNS/NTP/Cert pillars | 58 (Fleet Management — 3 column) | Re-skin as 3 pillars |
| Ch 06 — Ports & protocols | 62 (Enhanced Fleet-level Config) | Re-skin as port table |
| Ch 06 — Compatibility tools | 76 (Four Square 1) | 4-cell tool grid |
| Ch 06 — Final checklist | 67 (Diagram with Content on R) | Re-skin as 4-quadrant checklist |
| Closing | 150 (Thank You / Closing - Plum) | |

## Required content elements

For each Greenfield customer deck, gather and embed:

### Resource summary (Ch 03)
- Total vCPU / RAM / Disk for management domain
- Per-component sizing table (SDDC Mgr, vCenter, NSX, VCF Ops, VCF Auto, VKS, License Hub if vDefend)
- Reference: VCF 9.1 Planning and Preparation Workbook → "Management Domain Sizing" sheet

### Network plan (Ch 04)
- VLAN ID list (ESX Mgmt / VM Mgmt / VCF Mgmt / vMotion / vSAN / Host Overlay / Edge Overlay / Edge Uplink-01 / Edge Uplink-02)
- Per-VLAN subnet + gateway + MTU
- IP Pool ranges per VLAN
- BGP plan if Edge present (local AS, remote AS, peer IPs)

### FQDN list (Ch 05)
- HA mode: ~32–34 FQDNs (cover SDDC Mgr, vCenter ×2, NSX cluster + 3 nodes ×2, VCF Ops cluster + Fleet + Collector, VCF Ops for Logs ×3, VCF Auto VIP + 3 IaaS + Proxy, VKS Supervisor ×3, ESXi mgmt ×4, ESXi workload ×4, License Hub controller + worker if vDefend)
- VCF 9.1 specifically adds: `sddc-idb` (Identity Broker), `sddc-sr` (Services Runtime), `sddc-fc` (Fleet Component), `sddc-ic` (Instance Component), `sddc-lc` (License Server), `sddc-ops` cluster (3-node HA), `sddc-cp` (Cloud Proxy), `sddc-auto` (VCF Automation), `sddc-vcfa-sr` (VCF Auto services runtime)

### Pre-deployment checklist (Ch 06)
- DNS forward + reverse for every FQDN
- NTP at least 2 sources
- Certificates plan (Self-signed default; enterprise CA recommended)
- Ports & protocols (reference https://ports.broadcom.com filtered by VCF 9.1)
- BCG hardware compatibility check
- Configuration Maximums check

## VCF 9.1 specifics to surface

Always include the following 9.1-only content in a deployment planning deck:

1. **VCF Management Services Cluster** (k8s-based services) — needs 12 contiguous IPs for worker nodes + 4 service FQDNs (sr / fc / ic / idb)
2. **License Server VM** (sddc-lc, 2 vCPU / 4 GB / 50 GB) — mandatory new VM in 9.1
3. **VCF Operations replaces vROps** — 3-node HA + VIP + Cloud Proxy + Fleet Mgmt
4. **VCF Automation replaces Aria Automation** — naming change matters for customer-facing slides
5. **VCF Identity Broker (vIDB)** — was a separate cluster in 9.0, absorbed into Services Cluster in 9.1
6. **License Hub** if customer uses vDefend SSP — needs 1 Controller + 1 Worker + 4-IP Node Pool + 4-IP Service Pool

## Customer-specific elements to gather

Before drafting, ask the user (or check existing artifacts) for:

- Customer domain (e.g. `esunbank.com.tw`, `corp.foxconn.com.tw`)
- Management subnet (e.g. `172.17.79.0/24`)
- ESXi subnets (e.g. `172.17.72.0/23`, `172.17.76.0/22`)
- DNS / NTP server IPs
- VLAN ID allocation
- Number of ESXi hosts per domain
- Workload domain count
- Whether HCX, Live Recovery, vDefend, Private AI are in scope

If a network table or xlsx already exists in the workspace, read it first and reuse the existing IP/FQDN assignments.

## Output filename

`{YYYYMMDD}-{Customer}-VCF9.1-DeploymentPlanning.pptx`

Example: `20260618-EsunBank-VCF9.1-DeploymentPlanning.pptx`
