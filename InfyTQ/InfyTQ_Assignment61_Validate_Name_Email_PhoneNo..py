def validate_name(name):
    if not name or len(name) > 15 or not name.isalpha():
        return False
    return True


def validate_phone_no(phno):
    if len(phno) != 10 or not phno.isdigit() or phno.count(phno[0]) == len(phno):
        return False
    return True


def validate_email_id(email_id):
    if '@' not in email_id or '.com' not in email_id or not email_id.endswith('.com') or email_id.count('@') > 1 or email_id.count('.') > 1:
        return False
    a = email_id.split('@')[1].split('.')[0]
    if a not in ['gmail', 'yahoo', 'hotmail']:
        return False

    return True


def validate_all(name, phone_no, email_id):
    if validate_name(name) and validate_email_id(email_id) and validate_phone_no(phone_no):
        print("All details are the Same.")
    else:
        if not validate_name(name):
            print("Invalid Name")

        elif not validate_email_id(email_id):
            print("Invaild Email Id")

        elif not validate_phone_no(phone_no):
            print("Invalid Phone Number")


validate_all("Prakhar", '8874109902', 'prakharkumar506978@gmail.com')
