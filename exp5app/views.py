from django.shortcuts import render
def Power(request):
    Power=''
    if request.method=="POST":
        Intensity = float(request.POST.get("Intensity"))
        Resistance = float(request.POST.get("Resistance"))
        Power=Intensity**2*Resistance
        print(f"Intensity:{Intensity},Resistance:{Resistance},Power:{Power:.2f}")
    return render(request, 'Power.html',{'Power':Power})