from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404

from .serializers import PostSerializer
from .models import Post

posts = [
    {
        "name": "James",
        "department": "Law"
    },
    {
        "name": "Samuel",
        "department": "Computer"
    },
    {
        "name": "David",
        "department": "Agency"
    },
]

@api_view(http_method_names=["GET","POST"])
def homepage(request:Request):
    if request.method == "POST":
        data = request.data
        response = {
            "message": "Hello world!",
            "data": data
        }
        return Response(data=response, status=status.HTTP_200_OK)
    response = {
        "message": "Hello world!"
    }
    return Response(data=response, status=status.HTTP_200_OK)

@api_view(http_method_names=["GET","POST"])
def get_posts(request:Request):
    values = Post.objects.all()
    
    if request.method == "POST":
        data = request.data
        serializes = PostSerializer(data=data)
        if not serializes.is_valid():
            return Response(data={"error": "Bad request"}, status=status.HTTP_400_BAD_REQUEST)
        
        serializes.save()
        response = {
            "message": "Hello world!",
            "data": serializes.data
        }
        return Response(data=response, status=status.HTTP_200_OK)

    serializes = PostSerializer(instance=values, many = True)
    response = {
        "message": "Successful",
        "data": serializes.data
    }
    return Response(data=response, status = status.HTTP_200_OK)

@api_view(http_method_names=["GET"])
def get_single_post(request:Request, postId:int):

    try:
        info = get_object_or_404(Post, pk=postId)
        serializer = PostSerializer(instance=info)

        if info:
            return Response(data=serializer.data, status=status.HTTP_200_OK)
    except:
        return Response(data={"error": "Bad request"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(http_method_names=["PUT"])
def update_single_post(request:Request, postId:int):
    try:
        info = get_object_or_404(Post, pk=postId)
        serializer = PostSerializer(instance=info, data=request.data)

        if not serializer.is_valid():
            return Response(data={"error": "Bad Data format"}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer.save()
        response = {
            "message": "Successful",
            "data": serializer.data
        }
        return Response(data=response, status = status.HTTP_200_OK)
    except:
        return Response(data={"error": "Bad request"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(http_method_names=["DELETE"])
def delete_single_post(request:Request, postId:int):
    data = get_object_or_404(Post, pk=postId)
    data.delete()

    return Response(data={"message": "Successful"}, status = status.HTTP_204_NO_CONTENT)
