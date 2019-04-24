from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/',views.login_user,name = 'login'),
    path('logout/',views.logout_view,name = 'logou'),
    # path('login/my-app/',views.login_user,name = 'login_url'),


]
