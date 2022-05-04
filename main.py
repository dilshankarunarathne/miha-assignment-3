# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
people = []


class Person:
    contacts = {}

    def __init__(self, person_nic):
        self.nic = person_nic


def parse_input_file():
    file = open('Input.txt', 'r')
    for line in file:
        (first_person_nic, contacted_person_nic, contact_date) = line.split(",")
        new_person = Person(first_person_nic)
        new_person.contacts[contacted_person_nic] = contact_date
        people.append(new_person)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parse_input_file()
    print(people)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
