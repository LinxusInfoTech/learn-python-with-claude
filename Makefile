.PHONY: help install dev test lint format clean run docker-build docker-run k8s-deploy k8s-delete

help:
	@echo "Learn Python with Claude - Development Commands"
	@echo ""
	@echo "Setup:"
	@echo "  make install       Install package in development mode"
	@echo "  make dev           Install with dev dependencies"
	@echo ""
	@echo "Development:"
	@echo "  make run           Run the app locally"
	@echo "  make test          Run tests"
	@echo "  make lint          Lint code (flake8, black check)"
	@echo "  make format        Format code (black, autoflake)"
	@echo "  make clean         Clean build artifacts"
	@echo ""
	@echo "Docker:"
	@echo "  make docker-build  Build Docker image"
	@echo "  make docker-run    Run with docker-compose"
	@echo "  make docker-stop   Stop docker-compose"
	@echo "  make docker-logs   View docker logs"
	@echo ""
	@echo "Kubernetes:"
	@echo "  make k8s-deploy    Deploy to Kubernetes"
	@echo "  make k8s-delete    Remove from Kubernetes"
	@echo "  make k8s-logs      View Kubernetes logs"
	@echo "  make k8s-port-fwd  Port forward to localhost:8000"
	@echo ""

install:
	pip install -e .

dev:
	pip install -e ".[dev]"
	pip install pytest pytest-cov black flake8 mypy

run:
	learnwithclaude

test:
	pytest tests/ -v --cov=learn_python_with_claude

lint:
	flake8 learn_python_with_claude/
	black --check learn_python_with_claude/

format:
	black learn_python_with_claude/

clean:
	rm -rf build/ dist/ *.egg-info
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.pyo' -delete

docker-build:
	docker build -t learn-python-with-claude:latest .

docker-run:
	docker-compose up --build

docker-stop:
	docker-compose down

docker-logs:
	docker-compose logs -f

docker-clean:
	docker-compose down -v
	docker system prune

k8s-deploy:
	kubectl apply -f k8s/

k8s-delete:
	kubectl delete -f k8s/

k8s-logs:
	kubectl logs -f deployment/learn-python-with-claude

k8s-port-fwd:
	kubectl port-forward svc/learn-python-with-claude 8000:80

k8s-scale:
	@read -p "Enter number of replicas: " replicas; \
	kubectl scale deployment learn-python-with-claude --replicas=$$replicas

k8s-status:
	kubectl get deployment,pods,svc -l app=learn-python-with-claude

k8s-restart:
	kubectl rollout restart deployment/learn-python-with-claude

.DEFAULT_GOAL := help
