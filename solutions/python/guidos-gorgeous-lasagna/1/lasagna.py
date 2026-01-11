"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time: int) -> int:
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers: int) -> int:
    """Calculate preparation time

    :param number_of_layers: int - the number of layers added to the lasagna

    Function that takes the number of layers of lasagna and then
    multiplies that by the PREPARATION_TIME: int to get the amount of time
    that preparing the lasagna will take
    """

    return PREPARATION_TIME * number_of_layers


def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int) -> int:
    """Calculate total elapsed time (prepping + baking) in minutes

    :param number_of_layers: int - the number of layers added to the lasagna
    :param elapsed_bake_time: int - the number of minutes the lasagna has spent baking in the oven already

    Function that takes the number of layers and elapsed baking time and
    then calculates the total elapsed time using the preperation time and baking time functions
    """

    return (
        preparation_time_in_minutes(number_of_layers)
        + EXPECTED_BAKE_TIME
        - bake_time_remaining(elapsed_bake_time)
    )


print(elapsed_time_in_minutes(3, 20))

# TODO: Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)
