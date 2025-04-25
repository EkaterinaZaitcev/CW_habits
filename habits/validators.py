from datetime import timedelta

from rest_framework.serializers import ValidationError

from habits import serializers
from habits.models import Habit


class HabitValidators:
    """Валидаторы привычек по техзаданию"""

    def valid_time(self, value):
        val = dict(value)
        if val.get('time_to_complete' > timedelta(seconds=120)):
            raise ValidationError(
                'Время выполнения должно быть не больше 120 секунд.'
            )


    def valid_days_of_week(self, value):
        val = dict(value)
        if int(val.get('periodicity')) < 1 or int(val.get('periodicity')) > 7:
            raise ValidationError(
                'Нельзя выполнять привычку реже, чем 1 раз в 7 дней.'
            )


    def valid_related_habit(self, value):
        if value.get('related_habit_id'):
            related_habit = Habit.objects.get(pk=value.get('related_habit_id'))
            if not related_habit.is_pleasant:
                raise serializers.ValidationError(
                'В качестве приятной привычки можно выбрать только одно связанную привычку.'
                )


    def valid_reward(self, value):
        if value.get('related_habit_id') and value.get('reward'):
            raise serializers.ValidationError(
                'Связанные привычка и вознаграждение не могут быть выбраны одновременно. Выберите 1 из 2 вариантов.'
            )


    def __call__(self, value):
        self.valid_time(value)
        self.valid_days_of_week(value)
        self.valid_related_habit(value)
        self.valid_reward(value)
