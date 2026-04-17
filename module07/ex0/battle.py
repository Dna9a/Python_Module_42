'''
Authorized: builtins, standard types, import typing, import abc
Let’s start our game with the creation of basic Creature cards. But, as you may know,
Creatures are classified into various families and can evolve. This exercise will focus on
the abstract factory design pattern. You will implement the following elements in the
ex0/ folder:
•A Creature abstract class that holds attributes for the name and the type of the
Creature, an abstract method attack and a concrete generic method describe
that will return a standard message using the name and the type of the Creature.
•The following concrete classes that inherit from Creature: Flameling, Pyrodon,
Aquabub, and Torragon. Their attack method will return an appropriate string
message (see example).
•A CreatureFactory abstract class that will allow you to create the base Crea-
ture and the evolved Creature for the same family, using the create_base and
create_evolved abstract methods.
•The concrete classes FlameFactory and AquaFactory, inheriting from CreatureFactory,
that will handle the creation of the base and evolved Creature for each family (re-
spectively Flameling and Pyrodon for FlameFactory, and Aquabub and Torragon
for AquaFactory).
•Your ex0 package cannot expose concrete Creature directly, it must only expose
factories.
The battle.py script, at the root of the repository, will test the ex0 package. The
following scenario will be implemented:

DataDeck Abstract Card Architecture
•Instantiate the Flameling and Aquabub factories.
•Use a single function that receives a factory object and verifies that it can create
the base and evolved Creature, and then each Creature can be described and can
attack.
•Another function that receives both factories and makes base Creature fight.
You can use different Creatures, but you must keep the involved
concepts (families and abstract factories).
Example:
$> python3 battle.py
Testing factory
Flameling is a Fire type Creature
Flameling uses Ember!
Pyrodon is a Fire/Flying type Creature
Pyrodon uses Flamethrower!
Testing factory
Aquabub is a Water type Creature
Aquabub uses Water Gun!
Torragon is a Water type Creature
Torragon uses Hydro Pump!
Testing battle
Flameling is a Fire type Creature
vs.
Aquabub is a Water type Creature
fight!
Flameling uses Ember!
Aquabub uses Water Gun!

'''
from abc import ABC, abstractmethod
from typing import Any

class Creature():
	