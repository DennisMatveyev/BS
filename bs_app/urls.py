from django.conf.urls import url
from .views import Register, UserList, UserDetail, PostList, PostDetail, AllPostList
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token


urlpatterns = [
    url(r'^register/$', Register.as_view()),
    url(r'^login/', obtain_jwt_token),
    url(r'^users/$', UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', UserDetail.as_view(), name='user-detail'),
    url(r'^posts/$', PostList.as_view(), name='post-list'),
    url(r'^posts/all/$', AllPostList.as_view(), name='all-post-list'),
    url(r'^posts/(?P<pk>[0-9]+)/$', PostDetail.as_view(), name='post-detail'),
    url(r'^verify-token/', verify_jwt_token),
]