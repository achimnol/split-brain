# SplitBrain

Split virtualenvs for Python subinterpreters

## Testing

```
cd samples/example-plugin/
uv run pex $(uv pip freeze) -o example-plugin.pex
cd ../../
uv run hello.py
```
