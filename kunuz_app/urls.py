from django.urls import path
from .views import HomePageView, UzbNewsView, JahonNewsView, DetailView

urlpatterns = [
    path("", HomePageView.as_view(), name="home-page"),
    path('uzb/', UzbNewsView.as_view(), name="uzb-news"),
    path('jahon/', JahonNewsView.as_view(), name="jahon-news"),
    path('<int:id>/', DetailView.as_view(), name="detail"),
]