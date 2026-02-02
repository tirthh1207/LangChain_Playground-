from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableBranch
from dotenv import load_dotenv
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation",
    temperature=0.3)
model = ChatHuggingFace(llm=llm)

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template='Explain {topic} in siple words.',
    input_variables=['topic']
)
prompt2 = PromptTemplate(
    template='Summarize this text in unter 500 words.\n Text: {text}',
    input_variables=['text']
)

chain1 = prompt1 | model | parser 
chain2 = RunnableBranch(
    (lambda x : len(x.split()) > 500, chain1 | prompt2 | model | parser),
    RunnablePassthrough()
)

chain3 = chain1 | chain2
result = chain3.invoke({'topic': 'AI'})

print(result)