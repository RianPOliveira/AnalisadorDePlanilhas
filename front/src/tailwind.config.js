// tailwind.config.js
/** @type {import('tailwindcss').Config} */
export default {
  // A propriedade 'content' é CRUCIAL. Ela diz ao Tailwind onde procurar classes.
  content: [
    "./index.html", // Escaneia o index.html
    "./src/**/*.{js,ts,jsx,tsx}", // Escaneia todos os ficheiros JS, TS, JSX, TSX dentro da pasta src/
  ],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Inter', 'sans-serif'], // Define a fonte Inter como padrão para 'font-sans'
      }
    },
  },
  plugins: [],
}
