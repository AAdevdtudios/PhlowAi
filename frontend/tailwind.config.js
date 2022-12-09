/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'class',
  mode: 'jit',
  content: [
    "./assets/**/*.css",
    "./components/*.{vue,js}",
    "./components/**/*.{vue,js}",
    "./layouts/**/*.{vue,js}",
    "./pages/*.vue",
    "./pages/**/*.vue",
    "./plugins/**/*.{js,ts}",
    "./*.{vue,js,ts}"
  ],
  theme: {
    extend: {
      fontFamily: {
        'workSans': ['Work Sans', 'sans-serif']
      },
      colors:{
        'pri' : '#F0D808'
      }
    },
  },
  plugins: [],
}
