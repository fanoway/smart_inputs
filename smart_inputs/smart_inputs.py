"""smart_inputs methods to collect user inputs in an easier to read way
"""

import re
from typing import Optional, Any, Callable, Union


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
        """Summary

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
def string_validator(test_string: str = "", regex: Optional[str] = None) -> bool:
    """Validate string against regex

    Parameters
    ----------
    test_string : str, optional
        String to Validate.
    regex : Optional[str], optional
        Regex expression to validate.

    Returns
    -------
    bool
        True if test_string is validated
    """

    if regex is None:
        return True

    return re.fullmatch(regex, str(test_string)) is not None


@SmartLoop
def int_validator(
    test_string: str = "", min_val: int = None, max_val: int = None
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

    Returns
    -------
    bool
        True if test_string is validated
    """
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
    test_string: str = "", min_val: float = None, max_val: float = None
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

    Returns
    -------
    bool
        True if test_string is validated
    """

    try:
        test_val = float(test_string)
    except ValueError:
        return False

    if (min_val is not None) and (test_val < min_val):
        return False

    if (max_val is not None) and (test_val > max_val):
        return False

    return True


def string_input(prompt: str, regex: Optional[str] = None) -> str:
    """Test method to check imports are working correctly

    Parameters
    ----------
    prompt : str
        User Prompt to display.
    regex : Optional[str], optional
        Description

    Returns
    -------
    str
        Users validated input.
    """

    string_validator.prompt = prompt
    return string_validator(regex=regex)


def num_input(
    prompt: str,
    min_val: Optional[Union[int, float]] = None,
    max_val: Optional[Union[int, float]] = None,
    force_int: bool = False,
) -> Union[int, float]:
    """Summary

    Parameters
    ----------
    prompt : str
        User Prompt to Display
    min_val : Optional(Union[int, float]), optional
        Minimum Value to accept.
    max_val: Optional(Union[int, float]), optional
        Maximum Value to accept.
    force_int : bool, optional
        Force user to input an int
    """
    if force_int:
        int_validator.prompt = prompt
        return int(int_validator(min_val=min_val, max_val=max_val))
    else:
        float_validator.prompt = prompt
        return float(float_validator(min_val=min_val, max_val=max_val))
