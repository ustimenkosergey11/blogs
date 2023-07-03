from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from blogsapp.views import PostView, PostDetail, AddPost


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PostView.as_view(), name='main'),
    path('addpost/', AddPost.as_view(), name='addpost'),
    path('<int:pk>/', PostDetail.as_view()),

    path('users/', include('blogsapp.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)