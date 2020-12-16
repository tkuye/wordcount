
from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(request):
    return render(request, 'home.html', {'hi':"This is me hehe"} )

def count(request):
    fulltext = request.GET['fulltext']
    fulllist = fulltext.split()
    worddic = {}
    for word in fulllist: 
        if word in worddic:
            worddic[word] += 1 
        else:
            worddic[word] = 1

    words = sorted(worddic.items(), key = operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'fulltext': fulltext, 'count':len(fulllist), 'worddictionary': words}) 

def about(request):
    return render(request, 'about.html')