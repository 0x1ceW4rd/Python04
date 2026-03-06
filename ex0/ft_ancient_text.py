#!/usr/bin/env python3

import sys


print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
try:

    file = open("ancient_fragment.txt", "r")

    print(f"Accessing Storage Vault: {file.name}")
    print("Connection established...")
    print()
    print("WHAT WAS FOUND:")
    print(file.read())

    file.close()
    print()
    print("Data recovery was succesfull. Storage unit disconnected.")
except FileNotFoundError:
    print("Oops!\nThe file you are looking for siezed to exist.")