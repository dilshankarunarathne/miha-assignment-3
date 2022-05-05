# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
people = {}


class Person:
    contacts = {}

    def __init__(self, person_one_nic):
        self.nic = person_one_nic


def populate():
    file = open('Input.txt', 'r')
    for line in file:
        if line is None:
            pass
        (first_person_nic, second_person_nic, contact_date) = line.split(",")
        # print(first_person_nic, " touched ", contacted_person_nic, " on ", contact_date)
        if first_person_nic not in people:
            print(first_person_nic, " was not found in the list")
            new_person = Person(first_person_nic)
            new_person.contacts[second_person_nic] = contact_date
            people[first_person_nic] = new_person
        else:
            people[first_person_nic].contacts[second_person_nic] = contact_date
        if second_person_nic not in people:
            print(second_person_nic, " was not found in the list")
            new_person = Person(second_person_nic)
            new_person.contacts[first_person_nic] = contact_date
            people[second_person_nic] = new_person
        else:
            people[second_person_nic].contacts[first_person_nic] = contact_date


def check_for(nic):
    if nic in people:
        for contact in people[nic].contacts:
            print(contact)


def print_all_contacts():
    for p in people:
        for c in p:
            print(people[p].nic, " <-> ", c)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    populate()
    # (person_nic, contact_dd) = str(input()).split(" ")
    # check_for(person_nic)
    print_all_contacts()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
