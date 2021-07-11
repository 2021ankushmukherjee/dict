
dict = {
         "pakha" : "Fan , https://en.wikipedia.org/wiki/Fan_(machine) " ,
         "bakso" : "Box , https://en.wikipedia.org/wiki/The_Box " ,
         "alo" : "Light , https://en.wikipedia.org/wiki/Light " ,
         "ratri" : "Night , https://en.wikipedia.org/wiki/Night " ,
         "sokal" : "Morning , https://en.wikipedia.org/wiki/Morning " ,
}
print("Available words:", dict.keys())
print("This is case sensitive")
a=input("enter the bengali word\n")
print("The meaning of your word is:", dict.get(a))
