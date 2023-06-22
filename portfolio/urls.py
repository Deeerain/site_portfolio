from django.urls import path

from portfolio import views


app_name = 'portfolio'

urlpatterns = [
    path('', views.WorkList.as_view(), name='work-list'),
    path('<slug:slug>/', views.WorkDetail.as_view(), name='work-detail'),
]
