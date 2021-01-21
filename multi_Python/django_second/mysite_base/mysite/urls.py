from django.contrib import admin
from django.urls import path, include

from bookmark.views import BookmarkLV, BookmarkDV

urlpatterns = [
    path('admin/', admin.site.urls),

    path('bookmark/', BookmarkLV.as_view(), name='index'),
    path('bookmarks/<int:pk>', BookmarkDV.as_view(), name='detail'),
]
