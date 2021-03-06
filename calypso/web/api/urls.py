from django.urls import path, include
from rest_framework import routers
from . import views

app_name = "web_api"


web_routers = routers.DefaultRouter()
web_routers.register(r'configuration', views.ConfigurationView,
                     basename="configuration")


urlpatterns = [
    path('', include(web_routers.urls)),
    path('contact-us/', views.ContactForm.as_view(), name="contact-us"),
    path(
        'slider/', views.SliderViewSet.as_view({'get': 'list'}), name="sliders"),
    path(
        'instagram-feed/', views.InstagramFeed.as_view(), name="instagram"),
    path(
        'search/', views.Search.as_view(), name="search"),
    # path(
    #     'configuration/<slug:slug>/', views.ConfigurationView.as_view({"slug":"slug"}), name="configuration"),
]
