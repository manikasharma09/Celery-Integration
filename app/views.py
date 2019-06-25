from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class BuildTrigger(APIView):
	def post(self,request):
		build_something()   #this would take 1 minute to finish
		return Response(None , status=201)
