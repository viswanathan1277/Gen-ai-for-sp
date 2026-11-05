import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv("GEMINI_API_KEY")
if API_KEY and API_KEY != "your_gemini_api_key_here":
    genai.configure(api_key=API_KEY)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/explain", methods=["POST"])
def explain():
    data = request.get_json() or {}
    word = data.get("word", "").strip()
    tone = data.get("tone", "general").strip()

    if not word:
        return jsonify({"error": "Please provide a word to explain."}), 400

    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key or api_key == "your_gemini_api_key_here":
        return jsonify({
            "error": "Gemini API key is not configured. Please add GEMINI_API_KEY to your .env file."
        }), 500

    prompt = f"""You are an educational assistant. Provide a structured, insightful explanation for the word or concept: '{word}'.
Tone preference: {tone}.

Structure your response into:
- An informative, cohesive paragraph (100-140 words) defining the term, why it matters, and how it works.
- 3 key bullet points summarizing core facts or characteristics.
- A 1-sentence real-world application or example.

Ensure the output is clean and easy to read."""

    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        return jsonify({
            "word": word,
            "tone": tone,
            "explanation": response.text
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    print(f"Starting LexiGen Web App on http://localhost:{port}")
    app.run(host="0.0.0.0", port=port, debug=True)
