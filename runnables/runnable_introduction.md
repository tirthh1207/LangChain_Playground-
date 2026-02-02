# LangChain Runnables – Beginner Notes

---

## What is a Runnable?

In LangChain, a Runnable is a standardized execution unit.

It:
- Takes input
- Performs an operation
- Returns output

Almost all modern LangChain components are built as Runnables.

This allows:
- Easy chaining
- Workflow building
- Agent pipelines

---

## Structure of Runnables

Runnables are divided into two main categories:

Runnables  
├── Task-Specific Runnables  
└── Runnable Primitives  

---

# 1. Task-Specific Runnables

These are LangChain components that perform actual AI tasks.

### Purpose
Perform real operations like model calls, prompt formatting, and retrieval.

---

### Common Examples

#### LLM / Chat Model
Runs a language model.

Input → Prompt  
Output → Model response  

Examples:
- ChatOpenAI
- HuggingFace models

---

#### PromptTemplate
Formats input variables into a structured prompt.

Input → Variables  
Output → Final prompt string  

---

#### Retriever
Fetches relevant documents from a database or vector store.

Input → Query  
Output → Documents  

---

### Summary

Task-Specific Runnables are the workers of LangChain.

They handle:
- AI model calls
- Prompt creation
- Data retrieval

---

# 2. Runnable Primitives

These control how Runnables are connected and executed.

They do not perform AI tasks themselves.

---

## RunnableSequence

Runs steps one after another.

Output of each step becomes input to the next.

Example flow:

Prompt → LLM → Output Parser

---

## RunnableParallel

Runs multiple Runnables at the same time.

Useful for getting different outputs from the same input.

Example:
- Summary
- Sentiment analysis

---

## RunnableMap

Sends the same input to multiple Runnables.

Example:

Input text →  
- Summary  
- Keywords  
- Sentiment  

---

## RunnableBranch

Adds conditional logic to workflows.

Example:

If input is simple → fast model  
Else → complex pipeline  

---

## RunnableLambda

Wraps a custom Python function as a Runnable.

Used for:
- Data cleaning
- Formatting
- Custom processing

---

## RunnablePassthrough

Forwards input directly as output.

Used as a placeholder in pipelines.

---

# Core Concept

LangChain pipelines are built using:

Task-Specific Runnables → What work is done  
Runnable Primitives → How work flows  

Together they form powerful AI workflows.

---

# Simple Pipeline Example (Conceptual)

PromptTemplate  
↓  
LLM Model  
↓  
Output Parser  

(connected using RunnableSequence)

---

# Why Runnables Matter

They help you:

- Build modular systems
- Create clean pipelines
- Scale AI workflows
- Develop agent architectures

---

# Quick Summary

Runnable  
→ Standard execution block

---

Task-Specific Runnables:
- LLMs
- PromptTemplates
- Retrievers

Do real AI work.

---

Runnable Primitives:
- Sequence
- Parallel
- Map
- Branch
- Lambda
- Passthrough

Control workflow logic.

---

# Beginner Focus

Start by understanding:

- RunnableSequence
- RunnableLambda
- RunnableBranch

These are enough to build most real-world pipelines.
