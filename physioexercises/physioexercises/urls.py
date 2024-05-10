"""
URL configuration for physioexercises project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from django.contrib import admin
from django.urls import path, include
from exercises.views import search_exercises, send_email, SuccessView, ExerciseListView, HomeView, LoggedOutView
from django.conf import settings
from django.conf.urls.static import static
from patient_activation.views import handle_report_upload, preview_activation_email
from insights.views import produce_insights
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("admin/", admin.site.urls, name="edit"),
    path("", HomeView.as_view(), name="home"),
    path("logout", LogoutView.as_view(next_page="logged_out"), name="logout"),
    path("logged_out", LoggedOutView.as_view(), name="logged_out"),

    path("prescribe/", search_exercises, name="prescribe"),
    path("send_email/", send_email, name="send_email"),
    path("success/", SuccessView.as_view(), name="success"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("exercises/", ExerciseListView.as_view(), name="exercises"),
    path("activate/", handle_report_upload, name="activate"),
    path("preview_activation/", preview_activation_email, name="preview_activation"),
    path("insights/", produce_insights, name="insights"),




]
if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#     urlpatterns += path("silk/", include("silk.urls", namespace="silk")),
