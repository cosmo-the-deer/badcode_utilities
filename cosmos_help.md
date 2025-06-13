# help doc for cosmo the deer
lol im sorry

## how to publish:

update the version in ```set_up.py```

---

delete old build files to not get confused

``` bash
rm -rf dist/ build/ *.egg-info
```
---

Rebuild your package:

```bash
python3 setup.py sdist bdist_wheel
```
---

Upload again:

```bash
twine upload dist/*
```

## how to upload docs: