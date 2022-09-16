import requests

response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method":"DELETE"})
print(response.text)