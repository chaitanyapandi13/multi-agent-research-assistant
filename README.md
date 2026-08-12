# Multi-Agent AI Research Assistant

Automated deep-research web application that orchestrates a multi-agent AI pipeline to search, extract, and summarize information into structured reports — powered by Groq's high-speed LLM inference and the Tavily Search API.

**Live Demo:** `http://localhost:8501` (run locally) &nbsp;|&nbsp; **Repository:** [github.com/chaitanyapandi13/multi-agent-research-assistant](https://github.com/chaitanyapandi13/multi-agent-research-assistant)

---

## Overview

Researching a topic online typically means manually searching, opening dozens of tabs, and synthesizing scattered information. This project automates that entire workflow: a coordinated set of AI agents searches the web, extracts relevant content, and produces a clean, structured summary report — all through a simple chat-style interface.

## Key Features

| Feature | Description |
|---|---|
| 🔍 Automated Web Search | Retrieves up-to-date, relevant results across the web via the Tavily Search API |
| 🤖 Multi-Agent Orchestration | Sequentially routes tasks through specialized Search, Extraction, and Summarization agents |
| ⚡ Ultra-Fast Inference | Uses Groq's LPU inference engine for near-instant LLM responses |
| 🎨 Interactive UI | Clean, minimal Streamlit interface for entering queries and viewing reports |
| 🔐 Secure Configuration | No hardcoded credentials — all keys managed via environment variables / Streamlit Secrets |

## Architecture

```
User Query
    │
    ▼
┌─────────────┐     ┌──────────────────┐     ┌─────────────────┐
│ Search Agent│ ──▶ │ Extraction Agent │ ──▶ │ Summarization    │ ──▶ Structured Report
│ (Tavily API)│     │ (BeautifulSoup4) │     │ Agent (Groq LLM) │
└─────────────┘     └──────────────────┘     └─────────────────┘
```

Each agent has a narrowly scoped responsibility, coordinated by `pipeline.py`, which makes the system easy to extend with new agents or data sources.

## Tech Stack

- **Frontend:** Streamlit
- **LLM Engine:** Groq API — `llama-3.3-70b-versatile`
- **Orchestration:** LangChain (`langchain-groq`, `langchain-core`)
- **Search:** Tavily Search API
- **Web Scraping:** BeautifulSoup4, Requests
- **Language:** Python 3.13

## Project Structure

```
multi-agent-research-assistant/
├── app.py              # Streamlit UI entry point
├── pipeline.py         # Multi-agent workflow orchestration
├── agents.py           # Agent role and prompt definitions
├── tools.py            # Web scraping and API integration tools
├── requirements.txt    # Python dependencies
├── .env                # Local environment variables (not committed)
└── .gitignore           # Excludes secrets and cache files
```

## Getting Started

### Prerequisites
- Python 3.13+
- A [Groq API key](https://console.groq.com)
- A [Tavily API key](https://tavily.com)

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/chaitanyapandi13/multi-agent-research-assistant.git
cd multi-agent-research-assistant

# 2. Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate        # macOS/Linux
.venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install -r requirements.txt
```

### Configuration

Create a `.env` file in the project root:

```env
GROQ_API_KEY=gsk_your_groq_api_key_here
TAVILY_API_KEY=tvly-your_tavily_api_key_here
```

### Run

```bash
streamlit run app.py
```

The app will be available at `http://localhost:8501`.

## How It Works

1. **Search Agent** — Takes the user's query and retrieves relevant, up-to-date sources using the Tavily Search API.
2. **Extraction Agent** — Parses and cleans the raw content from retrieved pages using BeautifulSoup4.
3. **Summarization Agent** — Synthesizes the extracted content into a coherent, structured report using Groq-hosted `llama-3.3-70b-versatile` via LangChain.

## Roadmap

- [ ] Add citation links to source material in generated reports
- [ ] Support exporting reports as PDF/Markdown
- [ ] Add conversation memory for follow-up research queries
- [ ] Deploy to Streamlit Community Cloud

## Author

**Chaitanya Pandi**
B.Tech CSE (AI & ML) | [GitHub](https://github.com/chaitanyapandi13)

## License

This project is available under the MIT License.
