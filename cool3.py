import sys
from rich import print
from time import sleep

def printLyrics():
    lines = [
        ("feel like sun", 0.08),
        ("on my skin", 0.09),
        ("so this is love", 0.07),
        ("i know it is", 0.11),
        ("i know it sounds super cliché", 0.09),
        ("but you make me fell some type of way", 0.07),
        ("this is falling", 0.12),
        ("falling in love", 0.11),
        ("i got a lot on my mind", 0.08),
        ("got some more on my plate", 0.09),
        ("my baby got me looking", 0.07),
        ("forward to the end of the day", 0.09),
        ("what you say?", 0.08),
        ("you and me", 0.08),
        ("just forget about the past", 0.08),
        ("throw it in the trash", 0.08),
        ("what you say?", 0.08),
        ("you and me", 0.08),
        ("live the life we never had like", 0.1),
        ("we're never going back", 0.09),
    ]

    delays = [1.2, 1.2, 1.2, 0.7, 0.1, 0.1, 0.5, 8, 0.1, 0.1, 0.1, 0.1, 0.5, 0.9, 0.1, 0.1, 0.5, 0.9, 0.1, 0.1]

    for i, (line, char_delay) in enumerate(lines):
        words = line.split(" ")
        for word in words:
            if "you" in word.lower():
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
