import sys
class GenAIChatbot:
    def __init__(self):
        self.responses = {
            "what is genai": self.what_is_genai,
            "application in education": self.genai_applications,
            "advantages": self.genai_advantages,
            "limitations": self.genai_limitations,
            "ai tools": self.list_ai_tools,
            "latest ai tools": self.latest_ai_tools
        }

    def greet(self):
        print("Hello! I am your GenAI chatbot to help you understand Generative AI (GenAI) in Higher Education.\n")
        print("Ask me about:\n"
              "- What is GenAI?\n"
              "- Application in Education\n"
              "- Advantages\n"
              "- Limitations\n"
              "- AI Tools in Language, Humanities, Arts, and Science Teaching\n"
              "- Latest AI Tools for Teaching, Learning, and Assessment\n"
              "Type 'exit' to quit.\n")

    def what_is_genai(self):
        return (
            "GenAI, or Generative Artificial Intelligence, refers to AI systems (like GPT-4, DALL-E, etc.) that can "
            "generate text, images, audio, code, and more, often in response to prompts. These systems use large-scale "
            "machine learning models, typically neural networks, to learn patterns and information from data and then produce new, "
            "coherent outputs similar to the data they were trained on."
        )

    def genai_applications(self):
        return (
            "GenAI has several applications in higher education, including:\n"
            "- Automated content creation (e.g., quizzes, summaries, feedback)\n"
            "- Intelligent tutoring and personalized learning experiences\n"
            "- Automated grading and assessment of assignments or student work\n"
            "- Language translation, transcription, and support for non-native speakers\n"
            "- Creation of visual materials for teaching (images, diagrams, etc.)\n"
            "- Interactive chatbots or virtual teaching assistants for Q&A"
        )

    def genai_advantages(self):
        return (
            "Advantages of GenAI in education:\n"
            "- Reduces repetitive workload for teachers (e.g., grading, feedback)\n"
            "- Provides tailored learning materials and adaptive resources\n"
            "- Enhances student engagement through interactive and multimodal content\n"
            "- Supports inclusive education (e.g., accessibility, language support)\n"
            "- Enables quick prototyping and deployment of educational innovations"
        )

    def genai_limitations(self):
        return (
            "Limitations and challenges of GenAI in education:\n"
            "- Potential for bias or inaccuracies in AI-generated content\n"
            "- Dependence on quality of data and appropriate prompts\n"
            "- Risks of plagiarism and misuse by students\n"
            "- Privacy concerns regarding student data\n"
            "- Requires teacher training and critical assessment of AI outputs"
        )

    def list_ai_tools(self):
        return (
            "AI Tools in Language, Humanities, Arts, and Science Teaching:\n\n"
            "1. Language and Humanities:\n"
            "   - Grammarly: Advanced writing assistant - https://www.grammarly.com/\n"
            "   - Quillbot: Paraphrasing and summarization - https://quillbot.com/\n"
            "   - ChatGPT: Conversational AI for writing and research - https://chat.openai.com/\n"
            "\n"
            "2. Arts:\n"
            "   - DALL-E: AI image generation from text - https://labs.openai.com/\n"
            "   - DeepDream Generator: AI-assisted art creation - https://deepdreamgenerator.com/\n"
            "   - Canva (Magic Write): AI design and content suggestions - https://www.canva.com/\n"
            "\n"
            "3. Science:\n"
            "   - Wolfram Alpha: Computational knowledge engine - https://www.wolframalpha.com/\n"
            "   - Elicit: AI research assistant for literature reviews - https://elicit.org/\n"
            "   - Scite: AI for citation analysis - https://scite.ai/\n"
        )

    def latest_ai_tools(self):
        return (
            "Latest AI Tools for Teaching, Learning, and Assessment:\n\n"
            "1. Perplexity AI (https://www.perplexity.ai/):\n"
            "   - An advanced research assistant that gives detailed, referenced answers to complex questions.\n"
            "\n"
            "2. Khanmigo (by Khan Academy - https://www.khanacademy.org/khan-labs):\n"
            "   - An AI-powered tutor and teaching assistant designed to support teachers and students with problem-solving, feedback, and more.\n"
            "\n"
            "3. Eduaide.AI (https://eduaide.ai/):\n"
            "   - Supports educators in creating lesson plans, quizzes, rubrics, and other teaching materials with AI assistance.\n"
            "\n"
            "4. Copilot (Microsoft - https://copilot.microsoft.com/):\n"
            "   - Assists in drafting, brainstorming, and interactive problem solving across Microsoft 365 apps.\n"
            "\n"
            "5. Gradescope (AI-assisted grading - https://www.gradescope.com/):\n"
            "   - Streamlines assignment grading with AI that groups similar answers and provides feedback templates.\n"
            "\n"
            "6. Consensus (https://consensus.app/):\n"
            "   - AI research tool that summarizes findings from scientific literature, enabling teachers to access up-to-date knowledge quickly.\n"
            "\n"
            "7. Diffit (https://www.diffit.me/):\n"
            "   - Generates leveled reading materials, comprehension questions, and summaries to personalize classroom resources using AI.\n"
            "\n"
            "These tools typically function by leveraging large language models or multi-modal AI systems to analyze input (text, images, or code), generate relevant content, and often provide interactivity, references, or links to authoritative sources. Most offer web-based platforms accessible through the provided links."
        )

    def fallback(self):
        return (
            "I am sorry, I didn't understand your question. "
            "Please ask about 'What is GenAI', 'Application in Education', 'Advantages', 'Limitations', 'AI tools', or 'Latest AI Tools'."
        )

    def get_response(self, user_query):
        # Normalize query for keyword search
        q = user_query.strip().lower()
        if "what is genai" in q or ("genai" in q and "what" in q):
            return self.what_is_genai()
        elif "application" in q or ("genai" in q and "education" in q):
            return self.genai_applications()
        elif "advantage" in q:
            return self.genai_advantages()
        elif "limitation" in q:
            return self.genai_limitations()
        elif ("tool" in q or "ai" in q) and ("language" in q or "humanities" in q or "art" in q or "science" in q):
            return self.list_ai_tools()
        elif "latest" in q or ("ai tools" in q and "assessment" in q):
            return self.latest_ai_tools()
        else:
            return self.fallback()

    def chat(self):
        self.greet()
        while True:
            user_input = input("You: ")
            if user_input.strip().lower() in ['exit', 'quit']:
                print("Goodbye! Have a great day teaching and learning with GenAI!")
                sys.exit()
            response = self.get_response(user_input)
            print("\nBot:", response, "\n")


if __name__ == "__main__":
    bot = GenAIChatbot()
    bot.chat()