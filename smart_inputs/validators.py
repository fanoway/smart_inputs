import re
import typing as t


# Base class for validating inputs. Inherited as a base class by all input validators for different datatypes.
class BaseValidator:
    def __init__(self, validation_type: t.Type[t.Any]) -> None:
        self.validation_type = validation_type

    def validate(self, **kwargs: t.Any) -> None:
        raise NotImplementedError(
            "This method should be implemented by the child class."
        )


# Define the validator for the INT type.
class int_validator(BaseValidator):
    def __init__(self) -> None:
        super().__init__(int)

    def validate(self, **kwargs: t.Any) -> bool:
        # Get the minimum and maximum range values.
        min_value = kwargs.pop("min_value", None)
        max_value = kwargs.pop("max_value", None)

        # Check if the input can be empty.
        if kwargs.get("allow_empty", False):
            # If empty, return True.
            if kwargs["input"].strip() == "":
                return True

        # Validate and ensure it's the correct datatype by conversion.
        try:
            value = int(kwargs["input"])
        except ValueError:
            return False

        # Check if the value is within the range.
        if min_value is not None and value < min_value:
            return False

        if max_value is not None and value > max_value:
            return False

        return True


# Define the validator for the FLOAT type.
class float_validator(BaseValidator):
    def __init__(self) -> None:
        super().__init__(float)

    def validate(self, **kwargs: t.Any) -> bool:
        # Get the minimum and maximum range values.
        min_value = kwargs.pop("min_value", None)
        max_value = kwargs.pop("max_value", None)

        # Check if the input can be empty.
        if kwargs.get("allow_empty", False):
            # If empty, return True.
            if kwargs["input"].strip() == "":
                return True

        # Validate and ensure it's the correct datatype by conversion.
        try:
            value = float(kwargs["input"])
        except ValueError:
            return False

        # Check if the value is within the range.
        if min_value is not None and value < min_value:
            return False

        if max_value is not None and value > max_value:
            return False

        return True


# Define the validator for the STRING type.
class str_validator(BaseValidator):
    def __init__(self) -> None:
        super().__init__(str)

    def validate(self, **kwargs: t.Any) -> bool:
        # Get the minimum and maximum length values.
        min_length = kwargs.pop("min_length", None)
        max_length = kwargs.pop("max_length", None)

        # Get the validation regex.
        regex = kwargs.pop("regex", None)

        # Check if the input can be empty.
        if kwargs.get("allow_empty", False):
            # If empty, return True.
            if kwargs["input"].strip() == "":
                return True

        # Validate and ensure it's the correct datatype by conversion.
        try:
            value = str(kwargs["input"])
        except ValueError:
            return False

        # Check if the length is within the range.
        if min_length is not None and len(value) < min_length:
            return False

        if max_length is not None and len(value) > max_length:
            return False

        # Check if the value matches the regex.
        if regex is not None and not re.match(regex, value):
            return False

        return True


# Define the validator for the BOOLEAN type.
class bool_validator(BaseValidator):
    def __init__(self) -> None:
        super().__init__(bool)

    def validate(self, **kwargs: t.Any) -> bool:
        # Check if the input can be empty.
        if kwargs.get("allow_empty", False):
            # If empty, return True.
            if kwargs["input"].strip() == "":
                return True

        # Validate and ensure it's the correct datatype by conversion.
        try:
            _value = bool(kwargs["input"])
        except ValueError:
            return False

        return True
