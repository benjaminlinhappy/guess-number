import random
start = int(input('please decide the start value of the random number:'))
end = int(input('please decide the end value of the random number:'))

r = random.randint(start, end)
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
