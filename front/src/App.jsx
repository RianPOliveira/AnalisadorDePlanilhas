import { Outlet, Link, useLocation } from "react-router-dom";
import logo from "./assets/sergipetec-logo.jpg";

export default function App() {
    const { pathname } = useLocation();
    return (
        <div className="min-h-screen bg-white text-slate-800">
            <header className="border-b border-slate-100">
                <div className="container-prose h-16 flex items-center justify-between">
                    <Link to="/" className="flex items-center gap-3">
                        <img src={logo} alt="SergipeTec" className="h-10 w-auto rounded-sm" />
                        <span className="font-bold text-lg">SergipeTec</span>
                    </Link>
                    <nav className="flex items-center gap-6">
                        <Link to="/" className={navCls(pathname === "/")}>Início</Link>
                        <Link to="/analisar" className={navCls(pathname === "/analisar")}>Analisar</Link>
                    </nav>
                </div>
            </header>
            <main><Outlet /></main>
            <footer className="mt-24 border-t border-slate-100">
                <div className="container-prose py-8 text-sm text-slate-500">
                    © {new Date().getFullYear()} SergipeTec — Todos os direitos reservados.
                </div>
            </footer>
        </div>
    );
}

function navCls(active) {
    return `text-sm font-medium ${active ? "text-blue-700" : "text-slate-600 hover:text-slate-800"}`;
}
