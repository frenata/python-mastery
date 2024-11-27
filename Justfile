lint:
	#!/usr/bin/env bash
	cd Exercises
	uv run ruff format
	uv run ruff check

test:
	#!/usr/bin/env bash
	cd Exercises
	uv run pytest
