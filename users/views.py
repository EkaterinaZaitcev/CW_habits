from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from users.models import User
from users.serializers import UserSerializer


class UserCreateAPIView(CreateAPIView):
    """ Регистрация нового пользователя """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(serializer.validated_data["password"])
        user.is_active = True
        user.save()

class UserListAPIView(ListAPIView):
    """ Для просмотра списка профилей """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

class UserUpdateAPIView(UpdateAPIView):
    """ Изменение профиля пользователя """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

class UserRetrieveAPIView(RetrieveAPIView):
    """ Просмотр пользователя по ID """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
