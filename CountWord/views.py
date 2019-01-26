from django.http import HttpResponse
from django.shortcuts import render 
import operator 

def home(request):
    return render(request,'home.html',{'hi': 'this is me'})

def about(request):
    return render(request,'about.html')

def count(request):
    fulltext = request.GET['fulltext']
    lista = fulltext.split()

    lista = [elem.lower() for elem in lista]
    
    worddict = dict()
    for word in lista:
        if word in worddict:
            #Increase
            worddict[word] += 1
        else:
            #Add to the dictionary  
            worddict[word]=1
    a = sorted(worddict.items(), key=operator.itemgetter(1), reverse =True)
    return render(request,'count.html',{'hi': fulltext,'count':len(lista),'worddcit':a})


