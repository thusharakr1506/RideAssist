from django.urls import path
from api import views

from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns=[

path("customers/",views.CustomerListCreateView.as_view()),

path("customers/<int:pk>/",views.CustomerRetrieveUpdateDestroyView.as_view()),

path("token/",TokenObtainPairView.as_view()),

path("token/refresh/",TokenRefreshView.as_view()),

path("customers/<int:pk>/work/",views.WorkCreateView.as_view()),

]