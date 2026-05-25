import sys

class GenAIChatbot:
    def __init__(self):
        self.options = {
            "1": self.what_is_genai,
            "2": self.genai_applications,
            "3": self.genai_advantages,
            "4": self.genai_limitations,
            "5": self.list_ai_tools,
            "6": self.latest_ai_tools,
            "7": self.responsible_ai,
            "8": self.future_trends,
            "9": self.case_study,
            "10": self.faq
        }

    def greet(self):
        print("\n🤖 Hello! I am your GenAI chatbot to help you understand Generative AI (GenAI) in Higher Education.\n")
        print("Choose a topic by typing its number:\n"
              "1. What is GenAI?\n"
              "2. Applications in Education\n"
              "3. Advantages\n"
              "4. Limitations\n"
              "5. AI Tools in Teaching\n"
              "6. Latest AI Tools\n"
              "7. Responsible & Ethical AI\n"
              "8. Future Trends in AI\n"
              "9. Case Study Example\n"
              "10. FAQs for Beginners\n"
              "Type 'exit' to quit.\n")

    def what_is_genai(self):
        return ("GenAI, or Generative Artificial Intelligence, refers to AI systems (like GPT-4, DALL-E) "
                "that can generate text, images, audio, code, and more. These systems learn patterns from large datasets "
                "and produce new, coherent outputs useful in education, research, and creative fields.")

    def genai_applications(self):
        return ("Applications in Higher Education:\n"
                "- Automated content creation (quizzes, summaries)\n"
                "- Personalized tutoring and adaptive learning\n"
                "- Automated grading and feedback\n"
                "- Language translation and transcription\n"
                "- Creation of visual materials (diagrams, infographics)\n"
                "- Virtual teaching assistants and chatbots")

    def genai_advantages(self):
        return ("Advantages:\n"
                "- Saves time for teachers\n"
                "- Provides personalized learning materials\n"
                "- Enhances student engagement\n"
                "- Supports inclusive education (languages, accessibility)\n"
                "- Enables innovation in teaching methods")

    def genai_limitations(self):
        return ("Limitations:\n"
                "- Bias or inaccuracies in AI outputs\n"
                "- Risk of plagiarism or misuse\n"
                "- Privacy concerns with student data\n"
                "- Requires teacher training\n"
                "- Dependence on infrastructure")

    def list_ai_tools(self):
        return ("AI Tools in Teaching:\n"
                "- Grammarly (writing support)\n"
                "- QuillBot (paraphrasing)\n"
                "- ChatGPT (content generation)\n"
                "- DALL-E (image creation)\n"
                "- Wolfram Alpha (computational engine)\n"
                "- Labster (virtual science labs)")

    def latest_ai_tools(self):
        return ("Latest AI Tools:\n"
                "- Perplexity AI (research assistant)\n"
                "- Khanmigo (AI tutor by Khan Academy)\n"
                "- Eduaide.AI (lesson planning)\n"
                "- Microsoft Copilot (productivity)\n"
                "- Gradescope (AI grading)\n"
                "- Consensus (summarizes research)\n"
                "- Diffit (leveled reading materials)")

    def responsible_ai(self):
        return ("Responsible AI means developing and using AI ethically:\n"
                "- Transparency and explainability\n"
                "- Fairness and inclusiveness\n"
                "- Privacy and security\n"
                "- Accountability in AI decisions\n"
                "- Following UNESCO and G7 guidelines")

    def future_trends(self):
        return ("Future Trends:\n"
                "- More personalized learning experiences\n"
                "- AI‑powered simulations and labs\n"
                "- Integration with VR/AR for immersive teaching\n"
                "- AI for multilingual classrooms\n"
                "- Stronger focus on ethical AI policies")

    def case_study(self):
        return ("Case Study: AI in Language Learning\n"
                "A university used ChatGPT to support English writing classes. Students received instant feedback, "
                "improved grammar, and personalized exercises. Teachers reported reduced workload and higher student engagement.")

    def faq(self):
        return ("FAQs:\n"
                "Q: Is GenAI safe for students?\n"
                "A: Safe if used responsibly with teacher guidance.\n\n"
                "Q: Do I need coding skills?\n"
                "A: No, many tools are beginner‑friendly.\n\n"
                "Q: Can AI replace teachers?\n"
                "A: No, AI supports teachers but cannot replace human judgment and empathy.")

    def fallback(self):
        return "Please choose a valid option (1‑10) or type 'exit' to quit."

    def chat(self):
        self.greet()
        while True:
            user_input = input("Your choice: ").strip().lower()
            if user_input in ['exit', 'quit']:
                print("👋 Goodbye! Keep exploring AI responsibly in education.")
                sys.exit()
            response = self.options.get(user_input, self.fallback)()
            print("\nBot:", response, "\n")


if __name__ == "__main__":
    bot = GenAIChatbot()
    bot.chat()
