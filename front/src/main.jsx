import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import "./index.css";
import App from "./App.jsx";
import UploadPage from "./pages/UploadPage.jsx";

ReactDOM.createRoot(document.getElementById("root")).render(
    <React.StrictMode>
        <BrowserRouter>
            <Routes>
                <Route element={<App />}>
                    <Route path="/" element={<Home />} />
                    <Route path="/analisar" element={<UploadPage />} />
                    <Route path="*" element={<NotFound />} />
                </Route>
            </Routes>
        </BrowserRouter>
    </React.StrictMode>
);

function Home() {
    return <div className="py-24"><Hero /></div>;
}

function NotFound() {
    return <div className="container-prose py-20">Página não encontrada.</div>;
}

function Hero() {
    return (
        <div className="container-prose text-center">
            <h1 className="text-4xl md:text-6xl font-extrabold leading-tight text-slate-800">
                <span className="block">Transforme Dados em </span>
                <span className="block text-blue-700">Decisões Inteligentes</span>
            </h1>
            <p className="mt-6 text-lg md:text-xl text-slate-600">
                Nossa plataforma de IA analisa seus documentos PDF, CSV e XLS para extrair insights
                valiosos e gerar relatórios completos em segundos.
            </p>
            <div className="mt-10 flex items-center justify-center gap-4">
                <a href="/analisar" className="btn btn-primary">
                    Começar Agora <span aria-hidden>↗</span>
                </a>
                <a href="#como-funciona" className="btn btn-ghost">Saiba Mais</a>
            </div>
            <div id="como-funciona" className="mt-24 text-left max-w-3xl mx-auto">
                <h2 className="text-2xl font-bold text-slate-800 mb-3">Como funciona</h2>
                <ol className="list-decimal pl-5 space-y-2 text-slate-700">
                    <li>Envie um PDF, CSV ou XLS.</li>
                    <li>Descreva o que deseja descobrir.</li>
                    <li>Receba um relatório pronto para uso.</li>
                </ol>
            </div>
        </div>
    );
}