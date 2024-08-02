import logging
from openai import OpenAI
import os

def summarize_article(article_text):
    openai_api_key = os.getenv('OPENAI_API_KEY')
    if not openai_api_key:
        raise ValueError("No OPENAI_API_KEY set for environment")

    client = OpenAI(api_key=openai_api_key)
    try:
        response = client.completions.create(
            model="gpt-3.5-turbo-instruct",  
            prompt=f"Summarize the given article in 20 words or less:\n\n{article_text}",
            max_tokens=3000  
        )
        return response.choices[0].text.strip()
    except Exception as e:
        logging.error(f"Error in summarization: {e}")
        return f"Error in summarization: {e}"
