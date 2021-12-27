"""smart_inputs methods to collect user inputs in an easier to read way
"""
from typing import Any, Type

from . import validators


def smart_input(
    prompt: str, cast: Type = str, default: Any = None, **kwargs: Any
) -> Any:
    """Get the validated user input, will automatically repeatedly for the entry if it cannot be validated
    Parameters
    ----------
    prompt : str
        User Prompt to display.
    cast : Type, optional
        Type to cast the user input to, default is str
    default : Any, optional
        Default value, used if a blank is passed from the user.
    regex : str, optional
        Regex pattern that input string form user must match.
    minimum: int | float, optional
        Minimum acceptable value for numerical inputs
    maximum: int | float, optional
        Maximum acceptable value for numerical inputs
    error_message: str, optional
        Override default error message to display when an input is invalid

    Returns
    -------
    str
        Users validated input.
    """
    # Display default in prmompt if it is passed by user
    if default is not None:
        prompt = f"{prompt} [{default}] "

    # Get validator
    try:
        validator = getattr(validators, f"{cast.__name__}_Validator")()
    except AttributeError:
        raise NotImplementedError(f"Type {cast.__name__} not yet implemented")

    validator.validate.prompt = prompt
    validator.validate.error_message = kwargs.get(
        "error_message", "Invalid input, retry: "
    )
    response: Any = validator.validate(**kwargs, allow_empty=bool(default))

    # Return default if a blank returned and a default is specified
    if not bool(response) and default is not None:
        response = default

    return cast(response)
