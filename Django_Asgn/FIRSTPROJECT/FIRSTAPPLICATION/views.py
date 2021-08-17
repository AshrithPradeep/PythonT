from django.shortcuts import render
from django.http import HttpResponse
from FIRSTAPPLICATION.models import Candidate

def hi(request):
    return render(request, "first.html")

def candidate_info(request):
    candidates = Candidate.objects.order_by('name')
    dict = {'details':candidates}
    return render(request,'second.html',context=dict)

