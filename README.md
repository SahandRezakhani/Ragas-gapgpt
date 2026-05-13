<div align="center">
  
# 🧠 RAGAs - Automated Evaluation of RAG Systems
  
### *with gapgpt API* 🇮🇷

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![API: gapgpt](https://img.shields.io/badge/API-gapgpt-orange.svg)](https://gapgpt.ai)
[![Paper](https://img.shields.io/badge/Paper-2309.15217-red.svg)](https://arxiv.org/abs/2309.15217)

<p align="center">
  <em>📊 Automated RAG System Evaluation • No VPN Required</em>
</p>

</div>

---

## 📚 About

This project is a complete implementation of the **RAGAs** paper for automated evaluation of **Retrieval Augmented Generation** systems. Using the **gapgpt** service (OpenAI-compatible), it works without international internet access or VPN.

<div align="left">
  
```diff
+ ✅ No VPN required
+ ✅ Reference-free evaluation
+ ✅ JSON output for reproducibility
+ ✅ Multi-model support
```

</div>

---

## 🎯 Evaluation Metrics

| Metric | Description | Purpose |
|--------|-------------|---------|
| 🔷 **Faithfulness** | Is the answer grounded in the retrieved context? | Prevent hallucinations |
| 🔶 **Answer Relevancy** | Does the answer directly address the question? | Measure answer accuracy |
| 🔷 **Context Relevancy** | Is the retrieved context focused? | Optimize retrieval |

---

## 📦 Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/SahandRezakhani/ragas-gapgpt.git
cd ragas-gapgpt
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Set your API key

Make a .env file in root directory and place code below in it:

```bash
GAPGPT_API_KEY=GapGPT-API-Key
GAPGPT_BASE_URL=https://api.gapgpt.app/v1
DEFAULT_MODEL=gpt-4o
EMBEDDING_MODEL=text-embedding-3-small
```

---

## 🎨 Supported Models

| Model | gapgpt Name | Status |
|-------|-------------|--------|
| GPT-4o | `gpt-4o` | ✅ Full support |
| GPT-4 Turbo | `gpt-4-turbo` | ✅ Full support |
| Gemini Pro | `gemini-pro` | ✅ Full support |
| Claude 3 | `claude-3` | ✅ Full support |

---

## 📂 Project Structure

```bash
ragas-gapgpt/
├── 📄 README.md
├── 📄 requirements.txt
├── 📄 .env.example
├── 📁 src/
│    ├── 📄 utils.py
│    ├── 📄 evaluator.py
│    ├── 📁 metrics/
│    │    ├── 📄 faithfulness.py
│    │    ├── 📄 answer_relevancy.py
│    │    └── 📄 context_relevancy.py
│    └── utils.py
└── 📁examples/
     ├── 📄 simple_evaluation.py
     └── 📄 wikeval_demo.py
```

---

## 📖 Citation

If you use this implementation in your research, please cite the original RAGAs paper:

```bibtex
@article{es2023ragas,
  title={RAGAs: Automated Evaluation of Retrieval Augmented Generation},
  author={Es, Shahul and James, Jithin and Espinosa-Anke, Luis and Schockaert, Steven},
  journal={arXiv preprint arXiv:2309.15217},
  year={2023}
}
```

---

## 🤝 Contributing

1. **Fork** the repo
2. **Create a branch** (`git checkout -b feature/amazing`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing`)
5. **Open a Pull Request**

---

## 📜 License

This project is licensed under the **MIT License**.

<div align="center">
  
---
  
**Made with ❤️ for the Iranian open-source community**

[Report Bug](https://github.com/yourusername/ragas-gapgpt/issues) · [Request Feature](https://github.com/yourusername/ragas-gapgpt/issues)

</div>