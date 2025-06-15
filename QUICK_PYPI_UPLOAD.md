# Quick PyPI Upload Guide

## 0. Clean old builds (recommended)
```bash
rm -rf dist/ build/ *.egg-info
```

## 1. Build the distribution
```bash
python -m build
```

## 2. Check the distribution (optional)
```bash
twine check dist/*
```

## 3. Upload to PyPI
```bash
twine upload dist/*
```

## 4. (Optional) Test installation
```bash
pip install badcode_utilities
```

---

For more details, see: https://packaging.python.org/tutorials/packaging-projects/
