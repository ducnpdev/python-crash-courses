def greet_user():
    """Display a simple greeting."""
    print("Hello!")
greet_user()

# ---
def greet_user(username):
    """Display a simple greeting."""
    print("Hello, " + username.title() + "!")
greet_user('jesse')

# ---
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')

# ---
print("\n")
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(pet_name='willie')


# A dog named Willie.
print("----------")
describe_pet('willie')
describe_pet(pet_name='willie')
# A hamster named Harry.
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')

print("-----return value-----")
def get_formatted_name(first_name, middle_name, last_name):
       """Return a full name, neatly formatted."""
       full_name = first_name + ' ' + middle_name + ' ' + last_name
       return full_name.title()
musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)