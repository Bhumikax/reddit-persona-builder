from scraper import fetch_user_data, save_user_data
from persona_builder import build_persona
import os

def main():
    username = input("Enter Reddit username: ").strip().replace("https://www.reddit.com/user/", "").strip("/")
    
    data = fetch_user_data(username)
    
    os.makedirs("data", exist_ok=True)
    os.makedirs("output", exist_ok=True)
    
    raw_path = f"data/{username}_raw.json"
    save_user_data(data, raw_path)
    
    persona = build_persona(data)
    
    with open(f"output/{username}_persona.txt", "w", encoding="utf-8") as f:
        f.write(persona)
    
    print(f"Persona generated at output/{username}_persona.txt")

if __name__ == "__main__":
    main()
