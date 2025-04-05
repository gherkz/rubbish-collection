"""
URL routing for the base route exposing the API version

"""

from django.urls.conf import path

from . import views

urlpatterns = [path("", views.VersionsView.as_view(), name="available-versions")]
