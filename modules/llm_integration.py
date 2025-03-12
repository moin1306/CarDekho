"""
Handles interaction with Ollama LLM using Pydantic AI.
"""

import ollama

def query_llm(question, context):
    try:
        response = ollama.chat(model="llama3", messages=[
            {"role": "system", "content": "You are a CSV data analysis assistant."},
            {"role": "user", "content": f"Context: {context}\nQuestion: {question}"}
        ])
        return response['message']['content']
    except Exception as e:
        return f"LLM error: {str(e)}"
