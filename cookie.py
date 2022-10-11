import requests

def test_cookie():
    response = requests.get('https://playground.learnqa.ru/api/homework_cookie')

    print(response.cookies)

    assert (cookie := response.cookies.get('HomeWork')) == 'hw_value', f"Cookie 'HomeWork' must be 'hw_value', but {cookie}"

