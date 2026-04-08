.PHONY: test install clean

test:
	pytest tests/

install:
	pip install -r requirements.txt

clean:
	rm -rf __pycache__ .pytest_cache
