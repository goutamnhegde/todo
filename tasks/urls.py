from django.urls import path
from . import views
urlpatterns=[
    # path('',views.tasklist.as_view(),name='tasklist'),
    path('',views.addtask,name='addtask'),
    path('done/<int:id>/',views.done,name='uptask'),
    path('delete/<int:id>/',views.delet,name='deltask')
    
]