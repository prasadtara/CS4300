from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),

    # Home -> movies list
    path("", RedirectView.as_view(pattern_name="movie_list", permanent=False)),

    # HTML pages
    path("", include("bookings.web_urls")),

    #login/logout/password-reset routes
    path("accounts/", include("django.contrib.auth.urls")),

    # API
    path("api/", include("bookings.urls")),
]