#!/usr/bin/env python3

# T-strings, or template strings, are a new feature in Python 3.14 that allow for safer and more flexible string processing compared to f-strings.
# They provisde a way to access and manipulate interpolated values before combining them into a final string,
# reducing the risk of security vulnerabilities like SQL injection and cross-site scripting.

from string import Template

# Define some car data
car1 = {'make': 'Suzuki', 'model': 'Swift Sport', 'year': 2018, 'color': 'White Pearl'}
car2 = {'make': 'Toyota', 'model': 'GR Yaris', 'year': 2020, 'color': 'Blue'}
car3 = {'make': 'Ford', 'model': 'Mustang', 'year': 1967, 'color': 'Red'}

# Create a template string
car_template = Template("The ${color} ${year} ${make} ${model} is a fantastic car!")

# Use the template to generate descriptions for each car
print(car_template.substitute(car1))
# result: The White Pearl 2018 Suzuki Swift Sport is a fantastic car!

print(car_template.substitute(car2))
# result: The Blue 2020 Toyota GR Yaris is a fantastic car!

print(car_template.substitute(car3))
# result: The Red 1967 Ford Mustang is a fantastic car!

# You can also use safe_substitute if some placeholders might be missing
another_template = Template("Make: $make, Model: $model")
print(another_template.safe_substitute(make='Opel'))  # Model will be left as $model
# return: Make: Opel, Model: $model
