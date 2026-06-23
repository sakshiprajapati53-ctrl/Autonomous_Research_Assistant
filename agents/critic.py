from llm.llm_service import client
def critic_agent(query,retrieved_content):
    context = "\n".join(retrieved_content)

    prompt = f"""
    you are a research critic agent.
    evaluate the following research context.

    check:
    1-> missing information
    2-> weak evidence
    3-> hallucination risk
    4-> research quality

    query:{query}

    context:{context}

    return:
    -> strengths
    -> weaknesses
    -> confidence score out of 10
    """

    response = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages=[{
            "role":"user",
            "content":prompt
        }],
        temperature=0.2
    )

    critiquestion = response.choices[0].message.content

    return critiquestion