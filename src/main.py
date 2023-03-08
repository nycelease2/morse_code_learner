#!/bin/python3
import random, sys

running = True
main_dict = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h':'....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...','t': '-', 'u': '..-', 'v': '...-', 'w': '.---', 'x': '-..-', 'y':  '-.--', 'z': '--..'}

list_dict = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print("to exit type 'exit'")
score = 0
wrong = 0
while running:
    x = random.randint(1, 26)

    morse_input = input(f"what is the morse code for {list_dict[x]}: ")

    if morse_input.lower() == 'exit':
        print(f"score: {score}")
        print(f"wrong: {wrong}")
        running = False
    elif morse_input == main_dict[list_dict[x]]:
        print("correct")
        score += 1
    else:
        print("wrong :( ")
        print("the correct answer was")
        print(main_dict[list_dict[x]])
        wrong += 1
