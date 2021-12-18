PLACEHOLDER = '[name]'

with open("./input/names/invited_names.txt", mode='r') as names_file:
    names = names_file.readlines()

with open("./input/letters/starting_letter.docx", mode='r') as letter_file:
    letter = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter.replace(PLACEHOLDER, stripped_name)
        with open(f"output/readyToSend/letter_for_{stripped_name}.docx", mode='w') as completed_letter:
            completed_letter.write(new_letter)
