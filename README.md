# CBRkit Demo

To run the project, execute the following command:

```shell
poetry run python -m cbrkit_demo
```

# Hybrid Frame-Based Decision Modeling System

A modular knowledge representation prototype for decision-making grounded in **experiential**, **traditional**, and **indigenous knowledge**.

## Overview

This project attempts to model human sensemaking and ecological decision processes using:
- **Frames** for structured experiential knowledge
- **Graph Databases** for contextual relationships
- **Probabilistic Models** for uncertainty
- **ML/NLP Pipelines** for extracting knowledge from text or narratives

Inspired by ethnographic research and designed to be modular with Traditional Knowledg.

---

## Architecture

|        Layer        |        Technology        |       Description       |
|---------------------|--------------------------|-------------------------|
| Frame Layer         | Python classes           | Core symbolic knowledge |
| Graph Layer         | Neo4j                    | Knowledge graph storage |
| Probabilistic Layer | Pomegranate              | Uncertainty modeling    |
| ML/NLP Layer        | spaCy, Transformers      | Narrative ingestion     |
| UI Layer            | Streamlit                | Interactive dashboard   |

---

## Setup

```bash
git clone https://github.com/tuvafalk/arctic-phoenix.git
cd arctic-phoenix
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
