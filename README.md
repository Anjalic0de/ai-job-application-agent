# End-to-End Agentic AI Job Application System

## Overview

This project implements an end-to-end **agentic AI system** that automates the job application process. The agent processes a queue of job URLs and performs tasks such as resume tailoring, cover letter generation, ATS detection, and browser-based form interaction.

The system is designed with a modular architecture using **LangGraph for orchestration**, enabling scalable and extensible workflow automation.

---

## System Architecture

The agent follows a structured pipeline:

```
Fetch Job → Resume Generation → Cover Letter Generation → ATS Detection → Application Submission
```

Each stage operates on a shared **state object**, progressively enriching it with relevant data.

---

## Core Components

### 1. Agent Pipeline (LangGraph)

* Defines a directed workflow of tasks
* Each node processes and updates the shared state
* Ensures modular and maintainable design

### 2. AI Integration

* Resume and cover letter generation using LLMs
* Context-aware text generation based on job input

### 3. Browser Automation (Playwright)

* Opens job URLs dynamically
* Attempts to interact with application forms
* Simulates real user actions

### 4. Candidate Database (SQLite)

* Stores user profile (name, email, skills, etc.)
* Supports structured data retrieval
* Enables dynamic form filling

### 5. ATS Detection

* Detects platforms like:

  * Workday
  * Greenhouse
  * Lever
  * LinkedIn
* Based on URL pattern matching

---

## Form Field Mapping Strategy

The agent fills application forms using a hierarchical approach:

1. **Database Lookup** – Uses stored user profile data
2. **Custom Answers** – Handles additional form-specific inputs
3. **LLM Inference** – Generates responses when data is missing
4. **Human-in-the-Loop (HITL)** – Prompts user for unresolved fields

This ensures that no field is left unanswered when possible.

---

## Human-in-the-Loop (HITL)

* Triggered when the agent cannot confidently answer a field
* User is prompted for input during execution
* Responses can be stored for future reuse
* Improves adaptability over time

---

## Error Handling & Logging

* Graceful handling of inaccessible or invalid URLs
* Logs:

  * Application status (success / failed)
  * Failure reasons (e.g., ATS not detected, page load failure)
* Prevents pipeline crashes and ensures robustness

---

## Database Schema

### Users Table

* Name, email, phone
* Skills, experience, education
* Resume path

### Jobs Table

* Job URL, company, role
* ATS platform
* Status and failure reason

### Custom Answers Table

* Stores dynamic question–answer pairs
* Extensible without code changes

---

## Demo Setup

### Prerequisites

* Python 3.10+
* Virtual environment (recommended)

### Installation

```
pip install -r requirements.txt
playwright install
```

### Run the Agent

```
python main.py
```

---

## Demo Behavior

* Processes multiple job URLs sequentially
* Opens browser for each job
* Attempts form interaction
* Handles restricted pages gracefully

---

## Scalability Considerations

* Can be extended for multiple users via user_id mapping
* Queue-based job processing (e.g., Redis, Celery)
* Parallel agent execution for large-scale automation
* Integration with vector databases for better job–profile matching

---

## Key Highlights

* End-to-end autonomous workflow
* Modular agent-based architecture
* Real-world automation using Playwright
* Robust error handling and fallback mechanisms
* Extensible and production-oriented design

---

## Future Improvements

* Full ATS-specific form parsing
* Resume parsing and dynamic tailoring
* Advanced agent memory and personalization
* Integration with job platforms APIs

---

## Conclusion

This project demonstrates the design and implementation of a **production-oriented AI agent system** capable of automating complex workflows with minimal human intervention. It highlights strong capabilities in system design, AI integration, and automation engineering.
