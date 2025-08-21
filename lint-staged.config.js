export default {
  "docs/**/*.md": [
    "prettier --write",
    "markdownlint --fix --config markdownlint.json"
  ],
  "README.md": [
    "prettier --write",
    "markdownlint --fix --config markdownlint.json"
  ]
}
