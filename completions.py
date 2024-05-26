from openai import AzureOpenAI

def get_completion_result(client: AzureOpenAI, model: str, messages: list[dict]) -> str:
    completion = client.chat.completions.create(
        model=model,
        messages=messages
    )

    return completion.choices[0].message.content