from configuration import get_names
from generate_gift_map import generate_gift_map
from send_text import send_message

print("Looking up names: ")
names = get_names()
print("Generating a random map of gifts, with exclusions handled:")
gift_map = generate_gift_map(names)

print("Sending out automated texts:")
for giver, receiver in gift_map.items():

    message = (f"This is an automated message from C.J.'s script intended for {giver}. "
               f"For Secret Santa, you have been selected to give a gift to {receiver}! "
               f"If there's something wrong with this, text C.J. please!")

    send_message(message, giver)

print("Messages sent!")