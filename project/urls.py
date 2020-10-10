
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
	# admin url to open django default admin panel
    path('admin/', admin.site.urls),
    # default landing url endpoints it will sreach requested url in app/urls.py
    path('', include('app.urls')),

]
