[![pdm-managed](https://img.shields.io/badge/pdm-managed-blueviolet)](https://pdm.fming.dev)
[![PyPI version](https://badge.fury.io/py/smart-inputs.svg)](https://badge.fury.io/py/smart-inputs)

# smart_inputs
Smarter methods to get user input in python including regex and type validation. Requests for rentry are handled automatically if the validation fails

# Installation

	pip install smart_inputs

# Usage

	from smart_inputs import string_input

	string = string_input('What is your name? ', regex="[A-z][a-z]+")
