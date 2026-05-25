from flask import Flask, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Render!"

@app.route("/ask", methods=["GET", "POST"])
def ask():
    if request.method == "POST":
        data = request.get_json(silent=True)
        question = data.get("question") if data else None
        return {"answer": f"You asked: {question}"}
    return "Ask endpoint is working!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

# Configure Gemini with your API key
genai.configure(api_key="AIzaSyB5H_bUuwomSkkFS-GgmBuxig3N9kZ8BuY")  # Replace with your actual key

# --- Static chatbot responses ---
class GenAIChatbot:
    def __init__(self):
        self.options = {
            "1": self.what_is_genai,
            "2": self.genai_applications,
            "3": self.genai_advantages,
            "4": self.genai_limitations,
            "5": self.list_ai_tools,
            "6": self.latest_ai_tools
        }

    def what_is_genai(self):
        return "GenAI refers to AI systems that generate text, images, audio, or code by learning from large datasets."

    def genai_applications(self):
        return "Applications: content creation, tutoring, grading, translation, visual materials, chatbots."

    def genai_advantages(self):
        return "Advantages: saves time, personalized learning, engagement, inclusivity, innovation."

    def genai_limitations(self):
        return "Limitations: bias, plagiarism risk, privacy concerns, teacher training needed, infrastructure dependence."

    def list_ai_tools(self):
        return "Tools: Grammarly, QuillBot, ChatGPT, DALL-E, Wolfram Alpha, Labster."

    def latest_ai_tools(self):
        return "Latest: Perplexity AI, Khanmigo, Eduaide.AI, Microsoft Copilot, Gradescope, Consensus, Diffit."

    def fallback(self):
        return "Please choose a valid option (1–6)."

    def get_response(self, choice):
        return self.options.get(choice, self.fallback)()

bot = GenAIChatbot()

# --- Flask routes ---
@app.route("/chat", methods=["POST"])
def chat():
    """
    Handles structured menu queries (1–6).
    """
    data = request.get_json()
    choice = data.get("choice", "")
    response = bot.get_response(choice)
    return jsonify({"response": response})

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    user_query = data.get("query", "")

    # Use the correct Gemini model name
    model = genai.GenerativeModel("models/gemini-2.5-flash")
    response = model.generate_content(user_query)

    return jsonify({"response": response.text})


if __name__ == "__main__":
    app.run(debug=True)
