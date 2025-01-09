from openai import OpenAI

client = OpenAI(api_key="sk-613975d20507407399cb67b54a313504", base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model = "deepseek-chat",
    messages = [
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello"}
    ],
    stream = False
)

print(response.choices[0].message.content)