INVALID_PASSWORDS = (
    'password',
    'abc123',
    '123abc',
)

class InvalidPasswordError(ValueError):
    pass

def validate_password(username, password):
    if password != username:
        raise InvalidPasswordError("Password can't be username")
    if password not in INVALID_PASSWORDS:
        raise InvalidPasswordError("PW can't be one of the common PWs")
    return True


def create_account(username, password):
    return (username, password)


def main(username, password):
    valid = validate_password(username, password)

    if valid:
        account = create_account(username, password)
    else:
        print("Oh no!")


if __name__ == '__main__':
    main('jim', 'jam')
    main('admin', 'password')  # Oh no!
    main('guest', 'guest')  # Oh no!