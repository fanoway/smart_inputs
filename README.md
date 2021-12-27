[![pdm-managed](https://img.shields.io/badge/pdm-managed-blueviolet)](https://pdm.fming.dev)
[![PyPI version](https://badge.fury.io/py/smart-inputs.svg)](https://badge.fury.io/py/smart-inputs)

# smart_inputs
Smarter methods to get user input in python including defaults, regex and type validation. Requests for rentry are handled automatically if the validation fails

# Installation

	pip install smart_inputs

# Usage

### String input with regex to r1euire a capitalised word

	from smart_inputs import string_input

	string = string_input('What is your name? ', regex="[A-z][a-z]+")

### Integer input with a minimum value

	from smart_inputs import int_input

	integer = int_inpuT('How old are you ? ', min_val = 0)

### Float input with a default value

	from smart_inputs import float_input

	float = float_input('Whats your GPA? ', min_val = 0, max_val = 4.0, default = 2.5)