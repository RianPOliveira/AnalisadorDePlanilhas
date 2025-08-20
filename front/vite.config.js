import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  // Configuração do CSS/PostCSS
  css: {
    // Especifica o ficheiro de configuração do PostCSS.
    // O Vite deve encontrar 'postcss.config.js' na raiz do projeto automaticamente,
    // mas a especificação explícita pode ajudar em alguns casos.
    postcss: './postcss.config.js', 
  },
  // Opcional: Adicione um resolvedor para garantir que o Vite lida com extensões CSS corretamente.
  // Pode não ser necessário, mas ajuda a depurar problemas de importação de CSS.
  resolve: {
    extensions: ['.mjs', '.js', '.ts', '.jsx', '.tsx', '.json', '.vue', '.css', '.scss', '.sass'],
  },
});