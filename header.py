import requests

def test_header():
    response = requests.get('https://playground.learnqa.ru/api/homework_header')

    print(response.headers)

    assert (header := response.headers.get('x-secret-homework-header')) == 'Some secret value', f"Header 'x-secret-homework-header' must be 'Some secret value', but {header}"

