from django.urls import path
from . import views

urlpatterns = [
    path('fighters/', views.FightersListCreate.as_view()),
    path('fighters/<int:pk>/', views.FighterDetail.as_view()),
    path('weight-classes/', views.WeightClassesListCreate.as_view()),
    path('weight-classes/<str:code>/', views.WeightClassDetailByCode.as_view()),
    path('events/', views.EventsListCreate.as_view()),
    path('events/<int:pk>/', views.EventDetail.as_view()),
    path('bouts/', views.BoutsListCreate.as_view()),
    path('bouts/<int:pk>/', views.BoutDetail.as_view()),
]
