import React from 'react';
import ReactDOM from 'react-dom/client';
import UploadPage from "./pages/UploadPage.jsx";
import logo from "./assets/sergipetec-logo.jpg";
 // Certifique-se de que esta importação está correta

// Função auxiliar para classes de navegação (mantida, mas não utilizada no header agora)
function navCls() {
    return "text-sm font-medium text-slate-700 hover:text-blue-600 transition-colors duration-200";
}

function AppContent() {
    return (
        <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 text-slate-800 font-sans antialiased">
            <header className="bg-white shadow-md py-4 px-6 md:px-12 border-b border-blue-100 rounded-b-lg">
                <div className="max-w-7xl mx-auto flex items-center justify-between">
                    {/* Logotipo na parte superior esquerda */}
                    <a href="/" className="flex items-center gap-3 transition-transform duration-200 hover:scale-105">
                        <img src={logo} alt="SergipeTec" className="h-12 w-auto rounded-lg shadow-sm" />
                        <span className="font-bold text-2xl text-blue-800 tracking-tight">SergipeTec</span>
                    </a>

                    {/* Barra de navegação removida, deixando apenas o logótipo */}
                    {/* <nav className="flex items-center space-x-6">
                        <a href="#como-funciona" className={navCls()}>Como Funciona</a>
                        <a href="#recursos" className={navCls()}>Recursos</a>
                        <a href="#contacto" className={navCls()}>Contacto</a>
                        <button className="ml-4 px-4 py-2 bg-blue-600 text-white rounded-md text-sm font-semibold hover:bg-blue-700 transition-colors duration-200 shadow-md">
                            Fazer Login
                        </button>
                    </nav> */}
                </div>
            </header>

            <main className="flex-grow py-12 md:py-20 flex items-center justify-center">
                <div className="max-w-4xl w-full px-4 sm:px-6 lg:px-8">
                    <div className="bg-white p-8 md:p-10 rounded-xl shadow-lg border border-blue-100 transform transition-all duration-300 hover:shadow-xl">
                        <UploadPage />
                    </div>
                </div>
            </main>

            <footer className="mt-auto bg-blue-900 text-blue-200 py-6 text-sm text-center">
                <div className="max-w-7xl mx-auto px-4">
                    © {new Date().getFullYear()} SergipeTec — Todos os direitos reservados.
                    <p className="mt-1 text-blue-300">Desenvolvido com IA e paixão.</p>
                </div>
            </footer>
        </div>
    );
}

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <AppContent />
  </React.StrictMode>
);

export default AppContent;
