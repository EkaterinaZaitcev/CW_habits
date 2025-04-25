from rest_framework.serializers import ModelSerializer

from habits.models import Habit
from habits.validators import HabitValidators


class HabitsSerializer(ModelSerializer):
    """Сериализатор привычек"""
    class Meta:
        model = Habit
        fields = "__all__"
        validators = [HabitValidators]
