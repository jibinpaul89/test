'''
from django.shortcuts import render
from .models import Snippet
from django.http import HttpResponse
# Create your views here.


def getsnippets(request):
    queryset = Snippet.objects.all()
    response = HttpResponse(queryset)
    return response
'''

# import viewsets
from rest_framework import viewsets
# import local data
from .serializers import SnippetSerializer
from .models import Snippet

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse



def query_view(request):
    # Query the ORM to get the books
    print('dddddddddddddddddddddddd')
    books = Snippet.objects.all()

    # Serialize the books
    serialized_books = [{
        'id': book.id,
        'title': book.title,
        'author': book.author,
    } for book in books]
    print(serialized_books)
    #return Response(serialized_books)
    return JsonResponse({'results': serialized_books})