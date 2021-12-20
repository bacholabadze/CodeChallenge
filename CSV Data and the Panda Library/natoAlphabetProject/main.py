import pandas


nato_file = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_dict = {row.letter: row.code for (index, row) in nato_file.iterrows()}


student_dict = {
    "students": ['Angela', 'James', 'Lily'],
    "score": ['75', '87', '55']
}

student_data_frame = pandas.DataFrame(student_dict)


def pronounce_name(name):
    pronounced_list = []
    for char in name:
        pronounced_list.append(nato_dict[char.upper()])
    return pronounced_list


for (index, row) in student_data_frame.iterrows():
    nato_pronounced = pronounce_name(row.students)
    print(f"{row.students} = {nato_pronounced}")
