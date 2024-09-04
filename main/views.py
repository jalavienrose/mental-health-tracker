from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306219934',
        'name': 'Azzahra Salsabila',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)
