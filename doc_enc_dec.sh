#!/bin/bash

# Get the virtual environment name (modify if needed)
VENV_NAME="my_venv"

# Check if the virtual environment directory exists
if [[ -d "$VENV_NAME" ]]; then
  # Virtual environment exists
  echo "Virtual environment '$VENV_NAME' exists."
else
  echo "Virtual environment '$VENV_NAME' does not exist so creating..."
  python3 -m venv $VENV_NAME
  echo "Virtual environment has been created"
fi
# Activate a virtual environment
source $VENV_NAME/bin/activate
echo "Checking and installing required libraries"
python3 -m pip install -r requirements.txt
# Call your Python script with necessary arguments
python3 doc_enc_dec.py "$@"
# Deactivate virtual environment
deactivate