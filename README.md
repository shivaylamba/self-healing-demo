# self-healing-demo

A minimal demo repository for testing from e [Kimchi Self-Healing Action](https://github.com/shivaylamba/kimchi-self-healing-action).

## The Bug

`src/calculator.py` contains an intentional off-by-one bug in the `add` function:

```python
def add(a, b):
    return a + b + 1  # <-- bug: should be a + b
```

The test in `tests/test_calculator.py` expects `add(2, 3) == 5`, which fails because the function returns `6`.

## Self-Healing Workflow

`.github/workflows/self-heal.yml` runs the test suite and, on failure, invokes the composite action to automatically diagnose and fix the bug.

## Setup

1. Fork this repo
2. Add `KIMCHI_API_KEY` as a repository secret (Settings → Secrets → Actions)
3. Push a change or open a PR that breaks the test
4. Watch the self-healing workflow attempt to fix it

## License

MIT
