print("This is Dictionaries")

##################################################################################

# Simple Example to show use of single level dictionary

simple_mary = {
  "name": "Mary Jones",
  "age": 35,
  "occupation": "Python Developer, PyDev Inc."
}

# Prints: "Hi Mary Jones, I hear you're a Python Developer, PyDev Inc."
print(f'Hi {simple_mary["name"]}, I hear you\'re a {simple_mary["occupation"]}')

#################################################################################

# Complex Example to show use of multi level dictionary

complex_mary = {
  "name": {
    "first_name": "Mary",
    "middle_names": [
      "Donovan"
      ],
    "last_name": "Jones",
    },
  "age": 35,
  "occupation": {
    "job_title": "Python Developer",
    "business_name": "PyDev Inc."
    }
}

# Prints: "Hi Mary, I hear you art a Python Developer"
print(f'Hi {complex_mary["name"]["first_name"]}, I hear you art a {complex_mary["occupation"]["job_title"]}.')