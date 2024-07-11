from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound , Http404, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def simple_view(request) :
      return HttpResponse("Simple View")

def first_app_home(request) :
      return render(request, 'first_app/example.html')  # connecting to template

# news view for multiple topics

articles = {
      'sports' : "all the sports related data/ html page",
      'finance' : "all the finance related data/ html page",
      'politics' : "all the politics related data/ html page"
}
# dynamically feeding content to view from a dictionary, backing the dynamic url path 
def news_view(request, topic):
      try :
            result = articles[topic]
            return HttpResponse(result)
      except :
             #return HttpResponseNotFound("<h1>The topic you are looking for doesnt exist</h1>")
             raise Http404('404 Generic Error')

# not a recommended way to redirect but a possible way  
# target is to convert first_app/0 -> first_app/sports
def news_page_view(request, num_page) :
      topic_list = list(articles.keys())  # articles.keys() will be of type <class 'dict_keys'> 
                                 # so we need to convert it to List
      topic = topic_list[num_page]

      # webpage = reverse('topic_page', args=['topic'])
      return HttpResponseRedirect(reverse('topic_page', args=['topic']))

# responsive based on user input
def add_view(request, num1, num2) :
      message = f'{num1} + {num2} = {num1+num2}'
      return HttpResponse(message)


