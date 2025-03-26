from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework.decorators import api_view
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.db import transaction
from .models import (
    Director,
    Movie,
    Review,
    User,
    ConfirmationCode
)
from .serializers import (
    DirectorSerializer,
    MovieSerializer,
    ReviewSerializer,
    MovieDetailSerializer,
    UserRegistrationSerializer,
    ConfirmationSerializer
)

# User Auth Views
class RegisterUserView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"detail": "Код подтверждения отправлен."}, status=201)
        return Response(serializer.errors, status=400)

class ConfirmUserView(APIView):
    def post(self, request):
        serializer = ConfirmationSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)

        username = serializer.validated_data['username']
        code = serializer.validated_data['code']

        try:
            user = User.objects.get(username=username)
            confirmation = ConfirmationCode.objects.get(user=user)
        except (User.DoesNotExist, ConfirmationCode.DoesNotExist):
            return Response({"detail": "Неверные данные"}, status=400)

        if confirmation.code == code:
            user.is_active = True
            user.save()
            confirmation.delete()
            return Response({"detail": "Аккаунт активирован!"})
        return Response({"detail": "Неверный код"}, status=400)

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, _ = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })

# Director Views
class DirectorListCreateView(ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

class DirectorRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    lookup_field = 'id'

# Movie Views
class MovieListCreateView(ListCreateAPIView):
    queryset = Movie.objects.select_related('director').filter(is_active=True)
    serializer_class = MovieSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return MovieDetailSerializer
        return super().get_serializer_class()

class MovieRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieDetailSerializer
    lookup_field = 'id'

# Review Views
class ReviewListCreateView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = 'id'