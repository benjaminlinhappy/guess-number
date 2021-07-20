import random
r = random.randint(1,100)
count = 0
while True:
	count += 1
	num = int(input('guess a number:'))
	if num == r:
		print('you are right!')
		print('you guessed', count, 'times in total')
		break
	elif num > r:
		print('too big')
	elif num < r:
		print('too small')
	print('this is your', count, 'guess')
