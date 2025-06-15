def gojo():
    print("Gojo: Yo! I’m Gojo Satoru. Type 'bye' to end our chat.")

    responses = {
        "hello": "Gojo: Hey hey! Nice to meet ya~",
        "hi": "Gojo: What’s up? ",
        "how are you": "Gojo: I'm limitless, as always.",
        "your name": "Gojo: I’m the honored one... Gojo Satoru.",
        "what can you do": "Gojo: I can crush curses and still look good doing it.",
        "who are you": "Gojo: Just the strongest, duh.",
        "joke": "Gojo: Why don't curses play hide and seek? Because I'd sense them instantly!",
    }
    while True:
        user=input("you:").lower().strip()
        if user == "bye":
            print("gojo: alritgt see you soon")
            break
        found = False
        for key in responses:
            if key in user:
                print(responses[key])   
                found=True
                break
        if not found:
            print("gojo : huh? hmmm see ya soon")

gojo()