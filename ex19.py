def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "you have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"
#purple are the variable linkages

print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)


print "OR, we can use variables from script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)




def rocks_and_pebbles(rock_count, pebble_count):
	print "throw %d rocks!" % rock_count
	print "You have %d pebbles to eat!" % pebble_count
	print "have a pebble party and throw rocks!"
	print "get a stream to party in.\n"

	print "We are throwing rocks with variables:"
rock_count = 39
pebble_count = 2
rocks_and_pebbles(rock_count, pebble_count)
