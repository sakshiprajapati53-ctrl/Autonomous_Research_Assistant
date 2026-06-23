from llm.llm_service import client

def writer_agent(query,research_content,critique):

    context = "\n".join(research_content)

    prompt = f"""
    You are an expert AI research writer.

    Create a professional research report.

    Topic:
    {query}

    Research Content:
    {context}

    Critic Feedback:
    {critique}

    Generate:
    1. Executive Summary
    2. Key Findings
    3. Challenges
    4. Future Scope
    5. Conclusion
    """

    response = client.chat.completions.create(

        model="gpt-3.5-turbo",

        messages=[{
            "role": "user",
            "content": prompt
            }
        ],

        temperature=0.3
    )

    report = response.choices[0].message.content

    return report