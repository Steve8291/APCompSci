import time


y = 0
while y <= 5:
    print(y)
    y += 1
print(f"y is equal to {y}")

choice = "No"
while choice != 'Yes':
    print("Press ctrl-C to exit this infinite loop!")
    time.sleep(1)  # Pause so we don't crash the computer

print("Choice = 'Yes'")
