user_prompt = "Enter a project: "
user_prompt2 = "Enter a language: "


todos = {}

while True:
    todo1 = input(user_prompt)
    todo2 = input(user_prompt2)
    todos.update({todo1: todo2.upper()})
    print("\nCurrent total of active projects:", len(todos), "\n")

    for project, language in todos.items():
        print(f"Project: {project.title()} - Language: {language} \n")