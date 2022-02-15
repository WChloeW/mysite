from django.urls import path
from . import views

# path
urlpatterns = {
    path('', views.toLogin_view),
    path('index/', views.Login_view),
    path('toregister/', views.toregister_view),
    path('register/', views.register_view),
    path('me/', views.me_view)
}
