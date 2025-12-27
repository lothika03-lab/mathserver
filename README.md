# Ex.04 Design a Website for Server Side Processing
# Date:28.11.2025
# AIM:
To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side.

# FORMULA:
P = I2R
P --> Power (in watts)
 I --> Intensity
 R --> Resistance

# DESIGN STEPS:
## Step 1:
Clone the repository from GitHub.

## Step 2:
Create Django Admin project.

## Step 3:
Create a New App under the Django Admin project.

## Step 4:
Create python programs for views and urls to perform server side processing.

## Step 5:
Create a HTML file to implement form based input and output.

## Step 6:
Publish the website in the given URL.

# PROGRAM :
```
urls.py
from django.contrib import admin
from django.urls import path
from exp5app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Power,name='Power'),
]

views.py
from django.shortcuts import render
def Power(request):
    Power=''
    if request.method=="POST":
        Intensity = float(request.POST.get("Intensity"))
        Resistance = float(request.POST.get("Resistance"))
        Power=Intensity**2*Resistance
        print(f"Intensity:{Intensity},Resistance:{Resistance},Power:{Power:.2f}")
    return render(request, 'Power.html',{'Power':Power})

Power.html
<html>
    <head>
        <title>power</title>
    </head>
    <style>
        .bg img{
            position: absolute;
            width: 100%;
            height: 100%;
        }
        .box{
            position: absolute;
            text-align: center;
            height:100%;
            width: 100%;
            top:25%;
            font-size: 32px;
            color: white;
        }
        button{
            font-size:24px ;
            padding:5px;
            background-color: rgb(159, 213, 255);
        }
        button:hover{
            background-color: yellowgreen;
        }
    </style>
    <body>
        <form method ="POST">
            {% csrf_token %}
            <div class="bg">
                <img src="../static/bgimg.png">
            </div>
            <div class="box">
                <h3>Power</h3>
            <label>Intensity:
                <input type="number" name="Intensity"><br><br>
            </label>
            <label>Resistance:
                <input type="number" name="Resistance"><br><br>
            </label>
            <button type="submit">Calculate</button><br><br>
            <label>Power:
            </label>
            <input type="number" value={{Power}}><br><br>
            </div>
        </form>
    </body>
</html>
```
# SERVER SIDE PROCESSING:
<img width="1164" height="418" alt="Screenshot 2025-12-26 114011" src="https://github.com/user-attachments/assets/ffda73f7-e656-454b-b4d5-4c6b563ec6e4" />

# HOMEPAGE:
<img width="1920" height="1080" alt="Screenshot (74)" src="https://github.com/user-attachments/assets/632532af-b8a1-4ba1-a699-c0236e3d70bb" />

# RESULT:
The program for performing server side processing is completed successfully.
