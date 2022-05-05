mock_db = []


def populate():
    file = open('Input.txt', 'r')
    for line in file:
        if line is None:
            pass
        nic_1, nic_2, contact_date = line.split(",")
        mock_db.append(nic_1, nic_2, contact_date)
        mock_db.append(nic_2, nic_1, contact_date)


if __name__ == '__main__':
    populate()
    print(mock_db)
