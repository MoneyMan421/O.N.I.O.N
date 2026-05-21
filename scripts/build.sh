#!/bin/bash
# Build script for O.N.I.O.N services

set -e

echo "🧅 Building O.N.I.O.N Services..."

# Build all services
for service in services/*/; do
  if [ -f "$service/package.json" ]; then
    echo "Building $(basename $service)..."
    (cd "$service" && npm install && npm run build)
  fi
done

# Build all agents
for agent in agents/*/; do
  if [ -f "$agent/package.json" ]; then
    echo "Building $(basename $agent)..."
    (cd "$agent" && npm install && npm run build)
  fi
done

# Build Docker images
echo "Building Docker images..."
docker-compose build

echo "✅ Build complete!"
