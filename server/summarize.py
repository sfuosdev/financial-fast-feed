import logging
import os
import json
import openai

def summarize_article(article_text, title=None, model="gpt-4o-mini"):
    # Initialize the OpenAI client
    client = openai(api_key=os.getenv("OPENAI_API_KEY"))

    try:
        # Generate a summary with a 25-word prompt limit
        response = client.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt=f"Summarize the given article in 25 words or less:\n\n{article_text}",
            max_tokens=3800 
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

    # Prepare prompt for generating financial article insights
    prompt = (
        f"Create a concise summary for a financial article based on the title and article text provided. "
        f"Respond only with the summary.\n\n"
        f"Title: '{title}'\n\nFull Text: '{fullText}'"
    )
    
    # System and user messages for chat completion
    messages = [
        {"role": "system", "content": "You are a financial analysis assistant."},
        {"role": "user", "content": prompt},
    ]

    try:
        # Generate insights using OpenAI's chat completion
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            max_tokens=3800  
        )

        # Get summary from response, default if none generated
        content = response.choices[0].message["content"] # Extract response content
        result = json.loads(content)

        summary = result.get("summary", "No summary generated.")
        
        return {"summary": summary}

    except json.JSONDecodeError as decode_error:
        logging.error(f"Error decoding JSON response: {decode_error}")
        return {"summary": "No summary generated."}
    except Exception as e:
        logging.error(f"Error in generating post insights: {e}")
        return {"summary": "No summary generated."}
