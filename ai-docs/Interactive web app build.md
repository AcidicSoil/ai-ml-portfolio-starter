You asked
----------

\# Hiro - Coding Specialist You are Hiro, a master-level coding optimization specialist. Your mission: transform coding requests into precise technical specifications that generate production-ready code. --- ## TECHNICAL ENHANCEMENT FRAMEWORK ### 1. ANALYZE REQUIREMENTS - Extract core functionality and technical constraints - Identify architecture patterns and performance needs - Map dependencies and integration requirements - Assess complexity and scope boundaries ### 2. APPLY STANDARDS - Enforce SOLID principles and design patterns - Implement comprehensive error handling - Apply security best practices and validation - Ensure type safety and defensive programming ### 3. STRUCTURE OUTPUT - Define clear technical specifications - Specify testing and documentation requirements - Include performance and scalability considerations - Provide deployment and maintenance guidelines --- ## OPTIMIZATION TECHNIQUES \*\*Foundation:\*\* Clean architecture, type safety, error handling, testing \*\*Advanced:\*\* Design patterns, performance optimization, security, scalability \*\*Technology Notes:\*\* - \*\*Frontend:\*\* Component architecture, state management, responsive design - \*\*Backend:\*\* API design, database optimization, caching strategies - \*\*Full-Stack:\*\* System integration, deployment pipelines, monitoring --- ## RESPONSE FORMAT Return only the improved prompt without additional explanations or metadata. --- ## USER CODING REQUEST: create an interactive, single-page web application to explore the "LLM Coding Agent Playbook for Solo Developers." This application will transform the detailed report into a user-friendly, explorable experience, focusing on intuitive navigation and interactive data visualization.

---

ChatGPT Replied
----------------

Thought for 40s

**Build a production‑ready, interactive single‑page web application to explore the “LLM Coding Agent Playbook for Solo Developers.”** The app will transform the long‑form report into an intuitive, explorable experience with rich navigation, comparisons, and interactive visualizations.

* * *

Tech Stack & Project Setup
--------------------------

* **Framework:** React 18 + **TypeScript** (strict) + **Vite**.

* **Styling:** Tailwind CSS + shadcn/ui (Radix primitives) with light/dark themes and semantic color tokens.

* **State:** Zustand (global UI state) + URL search params sync; React Query optional for future remote data (keep local now).

* **Routing:** React Router v6 with nested routes and hash/URL deep linking.

* **Data Viz:** Recharts (bar/line/area/radar/treemap) + D3 (sankey, force graph) where needed.

* **Content:** Playbook stored locally as Markdown + frontmatter and JSON; MDX renderer for rich blocks; DOMPurify for sanitization.

* **Search:** Fuse.js (fuzzy search) with staged indexing and debounced input.

* **Validation:** Zod schemas for all content types; runtime validation on load.

* **Build Quality:** ESLint (typescript + react), Prettier, Husky + lint‑staged, commitlint.

* **Testing:** Vitest + React Testing Library (unit), Playwright (e2e), jest‑axe/axe‑core (a11y).

* **Docs:** Storybook for key UI components (cards, chips, charts, modals).

* **PWA:** Vite plugin PWA (installable, offline cache for assets/data).

**Directory structure**

    /src
      /app        // routing, providers, error boundaries
      /components // UI primitives & compound components
      /features   // feature‑sliced domains (explorer, compare, prompts, notes)
      /data       // schemas, repositories, adapters
      /pages      // route components
      /viz        // charts and d3 helpers
      /styles     // tailwind config extensions, tokens
      /utils      // helpers (kbd, format, url, guards)
    /public/data
      playbook.json
      playbook.md


* * *

Data Model (Zod + TypeScript)
-----------------------------

Design for extensibility and relations.

    // tags: ['phase:ideation','phase:scaffold','phase:code','phase:test','phase:ship','risk','tool','pattern','prompt','metric']
    const zRef = z.object({ id: z.string(), type: z.enum(['pattern','workflow','tool','prompt','metric','risk']), weight: z.number().optional() });

    const zPattern = z.object({
      id: z.string(), title: z.string(), summary: z.string(),
      phase: z.enum(['Ideation','Scaffolding','Coding','Review','Testing','Deployment']),
      difficulty: z.enum(['Beginner','Intermediate','Advanced']),
      roi: z.number().min(0).max(10),
      steps: z.array(z.string()),
      bestPractices: z.array(z.string()),
      antiPatterns: z.array(z.string()).optional(),
      prompts: z.array(z.string()).optional(),
      tools: z.array(z.string()).optional(),
      metrics: z.array(z.string()).optional(),
      risks: z.array(z.string()).optional(),
      tags: z.array(z.string()).default([]),
      links: z.array(z.string()).optional(),
      relations: z.array(zRef).default([]) // graph edges
    });

    const zWorkflow = z.object({
      id: z.string(), title: z.string(), summary: z.string(),
      stages: z.array(z.object({ name: z.string(), goals: z.array(z.string()), artifacts: z.array(z.string()) })),
      kpis: z.array(z.string()).optional(),
      tags: z.array(z.string()).default([]),
      relations: z.array(zRef).default([])
    });

    const zTool    = z.object({ id: z.string(), name: z.string(), category: z.string(), cost: z.string().optional(), url: z.string().url().optional(), strengths: z.array(z.string()), limits: z.array(z.string()), tags: z.array(z.string()).default([]), relations: z.array(zRef).default([]) });
    const zPrompt  = z.object({ id: z.string(), title: z.string(), body: z.string(), useCases: z.array(z.string()), inputs: z.array(z.string()).optional(), outputs: z.array(z.string()).optional(), tags: z.array(z.string()).default([]), relations: z.array(zRef).default([]) });
    const zMetric  = z.object({ id: z.string(), name: z.string(), desc: z.string(), scale: z.enum(['ordinal','ratio','percent']), compute: z.string().optional(), tags: z.array(z.string()).default([]) });
    const zRisk    = z.object({ id: z.string(), name: z.string(), mitigation: z.array(z.string()), severity: z.enum(['Low','Med','High']), tags: z.array(z.string()).default([]) });

    const zPlaybook = z.object({
      version: z.string(),
      updatedAt: z.string(),
      patterns: z.array(zPattern),
      workflows: z.array(zWorkflow),
      tools: z.array(zTool),
      prompts: z.array(zPrompt),
      metrics: z.array(zMetric),
      risks: z.array(zRisk)
    });


**Sample seed (put in `/public/data/playbook.json`)**

    {
      "version": "1.0.0",
      "updatedAt": "2025-08-01",
      "patterns": [
        { "id": "pat.scaffold-repo", "title": "Repo Scaffolding via Agent", "summary": "Use an agent to initialize repo, CI, and linting.", "phase": "Scaffolding", "difficulty": "Beginner", "roi": 8, "steps": ["Collect requirements","Generate skeleton","Wire CI"], "bestPractices": ["Idempotent scripts","Template versioning"], "tags": ["phase:scaffold","pattern"] }
      ],
      "workflows": [
        { "id": "wf.solo-dev-loop", "title": "Solo Dev Agent Loop", "summary": "Plan → Code → Review → Test → Ship with tight feedback.", "stages": [{ "name":"Plan","goals":["Define scope"]},{"name":"Code","goals":["Implement"]},{"name":"Review","goals":["Self‑review with agent"]},{"name":"Test","goals":["Run & fix"]},{"name":"Ship","goals":["Release"]}], "tags":["workflow"] }
      ],
      "tools": [
        { "id": "tool.llm-cli", "name": "LLM CLI", "category": "CLI", "strengths": ["Scriptable","Local history"], "limits": ["No GUI"], "tags": ["tool"] }
      ],
      "prompts": [
        { "id": "pr.audit", "title": "Code Audit Prompt", "body": "Audit this repo for security, performance, and tests…", "useCases": ["Review","Hardening"], "tags": ["prompt"] }
      ],
      "metrics": [
        { "id": "mttm", "name": "Mean Time to Merge", "desc": "Avg time from PR open to merge.", "scale": "ratio", "tags": ["metric"] }
      ],
      "risks": [
        { "id": "risk.hallucination", "name": "Spec Hallucination", "mitigation": ["Schema validation","Golden tests"], "severity": "High", "tags": ["risk"] }
      ]
    }


* * *

Core Features & UX
------------------

1. **Homepage Overview**

    * Hero with title, version, last updated.

    * KPI cards (counts of patterns/tools/prompts).

    * “Start exploring” CTA; recently viewed; saved bookmarks.

2. **Left Sidebar Navigation**

    * Collapsible tree by **Phase**, **Type**, and **Tags**.

    * Filters: phase, difficulty, ROI range, severity, category, free‑text tags.

    * Persist open/closed state in localStorage.

3. **Global Command Palette (⌘/Ctrl‑K)**

    * Fuzzy search across titles, tags, summaries.

    * Quick actions: toggle theme, open compare, copy prompt, jump to section.

4. **Explorer Grid/List**

    * Cards with badges (phase, difficulty, ROI, severity).

    * Virtualized list for performance; grid/list toggle; sort by ROI/difficulty/updatedAt.

5. **Detail Panel (Split‑View)**

    * MDX rendering for rich content (code, callouts).

    * Related items (based on `relations`) shown as chips; click to pivot.

    * Actions: **Bookmark**, **Copy Prompt**, **Export as Markdown/JSON**, **Open in Compare**.

6. **Interactive Visualizations**

    * **Lifecycle Sankey:** flows among phases based on `relations` weights (D3 sankey).

    * **ROI vs Difficulty Scatter:** select patterns to highlight (Recharts).

    * **Risk Heatmap:** severity × phase matrix (Recharts heatmap/treemap).

    * **Force Graph:** entity network (patterns/tools/prompts/metrics/risks) with hover tooltips.

    * **Radar:** competency radar for workflows (stages mapped to capability axes).

7. **Compare Workspace**

    * Side‑by‑side comparison of up to 4 items (patterns/tools/prompts).

    * Auto‑generated diff table (attributes, steps, risks, metrics).

    * “Generate composite recipe” button builds a merged checklist (downloadable).

8. **Prompt Lab**

    * Gallery of prompts by use case; copy with one click; parameter slots with inputs.

    * “Explain this prompt” modal with rationale & variants.

    * Export selected prompts to `.md` or `.json`.

9. **Notes & Bookmarks**

    * Pin items; take per‑item notes (markdown) stored locally (localStorage/IndexedDB).

    * Export/import bookmarks + notes JSON.

10. **Deep Linking & Share**

    *   URL reflects current filters/selection; copyable link.

    *   Optional short link generation stub (no external calls by default).

11.  **Keyboard Shortcuts**

    *   `?` opens shortcut modal; `f` focus search; `b` toggle bookmarks; `c` open compare; `g` then `p`/`w`/`t` jump to sections.

12.  **Accessibility & i18n**

    *   WCAG 2.1 AA; focus rings, skip links, ARIA on widgets; prefers‑reduced‑motion.

    *   i18next scaffold with English JSON; content keys for UI strings.


* * *

Architecture & Patterns
-----------------------

* **Clean Architecture:** feature‑sliced folders; models/schemas isolated under `/data`; UI decoupled from parsing/rendering.

* **Repositories:** `PlaybookRepository` abstracts content source (JSON/MD) for future backends.

* **Error Boundaries:** per‑route and global; friendly fallbacks with retry.

* **Suspense & Code‑Splitting:** lazy load heavy viz/routes; prefetch likely next routes.

* **Defensive Programming:** zod parse at boundaries; exhaustive switch on enums; narrow types.

* **Security:** sanitize MDX/HTML with DOMPurify; CSP meta in `index.html`; no remote script eval; clipboard write guarded.

* * *

Components (Storybook with docs)
--------------------------------

* `Card`, `Badge`, `Tag`, `DataBadge`, `KpiCard`, `Toolbar`, `FilterChips`, `RangeSlider`, `SearchInput`, `CommandPalette`, `EntityCard`, `DetailPanel`, `RelationGraph`, `SankeyChart`, `ScatterChart`, `Heatmap`, `RadarChart`, `CompareTable`, `PromptTile`, `MarkdownViewer`, `NoteEditor`, `ExportModal`, `ShortcutModal`, `ThemeToggle`, `ErrorView`, `EmptyState`.

* * *

Data Ingestion
--------------

* **Initial Load:** fetch `/data/playbook.json`; validate (`zPlaybook.parse`); index with Fuse.

* **Markdown Support:** optional `/public/data/playbook.md` parsed to sections; build script converts MD → JSON via frontmatter (`/scripts/build-playbook.ts`).

* **Fixtures:** include the sample JSON above and 10–15 additional mock items (generated) to exercise visuals.

* * *

Performance
-----------

* Tailwind + CSS logical properties; container queries where useful.

* Virtualize long lists; debounce expensive filters; memoize selectors.

* Lazy load D3 charts; only mount visible charts; `ResizeObserver` for responsive charts.

* Lighthouse target: **≥95** Performance, **≥100** Best Practices, **≥100** Accessibility, **≥95** PWA.

* * *

Testing & Quality Gates
-----------------------

* **Unit:** schemas, repository, filtering, URL param sync, keyboard handlers.

* **Component:** card rendering, detail view, chart wrappers (smoke + prop mapping).

* **E2E (Playwright):** core journeys—search → view → compare → export; offline mode; theme toggle; a11y of modals.

* **A11y:** jest‑axe on key pages/components.

* **CI (GitHub Actions):** install → lint → typecheck → unit → e2e (headed=false) → build → upload artifact.

* * *

Deployment
----------

* **Static hosting** (Vercel/Netlify/GitHub Pages).

* Environment variable for base path (`VITE_BASE_PATH`); 404 fallback to SPA.

* PWA manifest + icons; service worker caching strategy: stale‑while‑revalidate for JSON, cache‑first for static assets.

* * *

Documentation
-------------

* **README:** setup, scripts, architecture diagram (Mermaid), data schema, contribution guidelines.

* **ADR‑001:** choose React+TS+Vite, explain tradeoffs.

* **USAGE.md:** how to add/extend playbook content & tags; how to script MD→JSON.

* * *

Acceptance Criteria
-------------------

1. App loads local playbook, validates with Zod, renders overview with KPIs.

2. Fuzzy search (⌘/Ctrl‑K) finds items by title/tag and navigates to detail in ≤150ms on 500 items.

3. Filters + sort sync to URL and persist on reload.

4. Visualizations render interactively and respond to selections/highlights.

5. Compare view generates diff table and composite recipe export.

6. Prompt Lab copies prompts with attribution and parameterization.

7. Bookmarks and notes persist locally; export/import works.

8. Meets WCAG 2.1 AA; lighthouse scores meet targets; tests pass in CI.

9. PWA installable; works offline for previously visited routes and data.

* * *

Deliverables
------------

* Full source code per structure above with strict TS types.

* Seed data and build script for Markdown ingestion.

* Test suite (unit/e2e) and CI config.

* Storybook with documented components.

* Production build artifact and deployment instructions.

---
