from django.urls import path, include

from django.views.static import serve

from django.conf import settings
from django.urls import re_path as url
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    path('signup/',views.SignUpView.as_view(), name='signup'),
    # # path ('login/',views.LoginView.as_view(), name='login'),
 
    path('login/',views.TokenView.as_view(), name='submit'),
    # path('<int:pk>/update/',views.UserUpdateAPIview.as_view(), name='update'),


]