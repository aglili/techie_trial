from rest_framework.decorators import api_view
from .serializer import BlogSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .models import Blog

# Create your views here.

@api_view(["POST"])
def createBlog(request):
    try:
        if not request.user.is_authenticated:
            return Response({"error": "Invalid Login Credentials"}) 
        data = request.data
        data['author'] = request.user.id
        serializer = BlogSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data, 'message': "Blog Post Created"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response(str(e), status=status.HTTP_401_UNAUTHORIZED)
    

@api_view(["GET"])
def getUserBlog(request):
    try:
        if not request.user.is_authenticated:
            return Response({"error": "Invalid Login Credentials"}) 
        print(request.data)
        blogs = Blog.objects.filter(author = request.user)
        serializer = BlogSerializer(blogs, many=True)
        return Response({'data': serializer.data, 'message': "Posts fetched successfully"})
    except Exception as e:
        return Response(str(e), status=status.HTTP_401_UNAUTHORIZED)
    

## 44.19

