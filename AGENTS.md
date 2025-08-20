# Documentation-First Routing (Always Apply)

    **Policy:** For user requests involving code examples, setup/configuration steps, or library/API docs, route via a documentation-focused MCP tool.

- Preferred tools: `docfork`, `sourcebot`, `git-mcp` (set `owner/repo`), generic RAG
- Fallbacks:
- Detection cues: "example", "install", "configure", "setup", "API", "SDK", "how to", "usage", "params", "options".
- Guardrails: Read-only unless explicitly elevated; no secrets exposure; respect repo permissions.

    **Example Invocation (conceptual):**
- User: "Show me how to configure OAuth for Service X."
- Agent: Selects `docfork` → extracts relevant guides → returns step-by-step with citations.


