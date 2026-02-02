# LangChain Output Parsers – Beginner Notes

---

## What is an Output Parser?

An output parser converts the raw LLM response into a structured format.

LLMs usually return plain text.

Output parsers make it:

- Clean
- Structured
- Machine usable

---

## Why Use Output Parsers?

They help:

- Extract data
- Enforce format
- Reduce messy outputs

---

## Basic Idea

LLM response (text) → Output Parser → Structured output

---

## Common Types of Output Parsers

### StrOutputParser

Returns plain string.

Used when you just want clean text.

---

### JSONOutputParser

Forces output into JSON format.

Useful for:

- APIs
- Structured data
- Agents

---

### PydanticOutputParser

Uses Pydantic models to validate output structure.

Useful for:

- Strong typing
- Reliable data formats

---

## Conceptual Example

LLM output:

"Name: John, Age: 25"

Output Parser →

{
  "name": "John",
  "age": 25
}

---

## Why Parsers Matter

They:

- Make AI outputs predictable  
- Help automation  
- Reduce errors  

---

## Quick Summary

Output Parser  
→ Converts LLM text into usable format

Common ones:
- StrOutputParser
- JSONOutputParser
- PydanticOutputParser

---

## Beginner Focus

Start with:

- StrOutputParser  
- JSONOutputParser  

Then move to Pydantic later.
