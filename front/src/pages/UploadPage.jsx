import { useState } from "react"; // CORRIGIDO: de '=' para 'from'
import axios from "axios";       // CORRIGIDO: de '=' para 'from'
import * as XLSX from "xlsx";
import *as pdfjsLib from "pdfjs-dist";
import pdfWorker from "pdfjs-dist/build/pdf.worker.min?url";

pdfjsLib.GlobalWorkerOptions.workerSrc = pdfWorker;

const API = import.meta.env.VITE_API_URL;

export default function UploadPage() {
    const [file, setFile] = useState(null);
    const [instrucao, setInstrucao] = useState("");
    const [status, setStatus] = useState("");
    const [relatorio, setRelatorio] = useState("");

    async function handleSubmit(e) {
        e.preventDefault();
        if (!file) return;
        setStatus("Lendo arquivo...");
        try {
            const text = await extractTextFromFile(file);
            setStatus("Enviando para análise...");
            const { data } = await axios.post(`${API}/analisar_planilha`, {
                dados_planilha: text.slice(0, 200000), // evita payload imenso
                instrucao: instrucao || "Analise e gere um resumo executivo com insights."
            });
            setStatus("");
            setRelatorio(data?.relatorio ?? JSON.stringify(data, null, 2));
        } catch (err) {
            console.error(err);
            setStatus("Erro: " + (err?.message || "falha ao analisar"));
        }
    }

    return (
        <div className="container-prose py-16">
            <h1 className="text-3xl font-bold text-slate-800">Analisar Documento</h1>
            <p className="mt-2 text-slate-600">Envie um PDF, CSV ou XLS/XLSX e descreva o que deseja descobrir.</p>

            <form onSubmit={handleSubmit} className="mt-8 space-y-6 max-w-2xl">
                <div>
                    <input
                        type="file"
                        accept=".csv,.xls,.xlsx,.pdf"
                        onChange={(e) => setFile(e.target.files?.[0] || null)}
                        className="block w-full text-sm text-slate-700 file:mr-4 file:py-2 file:px-4 file:rounded-md file:border-0
                                       file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100"
                    />
                    {file && <p className="text-sm text-slate-500 mt-2">Selecionado: {file.name}</p>}
                </div>

                <div>
                    <label className="block text-sm font-medium text-slate-700 mb-2">Instrução de análise</label>
                    <textarea
                        value={instrucao}
                        onChange={(e) => setInstrucao(e.target.value)}
                        rows={5}
                        className="w-full rounded-lg border border-slate-200 p-3 outline-none focus:ring-2 focus:ring-blue-600"
                        placeholder="Ex.: encontre outliers, calcule métricas por categoria e sugira ações."
                    />
                </div>

                <div className="flex items-center gap-3">
                    <button
                        className="bg-indigo-600 hover:bg-indigo-700 text-white font-bold py-3 px-6 rounded-xl shadow-lg 
                                   transition-colors duration-300 focus:outline-none focus:ring-4 focus:ring-indigo-500 
                                   focus:ring-opacity-50 disabled:opacity-50 disabled:cursor-not-allowed"
                        disabled={!file || !!status}
                    >
                        Enviar para Análise
                    </button>
                    {status && <span className="text-sm text-slate-600">{status}</span>}
                </div>
            </form>

            {relatorio && (
                <div className="mt-10">
                    <h2 className="text-2xl font-bold text-slate-800 mb-3">Relatório</h2>
                    <div className="rounded-xl border border-slate-200 p-5 bg-slate-50 whitespace-pre-wrap">
                        {relatorio}
                    </div>
                </div>
            )}
        </div>
    );
}

// ===== Helpers =====
async function extractTextFromFile(file) {
    const ext = file.name.toLowerCase().split(".").pop();

    if (ext === "csv") {
        return await file.text();
    }

    if (ext === "xls" || ext === "xlsx") {
        const buf = await file.arrayBuffer();
        const wb = XLSX.read(buf, { type: "array" });
        return wb.SheetNames.map((name) => {
            const ws = wb.Sheets[name];
            return `--- Sheet: ${name} ---\n${XLSX.utils.sheet_to_csv(ws)}`;
        }).join("\n\n");
    }

    if (ext === "pdf") {
        const buf = new Uint8Array(await file.arrayBuffer());
        const pdf = await pdfjsLib.getDocument({ data: buf }).promise;
        let text = "";
        for (let i = 1; i <= pdf.numPages; i++) {
            const page = await pdf.getPage(i);
            const content = await page.getTextContent();
            const strings = content.items.map((it) => ("str" in it ? it.str : ""));
            text += strings.join(" ") + "\n\n";
        }
        return text;
    }

    throw new Error("Formato não suportado.");
}
