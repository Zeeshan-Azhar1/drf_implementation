from django.shortcuts import render
from .models import Comment
from .models import CommentModelSerailzer
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view 

@api_view(['GET', 'POST'])
# @csrf_exempt
def comments_list(request):
    if request.method == 'GET':
        comments = Comment.objects.all()
        serialized_comments = CommentModelSerailzer(comments, many = True)
        return Response(serialized_comments.data)
    elif request.method == 'POST':
        # data = JSONParser().parse(request)
        deserialized_data = CommentModelSerailzer(data = request.data)
        if deserialized_data.is_valid():
            deserialized_data.save()
            return Response(deserialized_data.data, status.HTTP_201_CREATED)
        return Response(deserialized_data.errors, status.HTTP_400_BAD_REQUEST) 

@api_view(['GET', 'PUT', 'DELETE' ])
# @csrf_exempt
def create_comment(request, id):
    comment = Comment.objects.get(id = id)
    if request.method == 'GET':
        serialized_comment = CommentModelSerailzer(comment)
        # print(serialized_comment.initial_data)
        print(serialized_comment.data)
        return Response(serialized_comment.data)
    elif request.method == 'PUT':
        # data = JSONParser().parse(request)
        deserialized_data = CommentModelSerailzer(comment , data = request.data)
        if deserialized_data.is_valid():
            deserialized_data.save()
            return Response(deserialized_data.data, status = 201)
        return Response(deserialized_data.errors, status = 400)
    elif request.method == 'DELETE':
        print(comment.title)
        comment.delete()
        return Response(status.HTTP_204_NO_CONTENT)
            
    




        
        
