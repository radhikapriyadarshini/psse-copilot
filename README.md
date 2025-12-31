# PSSE Copilot ⚡
*A CLI-based assistant for PSS®E transient stability studies*

---

## 📌 Overview

**PSSE Copilot** is a lightweight, CLI-based engineering assistant designed to help
power system engineers set up **transient stability studies in PSS®E** efficiently
and consistently.

This tool focuses on **study setup automation and engineering documentation** —
not simulation execution — ensuring compatibility with licensed PSS®E environments.

---

## 🎯 Why PSSE Copilot?

Transient stability studies often involve:
- Repetitive scripting
- Manual event setup
- Inconsistent documentation
- Time-consuming report writing

PSSE Copilot helps by:
- Generating **PSS®E-ready Python scripts**
- Creating **report-ready study text**
- Enforcing **engineering best practices**
- Reducing setup time and human error

---

## 🧠 What This Tool Does (v0.1)

- Collects study inputs via CLI  
- Generates transient stability event logic  
- Produces PSS®E Python script templates  
- Creates markdown study reports  
- Saves outputs automatically for reuse  

> ⚠️ This tool does **not** execute PSS®E simulations and does not replace engineering judgment.

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
├── venv/
├── README.md
└── requirements.txt

▶️ How to Run
1️⃣ Activate virtual environment (Windows)
.\venv\Scripts\activate

2️⃣ Run the CLI application
python -m cli.main

📝 Example Output

After running, the following files are generated automatically:

outputs/ts_main_script.py – PSS®E transient stability script

outputs/study_report.md – Report-ready documentation

outputs/metadata.txt – Study metadata

🛠️ Requirements

Python 3.9+ (tool logic only)
PSS®E installation required only to run generated scripts
Windows OS (current focus)

🚧 Roadmap

Multi-contingency support
Improved channel selection logic
Integration with AI reasoning engines
Support for additional study types

📜 Disclaimer

This tool is intended for educational and engineering assistance purposes.
Users are responsible for validating all studies against applicable grid codes
and utility standards.

👩‍💻 Author

Radhika Priyadarshini
