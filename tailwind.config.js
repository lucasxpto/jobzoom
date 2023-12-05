/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
      'jobs/templates/jobs/*.html',
        'jobs/templates/jobs/**/*.html',
      'usuarios/templates/usuarios/*.html',
        'usuarios/templates/usuarios/**/*.html',
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('@tailwindcss/forms'),
  ],
}

