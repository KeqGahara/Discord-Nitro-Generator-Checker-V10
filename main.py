import random, string

print("Discord Nitro Generator + Checker V1.0")

amount = int(input('Amount of nitro codes to generate: '))
value = 1
while value <= amount:
	code = "https://discord.gift/" + ('').join(
	    random.choices(string.ascii_letters + string.digits, k=16))
	f = open('Nitro Classic Codes.txt', "a+")
	f.write(f'{code}\n')
	f.close()
	print(f'Invalid | {code}')
	value += 1

	code = "https://discord.gift/" + ('').join(
	    random.choices(string.ascii_letters + string.digits, k=24))
	f = open('Nitro Boost Codes.txt', "a+")
	f.write(f'{code}\n')
	f.close()
	print(f'Invalid | {code}')
	value += 1
  