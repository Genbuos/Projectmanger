project = 'What is the project?'

language = 'What is the language?'

#this is how you comment in py!

#input() is a function built in to python.
"""
this is a multiline comment.

:input() is used to take in input from the console. or "user"


im gonna use this to build a to do app to help me 
manage any projects that i may be working on !

"""
todo1P = input(project)
todo1L = input(language)
todo2P = input(project)
todo2L = input(language)
todo3P = input(project)
todo3L = input(language)



todos = {todo1P:todo1L, todo2P:todo2L, todo3P:todo3L}
print("these are the current projects that i am working on:", todos,"\n",
      "there are: ", todos.__len__(), " projects")

print("Data structure im using to store the user input",type(todos))