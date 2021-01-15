from django.urls import path
from . import views
urlpatterns=[
    path('', views.index, name="index"),
    path('Congratulations', views.details, name="Congratulations"),
    path('Kanika', views.kanika, name='Thanks'),
    path('Ansh', views.ansh, name='Thanks'),
]