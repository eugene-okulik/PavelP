my_dict = {"my_tuple": (1, 2, 3, 4, 5), "my_list": ["a", "b", "c", "d", "f"],
           "dict_test": {"name": "Alice", "age": 30, "mail": "git_googl@gmail.com", "city": "London", "phone_number": 89997775544}, "my_set": {2, 3, "d", "f", False}}

print(my_dict["my_tuple"][-1])

my_dict["my_list"].append("text")
my_dict["my_list"].pop(1)
my_dict["dict_test"]["i_am_a_tuple"] = True
my_dict["my_set"].add(777)
my_dict["my_set"].remove("d")

print(my_dict)
