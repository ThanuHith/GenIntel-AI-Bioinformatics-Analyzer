# 🧬 GenIntel - AI Bioinformatics Gene Analyzer

GenIntel is an AI-powered bioinformatics command-line tool that retrieves real gene data from NCBI, performs sequence analysis, and generates intelligent explanations using an LLM.

This project integrates computational biology with modern AI models to create an automated gene analysis pipeline.



## 🚀 What This Project Does

Given a gene name (e.g., BRCA1, TP53), GenIntel will:

1. 🔎 Fetch gene information from NCBI
2. 🧬 Retrieve nucleotide sequence data
3. 📊 Calculate:
   - Sequence Length
   - GC Content
4. 🤖 Generate an AI-based biological explanation
5. 📝 Automatically create a structured report file



## 🧠 Why This Project?

This project was built to:

- Practice Python for Bioinformatics
- Learn real API integration
- Work with biological databases
- Explore AI-assisted scientific explanation
- Build a portfolio-ready GitHub project

It combines:
- Computational biology
- Sequence analysis
- AI integration
- Modular Python architecture


## 🏗️ Project Architecture

User Input  
↓  
main.py  
↓  
fetch_data.py → NCBI Entrez API  
sequence_analysis.py → Biopython  
ai_explainer.py → NVIDIA LLM API  
report_generator.py → Report File  

## 🔬 Technologies Used

- Python 3.10+
- Biopython
- Requests
- NCBI Entrez API
- NVIDIA LLM API (Llama 3.1 Instruct)


