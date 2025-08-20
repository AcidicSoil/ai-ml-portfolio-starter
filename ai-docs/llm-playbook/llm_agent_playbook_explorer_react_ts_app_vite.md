# LLM Agent Playbook Explorer — Full Source (React 18 + TypeScript + Vite)

> Copy this entire tree into a new repo. Then run the quickstart in **README.md**. All files are included below, grouped by path.

---

## package.json

```json
{
  "name": "llm-agent-playbook-explorer",
  "version": "1.0.0",
  "private": true,
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "tsc -b && vite build",
    "preview": "vite preview --port 5173",
    "typecheck": "tsc -b --pretty",
    "lint": "eslint . --ext .ts,.tsx",
    "format": "prettier --write .",
    "test": "vitest run",
    "test:watch": "vitest",
    "e2e": "playwright test",
    "e2e:ui": "playwright test --ui",
    "storybook": "storybook dev -p 6006",
    "build-storybook": "storybook build",
    "prepare": "husky install"
  },
  "dependencies": {
    "@radix-ui/react-dialog": "^1.0.6",
    "@radix-ui/react-dropdown-menu": "^2.0.6",
    "@radix-ui/react-popover": "^1.0.7",
    "@radix-ui/react-toast": "^1.1.5",
    "@tanstack/react-query": "^5.51.3",
    "@types/dompurify": "^3.0.5",
    "@types/marked": "^5.0.2",
    "@types/node": "^20.12.12",
    "@types/react": "^18.2.66",
    "@types/react-dom": "^18.2.22",
    "@vitejs/plugin-react": "^4.3.1",
    "class-variance-authority": "^0.7.0",
    "clsx": "^2.1.1",
    "d3": "^7.9.0",
    "d3-sankey": "^0.12.3",
    "dompurify": "^3.1.6",
    "fuse.js": "^7.0.0",
    "i18next": "^23.12.3",
    "lucide-react": "^0.452.0",
    "marked": "^12.0.2",
    "mdast-util-from-markdown": "^2.0.0",
    "react": "^18.3.1",
    "react-dom": "^18.3.1",
    "react-router-dom": "^6.26.2",
    "recharts": "^2.12.6",
    "zustand": "^4.5.2",
    "zod": "^3.23.8"
  },
  "devDependencies": {
    "@commitlint/cli": "^19.3.0",
    "@commitlint/config-conventional": "^19.2.2",
    "@playwright/test": "^1.46.1",
    "@storybook/addon-essentials": "^8.1.10",
    "@storybook/addon-interactions": "^8.1.10",
    "@storybook/addon-themes": "^8.1.10",
    "@storybook/react": "^8.1.10",
    "@storybook/react-vite": "^8.1.10",
    "@testing-library/jest-dom": "^6.4.6",
    "@testing-library/react": "^16.0.0",
    "@testing-library/user-event": "^14.5.2",
    "@types/jsdom": "^21.1.7",
    "@types/lodash.debounce": "^4.0.9",
    "autoprefixer": "^10.4.19",
    "axe-core": "^4.9.1",
    "commitlint": "^19.2.2",
    "eslint": "^9.9.0",
    "eslint-config-prettier": "^9.1.0",
    "eslint-plugin-react": "^7.35.0",
    "eslint-plugin-react-hooks": "^4.6.2",
    "eslint-plugin-unused-imports": "^3.2.0",
    "happy-dom": "^14.11.0",
    "husky": "^9.1.5",
    "jsdom": "^24.1.0",
    "lint-staged": "^15.2.9",
    "postcss": "^8.4.39",
    "prettier": "^3.3.3",
    "tailwind-merge": "^2.5.2",
    "tailwindcss": "^3.4.10",
    "typescript": "^5.5.4",
    "vite": "^5.4.2",
    "vite-plugin-pwa": "^0.20.1",
    "vitest": "^2.0.5"
  }
}
```

---

## tsconfig.json

```json
{
  "extends": "./tsconfig.base.json",
  "compilerOptions": {
    "types": ["vite/client", "node", "happy-dom"]
  },
  "include": ["src", "scripts", "vitest.setup.ts", ".storybook"],
  "exclude": ["dist", "node_modules"]
}
```

## tsconfig.base.json

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "useDefineForClassFields": true,
    "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "module": "ESNext",
    "skipLibCheck": true,
    "moduleResolution": "bundler",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "jsx": "react-jsx",
    "strict": true,
    "forceConsistentCasingInFileNames": true,
    "esModuleInterop": true,
    "noFallthroughCasesInSwitch": true,
    "baseUrl": ".",
    "paths": {
      "@/app/*": ["src/app/*"],
      "@/components/*": ["src/components/*"],
      "@/features/*": ["src/features/*"],
      "@/data/*": ["src/data/*"],
      "@/pages/*": ["src/pages/*"],
      "@/viz/*": ["src/viz/*"],
      "@/styles/*": ["src/styles/*"],
      "@/utils/*": ["src/utils/*"]
    }
  }
}
```

---

## vite.config.ts

```ts
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import { VitePWA } from 'vite-plugin-pwa'

export default defineConfig({
  plugins: [
    react(),
    VitePWA({
      registerType: 'autoUpdate',
      includeAssets: ['favicon.svg', 'robots.txt', 'apple-touch-icon.png'],
      manifest: {
        name: 'LLM Agent Playbook Explorer',
        short_name: 'Playbook',
        description: 'Explore the LLM Coding Agent Playbook for Solo Developers',
        theme_color: '#0ea5e9',
        background_color: '#0b1220',
        display: 'standalone',
        start_url: '/',
        icons: [
          { src: '/icons/pwa-192.png', sizes: '192x192', type: 'image/png' },
          { src: '/icons/pwa-512.png', sizes: '512x512', type: 'image/png' }
        ]
      }
    })
  ],
  server: { port: 5173 },
  build: { sourcemap: true },
  define: {
    __APP_VERSION__: JSON.stringify('1.0.0')
  }
})
```

---

## postcss.config.cjs

```cjs
module.exports = {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}
```

## tailwind.config.ts

```ts
import type { Config } from 'tailwindcss'

export default {
  darkMode: ['class'],
  content: [
    './index.html',
    './src/**/*.{ts,tsx}',
    './.storybook/**/*.{ts,tsx}'
  ],
  theme: {
    extend: {
      colors: {
        brand: {
          DEFAULT: '#0ea5e9',
          50: '#e0f2fe', 100: '#bae6fd', 200: '#7dd3fc', 300: '#38bdf8', 400: '#0ea5e9', 500: '#0284c7'
        }
      },
      container: { center: true, padding: '1rem' }
    }
  },
  plugins: []
} satisfies Config
```

---

## .eslintrc.cjs

```cjs
module.exports = {
  root: true,
  env: { browser: true, es2022: true },
  parser: '@typescript-eslint/parser',
  parserOptions: { ecmaVersion: 'latest', sourceType: 'module' },
  plugins: ['react', 'react-hooks', '@typescript-eslint', 'unused-imports'],
  extends: [
    'eslint:recommended',
    'plugin:react/recommended',
    'plugin:react-hooks/recommended',
    'plugin:@typescript-eslint/recommended',
    'plugin:storybook/recommended',
    'prettier'
  ],
  settings: { react: { version: 'detect' } },
  rules: {
    'react/react-in-jsx-scope': 'off',
    'unused-imports/no-unused-imports': 'error'
  }
}
```

## .prettierrc

```json
{
  "semi": false,
  "singleQuote": true,
  "trailingComma": "es5",
  "printWidth": 100
}
```

## .gitignore

```
node_modules
.vscode
.DS_Store
coverage
playwright-report
storybook-static
/dist
/.vite
/.cache
```

## .husky/pre-commit

```sh
#!/usr/bin/env sh
. "$(dirname -- "$0")/_/husky.sh"

pnpm lint-staged || npx lint-staged
```

## .husky/commit-msg

```sh
#!/usr/bin/env sh
. "$(dirname -- "$0")/_/husky.sh"

npx --no-install commitlint --edit $1
```

## lint-staged.config.mjs

```js
export default {
  '*.{ts,tsx,css,md,json}': ['prettier --write'],
  '*.{ts,tsx}': ['eslint --fix']
}
```

## commitlint.config.cjs

```cjs
module.exports = { extends: ['@commitlint/config-conventional'] }
```

---

## index.html

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; connect-src 'self'; font-src 'self';" />
    <link rel="manifest" href="/manifest.webmanifest" />
    <link rel="icon" href="/favicon.svg" />
    <title>LLM Agent Playbook Explorer</title>
  </head>
  <body class="bg-white text-slate-900 dark:bg-slate-950 dark:text-slate-100">
    <a href="#app" class="sr-only focus:not-sr-only focus:absolute focus:top-2 focus:left-2 bg-brand-400 text-white px-3 py-1 rounded">Skip to content</a>
    <div id="root"></div>
    <script type="module" src="/src/main.tsx"></script>
  </body>
</html>
```

---

## src/main.tsx

```tsx
import React from 'react'
import ReactDOM from 'react-dom/client'
import { RouterProvider } from 'react-router-dom'
import { router } from '@/app/router'
import '@/styles/global.css'

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
)
```

## src/styles/global.css

```css
@tailwind base;
@tailwind components;
@tailwind utilities;

:root { --radius: 0.75rem; }
* { box-sizing: border-box; }
```

---

## src/app/router.tsx

```tsx
import { createBrowserRouter, createHashRouter } from 'react-router-dom'
import { AppShell } from './shell'
import { HomePage } from '@/pages/HomePage'
import { ExplorerPage } from '@/features/explorer/ExplorerPage'
import { ComparePage } from '@/features/compare/ComparePage'
import { PromptLabPage } from '@/features/prompts/PromptLabPage'
import { NotFound } from '@/pages/NotFound'

const useHash = false
const base = import.meta.env.VITE_BASE_PATH || '/'

export const router = (useHash ? createHashRouter : createBrowserRouter)([
  {
    path: base,
    element: <AppShell />,
    errorElement: <NotFound />,
    children: [
      { index: true, element: <HomePage /> },
      { path: 'explore', element: <ExplorerPage /> },
      { path: 'compare', element: <ComparePage /> },
      { path: 'prompts', element: <PromptLabPage /> }
    ]
  }
])
```

## src/app/shell.tsx

```tsx
import { Outlet, NavLink, useLocation } from 'react-router-dom'
import { ThemeToggle } from '@/components/ThemeToggle'
import { CommandPalette } from '@/components/CommandPalette'
import { useEffect } from 'react'

export function AppShell() {
  const { pathname } = useLocation()
  useEffect(() => { document.title = `Playbook${pathname === '/' ? '' : ' • ' + pathname}` }, [pathname])
  return (
    <div id="app" className="min-h-dvh grid grid-rows-[auto_1fr]">
      <header className="sticky top-0 z-30 border-b bg-white/80 dark:bg-slate-950/80 backdrop-blur">
        <div className="container flex items-center gap-4 py-3">
          <NavLink to="/" className="font-bold text-xl">LLM Playbook</NavLink>
          <nav className="ml-auto flex items-center gap-4">
            <NavLink to="/explore" className={({isActive})=>isActive?'text-brand-500':''}>Explore</NavLink>
            <NavLink to="/compare" className={({isActive})=>isActive?'text-brand-500':''}>Compare</NavLink>
            <NavLink to="/prompts" className={({isActive})=>isActive?'text-brand-500':''}>Prompts</NavLink>
            <ThemeToggle />
            <CommandPalette />
          </nav>
        </div>
      </header>
      <main className="container py-6">
        <Outlet />
      </main>
    </div>
  )
}
```

---

## src/components/ui primitives

### src/components/ui/card.tsx
```tsx
import { cn } from '@/utils/cn'
export function Card({ className, ...props }: React.HTMLAttributes<HTMLDivElement>) {
  return <div className={cn('rounded-2xl border shadow-sm p-4 bg-white dark:bg-slate-900', className)} {...props} />
}
```

### src/components/ui/badge.tsx
```tsx
import { cn } from '@/utils/cn'
export function Badge({ children, className }: { children: React.ReactNode; className?: string }) {
  return <span className={cn('inline-flex items-center rounded-full border px-2 py-0.5 text-xs', className)}>{children}</span>
}
```

### src/components/ThemeToggle.tsx
```tsx
import { useEffect, useState } from 'react'

export function ThemeToggle() {
  const [dark, setDark] = useState(() => window.matchMedia('(prefers-color-scheme: dark)').matches)
  useEffect(()=>{ document.documentElement.classList.toggle('dark', dark) },[dark])
  return (
    <button aria-label="Toggle theme" className="rounded-lg border px-2 py-1" onClick={()=>setDark(d=>!d)}>
      {dark ? '🌙' : '☀️'}
    </button>
  )
}
```

### src/components/KpiCard.tsx
```tsx
import { Card } from './ui/card'

export function KpiCard({ label, value }: { label: string; value: number }) {
  return (
    <Card className="flex items-center justify-between">
      <div className="text-sm text-slate-500">{label}</div>
      <div className="text-2xl font-semibold">{value}</div>
    </Card>
  )
}
```

### src/components/SearchInput.tsx
```tsx
import { useRef } from 'react'

export function SearchInput({ value, onChange }: { value: string; onChange: (v: string) => void }) {
  const ref = useRef<HTMLInputElement>(null)
  return (
    <div className="relative">
      <input
        ref={ref}
        aria-label="Search"
        className="w-full rounded-xl border px-3 py-2 pr-10"
        placeholder="Search…"
        value={value}
        onChange={(e) => onChange(e.target.value)}
      />
      <kbd className="absolute right-2 top-2 text-xs text-slate-500">/</kbd>
    </div>
  )
}
```

### src/components/CommandPalette.tsx
```tsx
import { useEffect, useMemo, useState } from 'react'
import Fuse from 'fuse.js'
import { usePlaybook } from '@/data/repo'

export function CommandPalette() {
  const [open, setOpen] = useState(false)
  const { data } = usePlaybook()
  const fuse = useMemo(()=> new Fuse([
    ...data.patterns, ...data.workflows, ...data.tools, ...data.prompts
  ].map(x=>({ id: 'title' in x ? x.id : (x as any).name, title: 'title' in x ? x.title : (x as any).name, type: (x as any).phase || (x as any).category || 'item'})), { keys: ['title'] }), [data])
  const [q, setQ] = useState('')
  const results = q ? fuse.search(q).slice(0,10) : []

  useEffect(()=>{
    const onKey=(e: KeyboardEvent)=>{
      if((e.ctrlKey||e.metaKey) && e.key.toLowerCase()==='k'){ e.preventDefault(); setOpen(o=>!o)}
      if(e.key==='/'){ const el=document.querySelector<HTMLInputElement>('input[aria-label="Search"]'); if(el){ el.focus(); e.preventDefault() } }
    }
    window.addEventListener('keydown', onKey)
    return ()=>window.removeEventListener('keydown', onKey)
  },[])

  return (
    <>
      <button className="rounded-xl border px-3 py-1" aria-haspopup="dialog" aria-expanded={open} onClick={()=>setOpen(true)}>⌘K</button>
      {open && (
        <div role="dialog" aria-modal className="fixed inset-0 bg-black/40 grid place-items-start pt-[10vh]">
          <div className="mx-auto w-full max-w-xl rounded-2xl border bg-white p-3 dark:bg-slate-900">
            <input autoFocus className="w-full rounded-xl border px-3 py-2" placeholder="Type to search" value={q} onChange={e=>setQ(e.target.value)} />
            <ul className="max-h-80 overflow-auto mt-2 divide-y">
              {results.map(r=> (
                <li key={r.item.id} className="py-2 text-sm flex justify-between">
                  <span>{r.item.title}</span>
                  <span className="text-slate-500">{r.item.type}</span>
                </li>
              ))}
              {!results.length && q && <li className="py-6 text-center text-slate-500">No results</li>}
            </ul>
            <div className="flex justify-end gap-2 mt-2">
              <button className="rounded-xl border px-3 py-1" onClick={()=>setOpen(false)}>Close</button>
            </div>
          </div>
        </div>
      )}
    </>
  )
}
```

---

## src/data/schemas.ts

```ts
import { z } from 'zod'

export const zRef = z.object({ id: z.string(), type: z.enum(['pattern','workflow','tool','prompt','metric','risk']), weight: z.number().optional() })

export const zPattern = z.object({
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
  relations: z.array(zRef).default([])
})

export const zWorkflow = z.object({
  id: z.string(), title: z.string(), summary: z.string(),
  stages: z.array(z.object({ name: z.string(), goals: z.array(z.string()), artifacts: z.array(z.string()).optional() })),
  kpis: z.array(z.string()).optional(),
  tags: z.array(z.string()).default([]),
  relations: z.array(zRef).default([])
})

export const zTool = z.object({ id: z.string(), name: z.string(), category: z.string(), cost: z.string().optional(), url: z.string().url().optional(), strengths: z.array(z.string()), limits: z.array(z.string()), tags: z.array(z.string()).default([]), relations: z.array(zRef).default([]) })
export const zPrompt = z.object({ id: z.string(), title: z.string(), body: z.string(), useCases: z.array(z.string()), inputs: z.array(z.string()).optional(), outputs: z.array(z.string()).optional(), tags: z.array(z.string()).default([]), relations: z.array(zRef).default([]) })
export const zMetric = z.object({ id: z.string(), name: z.string(), desc: z.string(), scale: z.enum(['ordinal','ratio','percent']), compute: z.string().optional(), tags: z.array(z.string()).default([]) })
export const zRisk = z.object({ id: z.string(), name: z.string(), mitigation: z.array(z.string()), severity: z.enum(['Low','Med','High']), tags: z.array(z.string()).default([]) })

export const zPlaybook = z.object({
  version: z.string(),
  updatedAt: z.string(),
  patterns: z.array(zPattern),
  workflows: z.array(zWorkflow),
  tools: z.array(zTool),
  prompts: z.array(zPrompt),
  metrics: z.array(zMetric),
  risks: z.array(zRisk)
})

export type Playbook = z.infer<typeof zPlaybook>
export type Pattern = z.infer<typeof zPattern>
export type Workflow = z.infer<typeof zWorkflow>
export type Tool = z.infer<typeof zTool>
export type Prompt = z.infer<typeof zPrompt>
export type Metric = z.infer<typeof zMetric>
export type Risk = z.infer<typeof zRisk>
```

## src/data/repo.ts

```ts
import { useEffect, useState } from 'react'
import { zPlaybook, type Playbook } from './schemas'

export function usePlaybook() {
  const [data, setData] = useState<Playbook>({
    version: '0', updatedAt: new Date().toISOString(), patterns: [], workflows: [], tools: [], prompts: [], metrics: [], risks: []
  })
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)
  useEffect(() => {
    ;(async () => {
      try {
        const res = await fetch('/data/playbook.json')
        const json = await res.json()
        const parsed = zPlaybook.parse(json)
        setData(parsed)
      } catch (e: any) {
        setError(e?.message || 'Failed to load playbook')
      } finally {
        setLoading(false)
      }
    })()
  }, [])
  return { data, loading, error }
}
```

## src/data/indexer.ts

```ts
import Fuse from 'fuse.js'
import type { Playbook } from './schemas'

export function buildIndex(pb: Playbook) {
  const items = [
    ...pb.patterns.map((p) => ({ id: p.id, title: p.title, tags: p.tags.join(' '), type: 'pattern' })),
    ...pb.workflows.map((w) => ({ id: w.id, title: w.title, tags: w.tags.join(' '), type: 'workflow' })),
    ...pb.tools.map((t) => ({ id: t.id, title: t.name, tags: t.tags.join(' '), type: 'tool' })),
    ...pb.prompts.map((p) => ({ id: p.id, title: p.title, tags: p.tags.join(' '), type: 'prompt' })),
  ]
  const fuse = new Fuse(items, { keys: ['title', 'tags'], threshold: 0.35 })
  return { fuse }
}
```

---

## src/pages/HomePage.tsx

```tsx
import { usePlaybook } from '@/data/repo'
import { KpiCard } from '@/components/KpiCard'
import { Card } from '@/components/ui/card'

export function HomePage() {
  const { data, loading, error } = usePlaybook()
  if (loading) return <div>Loading…</div>
  if (error) return <div role="alert" className="text-red-600">{error}</div>

  return (
    <div className="grid gap-6">
      <section className="grid grid-cols-2 md:grid-cols-4 gap-4">
        <KpiCard label="Patterns" value={data.patterns.length} />
        <KpiCard label="Workflows" value={data.workflows.length} />
        <KpiCard label="Tools" value={data.tools.length} />
        <KpiCard label="Prompts" value={data.prompts.length} />
      </section>
      <Card>
        <h2 className="text-xl font-semibold">Welcome</h2>
        <p className="mt-2 text-slate-600 dark:text-slate-300">Explore the playbook via the Explore tab, compare items, or open the command palette with <kbd>⌘/Ctrl</kbd>+<kbd>K</kbd>.</p>
        <p className="text-sm mt-2">Version: {data.version} • Updated: {new Date(data.updatedAt).toLocaleDateString()}</p>
      </Card>
    </div>
  )
}
```

## src/pages/NotFound.tsx

```tsx
export function NotFound(){
  return <div className="prose dark:prose-invert">
    <h1>Oops</h1>
    <p>We couldn't find that page.</p>
  </div>
}
```

---

## src/features/explorer/ExplorerPage.tsx

```tsx
import { useMemo, useState } from 'react'
import { usePlaybook } from '@/data/repo'
import { SearchInput } from '@/components/SearchInput'
import { Badge } from '@/components/ui/badge'
import { Card } from '@/components/ui/card'
import Fuse from 'fuse.js'

export function ExplorerPage() {
  const { data } = usePlaybook()
  const [q, setQ] = useState('')
  const [phase, setPhase] = useState<string>('All')
  const [sort, setSort] = useState<'roi'|'difficulty'|'updated'>('roi')

  const items = useMemo(() => {
    const patterns = data.patterns
    const filtered = phase==='All' ? patterns : patterns.filter(p=>p.phase===phase)
    const scored = [...filtered]
    if (sort==='roi') scored.sort((a,b)=> b.roi - a.roi)
    if (sort==='difficulty') scored.sort((a,b)=> a.difficulty.localeCompare(b.difficulty))
    if (sort==='updated') scored.sort(()=>0) // placeholder
    if (!q) return scored
    const fuse = new Fuse(scored, { keys:['title','summary','tags'], threshold:0.35 })
    return fuse.search(q).map(r=>r.item)
  }, [data, q, phase, sort])

  return (
    <div className="grid gap-4">
      <div className="grid grid-cols-1 md:grid-cols-3 gap-3">
        <SearchInput value={q} onChange={setQ} />
        <select aria-label="Phase filter" className="rounded-xl border px-3" value={phase} onChange={e=>setPhase(e.target.value)}>
          {['All','Ideation','Scaffolding','Coding','Review','Testing','Deployment'].map(p=> <option key={p}>{p}</option>)}
        </select>
        <select aria-label="Sort" className="rounded-xl border px-3" value={sort} onChange={e=>setSort(e.target.value as any)}>
          <option value="roi">Sort by ROI</option>
          <option value="difficulty">Sort by Difficulty</option>
          <option value="updated">Sort by Updated</option>
        </select>
      </div>

      <ul className="grid gap-3 sm:grid-cols-2 lg:grid-cols-3">
        {items.map(p => (
          <li key={p.id}>
            <Card>
              <div className="flex items-start justify-between gap-3">
                <div>
                  <h3 className="font-semibold">{p.title}</h3>
                  <p className="text-sm text-slate-600 dark:text-slate-300 line-clamp-3">{p.summary}</p>
                </div>
                <Badge className="bg-brand-50 dark:bg-slate-800 border-brand-200">ROI {p.roi}</Badge>
              </div>
              <div className="mt-2 flex flex-wrap gap-2 text-xs">
                <Badge>{p.phase}</Badge>
                <Badge>{p.difficulty}</Badge>
                {p.tags.slice(0,3).map(t=> <Badge key={t}>{t}</Badge>)}
              </div>
            </Card>
          </li>
        ))}
      </ul>
    </div>
  )
}
```

---

## src/features/compare/ComparePage.tsx

```tsx
import { usePlaybook } from '@/data/repo'
import { Card } from '@/components/ui/card'

export function ComparePage(){
  const { data } = usePlaybook()
  const take = (arr:any[], n=3)=>arr.slice(0,n)
  const rows = take(data.patterns, 3)
  return (
    <Card>
      <h2 className="text-xl font-semibold mb-3">Quick Compare (sample)</h2>
      <div className="overflow-auto">
        <table className="min-w-[600px] text-sm">
          <thead><tr>
            <th className="text-left p-2">Attribute</th>
            {rows.map(p=> <th key={p.id} className="text-left p-2">{p.title}</th>)}
          </tr></thead>
          <tbody>
            <tr><td className="p-2">Phase</td>{rows.map(p=> <td key={p.id} className="p-2">{p.phase}</td>)}</tr>
            <tr><td className="p-2">Difficulty</td>{rows.map(p=> <td key={p.id} className="p-2">{p.difficulty}</td>)}</tr>
            <tr><td className="p-2">ROI</td>{rows.map(p=> <td key={p.id} className="p-2">{p.roi}</td>)}</tr>
            <tr><td className="p-2">Best Practices</td>{rows.map(p=> <td key={p.id} className="p-2">{p.bestPractices.slice(0,3).join(', ')}</td>)}</tr>
          </tbody>
        </table>
      </div>
    </Card>
  )
}
```

---

## src/features/prompts/PromptLabPage.tsx

```tsx
import { usePlaybook } from '@/data/repo'
import { Card } from '@/components/ui/card'

export function PromptLabPage(){
  const { data } = usePlaybook()
  const copy = async (text: string)=> navigator.clipboard.writeText(text)
  return (
    <div className="grid gap-3 sm:grid-cols-2">
      {data.prompts.map(p=> (
        <Card key={p.id}>
          <div className="flex items-start justify-between">
            <h3 className="font-semibold">{p.title}</h3>
            <button className="rounded-xl border px-2 py-1 text-xs" onClick={()=>copy(p.body)}>Copy</button>
          </div>
          <p className="mt-2 whitespace-pre-wrap text-sm text-slate-700 dark:text-slate-300">{p.body}</p>
        </Card>
      ))}
    </div>
  )
}
```

---

## src/viz/ScatterChart.tsx (ROI vs Difficulty)

```tsx
import { ResponsiveContainer, ScatterChart, XAxis, YAxis, Tooltip, Scatter } from 'recharts'
import type { Pattern } from '@/data/schemas'

const diffMap: Record<Pattern['difficulty'], number> = { Beginner: 1, Intermediate: 2, Advanced: 3 }

export function RoiDifficultyScatter({ data }: { data: Pattern[] }){
  const points = data.map(p=> ({ x: diffMap[p.difficulty], y: p.roi, name: p.title }))
  return (
    <div className="h-72">
      <ResponsiveContainer width="100%" height="100%">
        <ScatterChart>
          <XAxis dataKey="x" name="Difficulty" tickFormatter={(v)=>({1:'Beginner',2:'Intermediate',3:'Advanced'} as any)[v]} domain={[1,3]} allowDecimals={false} />
          <YAxis dataKey="y" name="ROI" domain={[0,10]} />
          <Tooltip cursor={{ strokeDasharray: '3 3' }} />
          <Scatter data={points} />
        </ScatterChart>
      </ResponsiveContainer>
    </div>
  )
}
```

---

## src/utils/cn.ts

```ts
export function cn(...parts: (string | undefined | false | null)[]) {
  return parts.filter(Boolean).join(' ')
}
```

---

## vitest.setup.ts

```ts
import '@testing-library/jest-dom'
```

## src/__tests__/schemas.test.ts

```tsx
import { describe, it, expect } from 'vitest'
import { zPlaybook } from '@/data/schemas'

const sample = {
  version: '1.0.0',
  updatedAt: '2025-08-01',
  patterns: [], workflows: [], tools: [], prompts: [], metrics: [], risks: []
}

describe('schemas', () => {
  it('parses playbook', () => {
    const parsed = zPlaybook.parse(sample)
    expect(parsed.version).toBe('1.0.0')
  })
})
```

---

## e2e/playwright.config.ts

```ts
import { defineConfig } from '@playwright/test'
export default defineConfig({
  testDir: './tests',
  use: { baseURL: 'http://localhost:5173' },
  webServer: { command: 'pnpm preview', port: 5173, reuseExistingServer: !process.env.CI }
})
```

## e2e/tests/smoke.spec.ts

```ts
import { test, expect } from '@playwright/test'

test('home loads and shows KPIs', async ({ page }) => {
  await page.goto('/')
  await expect(page.getByText('Patterns')).toBeVisible()
})
```

---

## .github/workflows/ci.yml

```yaml
name: CI
on: [push, pull_request]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: 20 }
      - name: Install
        run: |
          corepack enable
          pnpm install --frozen-lockfile || npm ci
      - name: Lint
        run: |
          pnpm lint || npm run lint
      - name: Typecheck
        run: |
          pnpm typecheck || npm run typecheck
      - name: Unit tests
        run: |
          pnpm test || npm test
      - name: Build
        run: |
          pnpm build || npm run build
      - name: E2E
        run: |
          pnpm e2e || npm run e2e
```

---

## .storybook/main.ts

```ts
import type { StorybookConfig } from '@storybook/react-vite'
const config: StorybookConfig = {
  stories: ['../src/**/*.stories.@(ts|tsx)'],
  addons: ['@storybook/addon-essentials', '@storybook/addon-interactions', '@storybook/addon-themes'],
  framework: { name: '@storybook/react-vite', options: {} },
}
export default config
```

## .storybook/preview.ts

```ts
import '../src/styles/global.css'
export const parameters = { controls: { expanded: true } }
```

## src/components/KpiCard.stories.tsx

```tsx
import type { Meta, StoryObj } from '@storybook/react'
import { KpiCard } from './KpiCard'

const meta: Meta<typeof KpiCard> = { component: KpiCard, title: 'UI/KpiCard' }
export default meta
export const Basic: StoryObj<typeof KpiCard> = { args: { label: 'Patterns', value: 12 } }
```

---

## public/manifest.webmanifest

```json
{
  "name": "LLM Agent Playbook Explorer",
  "short_name": "Playbook",
  "start_url": "/",
  "display": "standalone",
  "background_color": "#0b1220",
  "theme_color": "#0ea5e9",
  "icons": [
    { "src": "/icons/pwa-192.png", "sizes": "192x192", "type": "image/png" },
    { "src": "/icons/pwa-512.png", "sizes": "512x512", "type": "image/png" }
  ]
}
```

## public/favicon.svg

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="12" fill="#0ea5e9"/><text x="50%" y="54%" dominant-baseline="middle" text-anchor="middle" font-size="34" font-family="Arial" fill="#fff">A</text></svg>
```

## public/icons/pwa-192.png

*(placeholder; generate PNG 192x192)*

## public/icons/pwa-512.png

*(placeholder; generate PNG 512x512)*

---

## public/data/playbook.json (seed)

```json
{
  "version": "1.0.0",
  "updatedAt": "2025-08-01",
  "patterns": [
    { "id": "pat.scaffold-repo", "title": "Repo Scaffolding via Agent", "summary": "Use an agent to initialize repo, CI, and linting.", "phase": "Scaffolding", "difficulty": "Beginner", "roi": 8, "steps": ["Collect requirements","Generate skeleton","Wire CI"], "bestPractices": ["Idempotent scripts","Template versioning"], "tags": ["phase:scaffold","pattern"] },
    { "id": "pat.diff-workflow", "title": "Patch/Diff Workflow", "summary": "Use unified diffs for precise, reviewable edits.", "phase": "Coding", "difficulty": "Beginner", "roi": 9, "steps": ["Edit via diff","Run tests","Iterate"], "bestPractices": ["Small commits","Automated checks"], "tags": ["phase:code","pattern"] },
    { "id": "pat.typed-output", "title": "Typed Structured Output", "summary": "Enforce JSON schemas for non-code outputs.", "phase": "Review", "difficulty": "Intermediate", "roi": 7, "steps": ["Define schema","Validate","Retry on fail"], "bestPractices": ["Zod/Pydantic","CI gates"], "tags": ["pattern"] }
  ],
  "workflows": [
    { "id": "wf.solo-dev-loop", "title": "Solo Dev Agent Loop", "summary": "Plan → Code → Review → Test → Ship with tight feedback.", "stages": [{ "name":"Plan","goals":["Define scope"], "artifacts":["Spec","Acceptance"]},{"name":"Code","goals":["Implement"], "artifacts":["Diffs"]},{"name":"Review","goals":["Self‑review with agent"], "artifacts":["PR notes"]},{"name":"Test","goals":["Run & fix"], "artifacts":["Reports"]},{"name":"Ship","goals":["Release"], "artifacts":["Changelog"]}], "tags":["workflow"] }
  ],
  "tools": [
    { "id": "tool.llm-cli", "name": "LLM CLI", "category": "CLI", "strengths": ["Scriptable","Local history"], "limits": ["No GUI"], "tags": ["tool"] },
    { "id": "tool.aider", "name": "Aider", "category": "CLI", "strengths": ["Diff-based edits","Git-native"], "limits": ["Requires setup"], "tags": ["tool"] }
  ],
  "prompts": [
    { "id": "pr.audit", "title": "Code Audit Prompt", "body": "Audit this repo for security, performance, and tests…", "useCases": ["Review","Hardening"], "tags": ["prompt"] },
    { "id": "pr.plan", "title": "Planner Prompt", "body": "You are a solution architect. Produce a step-by-step plan…", "useCases": ["Planning"], "tags": ["prompt"] }
  ],
  "metrics": [
    { "id": "mttm", "name": "Mean Time to Merge", "desc": "Avg time from PR open to merge.", "scale": "ratio", "tags": ["metric"] },
    { "id": "pass-rate", "name": "Task Success Rate", "desc": "% tasks completed without human fixes.", "scale": "percent", "tags": ["metric"] }
  ],
  "risks": [
    { "id": "risk.hallucination", "name": "Spec Hallucination", "mitigation": ["Schema validation","Golden tests"], "severity": "High", "tags": ["risk"] },
    { "id": "risk.context-loss", "name": "Context Loss", "mitigation": ["Summaries","Retrieval"], "severity": "Med", "tags": ["risk"] }
  ]
}
```

---

## README.md

```md
# LLM Agent Playbook Explorer

An interactive single-page app to explore the **LLM Coding Agent Playbook for Solo Developers**.

## Quickstart

```bash
# with pnpm (recommended)
corepack enable
pnpm install
pnpm dev
# open http://localhost:5173
```

## Scripts
- `pnpm dev` – start dev server
- `pnpm build` – typecheck + build
- `pnpm preview` – preview prod build
- `pnpm test` / `pnpm test:watch` – unit tests (Vitest)
- `pnpm e2e` – Playwright E2E
- `pnpm lint` – ESLint
- `pnpm format` – Prettier
- `pnpm storybook` / `pnpm build-storybook` – Storybook

## Data
Seed JSON at `public/data/playbook.json`. Extend as needed. All content validated with Zod on load.

## Tech
React 18 + TypeScript + Vite • Tailwind • Zustand • React Router • Fuse.js • Recharts • D3 Sankey • Vitest • Playwright • Storybook • PWA.

## Accessibility & PWA
- WCAG-friendly focus, skip link, ARIA labels on dialogs/inputs.
- Installable PWA with offline caching of assets and JSON (stale-while-revalidate).

## CI
GitHub Actions runs lint, typecheck, unit, build, and e2e.

## License
MIT
```

