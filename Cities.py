cities = {
		  'cairo' : {'country' : 'Egypt', 'population' : '12m', 'fact' : 'capital'},
		  'giza' : {'country' : 'Egypt', 'population' : '6m', 'fact' : 'pyramids'},
		  'manshatdamlo' : {'country' : 'Egypt', 'population' : '1200', 'fact' : 'mycity'},

		 }

for city, city_info in cities.items() :
	print(city)
	print(f"{city_info['country']}\t{city_info['population']}\t{city_info['fact']}")