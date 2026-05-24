---
name: vcf-ai
description: Create Broadcom VCF AI infrastructure presentation decks covering Private AI, GPU workloads, VKS (Kubernetes), NVIDIA AI Enterprise, and AI platform modernization. Trigger whenever the user wants a presentation on AI infra, Private AI Foundation, GPU cluster, VKS, NVIDIA vGPU, GenAI on-prem, LLM deployment, AI/ML workloads, or any 人工智慧/AI 基礎架構 topic. Also trigger for 生成式AI, RAG architecture on VCF, or enterprise AI governance. Always use official Broadcom template — never create from scratch.
---

# VCF AI Infrastructure Presentation Skill

Read `broadcom-ppt-base` SKILL.md first for template specs, colors, fonts, and editing workflow.
Location: `/home/claude/broadcom-ppt-skills/broadcom-ppt-base/SKILL.md`

> **⚡ 預設底版**：永遠使用 `APJ__Tech__Upgrade_Pathways_to_VCF_9_1-Slides.pptx` (3.8MB)。  
> 只有使用者明確說「用 5.2 Master」時才改用大檔。

---

## Industry Context

Enterprise AI infrastructure in 2025 centers on:
- **Private AI**: Run LLMs/GenAI models on-prem for data sovereignty and compliance
- **GPU Infrastructure**: NVIDIA H100/H200/A100 clusters for training and inference
- **Kubernetes Platform**: VKS for containerized AI/ML workloads
- **RAG Architecture**: Retrieval-Augmented Generation on private data
- **AI Governance**: Model versioning, data lineage, access control

VMware Private AI Foundation with NVIDIA is the key Broadcom offer:
- VCF as the compute/network/storage substrate
- NVIDIA AI Enterprise as the AI software stack
- VKS as the Kubernetes orchestration layer
- vGPU for multi-tenant GPU sharing

Key Taiwan AI customers/prospects:
- **Semiconductor EDA**: TSMC, MediaTek (SPICE simulation, DRC AI)
- **Financial AI**: 國泰世華, 玉山 (fraud detection, risk scoring, chatbot)
- **Government**: NCHC (國網中心), Academia Sinica (研究運算)
- **Manufacturing**: AI-driven quality inspection, predictive maintenance
- **Telecom**: CHT (network optimization, customer service AI)

---

## Recommended Deck Structure

### For Private AI / GenAI on VCF

1. **Title Slide** — `Title Slide – Plum` (AI = innovation, purple)
2. **Agenda**
3. **Section: 企業 AI 浪潮與挑戰**
   - GenAI 採用現況 (Big Statement - Aqua with stat)
   - 痛點：公有雲 AI 成本高、資料主權、合規要求
   - 為什麼需要 Private AI？
4. **Section: VMware Private AI Foundation**
   - 架構概覽 (Diagram with Content on Right)
   - VCF + NVIDIA AI Enterprise 整合堆疊
   - vGPU 多租戶 vs. GPU passthrough 選擇
   - VKS (Kubernetes) 支援 AI 容器工作負載
5. **Section: GPU 基礎架構設計**
   - NVIDIA H100/A100 GPU server sizing
   - vGPU profile 選擇 (C/Q/A profile)
   - GPU 記憶體分配策略
   - 網路：InfiniBand vs. RoCE for GPU-to-GPU
   - 儲存：NVMe for model weights, shared NFS for datasets
6. **Section: AI 使用案例**
   - RAG on VCF (LLM + Vector DB + Enterprise Data)
   - Fine-tuning pipeline (VKS + MLflow + S3-compatible storage)
   - Inference serving (Triton Inference Server on VKS)
   - AI for IT Operations (VCF Operations AI features)
7. **Section: 升級路徑**
   - 現有 vSphere GPU cluster → VCF + VKS
   - 逐步導入 NVIDIA AI Enterprise
8. **Big Statement** — Private AI ROI vs. public cloud AI spend
9. **Closing**

### For EDA / Semiconductor AI (TSMC / MediaTek)

1. Title
2. EDA workload 挑戰 (license contention, job scheduling, long run times)
3. VCF + NVIDIA A100 for EDA simulation
4. vGPU for SPICE/DRC acceleration
5. Kubernetes for EDA job scheduling (LSF on VKS)
6. 儲存：高效能 NVMe vSAN for EDA datasets
7. Closing

---

## Key Messages for AI Infrastructure

| Customer Pain | VCF Answer |
|---------------|-----------|
| 公有雲 AI 成本不可控 | Private AI on VCF — 固定 CapEx，可預測成本 |
| 訓練資料不能上公有雲 | 資料主權：AI 完全在地端運行 |
| GPU 資源利用率低 | vGPU 多租戶分享，提升 GPU 使用率 |
| AI 平台管理複雜 | VKS + NVIDIA AI Enterprise 整合堆疊 |
| 傳統 VM 與容器並存 | VCF 同時支援 VM + VKS 容器，統一平台 |
| AI 模型安全與合規 | vDefend + 加密 + RBAC 保護模型與資料 |
| 推論 (Inference) 延遲 | NVMe vSAN + 高速網路 + GPU passthrough |

---

## GPU Sizing Reference Slide

Include a sizing table:

| 模型規模 | GPU 建議 | vGPU Profile | Memory |
|---------|---------|-------------|--------|
| LLM 7B (Inference) | 1x A100 40GB | A100-40C | 40GB |
| LLM 13B (Inference) | 2x A100 80GB | A100-80C | 80GB |
| LLM 70B (Inference) | 4x H100 80GB | H100-80C | 320GB |
| LLM 70B (Fine-tuning) | 8x H100 80GB | Passthrough | 640GB |
| EDA Simulation | 1x A30 / A100 | vGPU Q-profile | 24-40GB |

---

## Private AI Architecture Diagram

```
┌─────────────────── VCF Private AI Platform ───────────────────┐
│                                                                  │
│  [VKS Cluster]                    [GPU Compute]                 │
│   AI Workload Namespace            NVIDIA H100/A100             │
│   ├─ LLM Inference Pod             vGPU / Passthrough           │
│   ├─ Vector DB (pgvector)          ──────────────               │
│   ├─ RAG Pipeline                 [vSAN NVMe]                   │
│   └─ MLflow / Kubeflow             Model Weights                │
│                                    Training Datasets            │
│  [Enterprise Data]                [NSX Network]                 │
│   SharePoint / Oracle / SAP        GPU RDMA Fabric              │
│   ↓ ETL / Indexing                 Tenant Isolation             │
│   Vector Embeddings                                             │
└──────────────────────────────────────────────────────────────── ┘
                        ↑
              [VCF Management Domain]
              SDDC Manager + vCenter
              VCF Operations (AI Ops)
```

---

## Slide Color Recommendation

Use **Plum** theme for AI/innovation:
- Primary: `#6C4B8F` (Plum) — AI, advanced tech
- Supporting: `#0193C2` (Sky Blue) — data flow, connectivity
- GPU/compute highlight: `#EDB516` (Gold) — high-value components
- Success metrics: `#61A00A` (Green)

---

## Speaker Notes Guidelines (中文)

- 開場：以「2025 年，每個企業都需要一個 AI 策略，但不是每個工作負載都適合公有雲」作為切入
- Private AI 章節：強調資料主權是台灣金融業、半導體業採用 Private AI 的核心驅動力
- GPU 章節：解釋 vGPU vs. passthrough 的選擇邏輯 (多租戶推論 → vGPU；單一大型訓練 → passthrough)
- VKS 章節：強調 VKS 是 Kubernetes 原生，不是 vSphere pod 的改版
- RAG 章節：以企業知識庫 + LLM 的 RAG 架構為例，說明 Private AI 的實際使用場景
- 競品對比：AWS Bedrock / Azure OpenAI 的資料出境風險 vs. VCF Private AI 的完全地端
- 結尾：建議 PoC 場景：1個 GPU server + VKS + open-source LLM (Llama 3 / Mistral) 快速驗證
