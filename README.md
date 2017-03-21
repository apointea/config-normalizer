# Uniform Configuration

**Goal of this project** : Build a configuration model for you application and fill it with various input.

**Principe** :

1. Load your configuration model(s)
2. Push it with various inputs (yaml, xlsx, json)
3. Export your model into an uniform configuration file (yaml)

**Benefits** :

It allows you to focus your application on the stuff it need to do not on the inputs it need to handle.

**Mecanisms builtins**:

* include - *cut your model into separate parts*
* pattern - *repeat a model over an array*
* validator - *assert value format*
* transformation - *transform values bef/aft validate*

## Requirements

`pip install openpyxl`

`pip install yaml`

## Quick Start

To start, I recommend you to launch the example into the interactive mode:

`./uniform-config.py --example --interactive`

Then type `help` to see the available commands (tips: `extract` is well to see a preview)
