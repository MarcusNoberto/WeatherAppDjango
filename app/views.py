from django.shortcuts import render, redirect
from .api_key import key
import requests
import math
def home(request):
    return render(request, "home.html")

def search(request):
    if request.method == "POST":
        city_name = request.POST["city"].lower()
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={key}"
        data = requests.get(url).json()
        try:
            context = {
                ####
                "city_name":data["city"]["name"],
                "city_country":data["city"]["country"],
                "wind":data['list'][0]['wind']['speed'],
                "degree":data['list'][0]['wind']['deg'],
                "status":data['list'][0]['weather'][0]['description'],
                "cloud":data['list'][0]['clouds']['all'],
                'date':data['list'][0]["dt_txt"],
                'date1':data['list'][1]["dt_txt"],
                'date2':data['list'][2]["dt_txt"],
                'date3':data['list'][3]["dt_txt"],
                'date4':data['list'][4]["dt_txt"],
                'date5':data['list'][5]["dt_txt"],
                'date6':data['list'][6]["dt_txt"],


                "temp": round(data["list"][0]["main"]["temp"] -273.0),
                "temp_min1":math.floor(data["list"][1]["main"]["temp_min"] -273.0),
                "temp_max1": math.ceil(data["list"][1]["main"]["temp_max"] -273.0),
                "temp_min2":math.floor(data["list"][2]["main"]["temp_min"] -273.0),
                "temp_max2": math.ceil(data["list"][2]["main"]["temp_max"] -273.0),
                "temp_min3":math.floor(data["list"][3]["main"]["temp_min"] -273.0),
                "temp_max3": math.ceil(data["list"][3]["main"]["temp_max"] -273.0),
                "temp_min4":math.floor(data["list"][4]["main"]["temp_min"] -273.0),
                "temp_max4": math.ceil(data["list"][4]["main"]["temp_max"] -273.0),
                "temp_min5":math.floor(data["list"][5]["main"]["temp_min"] -273.0),
                "temp_max5": math.ceil(data["list"][5]["main"]["temp_max"] -273.0),
                "temp_min6":math.floor(data["list"][6]["main"]["temp_min"] -273.0),
                "temp_max6": math.ceil(data["list"][6]["main"]["temp_max"] -273.0),


                "pressure":data["list"][0]["main"]["pressure"],
                "humidity":data["list"][0]["main"]["humidity"],
                "sea_level":data["list"][0]["main"]["sea_level"],


                "weather":data["list"][1]["weather"][0]["main"],
                "description":data["list"][1]["weather"][0]["description"],
                "icon":data["list"][0]["weather"][0]["icon"],
                "icon1":data["list"][1]["weather"][0]["icon"],
                "icon2":data["list"][2]["weather"][0]["icon"],
                "icon3":data["list"][3]["weather"][0]["icon"],
                "icon4":data["list"][4]["weather"][0]["icon"],
                "icon5":data["list"][5]["weather"][0]["icon"],
                "icon6":data["list"][6]["weather"][0]["icon"],

            }
        except:
            context = {

            "city_name":"Not Found, Check your spelling..."
        }

        return render(request, 'search.html', context)
    else:
        return redirect('home')






