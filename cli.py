import os
import sys
import argparse
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY or API_KEY == "your_gemini_api_key_here":
    print("Error: GEMINI_API_KEY is not set in your .env file.")
    print("Get a free API key at https://aistudio.google.com/ and add it to .env")
    sys.exit(1)

genai.configure(api_key=API_KEY)

def explain_word(word: str, tone: str = "general") -> str:
    """Generates a concise paragraph of information for a given word using Gemini."""
    model = genai.GenerativeModel("gemini-1.5-flash")
    
    prompt = f"""You are an educational assistant. Provide a well-structured, insightful paragraph explaining the concept or word: '{word}'.
Tone requirement: {tone}.

Formatting requirements:
1. First, provide an engaging, informative paragraph (around 100-140 words) capturing the definition, significance, and context of the word.
2. Next, list 3 quick key bullet takeaways.
3. Finish with 1 sentence showing a real-world example or practical application.

Keep the language clear, natural, and informative."""

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error communicating with Gemini API: {e}"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="GenAI Word Information Generator")
    parser.add_argument("word", nargs="?", default="Entropy", help="The word or term to explain")
    parser.add_argument("--tone", choices=["general", "technical", "simple", "historical"], default="general", help="Explanation tone")
    
    args = parser.parse_args()
    print(f"\n--- Generating Explanation for: '{args.word}' (Tone: {args.tone}) ---\n")
    result = explain_word(args.word, args.tone)
    print(result)
    print("\n-------------------------------------------------------------")
