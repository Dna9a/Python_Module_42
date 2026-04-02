def get_plant_info():
	name = "Rose"
	height = "25cm"
	age = "30 days"
	return name, height, age

if __name__ == "__main__":
	print("=== Welcome to My Garden ===")
	name, height, age = get_plant_info()
	print(f"Name: {name}")
	print(f"Height: {height}")
	print(f"Age: {age}")
	print()
	print("=== End of Program ===")
