SOME_CONSTANT = "some string"


def fake_input(message):
    response = {"First Name: ": "Adam", "Surname ": "Carruthers"}[message]
    print(message + response)
    return response
