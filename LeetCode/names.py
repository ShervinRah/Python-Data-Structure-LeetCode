print("Hello Airbnb!")
name = "Camila"
age = 23
gender = "female"
school = "UCLA Graduate"
hobbies = ["playing tennis", "helping marginalized communities", "swimming", "taking walks to the beach"]
rank_hobbies = {}

print("My name is", name, "and I am", age ,"years old.")
print("I am a first generation", gender, school)

for i in range(len(hobbies)):
    rank_hobbies[hobbies[i]] = i + 1

print("My hobbies preferences by rank!")
print(rank_hobbies)

