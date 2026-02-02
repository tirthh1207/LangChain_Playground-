# imports
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda
from pydantic import BaseModel, Field
from typing import Literal
from dotenv import load_dotenv

load_dotenv()

# Models
llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V3.2",
    task="text-generation")
model = ChatHuggingFace(llm = llm)

llm2 = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    temperature=0.7)
model2 = ChatHuggingFace(llm = llm2)

#parsers
parser = StrOutputParser()

class Feedback(BaseModel):

    sentiment : Literal['positive', 'negative'] = Field(description='Give the sentiment of the feedback')
# since it is a llm we dont have control on its responce so we need to structure the output using Pydantic output parser to get controled and consistent output.
parser2 = PydanticOutputParser(pydantic_object=Feedback)

# review
review = '''WI got a defective ASUS laptop — it would shut down during normal use, the screen was flickering, it would hang, and I couldn’t close apps from the taskbar. I complained to Amazon customer care within 3 days, while it was still under the replacement period. They told me to contact ASUS support.

I spoke with ASUS customer care, and they sent a technician. He checked and confirmed the problem, then said Windows would need to be reinstalled. I told him that this is a new product, and it shouldn’t arrive defective — I wanted a replacement, not a repair. He wrote down the issue in a letter and said he’d check with the company and get back to me.

Two days passed with no response. When I called again, they said the replacement request was cancelled. I contacted customer care again, and they sent another technician. He submitted a replacement request and took a copy of the invoice.

Now, for a replacement, a DOA (Dead on Arrival) letter is required, which is made using the details from the invoice. But my invoice didn’t have the laptop’s serial number. Because of that, ASUS refused to issue the DOA letter, saying you needed to talk to Amazon.

After talking to Amazon 5–7 times, they kept saying their policy doesn’t allow adding a serial number to the invoice. ASUS said they can’t make the DOA letter without it. Later, I gave them the warranty slip, and after 2–3 days they somehow managed to create the letter.

But when I tried to submit the replacement request on Amazon, they said replacement isn’t available at all — it won’t happen. They told me to contact the manufacturer or seller. The seller’s phone didn’t even connect. ASUS then said it’s Amazon’s issue, not theirs.

So now both of them are refusing to take responsibility, and the replacement just isn’t happening.

I recieved the defective laptop on 27 September , and today is 17 october and still nothing has changed.'''

# get detailed summary of review
prompt = PromptTemplate(
    template='''You are a customer experience analyst.

Summarize the following customer review clearly and objectively.

Guidelines:

Identify whether the review is positive, negative, or mixed

Highlight the main points the customer mentioned

Do NOT add assumptions or extra information

Keep it short and factual (2–4 bullet points or 2–3 lines)

Customer Review:
{feedback}''',
    input_variables=['feedback'])

# Get positive or negative
prompt1 = PromptTemplate(
    template=' Classify the sentiment of the following feedback text into possitive or negative:\n {feedback}. \n {format_instruction}',
    input_variables=['feedback'],
    partial_variables={'format_instruction': parser2.get_format_instructions()})

# Responce for positive review
prompt2 = PromptTemplate(
    template='''You are a customer support manager for a professional company.

Write a calm, polite, and empathetic response to the following negative customer review.

Guidelines:

Acknowledge the customer’s concern clearly

Apologize where appropriate (without admitting legal fault)

Offer a solution or next step

Keep the tone respectful and professional

Do not argue or sound defensive

Keep it concise but helpful

Customer Review:
{feedback}
''',
    input_variables=['feedback'])

# Responce for negative review
prompt3 = PromptTemplate(
    template='''You are a customer support manager for a professional company.

Write a warm, appreciative, and professional response to the following positive customer review.

Guidelines:

Thank the customer genuinely

Acknowledge what they liked specifically

Reinforce the company’s commitment to quality/service

Keep the tone friendly but professional

Keep it concise

Customer Review:
{feedback}
''',
    input_variables=['feedback'])

# summary of review
sentiment = prompt | model | parser
review_summary = sentiment.invoke({'feedback': review})

# classify positive or negaive
classifier_chain = prompt1 | model | parser2

# conditional runnable for positive or negative responce
branched_chain = RunnableBranch(
    (lambda x: x.sentiment == 'positive', prompt3 | model2 | parser),
    (lambda x: x.sentiment == 'negative', prompt2 | model2 | parser),
    RunnableLambda(lambda x: ' we could not find sentiment'))

# final chain for responce
chain = classifier_chain | branched_chain
result = chain.invoke({'feedback': review})

# Output
print('--> sentiment:\n',review_summary)
print()
print(result)