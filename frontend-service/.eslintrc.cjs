/* eslint-env node */
require('@rushstack/eslint-patch/modern-module-resolution')

module.exports = {
  root: true,
  parser: "vue-eslint-parser",
  env: {
    browser: true,
    commonjs: true,
    es2021: true
  },
  extends: [
    'plugin:vue/vue3-essential',
    'plugin:vue/vue3-recommended',
    'eslint:recommended',
    'plugin:vue/vue3-strongly-recommended'
  ],
  overrides: [
  ],
  parserOptions: {
    parser: "@typescript-eslint/parser",
    ecmaVersion: 'latest',
  },
  plugins: [
    'vue'
  ],
  rules: {
    '@typescript-eslint/consistent-type-imports': 'off',
  }
}
