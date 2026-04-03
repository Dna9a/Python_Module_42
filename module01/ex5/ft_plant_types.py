

'''

Authorized: super(), print(), range(), round()

The garden now needs to handle different types of plants: flowers, trees, and vegetables.
Each type has unique characteristics but inherits common plant features from its parent
category.
Requirements:
• Start with your Plant class from the previous exercise, which holds the common
features (name, height, and age)
• Create specialized types: Flower, Tree, and Vegetable
• Each specialized type should inherit the basic plant features
• Flower needs: a color attribute and ability to bloom()
• Tree needs: a trunk_diameter attribute and the ability to produce_shade()
• Vegetable needs: a harvest_season and a nutritional_value attributes
• When creating specialized plants, call the parent methods from inside your new
class using super(). It can be applied to any method, including __init__()
• A call to show() on a specialized class needs to print the standard Plant output
and the extra characteristics of your specialized plant. Your method override can
re-use the already existing code in the parent.
• Create at least one instance of each plant type; make the flower bloom; make the
nutritional value start from 0, then increase when the vegetable’s age() and grow()
methods are called.
Avoid duplicating common plant code across different specialized types.
• No need to validate the new attributes in the three new classes


Example:
$> python3 ft_plant_types.py
=== Garden Plant Types ===
=== Flower
Rose: 15.0cm, 10 days old
Color: red
Rose has not bloomed yet
[asking the rose to bloom]
Rose: 15.0cm, 10 days old
Color: red
Rose is blooming beautifully!
=== Tree
Oak: 200.0cm, 365 days old
Trunk diameter: 5.0cm
[asking the oak to produce shade]
Tree Oak now produces a shade of 200.0cm long and 5.0cm wide.
=== Vegetable
Tomato: 5.0cm, 10 days old
Harvest season: April
Nutritional value: 0
[make tomato grow and age for 20 days]
Tomato: 47.0cm, 30 days old
Harvest season: April
Nutritional value: 20

How are you handling the common features shared by all plant types?
It is advised to avoid repeating the same code in the different
classes to handle these common features.

'''