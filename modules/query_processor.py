"""
Processes user queries and extracts relevant data from CSV.
"""

from modules.llm_integration import query_llm

def process_query(df, question):
    try:
        context = df.to_dict(orient="records")[:100]  # Limiting rows for efficiency
        return query_llm(question, context)
    except Exception as e:
        return f"Error processing query: {str(e)}"
