# 📰 Scraping Project

A Python‑based Selenium automation project that extracts section headings from the BBC homepage.

This version includes  **dynamic user‑agent generation** , human‑like browser behaviour, and a clean foundation for future expansion into a full news‑analysis toolkit.

## 🚀 Project Overview

This project launches a real Chrome browser using Selenium, navigates to the BBC homepage, and collects all visible heading elements (`h1`–`h6`).

It’s designed as the first step in a larger portfolio project that will grow into a structured, modular scraping and analysis system.

Current capabilities include:

* Automated Chrome session using Selenium
* Dynamic user‑agent generation on each run
* Human‑like behaviour (scrolling, randomised delays, explicit waits)
* Clean extraction of all heading tags
* Fully isolated Python environment using `venv`

## 🧱 Features

✔ Dynamic User‑Agent Generation

Each run generates a realistic Chrome user agent with a random version number, improving compatibility and mimicking natural browser diversity.

✔ Human‑Like Interaction

The script scrolls, waits, and pauses in a natural way to reduce false positives and improve stability.

✔ Modular, Expandable Design

The project is intentionally simple but structured so it can evolve into:

* A multi‑page scraper
* A news‑analysis pipeline
* A scheduled cloud function
* A Dockerised microservice
* A Streamlit dashboard

## 🛠️ Installation & Setup

### * Clone the repository

git clone https://github.com/yourusername/bbc-headline-scraper.git
cd bbc-headline-scraper

```powershell
git clone https://github.com/yourusername/bbc-headline-scraper.git
cd bbc-headline-scraper
```

2. Create a virtual environment

```powershell
python -m venv venv
```

Activate the virtual environment (PowerShell)

```powershell
.\venv\Scripts\Activate.ps1
```

.\venv\Scripts\Activate.ps1

To deactivate:

```powershell
deactivate
```

deactivate

4. Install dependencies

```powershell
pip install -r requirements.txt
```

pip install -r requirements.txt

### 🧩 Chrome WebDriver Setup

This project uses  **webdriver‑manager** , which automatically downloads and manages the correct ChromeDriver version.

No manual installation required.

### ▶️ Running the Scraper

```powershell
python scraper.py
```

You’ll see output similar to:

Using User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) ...
BBC Homepage Headings:

- News
- Sport
- Business
- Technology
  ...

### 📁 Project Structure

bbc_scraper/
│
├── scraper.py          # Main Selenium script with dynamic UA generation
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation

## Future versions may introduce:

scraper/
│   browser.py
│   extract.py
│   storage.py
│   analysis/
│   utils/
docker/
tests/

### 🔮 Roadmap

Planned enhancements include:

* Save scraped data to JSON/CSV
* Extract article URLs, summaries, timestamps
* Add structured logging
* Build a CLI interface
* Add retry logic and error handling
* Containerise with Docker
* Schedule scraping jobs (cron or cloud functions)
* Add NLP analysis (sentiment, topic modelling)
* Build a Streamlit dashboard for visualisation

### 🧑‍💻 Skills Demonstrated

* Selenium browser automation
* Dynamic user‑agent generation
* Web scraping fundamentals
* Python scripting and virtual environments
* Clean, modular project design
* Git/GitHub workflow
* Portfolio‑ready documentation













## Dev Settings

### Venv

Activate the venv

1. Create the vritual environment

```powershell
python -m venv venv
```

2. Activate the venv

```powershell
.\venv\Scripts\Activate.ps1
```

The (venv) should then appear in the CLI

3. To Deactivate

```powershell
deactivate
```
