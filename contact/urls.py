from django.urls import path
from contact import views

app_name = 'contact' # isso é o primeiro parametro do link id da tabela em index.html >>contact<<:contact

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    #contact (CRUD)
    path('contact/<int:contact_id>/', views.contact, name='contact' ),
    path('contact/create/', views.create, name='create' ),
]
# name='contact' é o segundo parametro do link id da tabela em index.html contact:>>contact<<

    
