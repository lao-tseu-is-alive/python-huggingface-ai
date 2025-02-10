#!/bin/bash
pyenv virtualenv 3.12.4 python-huggingface-ai
pyenv activate python-huggingface-ai
python -m pip install --upgrade pip
pip install tensorflow
pip install transformers
pip install tf-keras
pip install --upgrade huggingface_hub
pip install duckduckgo-search
pip install langchain
pip install langchain-community
pip install smolagents
