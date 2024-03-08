Arc42 Demo Architecture
===

Requirements to build locally
---

- Python 3.9+
- Sphinx: https://www.sphinx-doc.org/en/master/usage/installation.html
  - Python venv: `pip install -U sphinx`
  - Ubuntu: `apt install python3-sphinx`
  - Mac: `brew install sphinx-doc`
  - Windows: `choco install sphinx`
- PlantUML for Sphinx: `pip install -U sphinxcontrib-plantuml`
- PlantUML: https://plantuml.com/en/download
  - Ubuntu: `apt install plantuml`
  - Mac: `brew install plantuml`
  - Windows: `choco install plantuml`


How to build
---

- Ubuntu/Mac: `make html`
- Windows: `make.bat html`

The created pages are in `_build/html`.
