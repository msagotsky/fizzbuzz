x = 0

while x < 100:	x +=  1
	fizz = x % 3
	buzz = x % 5
	if fizz == 0 and buzz == 0:
		 print 'fizz buzz'
	elif fizz == 0:
		print 'fizz'
	elif buzz == 0:
		print 'buzz'
	else:
		print x