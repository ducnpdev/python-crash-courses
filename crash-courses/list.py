bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles) 
print(bicycles[-1]) 

# ---
motorcycles = ['honda', 'yamaha', 'suzuki'] 
print(motorcycles)
popped_motorcycle = motorcycles.pop() 
print(motorcycles)
print(popped_motorcycle)

# ---
popped_motorcycl1e = motorcycles.pop(0) 
print(popped_motorcycl1e)


# --- sort
cars = ['bmw', 'audi', 'toyota', 'subaru'] 
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

# --
print(len(cars))
# --------
print("for loop:")
magicians = ['alice', 'david', 'carolina'] 
for magician in magicians:
    print(magician) 


# --------
print("for loop number:")
for value in range(1,5):
    print(value)

numbers = list(range(1,6))
print(numbers)

# ----
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))


# ----
squares = [value**2 for value in range(1,11)]
print(squares)
