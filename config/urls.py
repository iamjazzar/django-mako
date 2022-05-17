from django.urls import re_path

from niceapp import views

urlpatterns = [
    re_path(r"^(?P<engine>django|mako)?$", views.function_based_view),
    re_path(
        r"^class/(?P<engine>django|mako)?$", views.ClassBasedView.as_view(), name="CBV"
    ),
]
