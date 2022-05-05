mock_db = []


def populate():
    file = open('Input.txt', 'r')
    for line in file:
        if line is None:
            pass
        nic_1, nic_2, contact_date = line.split(",")
        mock_db.append((nic_1, nic_2, contact_date))
        mock_db.append((nic_2, nic_1, contact_date))


def print_list(nic):
    for contact in mock_db:
        nic_1, nic_2, contact_date = contact
        if nic_1 == nic:
            print(nic_2)
            print_list_rec(nic_2, contact_date)


def print_list_rec(nic, contact_date):
    for contact in mock_db:
        nic_1, nic_2, contact_date = contact
        if nic_1 == nic:
            print(nic_2)
            print_list(nic_2)


if __name__ == '__main__':
    populate()
    # print(mock_db)
    c_person_nic, c_contact_date = str(input()).split(" ")
    print_list(c_person_nic)

