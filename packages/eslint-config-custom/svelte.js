module.exports = {
    root: true,
    extends: [
      'eslint:recommended',
      'plugin:@typescript-eslint/recommended',
      'plugin:svelte/recommended',
      'prettier'
    ],
    parser: '@typescript-eslint/parser',
    plugins: ['@typescript-eslint'],
    ignorePatterns: ['*.cjs'],
    parserOptions: {
      sourceType: 'module',
      ecmaVersion: 2020,
      extraFileExtensions: ['.svelte']
    },
    env: {
      browser: true,
      es2017: true,
      node: true
    },
    overrides: [
      {
        files: ['*.svelte'],
        parser: 'svelte-eslint-parser',
        parserOptions: {
          parser: '@typescript-eslint/parser'
        }
      }
    ],
    rules: {
      // Suppress explicit any rule
      '@typescript-eslint/no-explicit-any': 'off',
      'no-console': ['error', { allow: ['error'] }], // Disallow  other console methods except error
      'no-unsafe-optional-chaining': 'off'
  
      // ... other rules ...
    }
  };
  