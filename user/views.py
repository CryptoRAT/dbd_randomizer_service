from django.views.decorators.csrf import csrf_protect
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import api_view, permission_classes
from .models import RegisteredUser
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .serializers import RegisteredUserSerializer


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
            return Response({'error': 'Email, password, confirm password, and name are required'},
                            status=status.HTTP_400_BAD_REQUEST)
        print(email, password, display_name, confirm_password)
        print("confirming password")
        if password != confirm_password:
            return Response({'error': 'Passwords do not match'}, status=status.HTTP_400_BAD_REQUEST)

        # Creating a new user with create_user automatically hashes the password
        new_user = RegisteredUser.objects.create_user(
            password=password,
            name=display_name,
            email=email
        )

        serializer = self.get_serializer(new_user)
        headers = self.get_success_headers(serializer.data)

        return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED, headers=headers)


class LoginView(APIView):

    permission_classes = [AllowAny]
    authentication_classes = [JWTAuthentication]

    def post(self, request, *args, **kwargs):
        print("Executing a post on /login/ ")
        try:
            # Your login logic here
            username = str(request.data.get('email'))
            password = str(request.data.get('password'))
            print("Username: " + username)

            # Validate credentials using Django's authenticate method
            user = authenticate(request, username=username, password=password)

            if user is not None:
                # Authentication successful, generate JWT token
                refresh = RefreshToken.for_user(user)
                access_token = str(refresh.access_token)

                return Response({'access_token': access_token}, status=status.HTTP_200_OK)
            else:
                # Authentication failed
                return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        except Exception as e:
            # Handle other exceptions
            return Response({'detail': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# views.py


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def check_auth(request):
    print("entered check_auth")
    # If the user is authenticated, return user data
    refresh = RefreshToken.for_user(request.user)
    access_token = str(refresh.access_token)
    return Response({'username': request.user.username, 'access_token': access_token})
