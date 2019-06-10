from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection

#create Views for product

from .models import  Teams , Rankig , Testrankig , Ground , Stats , Runs , Playerstat

def product_detail_view(request,my_id):
	obj = Abcd.objects.get(id=my_id)
	# context={
	# 	'title': obj.title,
	# 	'description': obj.description

	# }
	context={
		'object':obj
	}

	return render(request , "Products/details.html",context)


def teams_detail(request):
	obj = Teams.objects.get(id=1)
	obj1 = Teams.objects.get(id=2)
	obj2= Teams.objects.get(id=3)
	obj3= Teams.objects.get(id=4)
	obj4= Teams.objects.get(id=5)
	obj5= Teams.objects.get(id=6)
	obj6= Teams.objects.get(id=7)
	obj7= Teams.objects.get(id=8)
	obj8= Teams.objects.get(id=9)

	# context={
	# 	'name':obj.name,
	# 	'Matches':obj.Matches,
	# 	'ranking':obj.ranking,
	# 	'players':obj.players,
	# }
	context={
		'object':obj,
		"object1":obj1,
		"object2":obj2,
		"object3":obj3,
		"object4":obj4,
		"object5":obj5,
		"object6":obj6,
		"object7":obj7,
		"object8":obj8
	}


	return render(request , "Products/teams.html",context)



def ground_detail(request):
	obj = Ground.objects.get(id=1)
	obj1 = Ground.objects.get(id=2)
	obj2= Ground.objects.get(id=3)
	obj3= Ground.objects.get(id=4)
	obj4= Ground.objects.get(id=5)
	obj5= Ground.objects.get(id=6)
	from django.db import connection, transaction;
	cursor = connection.cursor()
	cursor.execute('call abc()')
	# for result in cursor.stored_results():
	abcd=cursor.fetchall()
	for abc in abcd:
		print(abc)
	for ab in abc:
		print(ab)	
	# print(abcd)
	# obj6= Ground.objects.get(id=7)
	# obj7= Ground.objects.get(id=8)
	# obj8= Ground.objects.get(id=9)
	

	# context={
	# 	'name':obj.name,
	# 	'Matches':obj.Matches,
	# 	'ranking':obj.ranking,
	# 	'players':obj.players,
	# }
	context={
		'object':obj,
		"object1":obj1,
		"object2":obj2,
		"object3":obj3,
		"object4":obj4,
		"object5":obj5,
		"object6":ab,
		
		
		# "object6":obj6,
		# "object7":obj7,
		# "object8":obj8
	}


	return render(request , "Products/ground.html",context)
	
# def groundcount(request):

# 	return render(request , "Products/ground.html",context)
	

def moreground(request):

	obj6=Ground.objects.raw('SELECT * FROM products_ground WHERE id>6')
	context={
		"yadata":obj6
	}
	return render(request, "Products/moregrounds.html",context)


def  player(request):
    if request.method == 'POST':
        team_one =  request.POST.get('search')
        print(team_one)
        # team_two =  request.POST.get('search1')
        status = Playerstat.objects.filter(name=team_one )
        # print(status)
        if status==None :
            status = Runs.objects.filter(name=team_one)
            print("abcd")

        return render(request,"Products/playersstat.html",{"name":status})
    if request.method == 'GET':

        return render(request,'Products/playersstat.html',{})

def stat(request):
    if request.method == 'POST':
        team_one =  request.POST.get('search')
        print(team_one)
        team_two =  request.POST.get('search1')
        status = Stats.objects.filter(name=team_one , ame = team_two)
        # print(status)
        if status==None :
            status = Stats.objects.filter(name=team_one , ame = team_two)
            print("abcd")

        return render(request,"Products/stats.html",{"name":status})
    if request.method == 'GET':

        return render(request,'Products/stats.html',{})

def index(request):
    return render(request,'mysite3/login.html')


def  runs(request):
    if request.method == 'POST':
        team_one =  request.POST.get('search')
        print(team_one)
        # team_two =  request.POST.get('search1')
        status = Runs.objects.filter(name=team_one )
        # print(status)
        if status==None :
            status = Runs.objects.filter(name=team_one)
            print("abcd")

        return render(request,"Products/statspla.html",{"name":status})
    if request.method == 'GET':

        return render(request,'Products/statspla.html',{})

def index(request):
    return render(request,'mysite3/login.html')

def testrankig_detail(request):
	obj = Teams.objects.get(id=1)
	obj1 = Teams.objects.get(id=2)
	obj2= Teams.objects.get(id=3)
	obj3= Teams.objects.get(id=4)
	obj4= Teams.objects.get(id=5)
	obj5= Teams.objects.get(id=6)
	obj6= Teams.objects.get(id=7)
	obj7= Teams.objects.get(id=8)
	obj8= Teams.objects.get(id=9)
	obj9 = Testrankig.objects.get(id=1)
	obj10 = Testrankig.objects.get(id=2)
	obj11 = Testrankig.objects.get(id=3)
	obj12 = Testrankig.objects.get(id=4)
	obj13 = Testrankig.objects.get(id=5)
	obj14= Testrankig.objects.get(id=6)
	obj15 = Testrankig.objects.get(id=7)
	obj16 = Testrankig.objects.get(id=8)
	obj17 = Testrankig.objects.get(id=9)
	# context={
	# 	'name':obj.name,
	# 	'Matches':obj.Matches,
	# 	'ranking':obj.ranking,
	# 	'players':obj.players,
	# }
	context={
		'object':obj,
		"object1":obj1,
		"object2":obj2,
		"object3":obj3,
		"object4":obj4,
		"object5":obj5,
		"object6":obj6,
		"object7":obj7,
		"object8":obj8,
		"object9":obj9,
		"object10":obj10,
		"object11":obj11,
		"object12":obj12,
		"object13":obj13,
		"object14":obj14,
		"object15":obj15,
		"object16":obj16,
		"object17":obj17,
	}


	return render(request , "Products/testranking.html",context)


def rankig_detail(request):
	obj = Rankig.objects.get(id=1)
	obj1 = Rankig.objects.get(id=7)
	obj2= Rankig.objects.get(id=8)
	obj3= Rankig.objects.get(id=9)
	obj4= Rankig.objects.get(id=10)
	obj5= Rankig.objects.get(id=11)
	obj6= Rankig.objects.get(id=12)
	obj7= Rankig.objects.get(id=13)
	obj8= Rankig.objects.get(id=14)
	obj9 = Teams.objects.get(id=1)
	obj11 = Teams.objects.get(id=2)
	obj12= Teams.objects.get(id=3)
	obj13= Teams.objects.get(id=4)
	obj14= Teams.objects.get(id=5)
	obj15= Teams.objects.get(id=6)
	obj16= Teams.objects.get(id=7)
	obj17= Teams.objects.get(id=8)
	obj18= Teams.objects.get(id=9)

	# context={
	# 	'name':obj.name,
	# 	'Matches':obj.Matches,
	# 	'ranking':obj.ranking,
	# 	'players':obj.players,
	# }
	context={
		'object':obj,
		"object1":obj1,
		"object2":obj2,
		"object3":obj3,
		"object4":obj4,
		"object5":obj5,
		"object6":obj6,
		"object7":obj7,
		"object8":obj8,
		'object9':obj9,
		"object10":obj11,
		"object12":obj12,
		"object13":obj13,
		"object14":obj14,
		"object15":obj15,
		"object16":obj16,
		"object17":obj17,
		"object18":obj18
	}


	return render(request , "Products/ranking.html",context)

def product_create_view(request):
	# obj = Product.objects.get(id=2)
	form=ProductForm(request.POST or None)
	if form.is_valid():
		form.save()
	context={
			'form':form
		}

	return render(request , "Products/create.html",context)


# def product_create_view(request):
	
# 	context={
			
# 		}

# 	return render(request , "Products/create.html",context)
 