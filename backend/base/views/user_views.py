from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from ..serializers import ProductSerializer, UserSerializer, UserSerializerWithToken
# Create your views here.
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

User = get_user_model()


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = UserSerializerWithToken(self.user).data
        for k, v in serializer.items():
            data[k] = v

        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['POST'])
def register_user(request):
    data = request.data
    try:
        user = User.objects.create(
            first_name=data['name'],
            username=data['email'],
            email=data['email'],
            password=make_password(data['password'])
        )

        serializer = UserSerializerWithToken(user, many=False)
        return Response(serializer.data)
    except:
        message = {
            'detail': 'User with this email address already exists.'
        }
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@permission_classes([IsAuthenticated, ])
@api_view(['PUT'])
def update_user_profile(request):
    my_user = request.user

    serializers = UserSerializerWithToken(my_user, many=False)
    data = request.data
    my_user.first_name = data['name']
    my_user.username = data['email']
    my_user.email = data['email']

    if data['password'] != '':
        my_user.password = make_password(data['password'])

    my_user.save()

    return Response(serializers.data)


@permission_classes([IsAuthenticated, ])
@api_view(['GET'])
def get_user_profile(request):
    my_user = request.user
    serializers = UserSerializer(my_user, many=False)
    return Response(serializers.data)


@api_view(['GET'])
@permission_classes([IsAdminUser, ])
def get_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)
