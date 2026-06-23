from openai import OpenAI
from config import OPENAI_API_KEY

client =  OpenAI(api_key = OPENAI_API_KEY)

def generate_answer(query,context):

    #combine chunks
    combined_context = "\n".join(context)

    #prompt 
    prompt = f"""
    you are AI research assistant.

    Answers the user's question
    using only the provided context.

    Context: {combined_context}
    Question: {query}
    Answer:
    """

    #llm 
    response = client.chat.completions.create(

        model = "gpt-3.5-turbo",
        messages=[{
            "role":"system",
            "content": (
                "you are a helpful"
                "AI researcher."
            )
        },
        {"role":"user",
         "content":prompt
         }
        ],
        temperature=0.3
    )

    answer = response.choices[0].message.content

    return answer