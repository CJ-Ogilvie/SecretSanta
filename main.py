from configuration import get_names
from generate_gift_map import generate_gift_map
from results_log import get_log_path, log_event, log_gift_map
from send_text import send_message

print("Looking up names: ")
names = get_names()
print("Generating a random map of gifts, with exclusions handled:")
gift_map = generate_gift_map(names)

log_event(f"Names in this draw: {', '.join(sorted(names))}")
log_gift_map(gift_map)

print("Sending out automated texts:")
failed_givers = []
for giver, receiver in gift_map.items():

    message = (f"Secret Santa message for {giver}. "
               f"You have been selected to give a gift to {receiver}! "
               f"- C.J.'s script")

    # Keep going if one text fails, so the rest of the group still gets told
    try:
        send_message(message, giver)
    except Exception as error:
        failed_givers.append(giver)
        log_event(f"FAILED to send to {giver}: {error!r}")
        print(f"Sending to {giver} failed: {error}")
    else:
        log_event(f"Sent to {giver}")

if len(failed_givers) > 0:
    log_event(f"Run finished with {len(failed_givers)} failed message(s).")
    print(f"Messages sent, except for: {', '.join(failed_givers)}. "
          f"Tell them their assignment yourself, it is in the log file.")
else:
    log_event("Run finished, all messages sent.")
    print("Messages sent!")

# Only the location is printed, never the results themselves
print(f"Results were written to '{get_log_path()}' if you ever need to look them up.")
