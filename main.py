with open("./Input/Names/invited_names.txt") as file:
    names = file.readlines()
    names = [name.strip() for name in names]

with open("./Input/Letters/starting_letter.txt") as file:
    letter = file.read()
    for name in names:
        new_letter = letter.replace("[name]", name)
        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as new_file:
            new_file.write(new_letter)
