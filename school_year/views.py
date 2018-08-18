from django.shortcuts import render

def index(request):
	return render(request, 'school_year/school_year_list.html')