import openai

api_key = "<ENTER-API-KEY-HERE>"

client = openai.OpenAI(
	api_key=api_key,
	base_url="https://litellm.plattform-int.k8s.ma.nrk.cloud"
)

# Example with text only
response = client.chat.completions.create(
    model="azure/gpt-5",
    messages=[
    {
        "role": "user",
        "content": "What is the capital of Norway?"
    }
]
)

print(response)