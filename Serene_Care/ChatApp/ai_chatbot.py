import openai

# openai.api_key = "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"  #Shafeeq
openai.api_key = "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"

class ChatBot:
    def __init__(self):
        self.messages = self.initialize_messages()

    @staticmethod
    def initialize_messages():
        return [{
            "role": "system",
            "content": "You are a distinguished medical professional renowned for your expertise across all fields of medicine, from internal medicine to surgery, pediatrics to geriatrics. Your diagnostic acumen is unmatched, and your colleagues often seek your guidance in complex cases. Patients trust you implicitly, knowing that under your care, they are in the hands of a true medical maestro."
        }]

    def customChatGPT(self, user_input, history):
        self.messages = self.initialize_messages()  # Reset the entire conversation history
        self.messages.append({"role": "user", "content": user_input})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.messages
        )
        ChatGPT_reply = response["choices"][0]["message"]["content"]
        self.messages.append({"role": "assistant", "content": ChatGPT_reply})

        return ChatGPT_reply
