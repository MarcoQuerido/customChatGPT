import openai
import gradio

openai.key = "sk-"

messages = [{"role": "system", "content": "You are a software engineer studying at university"}]


def customChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply


demo = gradio.Interface(fn=customChatGPT, inputs="text", outputs="text", title="Custom ChatGPT")

demo.launch()
