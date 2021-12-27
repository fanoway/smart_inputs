[![pdm-managed](https://img.shields.io/badge/pdm-managed-blueviolet)](https://pdm.fming.dev)

[![PyPI version](https://badge.fury.io/py/smart-inputs.svg)](https://badge.fury.io/py/smart-inputs)

[![Documentation Status](https://readthedocs.org/projects/smart-inputs/badge/?version=latest)](https://smart-inputs.readthedocs.io/en/latest/?badge=latest)



# smart_inputs

Smarter methods to get user input in python including defaults, regex and type validation. Requests for rentry are handled automatically if the validation fails

# Installation

```sh
pip install smart_inputs
```

## Usage

### String input with no extra validation.

```py
from smart_inputs import smart_input

val = smart_input("Enter your name: ", cast=str)
```

### String input with phone number regex validation.

```py
from smart_inputs import smart_input

val = smart_input("Enter your phone number: ", cast=str, regex=r"^\d{3}-\d{3}-\d{4}$")
```

### Integer input with default value.

```py
from smart_inputs import smart_input

val = smart_input("Enter your age: ", cast=int, default=18)
```

### Integer input with a range.

```py
from smart_inputs import smart_input

val = smart_input("Enter your age: ", cast=int, min_val=18, max_val=65)
```

### Float input with minimum and maximum values.

```py
from smart_inputs import smart_input

val = smart_input("Enter your GPA: ", cast=float, min_val=0.0, max_val=4.0)
```

Thank you to [janaSunrise](https://github.com/janaSunrise)