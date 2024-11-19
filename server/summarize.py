import logging
import os
import openai

def summarize_article(article_text, title=None, model="gpt-3.5-turbo-instruct"): # Switch models soon?
    openai_api_key = os.getenv('OPENAI_API_KEY')
    if not openai_api_key:
        raise ValueError("No OPENAI_API_KEY set for environment")

    client = openai.OpenAI(api_key=openai_api_key)

    try:
        # Create the prompt
        if title:
            prompt = (
                f"You are a financial summarization assistant. Summarize the article below in 25 words or less. "
                f"Focus on financial trends, market impacts, and actionable insights. "
                f"Title: '{title}'\n\nArticle: '{article_text}'"
            )
        else:
            prompt = f"Summarize the given article in 25 words or less:\n\n{article_text}"

        # Generate the summary
        response = client.completions.create(
            model=model,
            prompt=prompt,
            max_tokens=3800
        )

        return response.choices[0].text.strip()

    except Exception as e:
        logging.error(f"Error in summarization: {e}")
        return f"Error in summarization: {e}"
