# 🔍 Anomalyze (LLM-Powered Log Analyzer)

A lightweight tool that uses Google's Gemini model to semantically summarize, cluster, and optionally hypothesize root causes of anomalies in logs.

## 🚀 Features

- Semantic log clustering via LLM embeddings
- Summarized operational patterns
- Optional root cause suggestions
- CLI-friendly with customizable flags

## 📁 Project Structure

anomalyze/

├── src/...

├── data/input/

├── data/output/

├── .env

├── main.py

├── README.md

└── requirements.txt


## 🔧 Setup

### 1. Clone the repo

    ```bash
    git clone https://github.com/Silver094/anomalyze.git
    cd anomalyze
    ```
### 2. Create a virtual environment (recommended)

    python -m venv venv
    source venv/bin/activate      

    On Windows:
    venv\Scripts\activate

### 3. Install dependencies

    pip install -r requirements.txt

### 4. Set up your .env file
    Create a .env file in the root with the following:
    GEMINI_API_KEY=your_api_key_here
    GEMINI_MODEL=models/gemini-pro


## ⚙️ Usage

    python main.py --input data/input/var.log --output data/output/summary.txt --root-causes

- "--root-causes" is optional. Omit it if you just want summaries.

## 🧠 Motivation

Traditional observability tools like Splunk, ELK, and CloudWatch offer deterministic filters, alerts, and dashboards — but they lack semantic understanding.

This project augments such tools by:

- Clustering similar logs
- Generating operational summaries
- Suggesting possible root causes (hypotheses) for anomalies

All using Google's Gemini LLM, making debugging and triage much faster.

## 🛠️ Future Enhancements
- Web UI for real-time priority
- Live log stream support
- Multi-modal observability (metrics + traces + logs)
- GitHub Actions bot for PR logs
- Vector DB integration for historical context

## 👤 Author
Made with ❤️ by [Deepanshu Vishwakarma](https://www.linkedin.com/in/deepanshu094/)

