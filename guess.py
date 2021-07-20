import random
r = random.randint(1,100)
while True:
	num = int(input('guess a number:'))
	if num == r:
		print('you are right!')
		break
	elif num > r:
		print('too big')
	elif num < r:
		print('too small')
		