#!/bin/bash
# Local development environment setup

set -e

echo "🧅 Starting O.N.I.O.N Local Development Environment..."

# Check prerequisites
command -v docker >/dev/null 2>&1 || { echo "Docker is required but not installed."; exit 1; }
command -v docker-compose >/dev/null 2>&1 || { echo "Docker Compose is required but not installed."; exit 1; }
command -v node >/dev/null 2>&1 || { echo "Node.js is required but not installed."; exit 1; }

# Create dev environment file if it doesn't exist
if [ ! -f "configs/dev.env" ]; then
  echo "Creating dev.env from example..."
  cp configs/dev.env.example configs/dev.env
fi

# Start services
echo "Starting services with Docker Compose..."
docker-compose up -d

# Wait for services to be healthy
echo "Waiting for services to be ready..."
sleep 10

# Check health
echo "Checking service health..."
curl -f http://localhost:8080/health || echo "⚠️  API Gateway not healthy yet"
curl -f http://localhost:8081/health || echo "⚠️  PDP not healthy yet"

echo "✅ Local development environment is running!"
echo ""
echo "Services:"
echo "  - API Gateway: http://localhost:8080"
echo "  - Policy PDP: http://localhost:8081"
echo "  - Approval Service: http://localhost:8082"
echo "  - Notification Service: http://localhost:8083"
echo "  - Audit Service: http://localhost:8084"
echo "  - Telemetry Ingest: http://localhost:8085"
echo ""
echo "To stop: docker-compose down"
echo "To view logs: docker-compose logs -f"
