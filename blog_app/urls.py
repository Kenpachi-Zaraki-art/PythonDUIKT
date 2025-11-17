from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='home'),

    path('profiles/', views.profiles_list, name='profiles-list'),

    re_path(
        r'^profile/(?P<blogger_slug>[a-z0-9-]+)/$',
        views.profile_detail,
        name='profile-detail'
    ),

    path('news/', views.news_page_redirect, name='news-redirect'),
]