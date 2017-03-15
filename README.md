# Uniform Configuration

**Goal of this project** : Build a configuration model for you application and fill it with various input.

**Principe** :

1. Load your configuration model(s) - *MECANISMS : include, pattern, validator, transformation, default values*
2. Push it with various inputs (yaml, xlsx, json) - *MECANISMS : fit, fill*
3. Export your model into an uniform configuration file (yaml)

**Benefits** :

It allows you to focus your application on the stuff it need to do not on the inputs it need to handle.

## Requirements

`pip install openpyxl`

`pip install yaml`

## Quick Start

`./main.py -o out.xml`
