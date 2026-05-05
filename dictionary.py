country_code = {'India' : '0091',

'Australia' : '0025',

'Nepal' : '00977'}
# search dictionary for country code of India

print("Country code for India -")

print(country_code.get('India', 'Not Found'))


# search dictionary for country code of Japan

print("Country code for Japan -")

print(country_code.get('Japan', 'Not Found')) 
# Dictionary of students (id -> details)

# Dictionary of students (id -> details)
student_data = {
    "id1": {"name": "vibhav",  "class": "V", "subject_integration": "english, math, science"},
    "id2": {"name": "abeer", "class": "V", "subject_integration": "english, math, science"},
    "id3": {"name": "ojas",  "class": "V", "subject_integration": "english, math, science"},  # duplicate of id1
    "id4": {"name": "purpansh", "class": "V", "subject_integration": "english, math, science"},
}

result = {}
seen_keys = []  # using a list instead of set

for student_id, details in student_data.items():
    unique_key = (details["name"], details["class"], details["subject_integration"])

    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result[student_id] = details

# print output line by line
for k, v in result.items():
    print(k, ":", v)
