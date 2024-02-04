from django.urls import path
from contact import views

app_name = 'contact' # isso é o primeiro parametro do link id da tabela em index.html >>contact<<:contact

urlpatterns = [
    path('<int:contact_id>/', views.contact, name='contact' ),
    path('', views.index, name='index'),
]

# name='contact' é o segundo parametro do link id da tabela em index.html contact:>>contact<<