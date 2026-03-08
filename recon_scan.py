import os

target = input("Enter target IP: ")

print("\nStarting Nmap Scan...\n")

command = f"nmap -sV {target} -oN scan_results.txt"
os.system(command)

print("\nScan complete!")
print("Results saved in scan_results.txt")
