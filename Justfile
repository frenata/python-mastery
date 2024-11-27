set positional-arguments

lint:
	#!/usr/bin/env bash
	cd Exercises
	uv run ruff format
	uv run ruff check

up:
	devcontainer build --workspace-folder .
	devcontainer up \
		--mount "type=bind,source=$HOME/.config/nvim,target=/home/${USER}/.config/nvim" \
		--mount "type=bind,source=$HOME/.gitconfig,target=/home/${USER}/.gitconfig" \
		--mount type=bind,source=$SSH_AUTH_SOCK,target=/ssh-agent \
		--workspace-folder . --remove-existing-container true

enter:
	devcontainer exec --workspace-folder . bash

test:
	#!/usr/bin/env bash
	cd Exercises
	uv run pytest
