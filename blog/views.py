from rest_framework.decorators import api_view
from .serializer import BlogSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

@api_view(["POST"])
def blogView(request):
    try:
        if not request.user.is_authenticated:
            raise PermissionError("Authentication credentials were not provided.")
        data = request.data
        serializer = BlogSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response(str(e), status=status.HTTP_401_UNAUTHORIZED)

