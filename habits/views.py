from rest_framework.exceptions import ValidationError
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.permissions import AllowAny, IsAuthenticated

from habits.models import Habit
from habits.paginations import HabitsPaginator
from habits.serializers import HabitsSerializer
from users.permissions import IsOwner
from users.serializers import UserSerializer


class HabitsCreateAPIview(CreateAPIView):
    """ Создание новой привычки """
    serializer_class = HabitsSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        habit = serializer.save
        habit.user == self.request.user
        habit = serializer.save
        habit.save()


class HabitsRetrieveAPIview(RetrieveAPIView):
    """ Просмотр определенной привычки """
    serializer_class = HabitsSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitsListAPIview(ListAPIView):
    """ Просмотр привычек пользователя """
    serializer_class = HabitsSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]
    pagination_class = HabitsPaginator

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class HabitsUpdateAPIview(UpdateAPIView):
    """ Изменение привычки """
    serializer_class = HabitsSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]

    def perform_update(self, serializer):
        """Перед сохранением привычки проверяем не ссылается связанная привычка на саму себя"""
        habit = serializer.save()
        if not habit.is_nice and habit.related_habit and habit.id == habit.related_habit.id:
            raise ValidationError(f"Связанная привычка не может ссылаться на саму себя")
        habit.save()


class HabitsDeleteAPIview(DestroyAPIView):
    """ Удаление привычки """
    serializer_class = HabitsSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitsPublishingListAPIview(ListAPIView):
    """ Просмотр публичных привычек """
    serializer_class = HabitsSerializer
    queryset = Habit.objects.all()
    pagination_class = HabitsPaginator
    permission_classes = [AllowAny]
