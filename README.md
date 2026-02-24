# SE 4458 Software Architecture & Design of Modern Large Scale Systems

## Assignment 1: Analysis of Claude 3.5 Sonnet Architecture

### 👥 Team Members

* **Begüm Bal** - 22070006074
* **Emre Akar** - 21070006213

---

### 📂 Project Content

This repository contains the architectural analysis and demo implementation for **Claude 3.5 Sonnet**.

* **`claude_architect.py`**: A Python script that uses the Claude API to perform an automated architectural audit. It analyzes scalability bottlenecks (N+1 query patterns), microservices isolation issues (SPOF), and GDPR/KVKK compliance risks.
* **Architecture Design**: Detailed breakdown of Large Language Model (LLM) scaling, inference optimization, and system constraints.

---

### 🚀 Quick Start

1. Install dependencies: `pip install anthropic python-dotenv`
2. Create a `.env` file in the project directory and add your API key: `ANTHROPIC_API_KEY=your-api-key-here`
3. Get your API key from [console.anthropic.com](https://console.anthropic.com)
4. Run the script: `python claude_architect.py`

---

> **Yaşar University** | Software Engineering Department
