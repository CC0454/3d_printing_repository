def say_hello():
    return "Hello!"
  
def say_goodbye():
	return "goodbye"

  #Store a function "say_hello" in a list
greetings = [say_hello, say_goodbye]

#Call the first function in the list
print(greetings[0]())
print(greetings[1]())