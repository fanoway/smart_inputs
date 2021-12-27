from typing import Any, Callable


class SmartLoop:
    """Decorator for validator methods to apply looping logic to it.
    Note: all returns are user inputted string, must cast to type outside of validator

    Attributes
    ----------
    prompt : str
        User prompt to dispaly when collecting input
    error_message: str
        Error message to display whenn an input is invalid
    val_func : Callable
        Validation method to be looped, Passed by decorator

    """

    def __init__(self, val_func: Callable, prompt: str = "", error_message: str = ""):
        """Initilaise SmartLoop Class decorator

        Parameters
        ----------
        val_func : Callable
            Validation Function to loop
        prompt : str, optional
            User Prompt to display
        error_message : str, optional
                Error MEssage to display

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
        kwargs["user_input"] = input(self.prompt)
        validated = self.val_func(**kwargs)

        while not validated:
            kwargs["user_input"] = input(kwargs.get("error_message", ""))
            validated = self.val_func(**kwargs)

        return kwargs["user_input"]
