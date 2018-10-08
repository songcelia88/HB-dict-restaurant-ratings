"""Restaurant rating lister."""


# put your code here
import sys, random

ratings={}

def set_ratings(filename):
	'''
	Set the ratings of a restaurant
	'''
	with open(filename) as file:
		for line in file:
			rating=line.strip().split(":")
			ratings[rating[0]]=rating[1]

def get_ratings():
	'''
	Print a list of rated restaurants and their ratings in alphabetical order
	'''
	
	sorted_restaurants = sorted(ratings.items())
	for restaurant, rating in sorted_restaurants:
		print(restaurant, "is rated at", rating)


def validate_rating():
	while True:
		try:
			new_rating = int(input("On the scale of 1-5, what would you rate it?\n"))
			while new_rating < 1 or new_rating > 5:
				print ("follow the rules, try again")
				new_rating = int(input("On the scale of 1-5, what would you rate it?\n"))

			break
		except ValueError:
			print("Invalid entry, please use 1-5")
	return new_rating	

def add_new_rating():
	'''
	Allow the user to add a new restaurant and rate it
	'''
	new_restaurant_name = input("What restaurant do you want to add\n").title()
	
	new_rating = validate_rating()

	ratings[new_restaurant_name] = new_rating
	print("Added {} with a score of {}".format(new_restaurant_name, ratings[new_restaurant_name]))

def update_rating(restaurant = ""):

	#if no restaurante is specified, choose a random restaurant to update
	if restaurant == "":
		restaurant = random.choice(list(ratings.keys()))
		print("{} was chosen. It has a rating of {}".format(restaurant, ratings[restaurant]))

	new_rating = validate_rating()
	ratings[restaurant] = new_rating

	

set_ratings(sys.argv[1])

user_choice = 0
while True:
	try:
		user_choice = int(input("\nWhat do you want to do? \n 1. View Ratings \n 2. Add a new restaurant \n 3. Quit \n (please enter a number 1-3.) \n\n"))
		
		
		if user_choice == 1:
			get_ratings()
		
		elif  user_choice==2:
			add_new_rating()
		
		elif user_choice ==3:
			print ("BYE!")
			break
		
		else:
			print ("invalid selection try again")

	

	except ValueError:
		print("\nINVALID ENTRY: Please enter a 1. 2. or 3.")


