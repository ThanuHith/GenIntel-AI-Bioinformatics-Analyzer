import os
import requests
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("NVIDIA_API_KEY")
API_URL = "https://integrate.api.nvidia.com/v1/chat/completions"

def get_ai_explanation(gene_data,sequence_analysis):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    prompt = f"""
You are a bioinformatics expert.

Explain the following gene scientifically and also in simple terms.

Gene Name: {gene_data['Name']}
Description: {gene_data['Description']}
Summary: {gene_data['Summary']}

Sequence Length: {sequence_analysis['Length']}
GC Content: {sequence_analysis['GC_Content']}%

Provide:
1. Scientific explanation
2. Clinical significance
3. Simple explanation for students
"""

    payload = {
        "model": "meta/llama3-8b-instruct",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.5,
        "max_tokens": 600
    }
    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        result = response.json()
        return result["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error connecting to NVIDIA API : {str(e)}"