from django.views.decorators.csrf import csrf_protect, csrf_exempt
from rest_framework import status, viewsets
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import RegisteredUser
from django.views import View
from .serializers import UserRegistrationSerializer, RegisteredUserSerializer
import pdb

class RegisteredUserViewSet(viewsets.ModelViewSet):
    queryset = RegisteredUser.objects.all()
    serializer_class = RegisteredUserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return self.queryset.filter(id=self.request.user.id)

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        confirm_password = request.data.get('confirmPassword')
        display_name = request.data.get('displayName')

        if not email or not password or not display_name or not confirm_password:
            return Response({'error': 'Email, password, confirm password and name are required'}, status=status.HTTP_400_BAD_REQUEST)

        if password != confirm_password:
            return Response({'error': 'Passwords do not match'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(data={'email': email, 'password': password, 'name': display_name})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED, headers=headers)


class UserRegistrationView(View):
    @authentication_classes([])  # Empty list to disable authentication
    @permission_classes([])  # Empty list to disable permission checks
    @csrf_exempt
    def create(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data)

        if serializer.is_valid():
            # Create a new user using Django's User model
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            display_name = serializer.validated_data['display_name']
            email = serializer.validated_data['email']
            new_user = RegisteredUser.objects.create_user(username=username,
                                                          password=password,
                                                          display_name=display_name,
                                                          email=email)

            return Response({'message': 'Registration successful'}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def LoginView(request):
    authentication_classes = []
    permission_classes = []

    @csrf_exempt
    def login(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data)

        if serializer.is_valid():
            # Create a new user using Django's User model
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            display_name = serializer.validated_data['display_name']
            email = serializer.validated_data['email']
            new_user = RegisteredUser.objects.create_user(username=username,
                                                          password=password,
                                                          display_name=display_name,
                                                          email=email)

            return Response({'message': 'Registration successful'}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
