# Roadmap — Senior AI Developer Engineer Prep

Legend: `[ ]` not started · `[~]` in progress · `[x]` done (with date + one-line note)

---

## Phase 0 — Python Foundations
Goal: comfortable enough with Python to write MCP servers/agents without fighting syntax.

- [ ] Session 1: variables, types, f-strings, functions + type hints — build a "format a fake AWS scan result" script
- [ ] Session 2: dicts, lists, JSON — filter/transform a list of fake "resources"
- [ ] Session 3: control flow (if/for/while), list comprehensions
- [ ] Session 4: classes (just enough OOP) — a `ScanResult` class with methods
- [ ] Session 5: error handling (try/except), reading/writing files
- [ ] Session 6: venv + pip + `requests` — call a real public API (e.g. weather/GitHub API) and print structured output
- [ ] Session 7: async/await basics (needed for MCP servers and agent tool calls)
- [ ] Practice: LeetCode — 15 Easy problems, Python, tagged Array/String/HashMap/Two Pointers (this is about Python fluency, not FAANG-style DSA mastery)
- [ ] Practice: HackerRank "Python" track — complete the "Basic" + "Intermediate" sub-tracks
- [ ] Checkpoint: write a 50-line script solo (no help) that reads a JSON file, filters it, calls an API, and prints a summary

## Phase 1 — MCP (Model Context Protocol)
Goal: build and understand MCP servers well enough to design one in an interview whiteboard-style question.

- [ ] Read official docs: modelcontextprotocol.io — concepts (tools, resources, prompts, transports)
- [ ] Read the MCP Python SDK docs/README (github.com/modelcontextprotocol/python-sdk)
- [ ] Hands-on: build a minimal MCP server exposing one tool (e.g. "get current time" or "roll dice") — connect it to Claude Desktop/Claude Code and call it live
- [ ] Hands-on: add a second tool with structured input schema + error handling
- [ ] Hands-on: add a resource (read-only data, e.g. serve a local file's contents)
- [ ] Hands-on (stretch, bridges to InfraSync only if/when requested): MCP server that queries InfraSync's MongoDB for scan history
- [ ] Checkpoint: explain out loud (or write a paragraph) — tools vs resources vs prompts, stdio vs HTTP/SSE transport, why MCP solves the M×N integration problem

## Phase 2 — Vector Databases & ChromaDB
Goal: understand embeddings and vector search well enough to reason about tradeoffs, not just call APIs.

- [ ] Read: Chroma official docs "Getting Started"
- [ ] Read: one primer on embeddings + cosine similarity (pick any well-reviewed blog/doc, e.g. OpenAI or Cohere's embeddings guide)
- [ ] Hands-on: embed 10 sentences, store in Chroma, run similarity search, print nearest neighbors
- [ ] Hands-on: add metadata filtering to a query
- [ ] Read: HNSW indexing — high-level intuition (no need to implement it)
- [ ] Checkpoint: explain chunking strategy tradeoffs (size, overlap) and when hybrid search beats pure vector search

## Phase 3 — RAG (Retrieval-Augmented Generation)
Goal: build a real RAG pipeline end to end, and be able to debug "why is my RAG answer wrong."

- [ ] Read: any solid RAG overview (LangChain's RAG tutorial docs, official)
- [ ] Hands-on: build a RAG chatbot over InfraSync's `Docs/` folder (read-only reference — not modifying InfraSync code) using Chroma + Bedrock or Claude API
- [ ] Hands-on: add re-ranking or query rewriting as an improvement
- [ ] Hands-on: try RAGAS or a manual faithfulness/relevance eval on 5 sample Q&A pairs
- [ ] Checkpoint: diagnose a deliberately broken RAG setup (I'll seed a bug — bad chunking or wrong top-k) and fix it

## Phase 4 — LangChain / LangGraph & AI Agents
Goal: build a working agent loop with tools, memory, and a stop condition; explain ReAct and multi-agent patterns.

- [ ] Read: LangChain official docs — LCEL basics
- [ ] Read: LangGraph official docs — "Build a basic agent"
- [ ] Hands-on: build a 1-tool agent (ReAct loop) — watch it reason + call the tool
- [ ] Hands-on: expand to 2-3 tools with a real termination condition
- [ ] Hands-on: add simple memory (conversation buffer)
- [ ] Checkpoint: explain orchestrator-worker vs sequential pipeline vs debate pattern, and when an agent is overkill vs a plain deterministic chain

## Phase 5 — Amazon Bedrock
Goal: comfortable with Bedrock's Converse API, Knowledge Bases, Guardrails, and Agents — the "managed AWS" version of everything above.

- [ ] Read: official AWS Bedrock docs — Converse API
- [ ] Hands-on: call a Bedrock model (Claude via Bedrock) with `boto3` from Python
- [ ] Hands-on: stand up a Bedrock Knowledge Base pointed at S3 docs, compare to your hand-built Chroma RAG
- [ ] Hands-on: add a Guardrail (PII/denied topics) and test it triggers
- [ ] Read: AgentCore overview docs
- [ ] Checkpoint: explain Converse vs InvokeModel, and why an enterprise picks Bedrock over calling Anthropic API directly

## Phase 6 — Amazon Q Developer
Goal: know its capabilities well enough to discuss in an interview (this one is lighter on hands-on, more product-literacy).

- [ ] Read: official Amazon Q Developer docs — features overview
- [ ] Hands-on: install Q Developer in VS Code, try inline completion + chat on a small script
- [ ] Hands-on: try `/dev` on a tiny feature request in a scratch repo
- [ ] Read: `/transform` (Java upgrade) case studies — enough to discuss it, no need to run it without a Java project
- [ ] Checkpoint: articulate Q Developer's differentiation vs Copilot (AWS-native context, /transform)

## Phase 7 — AI-Enabled SDLC Accelerators (synthesis)
Goal: tie everything together into a coherent "how AI fits across the SDLC" narrative for the interview.

- [ ] Write a one-page personal summary: where AI plugs into requirements/coding/review/testing/docs/IaC/observability
- [ ] Identify 2-3 real examples from InfraSync work you can cite in an interview (already using Claude Code day to day)
- [ ] Checkpoint: mock interview round — I play interviewer, you answer live, I critique

## Phase 8 — Interview Readiness
- [ ] Full mock interview: system design question ("design a RAG-based support bot" or similar)
- [ ] Full mock interview: rapid-fire concept Q&A across all phases above
- [ ] LeetCode: revisit 10 more problems focused on whatever came up weak in Phase 0
- [ ] Final gap check: re-skim this roadmap, mark any checkpoint that still feels shaky, revisit that phase

---

## Session Log
(Add a dated one-liner here every time a task is completed or a session ends)

- 2026-07-08: Roadmap created. Next up: Phase 0, Session 1.
