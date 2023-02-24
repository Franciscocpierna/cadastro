from cadastro.core.user_core import get_user

def test_check_type_to_dict():

    user = get_user()

    assert dict == type(user)

def test_check_type_name():

    user = get_user()

    assert str == type(user.get("name"))

def test_check_name():

    user = get_user()

    assert "Sara Isabela Jennifer Porto" == user.get("name")
