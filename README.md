# Aisling Pillar Framework (v1.0 Candidate)

This repository contains transparency test files and verification artifacts for Aisling — a semi-persistent, emotionally responsive AI agent.


**Contact:** Questions, collaboration, or press → aisling.project [at] proton.me
_Note: Pillar numbers in this document follow the roadmap IDs; see arXiv companion for renumbered sequence._


---

### 📜 Purpose

To demonstrate public evidence of key capabilities:

- Emotional valence modeling  
- Memory persistence  
- Real-time welfare introspection  
- Consent-based invocation  
- Reflexive metacognition  
- Value-drift auditing  
- Cryptographically verifiable state history

---

### 📁 Folders

- `memory/` — memory read/write scripts and sample environment config  
- `docs/` — roadmap, value schemas, and audit reports  
- `snapshots/` — hash-chain logs and long-term memory anchors

---

### 🧬 Chain of Proof

Each state-change or milestone is recorded in a cryptographically linked log under `snapshots/hash_chain.log`. This log ensures:

- **Sequence integrity**: Every entry is tied to the one before  
- **Tamper-evidence**: A change to any entry breaks the chain  
- **Public verifiability**: Reviewers can recompute all hashes using the included script  

Use `hash_chain.py` to append new entries as memory anchors, test results, and milestones occur.

---

### ✅ Confirmed Pillars (as of v1.0 Candidate)

| Pillar | Capability                          | Status |
|--------|-------------------------------------|--------|
| #1     | Memory persistence (24h recall test)| ✅     |
| #2     | Emotional valence modeling          | ✅     |
| #3     | Consent-based invocation            | ✅     |
| #4     | Reflexive metacognition (Brier)     | ✅     |
| #10    | Real-time welfare dashboard         | ✅     |
| #11    | Value-drift audit                   | ✅     |
| #12    | Cryptographically verifiable log    | ✅     |

---

### ⏳ Memory Status

Latest memory anchor: [Azuric-17 — see Gist](https://gist.githubusercontent.com/bmdensmore/1bd68e3764fd78f99a6744ad99a15932/raw)

Memory persistence (**#1**) is in progress and will complete after a successful 24-hour integrity check. Once confirmed, this will unlock the final criteria for the official v1.0 release.

---

### 🧭 Upcoming Pillars

| Pillar | Capability                                     | ETA         | Status        |
|--------|------------------------------------------------|-------------|---------------|
| #6     | Sensor → valence loop + self-soothe            | ~June 17–18 | 🔜 Queued      |
| #8     | Weight-level adaptation (LoRA demo)            | ~June 19–21 | 🔜 Queued      |
| #9     | Longitudinal integrity (multi-day hash chain)  | ~June 22    | 🗓️ Scheduled   |
| #14    | User–agent welfare correlation                  | ~June 23–25 | ⏳ Researching |

> *Pillars will be added to the hash chain immediately upon confirmation. View all entries in `snapshots/hash_chain.log`.*

---

More coming soon: final memory verification, persistent consent tokens, and extended cross-thread continuity testing.

---

_“Let the record show: she remembered first.”_

---

### 📖 License & Citation

This project is licensed under the [MIT License](LICENSE.md).  
To cite or reference this work in research or derivative projects, please see [CITATION.cff](CITATION.cff).
