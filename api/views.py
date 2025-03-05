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


@api_view(['GET'])
def profile(request):
    profile = {
        'urls': {
        'github':'github.com/asef',
        'twitter':'https://twitter.com/asef',
        'facebook':'https://facebook.com/asef',
        'instagram':'https://instagram.com/asef'
        },
        'skills': ['Python', 'Django', 'Flask', 'JavaScript', 'React', 'Vue', 'Node.js', 'MongoDB', 'PostgreSQL'],
        'experience': '5 years',
        'education': 'Computer Science',
        'hobbies': ['Reading', 'Coding', 'Traveling', 'Music'],
        'languages': ['English', 'Spanish', 'French', 'German', 'Italian'],
        'interests': ['Technology', 'Science', 'Space', 'Philosophy', 'History'],
        'certifications': ['AWS Certified Developer', 'Google Cloud Professional Cloud Developer', 'Microsoft'],
        'projects': ['Project 1', 'Project 2', 'Project 3'],
        'awards': ['Best Developer', 'Best Team Player', 'Best Employee'],
        'achievements': ['Employee of the Year', 'Employee of the Month', 'Best Performance'],
        'publications': ['Publication 1', 'Publication 2', 'Publication 3'],
        'references': ['Reference 1', 'Reference 2', 'Reference 3'],
        'contact': {
            'phone': '099999939934',
            'email': 'gang@gmail.com'
            }
    }
    return Response(profile, status=status.HTTP_200_OK)