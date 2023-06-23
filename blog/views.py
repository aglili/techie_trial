from rest_framework.decorators import api_view
from .serializer import BlogSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from .models import Blog
from django.core.paginator import Paginator

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
    #

@api_view(["GET"])
def getUserBlog(request):
    try:
        if not request.user.is_authenticated:
            return Response({"error": "Invalid Login Credentials"}) 
        #(request.data)
        blogs = Blog.objects.filter(author = request.user)
        ## Implement the ability to search through posts

        if request.GET.get('query'):
            query = request.GET.get('query')
            blogs = blogs.filter(Q(title__icontains=query) | Q(content__icontains=query))

        serializer = BlogSerializer(blogs, many=True)
        return Response({'data': serializer.data, 'message': "Posts fetched successfully"})
    except Exception as e:
        return Response(str(e), status=status.HTTP_401_UNAUTHORIZED)
    
@api_view(['PATCH'])
def updateUserBlog(request):
    try:
        data = request.data
       
        blog = Blog.objects.filter(user_id=data.get('user_id'))


        if not blog.exists():
            return Response({'message':'Blog Does Not Exist'},status=status.HTTP_404_NOT_FOUND)


        if request.user != blog[0].author:
            return Response({'message':'Unauthorized Access!!'},status=status.HTTP_401_UNAUTHORIZED)
        
        serializer= BlogSerializer(blog[0],data=data,partial=True)

        if not serializer.is_valid():
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)


    except Exception as e:
        return Response(str(e), status=status.HTTP_401_UNAUTHORIZED)
    


@api_view(["DELETE"])
def deleteBlog(request):
    try: 
        data = request.data

        blog = Blog.objects.filter(user_id=data.get('user_id'))

        
        if not blog.exists():
            return Response({'message':'Blog Does Not Exist'},status=status.HTTP_404_NOT_FOUND)
        
        if request.user != blog[0].author:
            return Response({'message':'Unauthorized Access!!'},status=status.HTTP_401_UNAUTHORIZED)
        

        blog[0].delete()
        return Response({"data":{},"message":"Blog Deleted"},status=status.HTTP_200_OK)
    except Exception as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)



# allow non-registered users read the blog
@api_view(["GET"])
def publicBlog(request):
        try:
            blogs = Blog.objects.all().order_by("?")
            ## Implement the ability to search through posts

            if request.GET.get('query'):
                query = request.GET.get('query')
                blogs = blogs.filter(Q(title__icontains=query) | Q(content__icontains=query))

        
            #add pagination
            page_number =request.GET.get('page',1)
            paginator  = Paginator(blogs,1)

            serializer = BlogSerializer(paginator.page(page_number),many=True)
            return Response({'data': serializer.data, 'message': "Posts fetched successfully"})
        except Exception as e:
            print(e)
            return Response({"message":"Wrong or Invalid Page"}, status=status.HTTP_401_UNAUTHORIZED)
        

