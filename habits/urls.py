from django.urls import path

from habits.apps import HabitsConfig
from habits.views import (HabitsCreateAPIview, HabitsDeleteAPIview,
                          HabitsPublishingListAPIview, HabitsRetrieveAPIview,
                          HabitsUpdateAPIview, HabitsListAPIview)

app_name = HabitsConfig.name

urlpatterns = [
    path('list/', HabitsListAPIview.as_view(), name="habits_list"),
    path('create/', HabitsCreateAPIview.as_view(), name="habits_create"),
    path('update/<int:pk>/', HabitsUpdateAPIview.as_view(), name="habits_update"),
    path('retrieve/<int:pk>/', HabitsRetrieveAPIview.as_view(), name="habits_retrieve"),
    path('delete/<int:pk>/', HabitsDeleteAPIview.as_view(), name="habits_delete"),
    path('publishing/', HabitsPublishingListAPIview.as_view(), name="publishing_list"),
]
