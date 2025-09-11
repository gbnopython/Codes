import sys
from rich import print
from time import sleep

def printLyrics():
    lines = [
        ("i think we're meant to be", 0.08),
        ("but i fucked up, definitely", 0.07),
        ("she keeps on texting me", 0.06),
        ("do i like her? no, definitely", 0.07),
        ("i'm just like stephanie", 0.09),
        ("do i like her? yeah 'speacially", 0.06),
    ]

    delays = [0.1, 0.1, 0.1, 0.1]

    for i, (line, char_delay) in enumerate(lines):
        
        words = line.split(" ")
        for word in words:
            for char in word:
                
                if word.lower() in ["like", "especially"]:
                    print(f"[bold][red]{char}[/red][/bold]", end='')
                
                elif word.lower() == "texting":
                    print(f"[orange4]{char}[/orange4]", end='')
               
                else:
                    print(f"[bold][gold3]{char}[/gold3][/bold]", end='')
                sys.stdout.flush()
                sleep(char_delay)
            print(" ", end='')  
        print()
        sleep(delays[i])

printLyrics()
