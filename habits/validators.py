from datetime import timedelta

from rest_framework.serializers import ValidationError


class HabitsValidators:
    """Валидаторы привычек по техзаданию"""
    def __call__(self, value):
        val = dict(value)
        if val.get('time_to_complete' > timedelta(seconds=120)):
            raise ValidationError(
                'Время выполнения должно быть не больше 120 секунд.'
            )

        elif int(val.get('periodicity')) < 1 or int(val.get('periodicity')) > 7:
            raise ValidationError(
                'Нельзя выполнять привычку реже, чем 1 раз в 7 дней.'
            )

        elif (
            val.get('pleasant_habit') is False
            and not val.get('related_habit')
            or not val.get('reward')
        ):
            raise ValidationError(
                'Исключить одновременный выбор связанной привычки и указания вознаграждения.'
            )

        elif(
                val.get('pleasant_habit') is False
                and val.get('related_habit')
                or val.get('reward')
        ):
            raise ValidationError(
                'У приятной привычки может быть заполнено только одно из полей: вознаграждения или связанная привычка.'
            )

        elif val.get('pleasant_habit') is True and val.get ('related_habit'):
            raise ValidationError(
                'У приятной привычки не может быть связанной привычки.'
            )

        elif val.get('pleasant_habit') is True and val.get('reward'):
            raise ValidationError(
                'У приятной привычки не может быть вознаграждения'
            )
