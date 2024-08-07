import openai
import os
import logging

def summarize_article(article_text):
    openai_api_key = os.getenv('OPENAI_API_KEY')
    if not openai_api_key:
        raise ValueError("No OPENAI_API_KEY set for environment")

    openai.api_key = openai_api_key
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",  
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes financial articles."},
                {"role": "user", "content": f"Summarize the key information of this article in 25 words or less: {article_text}"}
            ],
            max_tokens=3800 
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        logging.error(f"Error in summarization: {e}")
        return f"Error in summarization: {e}"
