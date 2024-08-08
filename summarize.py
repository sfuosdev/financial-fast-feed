import logging
import os
import openai
import json

def summarize_article(article_text):
    openai_api_key = os.getenv('OPENAI_API_KEY')
    if not openai_api_key:
        raise ValueError("No OPENAI_API_KEY set for environment")

    client = openai.OpenAI(api_key=openai_api_key)
    try:
        response = client.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt=f"Summarize the given article in 25 words or less:\n\n{article_text}",
            max_tokens=3800  # Adjusted token limit for brief summary
        )
        return response.choices[0].text.strip()
    except Exception as e:
        logging.error(f"Error in summarization: {e}")
        return f"Error in summarization: {e}"

def get_post_insights(title, fullText, model="gpt-3.5-turbo"):
    openai_api_key = os.getenv('OPENAI_API_KEY')
    if not openai_api_key:
        raise ValueError("No OPENAI_API_KEY set for environment")

    client = openai.OpenAI(api_key=openai_api_key)

    # Adjusted prompt for financial articles
    prompt = (
        f"Create a concise summary for a financial article based on the title and full text provided. "
        f"Respond only with the summary.\n\n"
        f"Title: '{title}'\n\nFull Text: '{fullText}'"
    )

    messages = [
        {"role": "system", "content": "You are a financial analysis assistant."},
        {"role": "user", "content": prompt},
    ]

    try:
        # Obtain completion for the prompt
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            max_tokens=3800  # Adjusted token count based on expected output length
        )

        # Extract summary from the response
        content = response.choices[0].message["content"]
        result = json.loads(content)

        summary = result.get("summary", "No summary generated.")
        return {"summary": summary}

    except json.JSONDecodeError as decode_error:
        logging.error(f"Error decoding JSON response: {decode_error}")
        return {"summary": "No summary generated."}
    except Exception as e:
        logging.error(f"Error in generating post insights: {e}")
        return {"summary": "No summary generated."}
