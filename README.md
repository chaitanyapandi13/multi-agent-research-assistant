<div align="center">

# 🧠 Multi-Agent AI Research Assistant

**An automated deep-research pipeline that searches, extracts, and synthesizes the web into structured reports — powered by Groq's ultra-fast LLM inference and the Tavily Search API.**

[![Python](https://img.shields.io/badge/Python-3.13+-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-UI-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Groq](https://img.shields.io/badge/Groq-LPU%20Inference-F55036?style=flat-square)](https://groq.com/)
[![LangChain](https://img.shields.io/badge/LangChain-Orchestration-1C3C3C?style=flat-square)](https://www.langchain.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)
[![Stars](https://img.shields.io/github/stars/chaitanyapandi13/multi-agent-research-assistant?style=flat-square)](https://github.com/chaitanyapandi13/multi-agent-research-assistant/stargazers)

[Overview](#-overview) • [Features](#-key-features) • [Architecture](#-architecture) • [Getting Started](#-getting-started) • [How It Works](#-how-it-works) • [Roadmap](#-roadmap)

</div>

---

## 📖 Overview

Researching a topic online usually means manually searching, opening dozens of tabs, and piecing together scattered information by hand. **Multi-Agent AI Research Assistant** automates that entire workflow.

A coordinated pipeline of specialized AI agents searches the web, extracts relevant content, and synthesizes it into a clean, structured report — all through a simple chat-style interface, in seconds rather than hours.

## ✨ Key Features

| Feature | Description |
|---|---|
| 🔍 **Automated Web Search** | Retrieves up-to-date, relevant results across the web via the Tavily Search API |
| 🤖 **Multi-Agent Orchestration** | Sequentially routes tasks through specialized Search, Extraction, and Summarization agents |
| ⚡ **Ultra-Fast Inference** | Uses Groq's LPU inference engine for near-instant LLM responses |
| 🎨 **Interactive UI** | Clean, minimal Streamlit interface for entering queries and viewing reports |
| 🔐 **Secure Configuration** | No hardcoded credentials — all keys managed via environment variables / Streamlit Secrets |

## 🏗️ Architecture

```
                 User Query
                     │
                     ▼
        ┌─────────────────────┐
        │     Search Agent      │   Retrieves relevant sources
        │     (Tavily API)      │
        └──────────┬────────────┘
                     │
                     ▼
        ┌─────────────────────┐
        │   Extraction Agent    │   Cleans & parses raw content
        │   (BeautifulSoup4)    │
        └──────────┬────────────┘
                     │
                     ▼
        ┌─────────────────────┐
        │ Summarization Agent   │   Synthesizes findings
        │     (Groq LLM)         │
        └──────────┬────────────┘
                     │
                     ▼
             📄 Structured Report
```

Each agent has a narrowly scoped responsibility, coordinated by `pipeline.py`, making the system easy to extend with new agents or data sources.

## 🧰 Tech Stack

| Layer | Technology |
|---|---|
| **Frontend** | Streamlit |
| **LLM Engine** | Groq API — `llama-3.3-70b-versatile` |
| **Orchestration** | LangChain (`langchain-groq`, `langchain-core`) |
| **Search** | Tavily Search API |
| **Web Scraping** | BeautifulSoup4, Requests |
| **Language** | Python 3.13 |

## 📁 Project Structure

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

## 🚀 Getting Started

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

## ⚙️ How It Works

1. **Search Agent** — Takes the user's query and retrieves relevant, up-to-date sources using the Tavily Search API.
2. **Extraction Agent** — Parses and cleans the raw content from retrieved pages using BeautifulSoup4.
3. **Summarization Agent** — Synthesizes the extracted content into a coherent, structured report using Groq-hosted `llama-3.3-70b-versatile` via LangChain.

## 🗺️ Roadmap

- [ ] Add citation links to source material in generated reports
- [ ] Support exporting reports as PDF/Markdown
- [ ] Add conversation memory for follow-up research queries
- [ ] Deploy to Streamlit Community Cloud

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/chaitanyapandi13/multi-agent-research-assistant/issues) or open a pull request.

## 👤 Author

**Chaitanya Pandi**
B.Tech CSE (AI & ML) · [GitHub](https://github.com/chaitanyapandi13)

## 📄 License

This project is available under the [MIT License](LICENSE).

---

<div align="center">

If you find this project useful, consider giving it a ⭐ on GitHub!

</div>
