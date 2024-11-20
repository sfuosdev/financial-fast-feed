import logging
import os
from openai import OpenAI

def summarize_article(article_text, title=None, model="gpt-4o-mini"):
    # Initialize the OpenAI client
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    try:
        # Construct the prompt
        if title:
            user_content = (
                f"You are a financial summarization assistant. Summarize the article below in 25 words or less, include key insights and financial metrics."
                f"Title: '{title}'\n\nArticle: '{article_text}'"
            )
        else:
            user_content = f"Summarize the given article in 25 words or less:\n\n{article_text}"

        # Define the chat messages
        messages = [
            {"role": "system", "content": "You are a helpful financial assistant."},
            {"role": "user", "content": user_content}
        ]

        # Make the API call
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            max_tokens=3800,
            temperature=0.75  # Control the creativity of the response
        )

        # Extract and return the summary
        return response.choices[0].message.content.strip()

    except Exception as e:
        logging.error(f"Error in summarization: {e}")
        return f"Error in summarization: {e}"
