from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("common.urls")),
    path('', include("restaurant.urls")),
    path('', include("account.urls")),
]

handler404 = 'common.views.page_not_found'