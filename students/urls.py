from django.urls import path
from students import views

urlpatterns = [
    path('',views.student_created,name='student_add'),
    path('list/',views.student_list,name='student_list'),
    path('edit/<int:id>/',views.student_update,name='student_update'),
    path('delete/<int:id>',views.student_delete,name='student_delete')
    
]
