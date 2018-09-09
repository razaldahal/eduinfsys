
	def create(self,request):
		serializer=self.get_serializer(data=request.data)
		if serializer.is_valid():
			data=serializer.data
			self.objects.get_or_create(serial_no=data['serial_no'],defaults={'name':data['name'],'author':data['author'],'publisher':data['publisher'],'editon':data['edition']})
			return Response(data)	
		else:
			return Response(srializer.errors)	

	def get (self,request,pk,format=None):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid()
		
		return Response(serializer.data)

			
	def retrive(self,request,pk):
		obj=self.get_object(pk=pk)
		return Response({obj.data})


	def update(self,request,pk):
		serializer=self.get_serilizer(data=request.data)
		data={}
		if serializer.is_valid():
			data=serializer.data
			obj=self.get_object()
			obj.serial_no=data['serial_no']
			obj.name=data['name']
			obj.author=data['author']
			obj.publisher=data['publisher']
			obj.editon=data['editon']
			obj.save()
		return Response(data)	
	
	def delete(self,request,pk):
		serializer=self.get_serilizer(data=request.data)
		if serializer.is_valid():
			data=serializer.data
			book.objects.get(pk=pk).delete()
		return Response(staus.HTTP_204_NO_CONTENT)
	

	def list(self, request):
		queryset = self.get_queryset()
		serializer = bookSerializer(queryset, many=True)
		return Response(serializer.data)




