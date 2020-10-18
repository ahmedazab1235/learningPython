FavoriteNumbers = {
					'ahmed' : ['1', '2', '3'],
				    'lol' : ['13', '24', '35'], 
				    'essam' : ['18', '27', '36'], 
				    'azab' : ['16', '24', '33'],
				    }

for name, fns in FavoriteNumbers.items() :
	print(name)
	for fn in fns :
		print(fn)
