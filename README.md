# PSSE Copilot ⚡  
*A CLI-based engineering assistant for PSS®E transient stability workflows*

---

## 📌 Overview

**PSSE Copilot** is a lightweight, CLI-based engineering assistant that helps
power system engineers **set up transient stability studies in PSS®E**
in a consistent and repeatable way.

The tool focuses on **workflow automation and structured study documentation** —
not simulation execution — ensuring compatibility with licensed PSS®E environments.

---

## 🎯 Why PSSE Copilot?

Transient stability studies often involve:
- Repetitive scripting for events and channels
- Manual setup of similar study cases
- Rewriting boilerplate sections of reports
- Inconsistent study documentation across projects

PSSE Copilot helps by:
- Automating **study setup logic**
- Generating **PSS®E-ready Python scripts**
- Producing **structured, report-ready documentation**
- Reducing repetitive engineering effort

---

## 🧠 What This Tool Does (v0.1 – Current)

- Collects study inputs via CLI  
- Generates deterministic transient stability event logic  
- Produces PSS®E Python script templates  
- Auto-generates **structured report sections** (objective, assumptions, criteria)  
- Saves all outputs for reuse and traceability  

> ⚠️ This version focuses on **deterministic automation**.  
> It does not interpret simulation results or replace engineering judgment.

---

## 📂 Project Structure

```text
psse-copilot/
├── agent/                 # Engineering logic
│   ├── prompts.py
│   └── stability_agent.py
├── cli/                   # CLI entry point
│   └── main.py
├── outputs/               # Generated study artifacts
│   ├── ts_main_script.py
│   ├── study_report.md
│   └── metadata.txt
├── templates/             # Future extensions
├── README.md
└── requirements.txt
