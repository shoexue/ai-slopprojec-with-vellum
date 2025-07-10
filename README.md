# 📚 Document-Grounded Study Assistant

This web app helps students study more effectively by querying uploaded class notes, readings, or PDFs. Unlike generic chatbots, it **never hallucinates**—if a question falls outside the scope of the provided documents, it responds with “No response” or “Can’t answer.” The result is a trusted, context-grounded Q&A tool built with **Flask**, **React**, and **Vellum AI**.

---

## ⚙️ How Vellum Was Used

The backend intelligence is fully orchestrated by Vellum:

### 🧠 RAG Workflow & CLI Integration
- Built a **Retrieval-Augmented Generation (RAG)** pipeline using Vellum’s no-code **Workflow builder**, combining search, prompt, branching, and output nodes.
- Integrated the entire workflow into the Flask backend using the **Vellum CLI**, allowing seamless code export and deployment.

### 📄 Document Ingestion & Retrieval
- Users upload PDFs or notes via `/api/upload-documents`.
- Documents are automatically segmented, embedded, and indexed using Vellum's API.
- A **Search Node** retrieves relevant chunks based on the user's query at runtime.

### 📝 Prompted, Grounded Generation
- Retrieved content is passed through a **Prompt Node**, which generates a response strictly based on that context.
- If no relevant context is found, the response is safely declined to avoid hallucinations.

### 🧪 Evaluation & Monitoring
- Vellum’s built-in evaluation suite was used to monitor retrieval accuracy, faithfulness, and output correctness.
- Integrated logs, latency metrics, and versioning support for ongoing improvement and observability.

---

## ✨ Why Vellum?

- **No/Low-Code with Full Control** – Visually build and edit workflows, then export them to production-ready code.
- **Flexible Model Integration** – Supports OpenAI, Anthropic, Cohere, and other providers.
- **Grounded Answers** – Ensures answers are always tied to uploaded documents, with fallback logic that avoids hallucinations.
- **Powerful Evaluation Tools** – Built-in support for testing, scoring, and improving RAG pipeline quality.
- **Agentic Orchestration** – Create advanced flows with retries, conditional logic, and custom decision trees.
- **Observability** – Provides insights, logs, versioning, and latency tracking to improve reliability.

---

## 🧩 Tech Stack

| Component     | Role                                                                 |
|--------------|----------------------------------------------------------------------|
| **Flask**     | REST API for uploading documents and querying questions              |
| **React**     | Frontend UI for file uploads and question submission                 |
| **Vellum AI** | Handles all retrieval, generation, and evaluation behind the scenes  |

---

## 🎥 Demo

Click below to watch a short demo of the app in action:

[![Video Demo](https://github.com/user-attachments/assets/e277e8b3-63e3-4aef-bbe8-8bae528f643f)](https://github.com/user-attachments/assets/e277e8b3-63e3-4aef-bbe8-8bae528f643f)

---

## 🧠 Summary

Vellum AI transformed what would’ve been weeks of manual orchestration and LLM pipeline code into a fast, reliable, and maintainable AI backend. It helped speed up development dramatically while enforcing guardrails that prevent misinformation. With Vellum’s flexibility, observability, and powerful tools, this project was able to stay lightweight while delivering trustworthy AI results.

---


https://github.com/user-attachments/assets/e277e8b3-63e3-4aef-bbe8-8bae528f643f
