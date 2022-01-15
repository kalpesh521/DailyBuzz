 
from django.shortcuts import render
import  requests
API_KEY='ba7d2ddaf555402fa18d2dadfa7015ab'
# Create your views here.
def  home(request):
    url= f'https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}'
    response=requests.get(url)
    data=response.json()
    articles = data['articles']
    
    context = {
        'articles' : articles
    }

    return render(request, 'home.html', context)
# def home(request):
#     country = request.GET.get('country')
#     category = request.GET.get('category')

#     if country:
#         url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
#         response = requests.get(url)
#         data = response.json()
#         articles = data['articles']
#     else:
#         url = f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}'
#         response = requests.get(url)
#         data = response.json()
#         articles = data['articles']



#     context = {
#         'articles' : articles
#     }

#     return render(request, 'news_api/home.html', context)
 