from django.shortcuts import render

# Create your views here.

def show_main(request):
    context = {
        "nama_aplikasi": "Tim Tarkam Shop",
        'name': 'Priyanggara Zuhaynanda Zavana',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)
