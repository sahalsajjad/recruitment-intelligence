from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import JsonResponse
import MySQLdb as mysql
import json
# Create your views here.
class IndexView(TemplateView):
	template_name = 'index.html'
	def get_context_data(self, **kwargs):
		context = dict()
		return context  
class MSPCView(TemplateView):
	template_name = 'mspc.html'
	def get_context_data(self, **kwargs):
		context = dict()
		return context 
class CSPCView(TemplateView):
	template_name = 'cspc.html'
	def get_context_data(self, **kwargs):
		context = dict()
		return context 
class MSPCLandingView(TemplateView):
	template_name = 'mspc-landing.html'
	def get_context_data(self, **kwargs):
		context = dict()
		return context 
class CSPCLandingView(TemplateView):
	template_name = 'cspc-landing.html'
	def get_context_data(self, **kwargs):
		context = dict()
		return context 
class ResumeBuilderView(TemplateView):
	template_name = 'build-resume.html'
	def get_context_data(self, **kwargs):
		context = dict()
		return context 
class CreatePostingView(TemplateView):
	template_name = 'create-posting.html'
	def get_context_data(self, **kwargs):
		context = dict()
		return context 

class EditPostingView(TemplateView):
	template_name = 'edit-posting.html'
	def get_context_data(self, **kwargs):
		context = dict()
		return context 

class RankView(TemplateView):
	template_name = 'rank.html'
	def get_context_data(self, **kwargs):
		context = dict()
		return context 

def GetITView(request):
		db = mysql.connect(host="localhost", user="root", passwd="iiits_12345", db="onet")        
		cur = db.cursor()
		cur.execute("SELECT DISTINCT career_pathway FROM it_careers")
		json_data = { "data":[]}
		for i in cur.fetchall():
			json_data['data'].append(i[0])
		db.close()
		return JsonResponse(json.dumps(json_data), safe=False)

def GetSubProfession(request):
		q = request.GET['q']

		print q.replace("%20"," ")
		db = mysql.connect(host="localhost", user="root", passwd="iiits_12345", db="onet")        
		cur = db.cursor()
		cur.execute("""SELECT DISTINCT occupation FROM it_careers WHERE career_pathway = \'"""+str(q)+"\'")
		json_data = { "data":[]}
		for i in cur.fetchall():
			print i
			json_data['data'].append(i[0])
		db.close()
		return JsonResponse(json.dumps(json_data), safe=False)
	


