from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('recommender', views.NewView)

urlpatterns = [
    path('', views.home_view, name='homeview'),
    path('form/', views.form_view, name='formview'),
    path('about/', views.about_view, name='aboutview'),
    path('api/', include(router.urls)),
]
