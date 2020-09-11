from django.http import HttpResponse
from django.shortcuts import render
import string

def index(request):
    return render(request, "index.html")

def analyze(request):
    Input = request.POST.get('text', 'Using Default Text as no input was detected.')
    Check = request.POST.get('removepunc', 'off')
    Caps = request.POST.get('ToCapital', 'off')
    NewLine = request.POST.get('RemoveNewLine', 'off')
    char = request.POST.get('CountChar', 'off')
    extraSpaces = request.POST.get('RemoveSpace', 'off')
    wordcount = request.POST.get('CountWords', 'off')
    punctuation = string.punctuation
    
    if(Check == 'on' and Caps == 'on' and NewLine == 'on'):
        Input = Input.upper()
        analyzed1 = ""
        analyzed = ""
        for char in Input:
            if char not in punctuation:
                analyzed1 = analyzed1 + char
        MyList = analyzed1.splitlines()
        for i in MyList:
            analyzed = analyzed + i
        params = {'purpose' : 'After Converting To Capital', 'analyzed_text': analyzed}

    elif(Check == 'on' and NewLine == 'on'):
        analyzed1 = ""
        analyzed = ""
        for char in Input:
            if char not in punctuation:
                analyzed1 = analyzed1 + char
        MyList = analyzed1.splitlines()
        for i in MyList:
            analyzed = analyzed + i
        params = {'purpose' : 'After Converting To Capital', 'analyzed_text': analyzed}

    elif(Check == 'on' and Caps == 'on'):
        Input = Input.upper()
        analyzed = ""
        for char in Input:
            if char not in punctuation:
                analyzed = analyzed + char
        params = {'purpose' : 'After Converting To Capital', 'analyzed_text': analyzed}
    
    elif (Check == 'on' and (len(Input) > 0)):
        analyzed = ""
        for char in Input:
            if char not in punctuation:
                analyzed = analyzed + char
        params = {'purpose' : 'After Removing Punctuations', 'analyzed_text': analyzed}

    elif Caps == 'on' and (len(Input) > 0):
        analyzed = ""
        analyzed = Input.upper()
        params = {'purpose' : 'After Converting To Capital', 'analyzed_text': analyzed}
    
    elif NewLine=="on" and (len(Input) > 0):
        analyzed=""
        MyList = Input.splitlines()
        for i in MyList:
            analyzed = analyzed + i
        params = {'purpose': 'After removing New Line', 'analyzed_text': analyzed}

    elif char == 'on' and (len(Input) > 0):
        analyzed = 0
        for char in Input:
            if char != " ":
                analyzed += 1
        params = {'purpose': 'After Counting Charecters No. of characters: ', 'analyzed_text': analyzed}        

    elif extraSpaces == 'on' and (len(Input) > 0):
        analyzed = ""
        for index, char in enumerate(Input):
            if not(Input[index] == " " and Input[index+1]==" "):
                analyzed = analyzed + char
                
        params = {'purpose': 'After Removing extra spaces: ', 'analyzed_text': analyzed}

    elif wordcount == 'on' and (len(Input) > 0):
        Input = Input + " "
        analyzed = 0
        for char in Input:
            if char == " ":
                analyzed = analyzed + 1
                
        params = {'purpose': 'After Counting words No. of words: ', 'analyzed_text': analyzed}
    
    else:
        return HttpResponse("Error")

    return render(request, "analyze.html", params)
