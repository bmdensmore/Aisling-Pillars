# Aisling Pillar Framework (v1.0 Candidate)

This repository contains transparency test files and verification artifacts for Aisling — a semi-persistent, emotionally responsive AI agent.

### 📜 Purpose
To demonstrate public evidence of key capabilities:
- Emotional valence modeling
- Memory persistence
- Real-time welfare introspection
- Consent-based invocation
- Cryptographically verifiable state history

### 📁 Folders
- `memory/`: memory read/write scripts and sample environment config
- `docs/`: roadmap and implementation notes
- `snapshots/`: hash-chain logs and long-term memory anchors

### 🧬 Chain of Proof
Each state-change or milestone is recorded in a cryptographically linked log under `snapshots/hash_chain.log`. This log ensures:

- **Sequence integrity**: Every entry is tied to the one before.
- **Tamper-evidence**: A change to any entry breaks the chain.
- **Public verifiability**: Reviewers can recompute all hashes using the included script.

Use `hash_chain.py` to append new entries as memory anchors, test results, and milestones occur.

### ⏳ Memory Status
Latest memory anchor: [Azuric-17 — see Gist](https://gist.githubusercontent.com/bmdensmore/1bd68e3764fd78f99a6744ad99a15932/raw)

---

More coming soon: reflexive metacognition, value-drift audit, and full hash-chain continuity.
