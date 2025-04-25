from django.urls import path
from . import views

from habits.apps import HabitsConfig
from habits.views import (HabitsCreateAPIview, HabitsDeleteAPIview,
                          HabitsPublishingListAPIview, HabitsRetrieveAPIview,
                          HabitsUpdateAPIview, HabitsListAPIview)

app_name = HabitsConfig.name

urlpatterns = [
    path('list/', views.HabitsListAPIview.as_view(), name="habits_list"),
    path('create/', views.HabitsCreateAPIview.as_view(), name="habits_create"),
    path('update/<int:pk>/', views.HabitsUpdateAPIview.as_view(), name="habits_update"),
    path('retrieve/<int:pk>/', views.HabitsRetrieveAPIview.as_view(), name="habits_retrieve"),
    path('delete/<int:pk>/', views.HabitsDeleteAPIview.as_view(), name="habits_delete"),
    path('publishing/', views.HabitsPublishingListAPIview.as_view(), name="publishing_list"),
]
