import alchemy

create_air = alchemy.create_air()


print("=== Alembic 4 ===")
print("Accessing the alchemy module using 'import alchemy'")
print(f"Testing create_air: {create_air}")
print("Now show that not all functions can be reached")
print("This will raise an exception!")
try:
    print(f"Testing the hidden"
          f" create_earth: {alchemy.create_earth()}")  # type: ignore
except AttributeError as f:
    print(f"Testing the hidden create_earth: {f}\n")
