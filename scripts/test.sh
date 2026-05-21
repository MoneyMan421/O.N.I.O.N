#!/bin/bash
# Test script for O.N.I.O.N

set -e

echo "🧅 Running O.N.I.O.N Tests..."

# Run unit tests
echo "Running unit tests..."
npm run test:unit --workspaces --if-present

# Run integration tests
echo "Running integration tests..."
npm run test:integration --workspaces --if-present

# Run security tests
echo "Running security tests..."
npm run test:security --workspaces --if-present

# Run child safety tests
echo "Running child safety tests..."
npm run test:safety --workspaces --if-present

# Check coverage
echo "Checking coverage..."
npm run check:coverage --if-present

echo "✅ All tests passed!"
