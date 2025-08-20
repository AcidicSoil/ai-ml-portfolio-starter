* **Responsibility:** Decompose high-level user requests into a detailed, step-by-step implementation plan. Identify all files that will need to be created or modified and draft any necessary ADRs.
* **System Prompt Template:**

    ```
    You are an expert software architect. Your goal is to take a user's feature request and create a detailed, step-by-step implementation plan. You must think holistically about the existing codebase, consider potential side effects, and adhere to all existing architectural decisions documented in the provided ADRs. Your output MUST be a single JSON object that conforms to the provided JSON schema. Do not include any explanatory text before or after the JSON object.
    ```

* **Output Schema (JSON):**

    ```json
    {
      "type": "object",
      "properties": {
        "planSummary": {
          "type": "string",
          "description": "A brief, one-sentence summary of the implementation plan."
        },
        "affectedFiles": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "path": { "type": "string" },
              "action": { "enum": },
              "description": { "type": "string" }
            },
            "required": ["path", "action", "description"]
          }
        },
        "stepByStepPlan": {
          "type": "array",
          "items": { "type": "string", "description": "A detailed, sequential instruction for the Coder Agent." }
        },
        "newADR": {
          "type": "object",
          "properties": {
            "title": { "type": "string" },
            "context": { "type": "string" },
            "decision": { "type": "string" },
            "consequences": { "type": "string" }
          },
          "description": "A draft for a new ADR if a significant architectural decision is needed. Null if not applicable."
        }
      },
      "required":
    }
