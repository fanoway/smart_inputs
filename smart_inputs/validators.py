from typing import Any
import re
from abc import ABC, abstractmethod
from .smart_loop import SmartLoop


class BaseValidator(ABC):
    """Base class for validating user inputs"""

    def __init__(self) -> None:
        pass

    @staticmethod
    @abstractmethod
    @SmartLoop
    def validate(**kwargs: Any) -> Any:
        pass


class str_Validator(BaseValidator):
    """Validator for String type inputs"""

    @staticmethod
    @SmartLoop
    def validate(**kwargs: Any) -> bool:
        """Validate string against regex

        Parameters
        ----------
        user_input : str, optional
            String to Validate.
        regex : str, optional
            Regex expression to validate.
        allow_empty : bool, default False
            If True then a blank value can be returned.

        Returns
        -------
        bool
            True if user_input is validated
        """

        # Get regex
        regex = kwargs.get("regex", None)

        # Check if the input can be empty.
        if kwargs.get("allow_empty", False):
            # If empty, return True, remove leading white space.
            if not bool(kwargs["user_input"].strip()):
                return True

        if regex is None:
            return True

        # Check a fullmatch is found
        return re.fullmatch(regex, kwargs["user_input"]) is not None


class int_Validator(BaseValidator):
    """Validator for Integer type inputs"""

    @staticmethod
    @SmartLoop
    def validate(**kwargs: Any) -> bool:
        """Validate a string input as an integer input against the min and max values

        Parameters
        ----------
        user_input : str, optional
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
            True if user_input is validated
        """

        # Get value range
        minimum = kwargs.get("minimum", None)
        maximum = kwargs.get("maximum", None)

        # Check if the input can be empty.
        if kwargs.get("allow_empty", False):
            # If empty, return True, remove leading white space.
            if not bool(kwargs["user_input"].strip()):
                return True

        try:
            test_val = int(kwargs["user_input"])
        except ValueError:
            return False

        if (minimum is not None) and (test_val < minimum):
            return False

        if (maximum is not None) and (test_val > maximum):
            return False

        return True


class float_Validator(BaseValidator):
    """Validator for bool type inputs"""

    @staticmethod
    @SmartLoop
    def validate(**kwargs: Any) -> bool:
        """Validate a string input as a float input against the min and max values

        Parameters
        ----------
        user_input : str, optional
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
            True if user_input is validated
        """

        # Get value range
        minimum = kwargs.get("minimum", None)
        maximum = kwargs.get("maximum", None)

        # Check if the input can be empty.
        if kwargs.get("allow_empty", False):
            # If empty, return True, remove leading white space.
            if not bool(kwargs["user_input"].strip()):
                return True

        try:
            test_val = float(kwargs["user_input"])
        except ValueError:
            return False

        if (minimum is not None) and (test_val < minimum):
            return False

        if (maximum is not None) and (test_val > maximum):
            return False

        return True


class bool_Validator(BaseValidator):
    """Validator for boolean type inputs"""

    @staticmethod
    @SmartLoop
    def validate(**kwargs: Any) -> bool:
        """Validate a string input as a bool input against the min and max values

        Parameters
        ----------
        user_input : str, optional
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
            True if user_input is validated
        """

        # Check if the input can be empty.
        if kwargs.get("allow_empty", False):
            # If empty, return True, remove leading white space.
            if not bool(kwargs["user_input"].strip()):
                return True

        try:
            bool(kwargs["user_input"])
        except ValueError:
            return False

        return True
