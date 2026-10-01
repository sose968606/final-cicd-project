from app import add_numbers, get_message
def test_add_numbers():
    assert add_numbers(2, 3) == 5
def test_get_message():
    assert get_message() == "CI/CD pipeline is running"
