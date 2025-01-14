from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router=DefaultRouter()
router.register("",views.PatientViewSet)

urlpatterns = [
    path('list/',include(router.urls)),
    path('register/',views.RegistrationApiView.as_view()),
    path('login/',views.LoginApiView.as_view(),name="login"),
    path('logout/',views.LogOutApiView.as_view(),name="logout"),
    path('patient/active/<uid64>/<token>/',views.activation,name="activate"),
]
