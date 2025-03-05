from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


@api_view(['GET'])
def get_data(request):
    data = {
        'name': 'john doe',
        'age': 30,
        'job': 'developer',
        'skin': 'brown',
        'phone': '099999939934',
        'email': 'asef@gmail.com',
        'list': [i for i in range(5)]
    }

    return Response(data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_info(request):
    info = {
        'company': 'Tech Corp',
        'location': 'New York',
        'website': 'https://techcorp.com',
        'employees': 150,
        'founded': 2010,
        'departments': ['Engineering', 'Marketing', 'Sales', 'HR']
    }

    return Response(info, status=status.HTTP_200_OK)
