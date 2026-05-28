import requests
key="key"
city=input("Enter the City")
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric"
ans=requests.get(url)
data=ans.json()
print(data)
#print("Weather:", data["weather"][0]["description"])