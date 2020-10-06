# Energy Tracker Build Controller 

## Installing & Running CLI app

For if you just want to run the app.

Ensure you are not in a virtual env, and run:
```
make install
```

Add bin location to path with:
```
export PATH="`make getbinpath`:$PATH"
```

Run using:
```
energy-tracker-build deploy
```

## Developing

### One time setup - Virtual env

Set up the virtual environment (just once, after checking out the repo).

From the builder directory run:

```
python3 -m venv --prompt cloudfront-cert-rotator venv
```

### When developing

Every time you start a new terminal session:
```
source venv/bin/activate
```

To install dependencies:
```
make deps
```

To run locally (dev run):
```
python3 app.py
```
