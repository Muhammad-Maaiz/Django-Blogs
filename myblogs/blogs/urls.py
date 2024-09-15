from django.urls import path
from blogs import views

urlpatterns = [
    path('addblog/', views.add_blog, name='addblog'),
    path('updateblog/<int:id>', views.update_blog, name='updateblog'),
    path('deleteblog/<int:id>', views.delete_blog, name='deleteblog'),

]
