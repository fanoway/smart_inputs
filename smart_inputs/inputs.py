import typing as t

from . import validators
from .loop import ValidatorLoop

# Update the global input function to be the same with `cast` argument that takes in the datatype parameter.
# Make use of the validator functions, and decorate with loop function, if `keep_looping` is enabled in input
# function.
def custom_input(
    prompt: t.Optional[str] = None,
    cast: t.Type[t.Any] = None,
    keep_looping: bool = False,
    default: t.Any = None,
    **kwargs: t.Any
) -> t.Any:
    """
    Custom input function built on top of the `input` function.
    This function takes in the datatype parameter and validates the input. Has keep_looping if there is
    need for looping over and over to validate and get the desired input, and the default to assign default
    value.

    The default and keep_loop arguments are optional, and cannot be used together.

    Parameters
    ----------
    prompt: str, optional
        The prompt to be displayed to the user.
    cast: t.Type, optional
        The datatype to cast the input to.
    keep_looping: bool
        Whether to keep looping over and over to validate and get the desired input.
    default: t.Any
        The default value to assign if the input is invalid.
    **kwargs: t.Any
        The keyword arguments to pass to the validator function, and some to the input function.
    """
    # Ensure cast is a valid datatype.
    if not cast:
        cast = str

    # Ensure default and keep looping are not enabled together.
    if default is not None and keep_looping:
        raise ValueError("Cannot enable default value and keep looping.")

    # Get the validator for the datatype.
    validator = getattr(validators, f"{cast.__name__}_validator")()

    # Initialize loop
    validator_loop = ValidatorLoop(validator, prompt, kwargs.get("error_message", None), keep_looping)

    # Set input to None.
    kwargs["input"] = None

    # Validate it using validator loop.
    kwargs["input"] = validator_loop(**kwargs)

    # If default is enabled and the value is doesn't pass validation, use the default value.
    if default is not None and not validator.validate(**kwargs):
        kwargs["input"] = default

    # Return casted value, if the validation checks pass, or the default.
    if validator.validate(**kwargs):
        return cast(kwargs["input"])

    return kwargs["input"]
