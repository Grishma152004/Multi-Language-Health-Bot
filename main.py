import sys

class MedicalBot:
    def __init__(self):
        # Dictionary of symptoms and advice
        # You can add more keywords here easily
        self.knowledge_base = {
            "diabetes": {
                "en": "Early signs: frequent urination, excessive thirst, and fatigue. Please see a doctor for a blood test.",
                "gu": "Madhumay na lakshano: varamvar peshab thavo, vadhare taras lagvi ane thak lagvo. Loh ni tapas karavo.",
                "hi": "Diabetes ke lakshan: bar-bar peshab ana, zyada pyas lagna aur thakan. Blood test karwayein."
            },
            "fever": {
                "en": "Rest well and stay hydrated. If the temperature is above 102°F, consult a physician.",
                "gu": "Aaram karo ane vadhare pani pivo. Jo tap 102 thi vadhare hoy toh doctor ne batavo.",
                "hi": "Aaram karein aur pani piyein. Agar bukhar 102 se zyada hai toh doctor ko dikhayein."
            },
            "headache": {
                "en": "It could be due to stress or dehydration. Try resting in a dark room.",
                "gu": "Aa tanav ke nirjalikaran (dehydration) ne karne hoi shake che. Shanti thi aaram karo.",
                "hi": "Ye tanav ya pani ki kami se ho sakta hai. Shanti se aaram karein."
            },
            "sardi": {
                "en": "Common cold: Drink warm fluids and take rest.",
                "gu": "Sardi mate garam pani pivo ane vaf lo.",
                "hi": "Sardi ke liye garam pani piyein aur aaram karein."
            }
        }
        self.disclaimer = "\n\n[DISCLAIMER]: I am a rule-based AI, not a doctor. Consult a professional for medical advice."

    def find_response(self, user_input):
        user_input = user_input.lower()
        
        # Checking for matches in our knowledge base
        for key in self.knowledge_base:
            if key in user_input:
                res = self.knowledge_base[key]
                return f"Bot (EN): {res['en']}\nBot (GU): {res['gu']}\nBot (HI): {res['hi']}" + self.disclaimer
        
        return "Bot: I'm sorry, I don't have information on that. Try asking about Diabetes, Fever, or Sardi."

# --- Main Program ---
if __name__ == "__main__":
    bot = MedicalBot()
    print("--- 🩺 Professional Medical Assistant (Offline) ---")
    print("Type 'exit' to quit the chat.")
    print("Example: 'Tell me about diabetes' or 'Mane fever che'")
    
    while True:
        user_query = input("\nUser: ")
        
        if user_query.lower() in ['exit', 'quit', 'bye']:
            print("Bot: Take care! Goodbye.")
            break
            
        if not user_query.strip():
            continue
            
        print("-" * 30)
        print(bot.find_response(user_query))
        print("-" * 30)
