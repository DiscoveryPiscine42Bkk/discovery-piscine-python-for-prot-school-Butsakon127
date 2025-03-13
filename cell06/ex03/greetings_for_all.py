def greetings(name="noble stranger"):
    if not isinstance(name, str):
        print("Error: Name must be a string.")
    else:
        print(f"Welcome, {name}!")
greetings()
greetings("ดาบ เจ็ด สี มณี เจ็ด แสง")
greetings(123)
