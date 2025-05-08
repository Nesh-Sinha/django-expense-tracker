from . import views

from django.urls import path, include

urlpatterns = [
    path('', views.home, name='home'),
    path('layout/', views.layout, name='layout'),
    path('expense/', views.expense, name='expense'),
    path('viewexp/',views.viewexp,name='viewexp'),
    path('addexpense/',views.addexpense,name='addexpense'),
    path('budget/',views.budget,name='budget'),
    path('delete_data/',views.delete_data,name='delete_data'),
    path('export_csv/', views.export_csv, name='export_csv'),
    path('chart/',views.chart,name='chart'),
    path('about/',views.about,name='about'),
]
