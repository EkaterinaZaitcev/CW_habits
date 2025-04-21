from django.urls import path

from habits.apps import HabitsConfig
from habits.views import (HabitsCreateAPIview, HabitsDeleteAPIview,
                          HabitsPublishingListAPIview, HabitsRetrieveAPIview,
                          HabitsUpdateAPIview)

app_name = HabitsConfig.name


urlpatterns = [
    path('', HabitsRetrieveAPIview.as_view(), name="habits-list"),
    path('create/', HabitsCreateAPIview.as_view(), name="habits-create"),
    path('update/', HabitsUpdateAPIview.as_view(), name="habits-update"),
    path('delete/', HabitsDeleteAPIview.as_view(), name="habits-delete"),
    path('habits/publishing/', HabitsPublishingListAPIview.as_view(), name="publishing-list"),
]
