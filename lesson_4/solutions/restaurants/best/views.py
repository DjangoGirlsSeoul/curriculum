from django.shortcuts import render

def list(request):
    restaurants = [{
                    "name": "mcdonalds", 
                    "price": "$", 
                    "review": "its ok"
                   }, 
                   {
                    "name": "burger king", 
                    "price": "$$", 
                    "review": "flame grilled burgers!"
                   }]
    return render(request, 'best/index.html', {"restaurants": restaurants})
