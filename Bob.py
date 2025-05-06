def response(hey_bob):
    speech = hey_bob.replace(" ", "").replace("\n", "").replace("\r", "").replace("\t", "")
    if speech == "":
        response = "Fine. Be that way!"
    elif speech.upper() == speech and speech[-1] == "?" and any(c.isalpha() for c in speech):
        response = "Calm down, I know what I'm doing!"
    elif speech[-1] == "?" :
        response = "Sure."
    elif speech.upper() == speech and any(c.isalpha() for c in speech):
        response = "Whoa, chill out!"
    else:
        response = "Whatever."
    print("bob:" + " " + hey_bob)
    return response




test_cases = [
    "WATCH OUT!",
    "Tom-ay-to, tom-aaaah-to.",
    "WHAT'S GOING ON?",
    "4?",
    "I HATE THE DENTIST",
    "\t\t\t\t\t\t\t\t\t\t",
    "\n\r \t",
    "This is a statement ending with whitespace      ",
    "Wait! Hang on. Are you going to be OK?"
]

print(response("WATCH OUT!"))