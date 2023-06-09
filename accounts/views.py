from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SignUpSerializer,LoginSerializer
from rest_framework import status


@api_view(['POST'])
def signUpView(request):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



@api_view(["POST"])
def loginView(request):
      serializer = LoginSerializer(data=request.data)
      if serializer.is_valid():
            response = serializer.jwt_token(serializer.data)
            return Response(response,status=status.HTTP_200_OK)
      return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

