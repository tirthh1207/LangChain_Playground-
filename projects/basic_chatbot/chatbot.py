from langchain_core.prompts import PromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation",
    temperature=0.3
)

model = ChatHuggingFace(llm=llm)
parser = StrOutputParser()

# ---- Load past memory properly (STRING) ----

with open("chat_history.txt", "r", encoding="utf-8") as f:
    past_memory = f.read()

# ---- Chat prompt ----

prompt = ChatPromptTemplate.from_messages([
    ('system', 
     "You are a helpful AI assistant. Give short, direct answers.\n\n"
     "Past conversation context:\n{past_memory}"
    ),
    MessagesPlaceholder(variable_name='memory'),
    ('human', '{query}')
])

chain = prompt | model | parser

memory = []

# ---- Chat loop ----

while True:
    query = input('--> You: ')
    if query.lower() == 'exit':
        break

    response = chain.invoke({
        'past_memory': past_memory,
        'query': query,
        'memory': memory
    })

    print('--> AI:', response)

    memory.append(HumanMessage(content=query))
    memory.append(AIMessage(content=response))

# ---- Convert messages to clean text ----

def messages_to_text(messages):
    lines = []
    for msg in messages:
        if isinstance(msg, HumanMessage):
            lines.append(f"Human: {msg.content}")
        elif isinstance(msg, AIMessage):
            lines.append(f"AI: {msg.content}")
    return "\n".join(lines)

clean_text = messages_to_text(memory)

# ---- Summarizer prompt ----

merge_prompt = PromptTemplate(
    template='''You are a memory summarizer for an AI assistant and You are updating long-term memory.

Old memory:
{old_memory}

New session summary:
{new_summary}

Merge them into one clean updated memory.
Summarize ONLY what the USER has explicitly stated, confirmed, or asked for.
Ignore AI opinions, advice, or assumptions.

IMPORTANT RULES:
- Treat ONLY the user's (Human) messages as factual reality
- DO NOT assume AI responses are true or reflect user intent
- AI messages may contain suggestions, mistakes, or hypotheticals
- Never infer user actions, goals, or learning paths from AI messages
- If the user did not explicitly say something, do NOT include it
- Keep important long-term information
- Remove duplicates
- Update outdated info if new one replaces it
- Keep concise bullet points

''',
    input_variables=["old_memory", "new_summary"]
)


summary_chain = merge_prompt | model | StrOutputParser()

updated_memory = summary_chain.invoke({
    "old_memory": past_memory,
    "new_summary": clean_text
})

with open("chat_history.txt", "w", encoding="utf-8") as f:
    f.write(updated_memory)
