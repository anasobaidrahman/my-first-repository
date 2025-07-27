import operator

from django.shortcuts import HttpResponse
from django.shortcuts import render
def analyze(request):
    return render(request,'Artical_analyzer.html')
def analyzed(request):
    article_a= request.POST['article']
    article = article_a.split(' ')
    word_dict= {}
    for word in article:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word]=1
    sort_dict = sorted(word_dict.items(),key=operator.itemgetter(1), reverse=True)
    word_cnt=len(article)

    return render(request,'2nd_analyzer.html',{'analyzed_dict':sort_dict,'word_cnt':word_cnt})

