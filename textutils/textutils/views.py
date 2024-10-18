# this is a file i've created
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # params = {'name':'surya','place':'Hyderabad'}
    return render(request,"index.html")

def analyze(request):
    djdetails = request.POST.get('details','default')
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremove = request.POST.get('newlineremove','off')
    extraspaceremove = request.POST.get('extraspaceremove','off')
    purpose = "Operations:"
    # Remove Punctuations from input text-------------------------
    if removepunc == "on":
        analyzed = ""
        purpose = purpose +"-"+ "Remove Punctuations"
        punctuations = '''!()-[]{;}:'"\,<>./?@#$%^&*_~'''
        for char in djdetails:
            if char not in punctuations:
                analyzed = analyzed+char
        params= {'purpose':purpose,'analyzed_text':analyzed}
        djdetails = analyzed
    # Capitalize Input text-----------------------------------------
    if fullcaps=="on":
        analyzed = ""
        purpose = purpose +"-"+ "Capitalize"
        for char in djdetails:
            analyzed = analyzed+ char.upper() 
        params= {'purpose':purpose,'analyzed_text':analyzed}
        djdetails = analyzed
    # New Line remover from input text------------------------------
    if newlineremove == "on":
        analyzed = ""
        purpose = purpose +"-"+ "New Line remover"
        for char in djdetails:
            if char!="\n" and char!="\r":
                analyzed = analyzed + char
        params= {'purpose':purpose,'analyzed_text':analyzed}
        djdetails = analyzed
    # Remove Extra spaces from input text----------------------------
    if extraspaceremove == "on":
        analyzed = ""
        purpose = purpose +"-"+ "Remove Extra spaces"
        for  index, char in enumerate(djdetails):
            if not(djdetails[index]==" " and djdetails[index+1]== " "):
                analyzed = analyzed + char
        params= {'purpose':purpose,'analyzed_text':analyzed}
        djdetails = analyzed
    # No checkbox is checked then return erroe----------------------------
    if removepunc!="on" and fullcaps!="on" and newlineremove!="on" and extraspaceremove!="on":
        return HttpResponse("ERROR")
    
    return render(request,'analyze.html',params)