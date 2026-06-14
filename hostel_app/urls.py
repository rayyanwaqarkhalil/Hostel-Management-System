from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    # Students
    path('students/', views.students, name='students'),
    path('students/add/', views.add_student, name='add_student'),
    path(
    'complaints/edit/<int:id>/',
    views.edit_complaint,
    name='edit_complaint'
),

    path('students/edit/<int:id>/', views.edit_student, name='edit_student'),
    path(
    'students/delete/<int:id>/',
    views.delete_student,
    name='delete_student'
),


    # Rooms
    path('rooms/', views.rooms, name='rooms'),
    path('rooms/add/', views.add_room, name='add_room'),

    # Wardens
    path('wardens/', views.wardens, name='wardens'),
    path('wardens/add/', views.add_warden, name='add_warden'),

    # Complaints
    path('complaints/', views.complaints, name='complaints'),
    path('complaints/add/', views.add_complaint, name='add_complaint'),
]