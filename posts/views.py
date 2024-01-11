from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
@api_view(http_method_names=['GET'])
def homePage(request:Request):
    response={"message": "Hello World!"}
    return Response(data=response, status=status.HTTP_200_OK)
