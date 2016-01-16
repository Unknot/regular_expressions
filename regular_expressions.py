import re

phone_number_regex = re.compile(r"(\d{3})-(\d{3}-\d{4})")
string_to_parse = "My number is 456-234-4666."
mo = phone_number_regex.search(string_to_parse)
print("Area code: " + mo.group(1))
print("Phone number: " + mo.group(2))
print("Full number: " + mo.group())
print(mo.groups())

new_regex = re.compile(r"Batman|Tina Frey")
string_to_parse_2 = "Batman and Tina Frey"
mo2 = new_regex.search(string_to_parse_2)
print(mo2.group())

bat_regex = re.compile(r"(Bat)(mobile|man|copter|bat)")
bat_string = "Batcopter is your Batman."
bat_mo = bat_regex.search(bat_string)
print(bat_mo.group())

batwoman_regex = re.compile(r"Bat(wo)?man")
batwoman_string = "Batman is into Batwoman, isn't he?"
batwoman_mo = batwoman_regex.search(batwoman_string)
print(batwoman_mo.group())
