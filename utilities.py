import time

def slow_print(text: str, delay = 0.09, end='\n'):
    for character in text:
        print(character, end="", flush=True)
        time.sleep(delay)
    print(end, end='', flush=True)