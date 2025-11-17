"""
Functions used in preparing Guido's gorgeous lasagna.
"""

# Constants
EXPECTED_BAKE_TIME = 40        # total expected bake time
PREPARATION_TIME = 2           # minutes per layer


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes)

    This function returns how many minutes the lasagna still needs 
    to bake based on the EXPECTED_BAKE_TIME.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time.

    :param number_of_layers: int - number of lasagna layers.
    :return: int - preparation time in minutes.
    """
    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate total elapsed cooking time.

    :param number_of_layers: int - number of lasagna layers.
    :param elapsed_bake_time: int - bake time already elapsed.
    :return: int - total time spent (prep + bake)
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
