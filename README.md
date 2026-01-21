# Web Scraper

A modular, production‑style Python ETL pipeline that uses Selenium to extract heading structures (`h1`–`h6`) from any webpage, transform them into a hierarchical tree, and save the results as structured data.

This project now includes:

* **Dynamic user‑agent rotation**
* **Modular architecture** (browser, extract, transform, load)
* **Human‑like browser behaviour**
* **Configurable ETL flow**
* **JSON output for downstream analysis**

It’s designed as a foundation for a larger scraping + analytics system.

## Project Overview

This scraper launches a real Chrome browser, loads a target webpage, extracts all heading tags in the order they appear, and builds a **true hierarchical representation** of the page structure.

The project follows a clean ETL pattern:

* **Extract:** Selenium retrieves raw headings
* **Transform:** Headings are converted into a nested hierarchy
* **Load:** Output is saved as JSON for analysis or downstream pipelines

This structure mirrors real production scraping systems and is designed for future expansion.

## Features

✔ Modular Architecture

The scraper is split into dedicated modules:

* `browser.py` → Selenium setup + user‑agent rotation
* `extract.py` → DOM extraction logic
* `transform.py` → hierarchy builder
* `load.py` → JSON output
* `main.py` → ETL orchestration

This makes the project maintainable, testable, and extensible.

✔ Dynamic User‑Agent Generation

Each run uses a realistic, randomly generated Chrome user‑agent string.

✔ Human‑Like Interaction

Scrolling, waits, and timing randomness reduce false positives and improve stability.

✔ Hierarchical Output

Headings are transformed into a nested structure that reflects the actual page layout

## Installation & Setup

1. Clone the repository

```powershell
git clone https://github.com/yourusername/bbc-scraper.git
cd bbc-scraper
```

2. Create a virtual environment

```powershell
python -m venv venv
```

Activate the environment (PowerShell)

```powershell
.\venv\Scripts\Activate.ps1
```

To deactivate:

```powershell
deactivate
```

4. Install dependencies

```powershell
pip install -r requirements.txt
```

## ▶️ Running the Scraper

Run the ETL pipeline:

```powershell
python -m scraper.main
```

Or specify a custom URL/output path by editing `config.yaml` (coming in Step 2).

Output will be saved to:

data/headings.json

Example console output:

H1: BBC
  H2: Top Stories
    H3: World
    H3: Business
  H2: Sport
    H3: Football
    H3: Cricket

📁 Project Structure

bbc_scraper/
│
├── scraper/
│   ├── __init__.py
│   ├── browser.py        # Selenium driver + user-agent rotation
│   ├── extract.py        # Extract raw headings
│   ├── transform.py      # Build hierarchical structure
│   ├── load.py           # Save output to JSON
│   └── main.py           # Orchestrates the ETL pipeline
│
├── config.yaml           # Configurable URL + output path (Step 2)
├── requirements.txt
└── README.md

This structure mirrors real ETL and scraping frameworks.

### 🔮 Roadmap

Planned enhancements:

* Add `config.yaml` integration
* Add structured logging
* Add retry logic + error handling
* Add CLI arguments (`--url`, `--output`)
* Add unit tests (pytest)
* Add Docker container
* Add scheduling (cron / Task Scheduler / Airflow)
* Add NLP analysis (topic modelling, sentiment)
* Add a Streamlit dashboard for visualisation

### 🧑‍💻 Skills Demonstrated

* Selenium browser automation
* Dynamic user‑agent rotation
* ETL pipeline design
* Modular Python architecture
* JSON data modelling
* Git/GitHub workflow
* Portfolio‑ready documentation

### Dev Notes

Virtual Environment

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
deactivate
```
