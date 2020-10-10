
from django.urls import path
from .views import *

urlpatterns = [
	# url to show data on html
    path('', DataView.as_view(),name="view_data"),
    
    # Url to upload a file and save in table
    path('upload-data', UploadData.as_view(),name="upload_file"),

]
