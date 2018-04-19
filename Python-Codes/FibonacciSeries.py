def getFib(position):
	if position == 0:
		return 0
	if position == 1:
		return 1
	first = 0
	second = 1
	third = first + second
	for i in range(2, position):
		first = second
		second = third
		third = first + second
	return third

def getFibRec(position):
	if position == 0 or position == 1:
		return position
	return getFibRec(position-1)+getFibRec(position-2)

if __name__ == '__main__':
	print getFibRec(6)

locations = {'North America': {'USA': ['Mountain View']}}
locations['North America']['USA'].append('Atlanta')
locations['Asia'] = {'India': ['Bangalore']}
locations['Asia']['China'] = ['Shanghai']
locations['Africa'] = {'Egypt': ['Cairo']}

print 1
usa_sorted = sorted(locations['North America']['USA'])
for city in usa_sorted:
    print city

print 2
asia_cities = []
for countries, cities in locations['Asia'].iteritems():
    city_country = cities[0] + " - " + countries 
    asia_cities.append(city_country)
asia_sorted = sorted(asia_cities)
for city in asia_sorted:
    print city