import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Use one of the working models
model = genai.GenerativeModel("models/gemini-2.5-pro")

def build_persona(user_data):
    posts = user_data.get("posts", [])
    comments = user_data.get("comments", [])

    sample_texts = "\n\n".join([
        f"Post: {p.get('title', '')} - {p.get('body', '')}" for p in posts[:5]
    ] + [
        f"Comment: {c.get('body', '')}" for c in comments[:5]
    ])

    prompt = f"""
You are an AI that generates a Reddit User Persona based on their posts and comments.

Use the following content to infer the user’s:
- Interests
- Personality traits
- Common themes
- Writing style
- Any notable patterns or beliefs

Also cite the post/comment snippet from which you inferred each trait.

Text:
{sample_texts}

Output in this format:
---
User Persona for: {user_data['username']}

Interests:
- [Interest] (from: “…”)

Personality Traits:
- [Trait] (from: “…”)

Themes:
- [Theme] (from: “…”)

Writing Style:
- [Style] (from: “…”)
---
"""

    response = model.generate_content(prompt)
    return response.text
