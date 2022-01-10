from django.urls import path,include,re_path
from . import views
app_name = "homepage"
urlpatterns = [
    path("", views.index, name="index"),
    path('new/',views.new_project, name = 'new_project'),
    #re_path('projects/<int:id>/',views.projects, name = 'projects'),
    path('projects/<id>/',views.projects,name = 'projects'),
    path('rate/<id>/',views.rate,name = 'rate'),
    path(r'ratings/', include('star_ratings.urls', namespace='ratings')),
    path('search/', views.searchprofile, name='search'),
]