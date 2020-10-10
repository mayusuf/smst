from django.shortcuts import render,HttpResponseRedirect, redirect
from django.views.generic import TemplateView
from django.http import HttpResponse
import csv
from .models import *
from datetime import datetime


def decode_utf8(input_iterator):
	for l in input_iterator:
		yield l.decode('utf-8')

# Fuction to track reqested user IP address
def visitorIP(request):
	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for:
		ip = x_forwarded_for.split(',')[0]
	else:
		ip = request.META.get('REMOTE_ADDR')
	return ip

# View to upload data from csv file #csv file format should be same as shared in task_data.csv
class UploadData(TemplateView):
	template_name = 'upload_file.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,locals())
	def post(self,request,*args,**kwargs):

		# read upload csv file and insert data in table
		read_uploaded_file = csv.DictReader(decode_utf8(request.FILES['upload_file']))
		data_list=[]
		for row in read_uploaded_file:
			id=row.get("id")
			timestamp=row.get("timestamp")
			temperature=row.get("temperature")
			duration=row.get("duration")

			obj=DataModel()
			obj.task_id=id
			obj.timestamp=timestamp
			obj.temperature=temperature
			obj.duration=duration
			data_list.append(obj)

		# bulk insert the file data in DataModel table
		DataModel.objects.bulk_create(data_list)
		return HttpResponseRedirect('/')

# View to show data on html page on get request
class DataView(TemplateView):
	template_name="data.html"
	def get(self,request,*args,**kwargs):
		# fetch all data from table to send it to front end page
		data=DataModel.objects.all().order_by("-id")

		# save request time and request ip
		visitor_ip_address=visitorIP(request)
		request_datetime=datetime.now()
		obj=VisitTracker(
			ip=visitor_ip_address,
			request_datetime=request_datetime
			)
		obj.save()
		return render(request,self.template_name,locals())
