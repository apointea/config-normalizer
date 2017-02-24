# Uniform Configuration

**Goal of this project** : Separate `Human noisy configuration file` and your
awesome application. Avoid hard coded parts in your application because of
the production needings.

**Principe** :

1. Load one of your models (yaml)
2. Merge one or more user configuration file(s)(yaml, xlsx) into the model.
3. Save the configurations into file validated and normalized.

Your application will thanks you so much.

## Requirements

`pip install openpyxl`

`pip install yaml`

## Quick Start

`./main.py -o out.xml`
