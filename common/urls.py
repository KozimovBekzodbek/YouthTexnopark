from django.urls import path
from common import views

app_name = "common"
handler404 = 'common.views.custom_404_view'

urlpatterns = [
        path("", views.HomeView.as_view(), name="home"),
        path("success/", views.SuccessView.as_view(), name="success"),
        path("nizom/", views.NizomView.as_view(), name="nizom"),
        path("error/", views.ErrorView.as_view(), name="error"),
        path("forms/", views.FormView.as_view(), name="forms"),
       ]

