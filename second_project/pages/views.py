from django.shortcuts import render
from .models import Person
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import PersonSerializer

def index(request):
    person = Person.objects.all()
    
    context = {
        "person": person
    }
    
    return render(request,"index.html",context)

def data_tables(request):
    return render(request,"data_tables.html")

@api_view(["GET"])
def data_tables_api(request):
    person = Person.objects.all()
    serializer = PersonSerializer(person, many=True)
    
    return Response(serializer.data)

def server_side_search(request):
    return render(request,"server_side_search.html")

@api_view(["POST","GET"])
def server_side_search_api(request):
    if request.method == "POST":
        received_data = request.data.get('search')
        
        searched_data = Person.objects.filter(name__contains = received_data)
        
        serializer = PersonSerializer(searched_data,many=True)

        return Response(serializer.data)