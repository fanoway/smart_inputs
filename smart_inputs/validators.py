from .smart_loop import SmartLoop
from Typing import Optional, Any
import re


class BaseValidator:
    """Base class for validating user inputs"""

    def __init__(self, validation_type: Any) -> None:
        self.validation_type = validation_type

    def validate(self, **kwargs: Any) -> None:

        raise NotImplementedError(
            "This method should be implemented by the child class."
        )


class Str_Validator:
    """ Validator for String type inputs"""

    def __init__(self) -> None:
        super().__init__(int)

    def validate(self, **kwargs) -> bool:
        


@SmartLoop
def string_validator(
    test_string: str = "", regex: Optional[str] = None, allow_empty: bool = False
) -> bool:
    """Validate string against regex

    Parameters
    ----------
    test_string : str, optional
        String to Validate.
    regex : Optional[str], optional
        Regex expression to validate.
    allow_empty : bool, default False
        If True then a blank value can be returned.

    Returns
    -------
    bool
        True if test_string is validated
    """

    # No Regex so everything is valid

    if regex is None:
        return True

    # if there is a default value allow empty strings

    if allow_empty and not test_string:
        return True

    # Check a fullmatch is found
    return re.fullmatch(regex, str(test_string)) is not None


@SmartLoop
def int_validator(
    test_string: str = "",
    min_val: int = None,
    max_val: int = None,
    allow_empty: bool = False,
) -> bool:
    """Validate a string input as an integer input against the min and max values

    Parameters
    ----------
    test_string : str, optional
        String to validate.
    min_val : int, optional
        Minimum allowable value.
    max_val : int, optional
        Maximum Allowable Value.
    allow_empty : bool, default False
        If True then a blank value can be returned

    Returns
    -------
    bool
        True if test_string is validated
    """

    # Default value case
    if allow_empty and not bool(test_string):
        return True

    try:
        test_val = int(test_string)
    except ValueError:
        return False

    if (min_val is not None) and (test_val < min_val):
        return False

    if (max_val is not None) and (test_val > max_val):
        return False

    return True


@SmartLoop
def float_validator(
    test_string: str = "",
    min_val: float = None,
    max_val: float = None,
    allow_empty: bool = False,
) -> bool:
    """Validate a string input as a float input against the min and max values

    Parameters
    ----------
    test_string : str, optional
        String to validate.
    min_val : float, optional
        Minimum allowable value.
    max_val : float, optional
        Maximum Allowable Value.
    allow_empty : bool, default False
        If True then a blank value can be returned

    Returns
    -------
    bool
        True if test_string is validated
    """

    # Default value case
    if allow_empty and not bool(test_string):
        return True

    try:
        test_val = float(test_string)
    except ValueError:
        return False

    if (min_val is not None) and (test_val < min_val):
        return False

    if (max_val is not None) and (test_val > max_val):
        return False

    return True
