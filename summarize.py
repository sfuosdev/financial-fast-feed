from openai import OpenAI

def summarize_article(article_text):
    """
    Summarizes the given article text using OpenAI's GPT model.
    """
    client = OpenAI(api_key="KEY")  # Replace 'YOUR_API_KEY' with your actual API key

    try:
        response = client.completions.create(
            model="gpt-3.5-turbo-instruct",  # or another model you prefer
            prompt=f"Summarize the given article in 20 words or less:\n\n{article_text}",
            max_tokens = 3800  # Adjust based on your needs
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error in summarization: {e}"
