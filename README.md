# 🤖 Multi-Agent AI Research Assistant

An intelligent web application that automates deep web research and generates structured summary reports using a multi-agent AI system powered by Groq and the Tavily Search API.

🚀📂 **[GitHub Repository](https://github.com/chaitanyapandi13/multi-agent-research-assistant)**

---

## 📌 Features

* 🔍 **Automated Web Search & Parsing:** Gathers up-to-date, relevant data across the web using Tavily Search API.
* 🤖 **Multi-Agent Orchestration:** Sequentially routes research tasks across specialized AI agents (Search, Extraction, Summarization).
* ⚡ **Ultra-Fast LLM Inference:** Powered by Groq's high-speed inference engine.
* 🎨 **Interactive User Interface:** Simple and intuitive frontend built with Streamlit.
* 🔐 **Secure Configuration:** Zero hardcoded keys; relies strictly on environment variables and Streamlit Secrets.

---

## 🛠️ Tech Stack

- **Frontend / UI:** Streamlit
- **LLM Engine:** Groq API (`llama-3.3-70b-versatile`)
- **Search Engine:** Tavily Search API
- **Web Scraping:** BeautifulSoup4 (`bs4`) & Requests
- **Framework:** LangChain (`langchain-groq`, `langchain-core`)
- **Language:** Python 3.13
- **Version Control:** Git & GitHub
- **Environment:** Localhost (`http://localhost:8501`)

---

## 📁 Repository Structure

```text
├── .gitignore          # Prevents tracking of secrets (.env) and caches
├── .env                # Local environment variables (Not committed to Git)
├── app.py              # Main Streamlit user interface entry point
├── pipeline.py         # Multi-agent workflow execution engine
├── agents.py           # Agent roles and prompt definitions
├── tools.py            # Web scraping and API tools
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation

```

---

## 🚀 Local Setup & Installation

Follow these steps to run the project locally on your machine:

### 1. Clone the Repository

```bash
git clone [https://github.com/chaitanyapandi13/multi-agent-research-assistant.git](https://github.com/chaitanyapandi13/multi-agent-research-assistant.git)
cd multi-agent-research-assistant

```

### 2. Set Up Virtual Environment (Recommended)

```powershell
# On Windows
python -m venv .venv
.venv\Scripts\activate

# On macOS/Linux
python3 -m venv .venv
source .venv/bin/activate

```

### 3. Install Dependencies

```bash
pip install -r requirements.txt

```

### 4. Configure Environment Secrets

Create a `.env` file in the root directory and add your API keys:

```env
GROQ_API_KEY=gsk_your_groq_api_key_here
TAVILY_API_KEY=tvly-your_tavily_api_key_here

```

### 5. Launch the Application

```bash
streamlit run app.py

```

---

## 📸 Application Demo

Run locally at `http://localhost:8501`

---

## 👤 Author

* **Chaitanya Pandi** - [GitHub Profile](https://github.com/chaitanyapandi13)


