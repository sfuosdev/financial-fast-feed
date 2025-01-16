from openai import OpenAI
import os
import logging

# Initialize logging
#logging.basicConfig(level=logging.INFO)

def summarize_article(article_text, max_words=50, tone="informative"):

    # Retrieve OpenAI API key from environment
    openai_api_key = os.getenv('OPENAI_API_KEY')
    if not openai_api_key:
        raise ValueError("No OPENAI_API_KEY set for environment")

    # Initialize OpenAI client
    client = OpenAI(api_key=openai_api_key)

    try:
        # Define messages for the summarization
        messages = [
            {
                "role": "system",
                "content": (
                    f"You are a financial news summarization assistant. Summarize the following article for business professionals by "
                    f"highlighting the most critical financial and market-related details. Ensure the style is {tone} and strictly under {max_words} words."
                    f"Focus on revenue figures, market trends, major announcements, and any immediate implications for investors or businesses."
                ),
            },
            {"role": "user", "content": f"Summarize this article:\n\n{article_text}"}
        ]

        # Call the OpenAI API
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            max_tokens=1500,
            temperature=0.15  # Lower temperature for more deterministic responses
        )

        # Correctly access the content of the response
        summary = response.choices[0].message.content.strip()
        return summary

    except Exception as e:
        logging.error(f"Error during summarization: {e}")
        return f"Error during summarization: {e}"
