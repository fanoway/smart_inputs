"""smart_inputs methods to collect user inputs in an easier to read way
"""

import re
from typing import Optional, Any, Callable


class SmartLoop:
    """Decorator for validator methods to apply looping logic to it.
    Note: all returns are user inputted string, must cast to type outside of validator

    Attributes
    ----------
    prompt : str
        User prompt to dispaly when collecting input
    val_func : Callable
        Validation method to be looped, Passed by decorator

    """

    def __init__(self, val_func: Callable, prompt: str = ""):
        """Initilaise SmartLoop Class decorator

        Parameters
        ----------
        val_func : Callable
            Description
        prompt : str, optional
            Description

        Deleted Parameters
        ------------------
        f : Optional[Callable], optional
            Description
        """
        self.val_func = val_func
        self.prompt = prompt

    def __call__(self, **kwargs: Any) -> str:
        """Applies looping logic to input fetching

        Parameters
        ----------
        **kwargs : Any
            Optional Keyword Arguments. See validator functions for arguments

        Returns
        -------
        str
            Validated User input
        """
        kwargs["test_string"] = input(self.prompt)
        validated = self.val_func(**kwargs)

        while not validated:
            kwargs["test_string"] = input("Invalid input, retry: ")
            validated = self.val_func(**kwargs)

        return kwargs["test_string"]


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


def string_input(
    prompt: str, regex: Optional[str] = None, default: Optional[str] = None
) -> str:
    """Get string value from the user input.

    Parameters
    ----------
    prompt : str
        User Prompt to display.
    regex : Optional[str], optional
        Regex pattern that input string form user must match.
    default : Optional[str], optional
        Default value, used if a blank is passed from the user.

    Returns
    -------
    str
        Users validated input.
    """

    # Display default in prmompt if it is passed by user
    if default is not None:
        prompt = f"{prompt} [{default}] "

    string_validator.prompt = prompt
    response: str = string_validator(regex=regex, allow_empty=bool(default))

    if not bool(response) and default is not None:
        response = default

    return response


def int_input(
    prompt: str, min_val: int = None, max_val: int = None, default: int = None
) -> int:
    """Get an interger value from the user

    Parameters
    ----------
    prompt : str
        User Prompt to display.
    min_val : int, optional
        Minimum Value to accept.
    max_val : int, optional
        Maximum Value to accept.
    default : int, optional
        Default value if a blank is returned

    Returns
    -------
    int
        Users validated input.
    """

    # Display default in prmompt if it is passed by user
    if default is not None:
        prompt = f"{prompt} [{default}] "

    int_validator.prompt = prompt
    response: str = int_validator(
        min_val=min_val, max_val=max_val, allow_empty=bool(default)
    )

    if not bool(response) and default is not None:
        response = str(default)

    return int(response)


def float_input(
    prompt: str, min_val: float = None, max_val: float = None, default: int = None
) -> float:
    """Return a float input from the user

    Parameters
    ----------
    prompt : str
        User Prompt to display.
    min_val : float, optional
        Minimum Value to accept.
    max_val: float, optional
        Maximum Value to accept.
    default : float, optional
        Default value if a blank is returned.

    Returns
    -------
    float
        Users validated input.
    """

    # Display default in prmompt if it is passed by user
    if default is not None:
        prompt = f"{prompt} [{default}] "

    float_validator.prompt = prompt
    response: str = float_validator(
        min_val=min_val, max_val=max_val, allow_empty=bool(default)
    )

    if not bool(response) and default is not None:
        response = str(default)

    return float(response)
