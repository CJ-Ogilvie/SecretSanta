import random
from configuration import get_exclusions

def generate_gift_map(names: list[str]) -> dict:

    # Set up data
    gift_map = {}
    remaining_givers = names.copy()
    remaining_receivers = names.copy()

    max_attempts = 100
    attempt = 0
    while len(remaining_givers) > 0:
        # Grab next giver to assign a receiver
        giver = remaining_givers.pop()

        # Get eligible receivers
        eligible_receivers = remaining_receivers.copy()
        for person in get_exclusions(giver):
            if person in eligible_receivers:
                eligible_receivers.remove(person)

        # Check if any solution is possible
        if len(eligible_receivers) == 0:
            print("Random generation did not produce an eligible solution. Resetting solution.")
            gift_map = {}
            remaining_givers = names.copy()
            remaining_receivers = names.copy()
            attempt += 1
            assert attempt < max_attempts, "Max attempts exceeded. No solution was found."
            continue  # Start the next iteration of the loop

        # Assign a random receiver
        receiver = random.choice(list(eligible_receivers))  # Cast 'set' to 'list' so it works with choice.

        # Update solution
        gift_map[giver] = receiver
        remaining_receivers.remove(receiver)
        # Note 'pop' already removed giver from the remaining givers set

    print("Solution found!")
    return gift_map
