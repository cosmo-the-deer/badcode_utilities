# Help Doc for Cosmo the Deer

Welcome! This guide will help you publish your Python package to PyPI and upload your documentation.

## How to Publish to PyPI

1. **Update the version in `setup.py`**
   - Make sure to increment the version number each time you publish.

2. **Delete old build files** (to avoid confusion):
   ```bash
   rm -rf dist/ build/ *.egg-info
   ```

3. **Rebuild your package:**
   ```bash
   python3 setup.py sdist bdist_wheel
   ```

4. **Upload to PyPI:**
   ```bash
   twine upload dist/*
   ```
   - When prompted for username, enter: `__token__`
   - When prompted for password, paste your PyPI API token (starts with `pypi-...`)

---

## How to Upload Docs (with MkDocs Material)

1. **Edit your documentation files** in the `docs/` folder.
2. **Commit and push your changes to the `main` branch:**
   ```bash
   git add docs/ mkdocs.yml
   git commit -m "Update docs"
   git push origin main
   ```
3. **GitHub Actions will automatically build and deploy your docs** to GitHub Pages at:
   [https://cosmo-the-deer.github.io/badcode_utilities/](https://cosmo-the-deer.github.io/badcode_utilities/)

---

If you have any issues, check the GitHub Actions tab for workflow logs and errors.