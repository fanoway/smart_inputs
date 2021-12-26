import pytest  # noqa

# from smart_inputs.smart_inputs import string_input, string_validator


# @pytest.mark.parametrize(
#     "prompt, response",
#     [
#         ("a", "a\n"),
#         (42, "42\n"),
#         ("56/nrte", "56/nrte\n"),
#         ("Hello World", "Hello World\n"),
#     ],
# )
# def test_prompt(monkeypatch, capfd, prompt, response):

#     monkeypatch.setattr("builtins.input", lambda x: print(prompt))

#     string_input(prompt)
#     out, err = capfd.readouterr()
#     assert out == response


# @pytest.mark.parametrize(
#     "user_input, regex, result",
#     [
#         ("a", "a", True),
#         (42, "[0-9][0-9]", True),
#         (42, "[0-9][0-9][0-9]", False),
#         ("abcd", "[a-z][a-z][a-z]", False),
#         ("Hello World", None, True),
#     ],
# )
# def test__basic_string_validator(monkeypatch, user_input, regex, result):

#     monkeypatch.setattr("builtins.input", lambda x: user_input)

#     response = string_validator(test_string=user_input, regex=regex)

#     assert response == result
