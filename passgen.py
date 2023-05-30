#!/usr/bin/env python3

import random
import string

import pyperclip


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    return password


def print_password(password):
    separator = "-" * len(password)
    print(f"\n{separator}\n{password}\n{separator}\n")


def copy_password_to_clipboard(password):
    pyperclip.copy(password)
    print("[*] Your password has been copied.")


def main():
    print("[!] Password Generator\n")
    while True:
        try:
            length = int(input("Enter password length: "))
            if length <= 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")
    password = generate_password(length)
    print_password(password)
    copy_password_to_clipboard(password)


if __name__ == "__main__":
    main()
