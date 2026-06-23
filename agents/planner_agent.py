from llm.llm_service import client
def planner_agent(query):
    prompt = f"""
    break the following research topic into clear research tasks.

    Topic:{query}

    Return a numbered task list.
    """

    response = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [{
            "role":"user",
            "content":prompt
        }
        ],
        temperature = 0.3
    )
    tasks = response.choices[0].message.content

    return tasks
