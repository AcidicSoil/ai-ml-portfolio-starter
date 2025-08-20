import { useEffect, useState } from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import { zPlaybook, type zPlaybook as PlaybookType } from "../data/schemas";
import playbookData from "../public/data/playbook.json";
import DOMPurify from "dompurify";

// Basic layout shell
function Layout({ children }: { children: React.ReactNode }) {
  return (
    <div className="flex min-h-screen bg-background text-foreground">
      <aside className="w-64 border-r p-4">
        <h1 className="text-xl font-bold mb-4">LLM Coding Agent Playbook</h1>
        <nav className="flex flex-col space-y-2">
          <Link to="/" className="hover:underline">Overview</Link>
          <Link to="/patterns" className="hover:underline">Patterns</Link>
          <Link to="/workflows" className="hover:underline">Workflows</Link>
          <Link to="/tools" className="hover:underline">Tools</Link>
          <Link to="/prompts" className="hover:underline">Prompts</Link>
          <Link to="/metrics" className="hover:underline">Metrics</Link>
          <Link to="/risks" className="hover:underline">Risks</Link>
        </nav>
      </aside>
      <main className="flex-1 p-6 overflow-y-auto">{children}</main>
    </div>
  );
}

function Overview({ playbook }: { playbook: PlaybookType }) {
  return (
    <div>
      <h2 className="text-2xl font-semibold mb-4">Overview</h2>
      <div className="grid grid-cols-2 md:grid-cols-3 gap-4">
        <div className="p-4 rounded-xl shadow bg-card">
          <h3 className="font-medium">Patterns</h3>
          <p className="text-2xl">{playbook.patterns.length}</p>
        </div>
        <div className="p-4 rounded-xl shadow bg-card">
          <h3 className="font-medium">Workflows</h3>
          <p className="text-2xl">{playbook.workflows.length}</p>
        </div>
        <div className="p-4 rounded-xl shadow bg-card">
          <h3 className="font-medium">Tools</h3>
          <p className="text-2xl">{playbook.tools.length}</p>
        </div>
        <div className="p-4 rounded-xl shadow bg-card">
          <h3 className="font-medium">Prompts</h3>
          <p className="text-2xl">{playbook.prompts.length}</p>
        </div>
        <div className="p-4 rounded-xl shadow bg-card">
          <h3 className="font-medium">Metrics</h3>
          <p className="text-2xl">{playbook.metrics.length}</p>
        </div>
        <div className="p-4 rounded-xl shadow bg-card">
          <h3 className="font-medium">Risks</h3>
          <p className="text-2xl">{playbook.risks.length}</p>
        </div>
      </div>
    </div>
  );
}

function ListPage<T>({ title, items, render }: { title: string; items: T[]; render: (item: T) => React.ReactNode }) {
  return (
    <div>
      <h2 className="text-2xl font-semibold mb-4">{title}</h2>
      <div className="grid gap-4">
        {items.map((item, idx) => (
          <div key={idx} className="p-4 rounded-xl shadow bg-card">{render(item)}</div>
        ))}
      </div>
    </div>
  );
}

export default function App() {
  const [playbook, setPlaybook] = useState<PlaybookType | null>(null);

  useEffect(() => {
    try {
      const parsed = zPlaybook.parse(playbookData);
      setPlaybook(parsed);
    } catch (e) {
      console.error("Invalid playbook data", e);
    }
  }, []);

  if (!playbook) return <div>Loading playbook…</div>;

  return (
    <Router>
      <Routes>
        <Route
          path="/"
          element={
            <Layout>
              <Overview playbook={playbook} />
            </Layout>
          }
        />
        <Route
          path="/patterns"
          element={
            <Layout>
              <ListPage
                title="Patterns"
                items={playbook.patterns}
                render={(p) => (
                  <>
                    <h3 className="font-bold">{(p as any).title}</h3>
                    <p>{(p as any).summary}</p>
                  </>
                )}
              />
            </Layout>
          }
        />
        <Route
          path="/workflows"
          element={
            <Layout>
              <ListPage
                title="Workflows"
                items={playbook.workflows}
                render={(w) => (
                  <>
                    <h3 className="font-bold">{(w as any).title}</h3>
                    <p>{(w as any).summary}</p>
                  </>
                )}
              />
            </Layout>
          }
        />
        <Route
          path="/tools"
          element={
            <Layout>
              <ListPage
                title="Tools"
                items={playbook.tools}
                render={(t) => (
                  <>
                    <h3 className="font-bold">{(t as any).name}</h3>
                    <p>{(t as any).category}</p>
                  </>
                )}
              />
            </Layout>
          }
        />
        <Route
          path="/prompts"
          element={
            <Layout>
              <ListPage
                title="Prompts"
                items={playbook.prompts}
                render={(p) => (
                  <>
                    <h3 className="font-bold">{(p as any).title}</h3>
                    <p>{(p as any).body}</p>
                  </>
                )}
              />
            </Layout>
          }
        />
        <Route
          path="/metrics"
          element={
            <Layout>
              <ListPage
                title="Metrics"
                items={playbook.metrics}
                render={(m) => (
                  <>
                    <h3 className="font-bold">{(m as any).name}</h3>
                    <p>{(m as any).desc}</p>
                  </>
                )}
              />
            </Layout>
          }
        />
        <Route
          path="/risks"
          element={
            <Layout>
              <ListPage
                title="Risks"
                items={playbook.risks}
                render={(r) => (
                  <>
                    <h3 className="font-bold">{(r as any).name}</h3>
                    <p>Severity: {(r as any).severity}</p>
                  </>
                )}
              />
            </Layout>
          }
        />
      </Routes>
    </Router>
  );
}
