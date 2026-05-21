#!/bin/bash
# Lint script for O.N.I.O.N

set -e

echo "🧅 Linting O.N.I.O.N Code..."

# Run ESLint
echo "Running ESLint..."
npm run lint --workspaces --if-present

# Run Prettier check
echo "Checking code formatting..."
npm run format:check --if-present

# Run TypeScript compiler check
echo "Checking TypeScript..."
npm run type-check --workspaces --if-present

echo "✅ Linting complete!"
