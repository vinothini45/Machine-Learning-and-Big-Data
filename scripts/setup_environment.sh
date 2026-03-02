#!/bin/bash

echo "Setting up environment..."

# Update pip
pip install --upgrade pip

# Install required Python packages
pip install pyspark
pip install datasets
pip install pyarrow
pip install pandas
pip install scikit-learn
pip install pyyaml

# Create project directory structure if not exists
mkdir -p data/raw
mkdir -p data/processed
mkdir -p data/exports
mkdir -p models
mkdir -p logs

echo "Environment setup completed."