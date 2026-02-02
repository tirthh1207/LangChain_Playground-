# LangChain Models – Beginner Notes

---

## What is a Model in LangChain?

A model is the component that generates responses using AI.

It takes input (prompt or messages) and produces output (text or structured response).

In LangChain, models are wrapped in a standard interface so they work easily in pipelines.

---

## Main Types of Models in LangChain

LangChain mainly works with:

- LLMs (Large Language Models – text in, text out)
- Chat Models (message-based conversation models)
- Embedding Models (convert text into vectors)

---

# 1. LLM (Large Language Model)

LLMs take plain text as input and return plain text as output.

### Input:
A string prompt

### Output:
Generated text

### Example Use:
- Simple question answering
- Text generation

---

# 2. Chat Models

Chat models work with messages instead of plain text.

Messages have roles like:

- System (instructions)
- Human (user input)
- AI (model response)

### Input:
List of messages

### Output:
AI message

### Example Use:
- Chatbots
- Assistants
- Agents

---

# 3. Embedding Models

Embedding models convert text into numerical vectors.

These vectors represent meaning.

### Input:
Text

### Output:
Vector (list of numbers)

### Example Use:
- Semantic search
- RAG (Retrieval Augmented Generation)
- Similarity matching

---

## How Models Fit in LangChain Pipelines

Typical flow:

Prompt → Model → Output Parser

Or for RAG:

Query → Embedding → Retriever → Model

---

## Why LangChain Wraps Models

LangChain provides:

- Unified interface
- Easy chaining
- Integration with workflows (Runnables)

This avoids writing custom API code every time.

---

## Core Idea

Models are the “brain” of the system.

Everything else (prompts, chains, retrievers) supports models.

---

# Quick Summary

Model  
→ AI that generates or processes text

Types:

- LLM → text in, text out  
- Chat Model → message-based interaction  
- Embedding Model → text to vectors  

Models are used inside pipelines and agents.

---

# Beginner Focus

Start by understanding:

- Chat Models (most used today)
- Embedding Models (important for RAG)

Plain LLMs are less common in modern apps.
