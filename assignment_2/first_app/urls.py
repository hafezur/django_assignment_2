
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='homepage'),
    path('reg_new_todo',views.store_todo,name='store_todo'),
    path('show_todo/',views.show_todo,name='show_todo'),
    path('edit_todo/<int:id>',views.edit_todo,name='edit_todo'),
    path('delete_todo/<int:id>',views.delete_todo,name='delete_todo'),
    path('change_status/<int:id>',views.delete_todo,name='change_status'),
]
