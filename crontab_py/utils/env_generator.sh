#!/bin/bash

# Setting parameters
ENV_NAME=$1
PATH_REQUIREMENTS=$2
ENV_DIR="/app/.env"

# Check if venv exists
if [ ! -d "$ENV_DIR/$ENV_NAME" ]; then
    if [ ! -d "$ENV_DIR" ]; then
        mkdir -p "$ENV_DIR"
    fi
    cd "$ENV_DIR" || exit
    python3 -m venv "$ENV_NAME"

    # Activate environment
    source "$ENV_DIR/$ENV_NAME/bin/activate"

    # upload pip
    python -m pip install --upgrade pip

    # Install requirements
    pip install -r "$PATH_REQUIREMENTS"

    # Deactivate environment
    deactivate
    
fi
