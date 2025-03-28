/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
      "./src/**/*.{html,js,jsx,ts,tsx}", // Update paths to match your project
      "./public/index.html" // Or your main HTML file
    ],
    theme: {
      extend: {
        fontFamily: {
            bodoni_moda : ['Bodoni Moda', 'sans-serif']
      },
    },
    plugins: [],
  }
}