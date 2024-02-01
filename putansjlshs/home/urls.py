from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("enrollment/", views.enrollment, name="enrollment"),
    path("login/", views.login, name="login"),
    path("offerings/", views.offerings, name="offerings"),
    path("organizations/", views.organizations, name="organizations"),
    path("signup/", views.signup, name="signup"),
    path("sitemap/", views.sitemap, name="sitemap"),
]
