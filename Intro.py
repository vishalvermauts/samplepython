import time
import sys

def type_with_sound(message, delay=0.1):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        print('\a', end='', flush=True)  # This prints the bell sound (beep)
        time.sleep(delay)

if __name__ == "__main__":
    cryptic_message = "H3LL0, W3LC0M3 T0 TH3 MYST3R1OUS W0RLD 0F PYTH0N!"
    type_with_sound(cryptic_message)
