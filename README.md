# Umbrela
Should you take a umbrella these days?


## How to run

1. Create a virtualenv and install the requirements.

```
$ pip install -r requirements_dev.txt
```

2. From the project root, run the command:

```
OPEN_WEATHER_API_KEY="YOUR_API_KEY_GOES_HERE" python -m umbrella.app --lat -21.1794579 --lon -47.8726259
```

*PS: replace the API KEY with yours.*


## Makefile
This project uses a makefile with the following commands:

* `clean`: remove pyc and pycache.
* `check`: check for formatting errors.
* `black`: apply the code formatter.
* `test`: run the tests.