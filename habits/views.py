from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.permissions import AllowAny, IsAuthenticated

from habits.models import Habit
from habits.paginations import HabitsPaginator
from users.serializers import UserSerializer


class HabitsCreateAPIview(CreateAPIView):
    """ Создание новой привычки """
    serializer_class = UserSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated]


class HabitsRetrieveAPIview(RetrieveAPIView):
    """ Просмотр привычки """
    serializer_class = UserSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitsUpdateAPIview(UpdateAPIView):
    """ Изменение привычки """
    serializer_class = UserSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitsDeleteAPIview(DestroyAPIView):
    """ Удаление привычки """
    serializer_class = UserSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitsPublishingListAPIview(ListAPIView):
    """ Просмотр публичных привычек """
    serializer_class = UserSerializer
    queryset = Habit.objects.all()
    pagination_class = HabitsPaginator
    permission_classes = [AllowAny]
