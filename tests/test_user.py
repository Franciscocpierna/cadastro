from cadastro.user import get_user

def test_check_type_to_dict():

    user = get_user()

    assert type(user) == dict

def test_check_name():

    user = get_user()

    assert user.get("name") == "Sara Isabela Jennifer Porto"




