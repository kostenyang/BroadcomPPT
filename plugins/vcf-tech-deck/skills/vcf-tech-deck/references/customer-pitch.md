# Customer pitch / EBC deck recipe

Use this recipe when the user asks for a VCF 9.1 customer briefing, executive briefing (EBC), business value pitch, CIO/CTO 簡報, or sales pitch.

## Audience

CIOs, CTOs, infra VPs, decision makers. Tone: business outcome focused, value proposition, less technical jargon. Pair every feature with a business benefit (cost / agility / risk reduction).

## Length

20–35 slides. Keep it tight — executives skim, they don't read.

## Required deliverable structure

```
Cover (template slide 1)
Why VCF — Business Initiatives (slide 3)
Private Cloud Constructs (slide 5)
Big Statement — value proposition (Big Statement - Plum)
Section: Storage value (21)
  vSAN ESA differentiation (24, 25, 26)
Section: Network value (34)
  NSX one-pager (35, 36, 38)
Section: Mobility (49)
  HCX use cases (50, 54)
Section: Operations (56)
  Fleet management (58, 63, 64)
Section: Automation (90)
  Self-service & VCF Automation Solution (91, 94)
Section: Modern apps (108)
  VKS one-pager (113, 114)
Section: AI (120)
  Private AI Services (124)
Section: Security (133)
  Defense in Depth (134)
  Resilience (140)
Big Statement — modern private cloud (143)
Closing (150)
```

## Slide picks from the 150-slide template

| Section | Pick | Purpose |
|---|---|---|
| Cover | 1 | Plum cover |
| Why VCF | 3 (Business Initiatives) | Set the business context |
| Constructs | 5 (Private Cloud Constructs) | One-page VCF architecture |
| Storage | 24, 25, 26 (Evolving platform / Next gen vSAN / vSAN difference) | Storage value |
| Storage TCO | 32 (Do more with what you have) | TCO story |
| Network | 35, 36, 38 (Network virtualization required / NSX virtual networking) | Why NSX |
| Mobility | 50, 54 (HCX capabilities, Non-disruptive migration) | Migration story |
| Operations | 58, 63, 64 (Fleet, Maximize utilization, Track-forecast) | Day-2 ops |
| Operations cost | 32, 63 | Cost reduction proof points |
| Automation | 91, 94 (Solution overview, Governance) | Self-service value |
| VKS | 113, 114 (Multi-cluster mgmt, Service enabled by Supervisor) | Cloud-native story |
| AI | 124, 126 (Private AI Services) | AI on-prem story |
| Security | 134, 140 (Defense in Depth, End-to-end Resilience) | Security posture |
| Cyber recovery | 149 (Cyber Recovery) | Ransomware resilience |
| Big Statement | 143 (Delivering the Modern Private Cloud) | Closing value statement |
| Closing | 150 (Thank You Plum) | Q&A / contact |

## Required proof points

Every customer pitch should embed at least 3 of these quantified outcomes (verify on https://www.broadcom.com/info/vmware-cloud-foundation before use):

- **52% lower TCO** vs public cloud equivalents
- **34% lower infrastructure cost** with VCF vs traditional silos
- **61% faster deployment** with VCF Installer wizard
- **40% server consolidation** with NVMe Memory Tiering
- **3x switching throughput** with NSX 9.1 vs prior gen
- **Hours → minutes** lifecycle ops with Fleet Management

## Customer success placeholder

If the customer has an existing reference architecture or peer customer story, insert a Customer Success slide (layout `Customer Success`) after the value statement and before Big Statement closing.

Reference peer customer hints:
- Banking / FSI: 中信銀行, 國泰世華, 玉山銀行, 富邦, 兆豐
- Semiconductor: 台積電 (TSMC), 聯發科, 力積電, 環球晶
- Telecom: 中華電信, 台灣大哥大, 遠傳
- Public sector: 中華郵政, 健保署, 監理所
- Healthcare: 台大醫院, 林口長庚, 國泰醫院

Do not name peer customers in the deck without explicit confirmation that the customer has been quoted publicly by Broadcom.

## What to avoid in EBC decks

- Long technical sizing tables (those belong in the deployment planning deck)
- Port numbers / firewall details
- Multi-step CLI / API examples
- Naming-convention deep dives (sddc-ops01/02/03 detail — keep "VCF Operations HA cluster")
- "Bring-up workflow" diagrams (too operational)

## Customer-specific elements to gather

- Customer name (Chinese + English if applicable)
- Customer industry (drives which proof points resonate)
- Current pain points (silos / cost / agility / compliance)
- Strategic initiatives (Digital transformation / AI adoption / Cloud migration / Ransomware resilience)
- Existing footprint (Existing VMware? VCF 5.x? Public cloud?)

## Output filename

`{YYYYMMDD}-{Customer}-VCF9.1-EBC.pptx` or `{YYYYMMDD}-{Customer}-VCF9.1-Pitch.pptx`

Example: `20260618-Foxconn-VCF9.1-EBC.pptx`
