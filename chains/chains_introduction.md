# LangChain Chains – Beginner Notes

---

## What is a Chain?

A Chain connects multiple components together.

Each step’s output becomes the next step’s input.

---

## Purpose of Chains

Chains allow:

- Multi-step workflows
- Organized pipelines
- Complex AI logic

---

## Basic Idea

Prompt → LLM → Output Parser

This is the simplest chain.

---

## Traditional Chains (Older LangChain)

Earlier versions used:

- LLMChain
- SequentialChain

These are now mostly replaced by Runnables.

---

## Modern Approach

LangChain now prefers:

RunnableSequence

Instead of old chain classes.

---

## Example Concept

Step 1: Format prompt  
Step 2: Call model  
Step 3: Parse output  

Connected in sequence.

---

## Types of Chains (Conceptual)

### Simple Chain
Single flow of steps.

---

### Sequential Chain
Multiple steps in order.

---

### Conditional Chain
Different flows based on input.

---

### Parallel Chain
Multiple outputs at once.

---

## Why Chains Are Important

They:

- Structure AI workflows  
- Enable complex systems  
- Form base of agents  

---

## Relationship with Runnables

Chains = Built using Runnables

Modern LangChain pipelines are Runnable-based chains.

---

## Quick Summary

Chain  
→ Connected sequence of components

Basic chain:

Prompt → LLM → Parser

Modern chains use:

RunnableSequence

---

## Beginner Focus

Understand:

- Simple sequential flow
- How chains map to Runnables

Old chain classes are less important now.
