import typing as t


class ValidatorLoop:
    def __init__(
        self,
        validator: t.Callable,
        prompt: t.Optional[str] = None,
        error_message: t.Optional[str] = None,
        keep_looping: bool = False
    ) -> None:
        self.validator = validator

        if prompt is None:
            prompt = ""

        if error_message is None:
            error_message = "Invalid input. Please try again."

        self.prompt = prompt
        self.error_message = error_message
        self.keep_looping = keep_looping

    def __call__(self, **kwargs: t.Any) -> t.Union[str, int, float, bool]:
        # Add input to the kwargs.
        kwargs["input"] = input(self.prompt, **kwargs)
        validated = self.validator.validate(**kwargs)

        # If the input is invalid and keep looping is enabled, loop until valid input is given.
        while not validated and self.keep_looping:
            print(self.error_message)

            kwargs["input"] = input(self.prompt, **kwargs)
            validated = self.validator.validate(**kwargs)

        return kwargs["input"]
