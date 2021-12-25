import pytest  # noqa
from smart_inputs.smart_inputs import string_input


@pytest.mark.parametrize(
    "prompt, response",
    [("a", "a"), (42, "42"), ("56/nrte", "56/nrte"), ("Hello World", "Hello World")],
)
def test_prompt(capfd, prompt, response):
    response = string_input(prompt)
    assert response == prompt
