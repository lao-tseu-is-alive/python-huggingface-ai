#!/bin/bash
pyenv virtualenv 3.12.4 python-huggingface-ai
pyenv activate python-huggingface-ai
python -m pip install --upgrade pip
pip install tensorflow
pip install transformers