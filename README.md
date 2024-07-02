Setup process:

```sh
# venv setup
poetry new pdm-act02
cd pdm-act02
poetry add flet
source ~/.cache/pypoetry/virtualenvs/pdm-act0-xYz-py3.12/bin/activate

# flet setup
flet --version
flet create pdm-act02

# flet live reload
flet run -d pdm-act02
```

Initial file hierarchy:

```
pdm-act02
├── README.md
├── pdm_act02
│   ├── __init__.py
│   ├── assets
│   │   └── icon.png
│   ├── main.py
│   └── requirements.txt
├── poetry.lock
├── pyproject.toml
└── tests
    └── __init__.py
```

## References
- [Getting started | Flet](https://flet.dev/docs/getting-started/)

