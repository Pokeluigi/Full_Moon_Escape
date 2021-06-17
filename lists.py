#coffee_order = [
#    "Alex - Cortado",
#    "Ben - Latte",
#    "Charlie - Whatever's new"
#]

#print(coffee_order)

#bad_trip_ideas = [
#    "Toga party in Marie Byrd Land",
#    "Wearing a pride flag cape to the westboro baptist church",
#    "France",
#]
#it is possible to change individual parts of the list for new parts
#bad_trip_ideas[1] = "baby shower in the pacific ocean"
#print(bad_trip_ideas)
#
#print(len(bad_trip_ideas))

#fav_websites = [
#    "twitter.com",
#    "onion.com",
#    "awebsite.com"
#]

#print(fav_websites)

#fav_websites.append("somewebsite.com")
#fav_websites.append("anotherwebsite.com")

#print(fav_websites)

list=[
    "Anteater",
    "Bear",
    "Dog",
    "Dog",
    "Dog",
    "Giraffe",
    "Tanuki",
    "Zebra",
]

#More methods include:
#The index() method whjch returns the index of the specified value in the list.
#syntax for index(): list.index(element, start, end)
#example below:
#print(list.index("Dog"))

#The extend() method adds all the elements of an iterable (list, tuple, string etc.) to the end of the list.
#syntax for extend(): list1.extend(iterable)
#example below:
#list1=[
#    "Cat",
#    "Hippopotamus",
#    "Rhino",
#    "Tapir",
#]
#print(list)
#print(list1)
#list.extend(list1)
#print(list)

#The list insert() method inserts an element to the list at the specified index.
#syntax for insert(): list.insert(i, elem)
#example below:
#list.insert(3, "Pig")
#print(list)

#The remove() method removes the first matching element (which is passed as an argument) from the list.
#syntax for remove(): list.remove(element)
#example below:
#print(list)
#list.remove("Dog")
#print(list)

#The count() method returns the number of times the specified element appears in the list. Must either print immediately or store in a variable
#syntax for count(): list.count(element)
#example below()
#print(list.count("Dog"))
#good_boys=list.count("Dog")

#The pop() method removes the item at the given index from the list and returns the removed item.
#syntax for pop(): list.pop(index) (if no index given will simply remove the last value of the list)
#print(list.pop())
#print(list.pop(2))

#The reverse() method reverses the elements of the list.
#syntax for reverse(): list.reverse()
#example below:
#list.reverse()
#print(list)

#The sort() method sorts the elements of a given list in a specific ascending or descending order.
#syntax for sort(): list.sort(key=..., reverse=...) alternatively sorted(list, key=..., reverse=...)
#sort changes the list and doesn't return a value while sorted doesn't change the list and returns the sorted list
#example below:
#list.sort(reverse=True)
#print(list)
#another example:
#list.sort(key=len)
#print(list)

#The copy() method returns a shallow copy of the list.
#syntax for copy(): new_list = list.copy()
#new_list = list.copy()
#new_list.append("Humans")
#print(list)
#print(new_list)

#The clear() method removes all items from the list.
#syntax for clear(): list.clear()
#print(list)
#list.clear()
#print("Clearing list")
#print(list)