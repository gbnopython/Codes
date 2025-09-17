import sys
from rich import print
from time import sleep

def printLyrics():
    lines = [
        ("it's driving' me out of my mind!", 0.11),
        ("that's why it's hard for me to find", 0.13),
        ("can't get it out of my head!", 0.15),
        ("miss her", 0.08),
        ("kiss her", 0.08),
        ("love her (wrong move you're dead!)", 0.04),
        ("that girl is", 0.06),
        ("poisoooooon", 0.1),
        ("never trust a big butt and a smile", 0.06),
        ("that girl is", 0.06),
        ("poisoooooon", 0.1),

    ]

    delays = [1.2, 0.5, 0.3, 0.4, 0.4, 0.1, 0.1, 5, 0.1, 0.1, 0.1, 0.1,]

    for i, (line, char_delay) in enumerate(lines):
        words = line.split(" ")
        for word in words:
            if "girl" in word.lower():
                color = "red"
            else:
                color = "white"
            
            for char in word:
                print(f"[bold][{color}]{char}[/{color}][/bold]", end='')
                sys.stdout.flush()
                sleep(char_delay)
            print(" ", end='')  
        print()
        if i < len(delays):
            sleep(delays[i])

printLyrics()
