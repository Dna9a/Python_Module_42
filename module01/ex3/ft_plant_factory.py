#!/Users/yoabied/.pyenv/versions/3.11.9/bin/python

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")






'''
Requirements:
• Plants need to be created directly with their initial information (name, starting height, starting age)
• Each plant should be ready to use immediately after construction (e.g., if you want to make it grow())
• Create at least 5 different plants with varying characteristics
• Display all created plants in an organized format

=== Plant Factory Output ===
Created: Rose: 25.0cm, 30 days old
Created: Oak: 200.0cm, 365 days old
Created: Cactus: 5.0cm, 90 days old
Created: Sunflower: 80.0cm, 45 days old
Created: Fern: 15.0cm, 120 days old
'''
