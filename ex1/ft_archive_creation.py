#!/usr/bin/env python3

print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
try:
    file = open("new_discovery.txt", "w")

    print(f"Initializing new storage unit: {file.name}")
    print("Storage unit created successfully...")
    print()
    print("Inscribing preservation data...")

    file.write("[ENTRY 001] New quantum algorithm discovered\n"
               "[ENTRY 002] Efficiency increased by 347%\n"
               "[ENTRY 003] Archived by Data Archivist trainee")

    file = open("new_discovery.txt", "w")
    print(file.read())
    file.close()
    print()
    print("Data inscription complete. Storage unit sealed.")
    print(f"Archive '{file.name}' ready for long-term preservation.")
except Exception as e:
    print(e)
