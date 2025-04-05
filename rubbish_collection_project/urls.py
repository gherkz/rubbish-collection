"""rubbish-collection URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, path, re_path

# Django debug toolbar is only installed in developer builds
try:
    import debug_toolbar

    HAVE_DDT = True
except ImportError:
    HAVE_DDT = False

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/", include("social_django.urls", namespace="social")),
    # use `healthy` rather than `healthz` as Cloud Run reserves the use of the `/healthz` endpoint
    path(
        "healthy",
        lambda request: HttpResponse("ok", content_type="text/plain"),
        name="healthy",
    ),
    path(
        "",
        include(
            "ui.urls",
            namespace="ui",
        ),
    ),
    # You'll also need to update api/tests/test_versions_view.py
    # Include the base API urls - which gives a view of the available API versions
    path("api/", include("api.urls")),
    # Include the v1alpha urls - allowing for any release version, the version is validated
    # by setting REST_FRAMEWORK.ALLOWED_VERSIONS in settings.base
    re_path(
        r"^api/(?P<version>v1alpha\d{1,3})/",
        include("api.v1alpha.urls", "v1alpha"),
    ),
]

# Selectively enable django debug toolbar URLs. Only if the toolbar is
# installed *and* DEBUG is True.
if HAVE_DDT and settings.DEBUG:
    urlpatterns = [
        path(r"__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
