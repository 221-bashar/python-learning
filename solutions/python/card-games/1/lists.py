"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """
    return [number,number+1,number+2]

def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """
    return rounds_1+rounds_2
    


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """

    return number in rounds


def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """
    return sum(hand) / len(hand)
    
def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average."""
    
    # Calculate the actual average
    true_avg = sum(hand) / len(hand)
    
    # Calculate the average of the first and last cards
    first_last_avg = (hand[0] + hand[-1]) / 2
    
    # Identify the middle card
    middle_card = hand[len(hand) // 2]
    
    # Return True if either match matches the actual average
    return true_avg == first_last_avg or true_avg == middle_card


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values)."""
    
    # Slicing syntax: [start:stop:step]
    even_indexed_cards = hand[0::2]  # Starts at 0, takes every 2nd element
    odd_indexed_cards = hand[1::2]   # Starts at 1, takes every 2nd element
    
    avg_even = sum(even_indexed_cards) / len(even_indexed_cards)
    avg_odd = sum(odd_indexed_cards) / len(odd_indexed_cards)
    
    return avg_even == avg_odd

    

def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """
    # Use -1 to access the last element in the list
    if hand[-1] == 11:
        hand[-1] = 22
        
    return hand
   
