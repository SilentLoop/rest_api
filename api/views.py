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
        'list': [i for i in range(5)]
    }

    return Response(data, status=status.HTTP_200_OK)
