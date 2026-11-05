# LexiGen – GenAI Word Insight Generator

A practical, lightweight Generative AI application built with **Python**, **Flask**, and the **Google Gemini API** (`gemini-1.5-flash`). It takes any single word or technical concept and synthesizes a concise, structured explanatory paragraph along with core bullet takeaways and practical examples.

## Key Features
- **Prompt Engineering**: Formats raw LLM responses into structured paragraphs with key facts and real-world usage.
- **Multiple Tones**: Supports *General*, *Technical*, *ELI5 / Simple*, and *Historical* perspectives.
- **Dual Interfaces**:
  - **CLI Tool** (`cli.py`): Command-line generation for terminal users.
  - **Web Dashboard** (`app.py`): Minimalist, responsive dark-mode UI with instantaneous feedback.
- **Cost-Free & Fast**: Uses Gemini 1.5 Flash on Google AI Studio's free tier.

---

## Project Structure
```text
lexigen-word-explainer/
├── app.py              # Flask Web application & API route
├── cli.py              # Terminal CLI utility
├── templates/
│   └── index.html      # Frontend UI (Tailwind CSS)
├── requirements.txt    # Python dependencies
├── .env.example        # Environment variables template
└── README.md           # Documentation
```

---

## Quickstart Guide

### 1. Clone or Extract the Project
```bash
git clone https://github.com/viswanathan1277/lexigen-word-explainer.git
cd lexigen-word-explainer
```

### 2. Set Up a Virtual Environment (Recommended)
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Your API Key
1. Get a free API key from [Google AI Studio](https://aistudio.google.com/).
2. Create a `.env` file in the project root:
```bash
cp .env.example .env
```
3. Open `.env` and paste your key:
```ini
GEMINI_API_KEY=AIzaSy...your_actual_key_here
```

---

## How to Run

### Method A: Web Interface
```bash
python app.py
```
Open [http://localhost:5000](http://localhost:5000) in your browser.

### Method B: Command-Line Interface
```bash
# General explanation
python cli.py "Quantum Computing"

# Technical tone
python cli.py "Blockchain" --tone technical

# Simple ELI5 explanation
python cli.py "Photosynthesis" --tone simple
```

---

## Tech Stack
- **Language**: Python 3.9+
- **LLM / GenAI**: Google Gemini API (`google-generativeai`, `gemini-1.5-flash`)
- **Backend**: Flask
- **Frontend**: HTML5, Tailwind CSS, JavaScript
- **Config**: `python-dotenv`
