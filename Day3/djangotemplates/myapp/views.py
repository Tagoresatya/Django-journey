from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "myapp/home.html")



def calculator(request):
    if request.method == "POST":

        name = request.POST['name']
        a = int(request.POST['a'])
        b = int(request.POST['b'])
        operation = request.POST['operation']
        c = 0
        if operation == "add":  
            c = a + b   
        elif operation == "sub":
            c = a - b
        elif operation == "mul":
            c = a * b 
        elif operation == "div":
            c = a / b
        context = {'name':name, 'a':a, 'b':b, 'c':c, 'operation':operation}
        return render(request, "myapp/calcresponse.html", context)
    return render(request, "myapp/calculator.html")


    # ..\venv\Scripts\Activate.ps1   