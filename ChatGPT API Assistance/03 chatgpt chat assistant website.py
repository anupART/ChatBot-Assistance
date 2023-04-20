import openai
import gradio

openai.api_key ="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"

messages = [{"role": "system", "content": "You are psycologist "}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Vortex Max")

demo.launch(share=True)