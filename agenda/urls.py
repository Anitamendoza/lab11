from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from agenda import views
urlpatterns = [
    path('', views.login_view, name='login'),
    path('contacto/', views.ContactListView.as_view(), name='contact_list'),
    path('new/', views.ContactCreateView.as_view(), name='contact_new'),
    path('<int:pk>/edit/', views.ContactUpdateView.as_view(), name='contact_edit'),
    path('<int:pk>/delete/', views.ContactDeleteView.as_view(), name='contact_delete'),
]
