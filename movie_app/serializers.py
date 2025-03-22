from rest_framework import serializers
from .models import Director, Movie, Review, Tag
from rest_framework import serializers
from .models import User, ConfirmationCode


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data.get('email'),
            is_active=False
        )
        code = ConfirmationCode.generate_code()
        ConfirmationCode.objects.create(user=user, code=code)
        return user

class ConfirmationSerializer(serializers.Serializer):
    username = serializers.CharField()
    code = serializers.CharField(max_length=6)

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'name id created updated'.split()

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Имя не может быть пустым.")
        if Director.objects.filter(name=value).exists():
            raise serializers.ValidationError("Режиссёр уже существует.")
        return value


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'



class MovieSerializer(serializers.ModelSerializer):
    director = DirectorSerializer(many=False)
    director_name = serializers.SerializerMethodField()
    tags = TagSerializer(many=True)

    class Meta:
        model = Movie
        fields = 'id title description release_year is_active created updated director director_name tags tag_name'.split()
    def get_director_name(self, movie):
        return movie.director.name if movie.director else None

    # Валидация года выпуска
    def validate_release_year(self, value):
        if value < 1900 or value > 2100:
            raise serializers.ValidationError("Некорректный год выпуска (1900-2100).")
        return value

    # Валидация тегов
    def validate_tags(self, value):
        if len(value) > 5:
            raise serializers.ValidationError("Максимум 5 тегов.")
        return value

    # Проверка существования режиссёра
    def validate_director_id(self, value):
        if not Director.objects.filter(id=value).exists():
            raise serializers.ValidationError("Режиссёр не найден.")
        return value


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

        # Валидация оценки (1-5)
        def validate_stars(self, value):
            if value < 1 or value > 5:
                raise serializers.ValidationError("Оценка должна быть от 1 до 5.")
            return value

        # Проверка существования фильма
        def validate_movie_id(self, value):
            if not Movie.objects.filter(id=value).exists():
                raise serializers.ValidationError("Фильм не найден.")
            return value

class MovieDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'