# I have Created this file 
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')
    
def analyze(request):
    print(request)
    djtext = request.POST.get('text' , 'default')
    removepunc = request.POST.get('removepunc' , 'off')
    fullcaps = request.POST.get('fullcaps' , 'off')
    newlineremover = request.POST.get('newlineremover' , 'off')
    extraspace = request.POST.get('extraspace' , 'off')
    charcount = request.POST.get('charcount' , 'off')
    
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"/\,<>.?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations' , 'analyzed_text' : analyzed}
        djtext = analyzed
        # return render(request , 'analyze.html' , params)
    
    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed To UPPERCASE' , 'analyzed_text' : analyzed}
        # return render(request , 'analyze.html' , params)
        djtext = analyzed

    elif(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char !="\n":
                analyzed = analyzed + char
        params = {'purpose': 'Changed To New Line removed' , 'analyzed_text' : analyzed}
        # return render(request , 'analyze.html' , params)
        djtext = analyzed
    
    if(extraspace=="on"):
        analyzed = ""
        for index,char in enumerate(djtext):
            if not(djtext[index] ==" " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Extra Space removed' , 'analyzed_text' : analyzed}
        # return render(request , 'analyze.html' , params)
        djtext = analyzed

    if(charcount=="on"):
        text = 0
        for char in djtext:
            if( char != "null"):
                text = text + 1
        params = {'purpose': 'Counting character in given text' , 'analyzed_text' : text}


    # if(removepunc != "on" and newlineremover!="on" and extraspace !="on" and fullcaps !="on" and charcount !="on"):
    #     return HttpResponse("Please Select Any operation and try again")

    return render(request , 'analyze.html' , params)