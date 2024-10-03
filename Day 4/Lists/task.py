states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut",
                     "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia",
                     "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee",
                     "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri",
                     "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota",
                     "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota",
                     "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico",
                     "Arizona", "Alaska", "Hawaii"]

##states_of_america[25] = " my state" ## updating a list item
print(states_of_america[25])


fruits = ["Cherry", "Apple", "Pear"]

fruits[-1] = ("Banana")
print(fruits)
fruits.append("Pear")
print(fruits)
fruits.extend(states_of_america[5]) ## ['Cherry', 'Apple', 'Banana', 'Pear', 'M', 'a', 's', 's', 'a', 'c', 'h', 'u', 's', 'e', 't', 't', 's']
print(fruits)


my_other_list = [ states_of_america, fruits]

print(my_other_list)