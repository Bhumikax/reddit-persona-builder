# 🧠 Reddit Persona Builder

A Python project that analyzes Reddit user activity (posts + comments) and generates a **User Persona** using an LLM. This was developed as part of the AI/LLM Intern assignment for **BeyondChats**.

---

## 🚀 What It Does

Given a **Reddit username**, this tool:
1. Scrapes the user's **posts and comments**.
2. Analyzes the content using **Google's Gemini 2.5 Pro LLM**.
3. Generates a **User Persona** in natural language:
   - Interests
   - Personality Traits
   - Themes
   - Writing Style
   - Beliefs / Patterns
4. Saves the persona as a `.txt` file.
5. **Cites specific posts/comments** used for inference.

---

## 🛠 Tech Stack

| Component         | Details                              |
|------------------|--------------------------------------|
| Language          | Python 3.10+                          |
| Reddit API        | `praw` (Pushshift-Reddit wrapper)     |
| LLM Used          | `gemini-2.5-pro` via `google-generativeai` |
| Env Management    | `python-dotenv`                      |
| Output Format     | `.json` (raw scraped data), `.txt` (persona) |

---

## 📂 Project Structure

reddit-persona-builder/
│
├── main.py # Entry point
├── persona_builder.py # LLM persona generation logic
├── reddit_scraper.py # Reddit post/comment scraper
├── utils.py # Helper functions
├── .env # API keys (not tracked on GitHub)
│
├── /data # Raw scraped data (JSON)
│ ├── spez_raw.json
│ └── ...
│
├── /outputs # Final persona .txt files
│ ├── spez_persona.txt
│ └── ...
│
└── README.md # You're reading it!


## 🔐 Setup Instructions

### 1. ✅ Clone the repository
---
git clone https://github.com/yourusername/reddit-persona-builder.git
cd reddit-persona-builder

2. ✅ Create a virtual environment
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows

4. ✅ Install dependencies
pip install -r requirements.txt

6. ✅ Add your API keys to a .env file
Create a .env file in the root directory:
REDDIT_CLIENT_ID=your_client_id
REDDIT_CLIENT_SECRET=your_client_secret
REDDIT_USER_AGENT=script:reddit.persona:v1.0 (by u/your_username)

GEMINI_API_KEY=your_gemini_api_key
💡 You can get your Gemini API key from https://makersuite.google.com/app/apikey

🧪 How to Run
1. Activate your environment:
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
2. Run the program:
python main.py
3. Enter a Reddit username:
Enter Reddit username: spez
✅ Output:
A .json file with raw scraped data is saved in /data

A .txt file with the generated persona is saved in /outputs, e.g.:

outputs/spez_persona.txt
📄 Sample Output (Truncated)
User Persona for: spez

Interests:
- Reddit platform development and community moderation (from: “Post: I’ve been testing some mod tools...”)

Personality Traits:
- Highly engaged and transparent (from: “Comment: AMA about Reddit’s future, happy to share...”)

Themes:
- Open communication with users, trust-building (from: “Post: Let’s talk about mod transparency...”)

Writing Style:
- Clear, conversational, confident (from: “Comment: Thanks for asking, here’s the roadmap...”)
📦 Sample Files in Repo
✅ data/spez_raw.json

✅ outputs/spez_persona.txt

✅ data/Hungry-Move-6603_raw.json

✅ outputs/Hungry-Move-6603_persona.txt

⚠️ Notes
This project does not use the official Reddit API for historical posts — it uses praw which internally supports limited scraping.

Gemini LLM was used over OpenAI due to rate limits and access restrictions.

All persona outputs are AI-generated and not definitive.

🧑‍💻 Author
Bhumika Chidrawar
LinkedIn - [https://www.linkedin.com/in/bhumika-chidrawar-72856325b/] 
