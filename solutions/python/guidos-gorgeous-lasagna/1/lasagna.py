"""
This module contains functions to calculate baking and preparation times for lasagna.
"""

# Constants
EXPECTED_BAKE_TIME = 40  # minutes the lasagna should bake in the oven
PREPARATION_TIME = 2     # minutes it takes to prepare one layer

# Function 1: Calculate remaining bake time
def bake_time_remaining(elapsed_bake_time):
    """
    Calculate the remaining bake time for the lasagna.

    :param elapsed_bake_time: int - time already spent baking
    :return: int - remaining bake time
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

# Function 2: Calculate preparation time based on layers
def preparation_time_in_minutes(number_of_layers):
    """
    Calculate preparation time based on the number of layers.

    :param number_of_layers: int - number of lasagna layers
    :return: int - total preparation time
    """
    return PREPARATION_TIME * number_of_layers

# Function 3: Calculate total elapsed time
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Calculate total time spent on lasagna (preparation + baking).

    :param number_of_layers: int - number of layers
    :param elapsed_bake_time: int - time already spent baking
    :return: int - total elapsed time
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
