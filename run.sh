#!/bin/bash
set -e

echo "Starting data validation..."
pytest tests/

echo "Running example analysis..."
python examples/python/example.py
