import time


num = 0
while num <= 5 or num > 20:
    print(f"num = {num}")
    num += 1

print(f"The final value of num = {num}")


choice = "No"
while choice != 'Yes':
    print("Press ctrl-C to exit this infinite loop!")
    time.sleep(1)  # Pause so we don't crash the computer

print("Choice = 'Yes'")
