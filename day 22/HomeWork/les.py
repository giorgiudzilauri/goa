#homework 1
list_of_name = ["spidarman", "saba", "gojo", "andria"]

name_to_count = "spidarman"
count = list_of_name.count(name_to_count)

print(f"name'{name_to_count}' list {count}-ჯერ გვხვდება")

#homework 2 
list_of_numbers = [1, 2, 3, 4, 5]
list_of_numbers.reverse()
print("updated list:", list_of_numbers)
reversed 

#homework 3
list_of_numbers = [1, 2, 3]
repeated_list = list_of_numbers * len(list_of_numbers)
print("Repeated list elements:", repeated_list)

#homework 4
insert_arr = ["Python", "Java", "C++"]
insert_arr.insert(1, "goku")
print("Updated list:", insert_arr)


#homework 5
list_of_numbers = [1, 2, 3, 1, 4, 1]
element_to_count = 1
count = list_of_numbers.count(element_to_count)
list_of_numbers.remove(element_to_count)
print(f"elements '{element_to_count}' in the list {count}-can be found first.")
print("Updated list:", list_of_numbers)