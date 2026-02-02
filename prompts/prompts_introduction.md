# LangChain Prompts – Beginner Notes

---

## What is a Prompt?

A prompt is the input given to a language model.

In LangChain, prompts are structured using PromptTemplate to make them dynamic and reusable.

---

## Why Use PromptTemplate?

Instead of writing raw strings, PromptTemplate allows:

- Variable insertion
- Clean formatting
- Reusability

---

## Basic Idea

PromptTemplate takes variables and creates a final prompt.

Example (concept):

Input variables → Template → Final prompt text

---

## Common Types of Prompts

### PromptTemplate

Used for single message prompts.

It contains:
- Template string
- Input variables

---

### ChatPromptTemplate

Used for chat-based models.

It allows:
- System messages
- Human messages
- AI messages (optional)

---

## Example Flow (Conceptual)

User input → PromptTemplate → Formatted prompt → LLM

---

## Why Prompts Matter

Good prompts:

- Improve response quality
- Control model behavior
- Reduce randomness

---

## Best Practices

- Be clear and specific  
- Use variables for dynamic input  
- Give context when needed  

---

## Quick Summary

Prompt  
→ Input text for LLM

PromptTemplate  
→ Structured reusable prompt

ChatPromptTemplate  
→ Prompt for chat-based models

---

## Beginner Focus

Learn first:

- PromptTemplate
- ChatPromptTemplate

These cover most real use cases.
