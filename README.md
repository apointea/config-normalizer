# Uniform Configuration

*Goal of this project* : Separate _Human noisy configuration file_ and your
awesome application. Avoid hard coded parts in your application because of
the production needings.

*Principe*:
1. Load one of your model (yaml)
2. Merge one or more user configuration file(s) into it (yaml, xlsx)
3. Save the configurations into file validated and normalized.

Your application will thanks you so much.

## Requirements

`pip install openpyxl`

`pip install yaml`
