# How to

```
python -m pip install -e . # install locally

python -m pip install pip-tools build twine pytest

pip-compile # produces requirements.txt

python -m build # build sdist(tar.gz) and bdist(wheel)

twine upload dist/* # publish to pypi
```