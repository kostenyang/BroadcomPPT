# Upgrade / migration deck recipe

Use this recipe when the user asks for a VCF 5.x → 9.1 upgrade deck, vSphere → VCF Import deck, Converge flow deck, or any "升級路徑 / migration path" presentation.

## Audience

Existing VMware customers and their operations teams. Tone: prescriptive, change-management focused, risk-aware. Always show what changes between current and target state.

## Length

20–30 slides.

## Required deliverable structure

```
Cover (template slide 1)
Why upgrade — business drivers
Current state → Target state (visual)
Supported upgrade paths matrix
Path 1: VCF 5.x → 9.1 (in-place)
Path 2: vSphere 9.0 → VCF Import
Path 3: vSphere 8.x → Converge to VCF
Path 4: Greenfield → migrate workloads (HCX)
Resource & FQDN/IP changes
HCX migration option
Pre-upgrade checklist
What's not supported (red callout)
Rollback plan
Closing
```

## Slide picks from the 150-slide template

| Section | Pick | Purpose |
|---|---|---|
| Cover | 1 | Plum cover |
| Business drivers | 3 (Business Initiatives) | Why upgrade |
| Section: Build & Deploy | 7 (Section Header – Plum) | |
| VCF Installer | 8 (Diagram with Outcome) | New 9.1 installer |
| Online/Offline depot | 9 | Air-gapped support |
| Wizard / JSON | 10 | UI-driven workflow |
| Deploy new fleets | 11 | Fleet construct |
| Existing components | 12 | Re-use vCenter / NSX |
| Planning & Prep | 13 | Workbook integration |
| Lifecycle Mgmt | 14, 15, 16 (Centralized Lifecycle Mgmt) | New centralized LCM |
| Software Depot | 17 (Central Software Depot) | One depot replaces multiple |
| VCF Download Tool | 18 | New tool |
| Upgrade Planning | 19 (Upgrade & Patch Planning) | Step-by-step planner |
| Prechecks | 20 (VCF Lifecycle Prechecks) | Built-in pre-validation |
| Section: Mobility | 49 | |
| HCX capabilities | 50 (HCX Capabilities in VCF) | Workload migration path |
| Migration use case | 51 (VCF Mobility Use Case) | |
| Migration options | 53 (HCX Migration Options) | Bulk / live / cold |
| Non-disruptive migration | 54 (Migrate Workloads Non-disruptively) | Zero downtime story |
| Time & cost savings | 55 (Efficient migrations) | Business case |
| Closing | 150 | |

## Upgrade path matrix — always include

Insert a comparison slide listing supported source versions and the upgrade method:

| Source | Target | Method | Notes |
|---|---|---|---|
| VCF 5.2 / 5.2.1 | VCF 9.1 | In-place via VCF Operations | SDDC Manager → Bring-up upgrade |
| VCF 4.5+ | VCF 9.1 | Two-step (4.5 → 5.2 → 9.1) | Cannot skip 5.2 |
| vSphere 9.0 / 9.0.1 / 9.0.2 | VCF 9.1 | VCF Import | Greenfield-style with existing vCenter |
| vSphere 8.0 U3+ | VCF 9.1 | Converge flow | Wrap vSphere into VCF Mgmt Domain |
| vSphere 7.x | VCF 9.1 | Upgrade vSphere first | Must go to 8.0U3 first, then Converge |
| Standalone Aria Suite | VCF 9.1 | Migrate to VCF Operations / Automation | Aria 8.18 → VCF 9.1 Operations |
| Standalone vRLI | VCF 9.1 | Migrate to VCF Operations for Logs | Containerized in 9.1 |
| Standalone vIDB | VCF 9.1 | Absorbed into Services Cluster | Old vIDB cluster decommissioned |
| Standalone Identity Manager (vIDM) | VCF 9.1 | Migrate to VCF Identity Broker | New unified broker |

## What's not supported — red callout

Always include a Gold/Red callout slide listing:

- ❌ Skipping VCF 5.2 (no direct 4.5 → 9.1)
- ❌ Skipping vSphere 8.0U3 (no direct 7.x → 9.1)
- ❌ Mixed-version Fleet (all instances must be on 9.1 to enable Fleet Management)
- ❌ Importing vCenter 7.x (must be 8.0U3 or 9.0+)
- ❌ Standalone NSX-T → VCF 9.1 without proper version alignment
- ❌ Cross-vendor storage migration in same upgrade (do storage migration separately)

Layout: use a Plum section break + add a callout box with `#EDB516` (Gold) accent.

## VCF 9.1 specific changes the upgrade introduces

Customers must plan for these net-new requirements:

1. **VCF Management Services Cluster** — 12 contiguous IPs for k8s worker nodes
2. **License Server VM** (sddc-lc) — new mandatory VM, 2 vCPU / 4 GB / 50 GB
3. **VCF Operations rebrand** — was vROps / Aria Operations. UI changes, dashboards re-organized
4. **VCF Automation rebrand** — was Aria Automation. Blueprints / catalog items carry over
5. **Identity Broker absorbed** — old vIDB cluster decommissioned during upgrade, FQDN re-points to Services Cluster
6. **Centralized Software Depot** — vCenter / NSX / SDDC Mgr no longer host individual depots
7. **SaltStack by default** — new default config management
8. **VCF Operations for Logs** — runs under Services Cluster, not dedicated vRLI cluster anymore

Each item should appear as a bullet on a "What changes" slide BEFORE the upgrade flow detail.

## Pre-upgrade checklist (always include)

A four-quadrant checklist slide covering:

- **Hardware & firmware** — BCG check, TPM 2.0, NIC firmware, BIOS to 9.1-certified versions
- **Network & DNS** — All new 9.1 FQDNs created, forward + reverse, no IP collisions
- **Backup & rollback** — vCenter backup, NSX manager backup, SDDC Mgr backup tested, snapshot strategy
- **License & assets** — Broadcom Support Portal license bound, Bundle downloaded + signature verified, JSON spec validated

## HCX migration story (when included)

If the upgrade path is "Greenfield 9.1 + HCX migration", surface:
- Three migration options: Bulk, Live (vMotion), Cold
- Site Pairing prerequisites
- Network extension via L2 stretch
- Cost / time savings table (slide 55)
- Rollback option: snapshots + reverse HCX migration

## Customer-specific elements to gather

- Current VCF / vSphere version
- Number of vCenter instances and Workload Domains
- NSX deployment (T0 + Edge cluster topology)
- Existing Aria Suite (Operations / Automation / Logs / Identity)
- HCX in scope?
- Maintenance window appetite (in-place vs side-by-side migration)
- Rollback expectations (typical: 7-day rollback window)

## Output filename

`{YYYYMMDD}-{Customer}-VCF9.1-Upgrade-From{SourceVersion}.pptx`

Example:
- `20260618-CTBC-VCF9.1-UpgradeFrom5.2.pptx`
- `20260618-Foxconn-VCF9.1-ImportFrom-vSphere9.0.pptx`
- `20260618-EsunBank-VCF9.1-ConvergeFrom-vSphere8U3.pptx`
