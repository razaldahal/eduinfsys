from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import serializers
from eduinfosys.serializers import *
from eduinfosys.models import *
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
class classeViewsets(viewsets.ModelViewSet):
	queryset=classe.objects.all()
	serializer_class=classeSerializer
	



	# def create(self,request):
	#  	classes=classe.objects.all()
	#  	serializer=classeSerializer(classes)

	# 	return Response(serializer.data)

	def create(self, request):

		serializer = self.get_serializer(data=request.data)
		if serializer.is_valid():
			data = serializer.data
			classe.objects.get_or_create(Class=data['Class'], defaults={'Section':data['Section'], 'Capacity':data['Capacity'], 'No_of_Students':data['No_of_Students']})
			return Response(data)

		else:
			return Response(serializer.errors)


	def get(self, request, pk, format=None):
		classe = self.get_object(pk)
		serializer = classeSerializer(classe)
		return Response(serializer.data)

	def retrieve(self, request, pk):
		classe = classe.objects.get(id=pk)
		serializer = self.get_serializer(data=classes)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		classe = self.get_object(pk)
		serializer = classeSerializer(classe, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def destroy(self, request, pk, format=None):
		classe = self.get_object(pk)
		classe.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


class sectionViewsets(viewsets.ModelViewSet):
	queryset=section.objects.all()
	serializer_class=sectionSerializer

	http_methods = ['post', 'put', 'get', 'delete']

	def create(self,request):
		serializer=self.get_serializer(data=request.data)
		if serializer.is_valid():
			data=serializer.data
			section.objects.get_or_create(section=data['section'],defaults={'r_class':data['r_class'],})
			return Response(data)
		else:
			return Response(serializer.errors)
	def get (self,request,pk,format=None):
		sec = section.objects.get(id=pk)
		serializer = self.get_serializer(data=sec)
		serializer.is_valid()
		return Response(serializer.data)

	def retrieve(self, request, pk):
		obj = self.get_object()
		return Response({obj.section,obj.r_class})


	def update(self,request, pk):
		serializer=self.get_serializer(data=request.data)
		data = {}
		if serializer.is_valid():
			data=serializer.data
		
			obj = self.get_object()

			obj.section = data['section']
			obj.r_class=data['r_class']

			obj.save()

		return Response(data)


	def delete(self,request,pk,format=None):
		serializer=self.get_serializer(data=request.data)
		if serializer.is_valid():
			data=serializer.data
			section.objects.get(pk=pk).delete()	

			return Response(status.HTTP_204_NO_CONTENT)






class teacherViewsets(viewsets.ModelViewSet):
	queryset=teacher.objects.all()
	serializer_class=teacherSerializer


	def create(self,request):
		serializer=self.get_serializer(data=request.data)
		if serializer.is_valid():
			data=serializer.data
			section.objects.get_or_create(Name=data['Name'],defaults={'Subjects':data['Subjects'],'Extras':data['Extras'],'Payments':data['Payments'],'Classes':data['Classes']})
			return Response(data)
		else:
			return Response(serializer.errors)
	def get (self,request,pk,format=None):
		sec = section.objects.get(id=pk)
		serializer = self.get_serializer(data=sec)
		serializer.is_valid()
		return Response(serializer.data)

	def retrieve(self, request, pk):
		obj = self.get_object()
		return Response({obj.Name,obj.Subjects,obj.Classes})


	def update(self,request, pk):
		serializer=self.get_serializer(data=request.data)
		data = {}
		if serializer.is_valid():
			data=serializer.data
		
			obj = self.get_object()

			obj.Name = data['Name']
			obj.Subjects=data['Subjects']
			obj.Extras=data['Extras']
			obj.Payments=data['Payments']
			obj.Classes=data['Classes']

			obj.save()

		return Response(data)


	def delete(self,request,pk,format=None):
		serializer=self.get_serializer(data=request.data)
		if serializer.is_valid():
			data=serializer.data
			section.objects.get(pk=pk).delete()	

			return Response(status.HTTP_204_NO_CONTENT)



class studentViewsets(viewsets.ModelViewSet):
	queryset=student.objects.all()
	serializer_class=studentSerializer

	

	def create(self,request):
		serializer=self.get_serializer(data=request.data)
		if serializer.is_valid():
			data=serializer.data
			section.objects.get_or_create(Name=data['Name'],defaults={'Class':data['Class'],'Section':data['Section'],'roll_no':data['roll_no'],'Father_name':data['Father_name'],'Mother_name':data['Mother_name'],'Guardians_name':data['Guardians_name'],'Guardians_contact':data['Guardians_contact'],'Address_current':data['Address_current'],'Address_permanent':data['Address_permanent'],'email':data['email']})
			return Response(data)
		else:
			return Response(serializer.errors)
	def get (self,request,pk,format=None):
		sec = section.objects.get(id=pk)
		serializer = self.get_serializer(data=sec)
		serializer.is_valid()
		return Response(serializer.data)

	def retrieve(self, request, pk):
		obj = self.get_object()
		return Response({obj.Name,obj.Class,obj.Section,obj.roll_no})


	def update(self,request, pk):
		serializer=self.get_serializer(data=request.data)
		data = {}
		if serializer.is_valid():
			data=serializer.data
		
			obj = self.get_object()

			obj.Name = data['Name']
			obj.Class=data['Class']
			obj.Section=data['Section']
			obj.roll_no=data['roll_no']
			obj.Father_name=data['Father_name']
			obj.Mother_name=data['Mother_name']
			obj.Guardians_name=data['Guardians_name']
			obj.Guardians_contact=data['Guardians_contact']
			obj.Address_current=data['Address_current']
			obj.Address_permanent=data['Address_permanent']
			obj.email=data['email']

			obj.save()

		return Response(data)


	def delete(self,request,pk,format=None):
		serializer=self.get_serializer(data=request.data)
		if serializer.is_valid():
			data=serializer.data
			section.objects.get(pk=pk).delete()	

			return Response(status.HTTP_204_NO_CONTENT)
class LibrarieViewsets(viewsets.ModelViewSet):
	queryset=Librarie.objects.all()
	serializer_class=LibrarieSerializer

	

	def create(self,request):
		serializer=self.get_serializer(data=request.data)
		if serializer.is_valid():
			data=serializer.data
			section.objects.get_or_create(Book=data['Book'],defaults={'No_of_Books_Total':data['No_of_Books_Total'],'No_of_Books_Avilable':data['No_of_Books_Avilable'],'Of_Class':data['Of_Class'],'Of_Subject':data['Of_Subject'],'Publisher_Name':data['Publisher_Name']})
			return Response(data)
		else:
			return Response(serializer.errors)
	def get (self,request,pk,format=None):
		sec = section.objects.get(id=pk)
		serializer = self.get_serializer(data=sec)
		serializer.is_valid()
		return Response(serializer.data)

	def retrieve(self, request, pk):
		obj = self.get_object()
		return Response({obj.Name,obj.Subjects,obj.Classes})


	def update(self,request, pk):
		serializer=self.get_serializer(data=request.data)
		data = {}
		if serializer.is_valid():
			data=serializer.data
		
			obj = self.get_object()

			obj.Book = data['Book']
			obj.No_of_Books_Total=data['No_of_Books_Total']
			obj.No_of_Books_Avilable=data['No_of_Books_Avilable']
			obj.Of_Class=data['Of_Class']
			obj.Of_Subject=data['Of_Subject']
			obj.Publisher_Name=data['Publisher_Name']


			obj.save()

		return Response(data)


	def delete(self,request,pk,format=None):
		serializer=self.get_serializer(data=request.data)
		if serializer.is_valid():
			data=serializer.data
			section.objects.get(pk=pk).delete()	

			return Response(status.HTTP_204_NO_CONTENT)

		return Response(status=status.HTTP_204_NO_CONTENT)
class ParentViewsets(viewsets.ModelViewSet):
	queryset=Parent.objects.all()
	serializer_class=ParentSerializer


	def create(self,request):
		serializer=self.get_serializer(data=request.data)
		if serializer.is_valid():
			data=serializer.data
			section.objects.get_or_create(Name_of_Father=data['Name_of_Father'],Name_of_Mother=data['Name_of_Mother'],Related_Student=data['Related_Student'],defaults={'Contacts':data['Contacts'],'Address_current':data['Address_current'],'Address_permanent':data['Address_permanent']})
			return Response(data)
		else:
			return Response(serializer.errors)
	def get (self,request,pk,format=None):
		sec = section.objects.get(id=pk)
		serializer = self.get_serializer(data=sec)
		serializer.is_valid()
		return Response(serializer.data)

	def retrieve(self, request, pk):
		obj = self.get_object()
		return Response({obj.Name_of_Father,obj.Name_of_Mother,obj.Related_Student})


	def update(self,request, pk):
		serializer=self.get_serializer(data=request.data)
		data = {}
		if serializer.is_valid():
			data=serializer.data
		
			obj = self.get_object()

			obj.Name_of_Father = data['Name_of_Father']
			obj.Name_of_Mother=data['Name_of_Mother']
			obj.Related_Student=data['Related_Student']
			obj.Address_current=data['Address_current']
			obj.Address_permanent=data['Address_permanent']
			obj.Contacts=data['Contacts']

			obj.save()

		return Response(data)


	def delete(self,request,pk,format=None):
		serializer=self.get_serializer(data=request.data)
		if serializer.is_valid():
			data=serializer.data
			section.objects.get(pk=pk).delete()	

			return Response(status.HTTP_204_NO_CONTENT)
class SubjectViewsets(viewsets.ModelViewSet):
	queryset=Subject.objects.all()
	serializer_class=SubjectSerializer


	def create(self,request):
		serializer=self.get_serializer(data=request.data)
		if serializer.is_valid():
			data=serializer.data
			section.objects.get_or_create(Name=data['Name'],defaults={'Class':data['Class'],'Teacher':data['Teacher'],'Book':data['Book']})
			return Response(data)
		else:
			return Response(serializer.errors)
	def get (self,request,pk,format=None):
		sec = section.objects.get(id=pk)
		serializer = self.get_serializer(data=sec)
		serializer.is_valid()
		return Response(serializer.data)

	def retrieve(self, request, pk):
		obj = self.get_object()
		return Response({obj.Name,obj.Class,obj.Book})


	def update(self,request, pk):
		serializer=self.get_serializer(data=request.data)
		data = {}
		if serializer.is_valid():
			data=serializer.data
		
			obj = self.get_object()

			obj.Name = data['Name']
			obj.Class=data['Class']
			obj.Teacher=data['Teacher']
			obj.Book=data['Book']

			obj.save()

		return Response(data)


	def delete(self,request,pk,format=None):
		serializer=self.get_serializer(data=request.data)
		if serializer.is_valid():
			data=serializer.data
			section.objects.get(pk=pk).delete()	

			return Response(status.HTTP_204_NO_CONTENT)

	
class ExamViewsets(viewsets.ModelViewSet):
	queryset=Exam.objects.all()
	serializer_class=ExamSerializer



	def create(self,request):
		serializer=self.get_serializer(data=request.data)
		if serializer.is_valid():
			data=serializer.data
			section.objects.get_or_create(Subject=data['Subject'],defaults={'Class':data['Class'],'Date':data['Date'],'full_marks':data['full_marks'],'pass_marks':data['pass_marks']})
			return Response(data)
		else:
			return Response(serializer.errors)
	def get (self,request,pk,format=None):
		sec = section.objects.get(id=pk)
		serializer = self.get_serializer(data=sec)
		serializer.is_valid()
		return Response(serializer.data)

	def retrieve(self, request, pk):
		obj = self.get_object()
		return Response({obj.Subject,obj.Class,obj.Date})


	def update(self,request, pk):
		serializer=self.get_serializer(data=request.data)
		data = {}
		if serializer.is_valid():
			data=serializer.data
		
			obj = self.get_object()

			obj.Subject = data['Subject']
			obj.Class=data['Class']
			obj.Date=data['Date']
			obj.full_marks=data['full_marks']

			obj.save()

		return Response(data)


	def delete(self,request,pk,format=None):
		serializer=self.get_serializer(data=request.data)
		if serializer.is_valid():
			data=serializer.data
			section.objects.get(pk=pk).delete()	

			return Response(status.HTTP_204_NO_CONTENT)
			
class AttendenceViewsets(viewsets.ModelViewSet):
	queryset=Attendence.objects.all()
	serializer_class=AttendenceSerializer

	

	def create(self,request):
		serializer=self.get_serializer(data=request.data)
		if serializer.is_valid():
			data=serializer.data
			section.objects.get_or_create(student=data['student'],defaults={'Is_Present':data['Is_Present'],'Date':data['Date']})
			return Response(data)
		else:
			return Response(serializer.errors)
	def get (self,request,pk,format=None):
		sec = section.objects.get(id=pk)
		serializer = self.get_serializer(data=sec)
		serializer.is_valid()
		return Response(serializer.data)

	def retrieve(self, request, pk):
		obj = self.get_object()
		return Response({obj.student,obj.Date,obj.Is_Present})


	def update(self,request, pk):
		serializer=self.get_serializer(data=request.data)
		data = {}
		if serializer.is_valid():
			data=serializer.data
		
			obj = self.get_object()

			obj.student = data['student']
			obj.Date=data['Date']
			obj.Is_Present=data['Is_Present']
			

			obj.save()

		return Response(data)


	def delete(self,request,pk,format=None):
		serializer=self.get_serializer(data=request.data)
		if serializer.is_valid():
			data=serializer.data
			section.objects.get(pk=pk).delete()	

			return Response(status.HTTP_204_NO_CONTENT)
class AccountingViewsets(viewsets.ModelViewSet):
	queryset=Accounting.objects.all()
	serializer_class=AccountingSerializer


	def create(self,request):
		serializer=self.get_serializer(data=request.data)
		if serializer.is_valid():
			data=serializer.data
			section.objects.get_or_create(student=data['student'],defaults={'Date_of_Transaction':data['Date_of_Transaction'],'Time_of_Transaction':data['Time_of_Transaction'],'fees_paid':data['fees_paid'],'fees_due':data['fees_due'],'status':data['status']})
			return Response(data)
		else:
			return Response(serializer.errors)
	def get (self,request,pk,format=None):
		sec = section.objects.get(id=pk)
		serializer = self.get_serializer(data=sec)
		serializer.is_valid()
		return Response(serializer.data)

	def retrieve(self, request, pk):
		obj = self.get_object()
		return Response({obj.student,obj.Date_of_Transaction,obj.fees_due,obj.status})


	def update(self,request, pk):
		serializer=self.get_serializer(data=request.data)
		data = {}
		if serializer.is_valid():
			data=serializer.data
		
			obj = self.get_object()

			obj.student = data['student']
			obj.Date_of_Transaction=data['Date_of_Transaction']
			obj.fees_paid=data['fees_paid']
			obj.fees_due=data['fees_due']
			obj.status=data['status']
			obj.Time_of_Transaction=data['Time_of_Transaction']
			

			obj.save()

		return Response(data)


	def delete(self,request,pk,format=None):
		serializer=self.get_serializer(data=request.data)
		if serializer.is_valid():
			data=serializer.data
			section.objects.get(pk=pk).delete()	