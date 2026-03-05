# StackOverflow tag page scraper (no Selenium)

This script downloads the HTML for a StackOverflow "tagged questions" page and extracts the **question titles + links**.

Target page (default): `https://stackoverflow.com/questions/tagged/python`

## Setup

```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

## Run

Print questions (title + link):

```bash
python main.py
```

JSON output:

```bash
python main.py --json
```

Scrape a specific page URL:

```bash
python main.py --url "https://stackoverflow.com/questions/tagged/python"
```

Pick a different tab/page:

```bash
python main.py --tag python --tab newest --page 1
```