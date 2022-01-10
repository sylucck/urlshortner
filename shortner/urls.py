from django.urls import path
from . import views


urlpatterns = [

    path('', views.index, name="index"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('<str:shortened_part>', views.redirect_url_view, name='redirect'),
    

]
