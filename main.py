mock_db = []
to_quarantine = []


def populate():
    file = open('Input.txt', 'r')
    for line in file:
        if line is None:
            pass
        nic_1, nic_2, contact_date = line.split(",")
        mock_db.append((nic_1, nic_2, contact_date))
        mock_db.append((nic_2, nic_1, contact_date))


def sorted_dict():
    mock_db.sort(key=lambda x: x[2])


def create_list(nic):
    to_check = [nic]
    for contact in mock_db:
        nic_1, nic_2, contact_date = contact
        if nic_1 in to_check:
            to_check.append(nic_2)
            to_quarantine.append(nic_2)


def print_list():
    for infected_person_nic in set(sorted(to_quarantine)):
        print(infected_person_nic)


if __name__ == '__main__':
    populate()
    sorted_dict()
    # print(mock_db)
    c_person_nic, c_contact_date = str(input()).split(" ")
    create_list(c_person_nic)
    print_list()
