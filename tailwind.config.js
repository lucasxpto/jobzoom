/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['jobs/templates/jobs/**/*.html'],
  theme: {
    extend: {},
  },
  plugins: [
    require('@tailwindcss/forms'),
  ],
}

