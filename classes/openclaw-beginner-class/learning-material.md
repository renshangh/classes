# Learning Material Notes

## Agentic AI Performance Framework

**Core equation:**

`Agentic AI performance = Model quality × Context quality × Tooling × Budget (tokens/latency)`

### 1) Model quality
- Reasoning depth
- Domain strength (coding, writing, multilingual, etc.)
- Reliability under long, multi-step tasks

### 2) Context quality
- Right information at the right time
- Clear task framing and constraints
- Low noise; high signal

### 3) Tooling
- Reliable tool calling and error handling
- Memory and retrieval quality
- Planning, retries, and verification loops

### 4) Budget (tokens/latency)
- Cost constraints shape architecture
- Latency requirements shape user experience
- Use tiered routing (cheap/fast first, escalate when needed)

## Practical Build Strategy
- Use a **tiered model stack**:
  1. Fast/cheap model for routine tasks and routing
  2. Strong reasoning model for hard tasks
  3. Specialist models for vision/voice/translation/long context
- Benchmark on your own workloads, not just public leaderboards.
- Add verification on high-risk outputs.

## One-line takeaway
Strong agents are not just “smart models” — they are smart systems.
