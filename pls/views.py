from django.http import HttpResponse,JsonResponse
from . models import pollingStation,facility,Candidate,pwd,ThirdGender,Suggestion,result
import base64
from django.views.decorators.csrf import csrf_exempt

def index(request):
	return HttpResponse('yep')

def stationAll(request):
	stations=pollingStation.objects.all()
	a=[]
	for station in stations:
		x=station.fName.all()
		b=[]
		for i in x:
			b.append(i.fname)
		
		data={}
		data['name']=station.name
		data['id']=station.pid
		data['address']=station.address
		data['lat']=station.lat
		data['lon']=station.lon
		data['no']=station.no
		data['facilities']=b
		data['picture']=station.picture.url
		a.append(data)
	return JsonResponse(a,safe=False)		

def searchStation(request):
	try:
		station=pollingStation.objects.get(pid=request.GET['pid'])
	except:
		return JsonResponse({'success':False})
	x=station.fName.all()
	a=[]
	for i in x:
		a.append(i.fname)
	
	data={}
	data['name']=station.name
	data['id']=station.pid
	data['address']=station.address
	data['lat']=station.lat
	data['lon']=station.lon
	data['no']=station.no
	data['facilities']=a
	data['picture']=station.picture.url
	return JsonResponse(data,safe=False)

def ViewAllCandidate(request):
	candidates=Candidate.objects.all()
	a=[]
	for candidate in candidates:
		data={}
		data['name']=candidate.name
		data['photo']=candidate.photo.url
		data['party']=candidate.party
		data['symbol']=candidate.symbol.url
		data['affitavit']=candidate.affitavid
		a.append(data)
	return JsonResponse(a,safe=False)		

def getCandidate(request):
	try:
		candidate=Candidate.objects.get(name=request.GET['name'])
	except:
		return JsonResponse({'success':False})
	data={}
	data['name']=candidate.name
	data['photo']=candidate.photo.url
	data['party']=candidate.party
	data['symbol']=candidate.symbol.url
	data['affitavit']=candidate.affitavid	
	return JsonResponse(data,safe=False)

@csrf_exempt
def getPwd(request):
	try:
		pd=pwd.objects.get(epic=request.POST['epic'])
	except:
		return JsonResponse({'success':False})
	data={}
	data['phone']=pd.phone
	data['name']=pd.point.name
	data['address']=pd.point.address
	data['pickupLat']=pd.point.pickupLat
	data['pickupLon']=pd.point.pickupLon
	data['pickupHour']=pd.point.pickupTime.hour
	data['pickupMin']=pd.point.pickupTime.minute
	data['picture']=pd.point.picture.url
	return JsonResponse(data,safe=False)

@csrf_exempt
def getThrd(request):
	try:
		pd=ThirdGender.objects.get(epic=request.POST['epic'])
	except:
		return JsonResponse({'success':False})
	data={}
	data['phone']=pd.phone
	data['name']=pd.point.name
	data['address']=pd.point.address
	data['pickupLat']=pd.point.pickupLat
	data['pickupLon']=pd.point.pickupLon
	data['pickupHour']=pd.point.pickupTime.hour
	data['pickupMin']=pd.point.pickupTime.minute
	data['picture']=pd.point.picture.url
	return JsonResponse(data,safe=False)	
@csrf_exempt
def getSuggestion(request):
	text=request.POST['text']
	rating=request.POST['rating']
	m=Suggestion(text=text,rating=rating)
	m.save()
	return JsonResponse({'success':True})

@csrf_exempt
def up(request):
	p=request.POST['pid']
	password=request.POST['password']
	q=request.POST['no']
	try:
		m=pollingStation.objects.get(pid=p)
	except:
		return JsonResponse({'success':False})	
	
	if password==m.password:
		pollingStation.objects.filter(pid=p).update(no=q)
		return JsonResponse({'success':True})	
	return JsonResponse({'success':False})	

def getResults(request):
	c=Candidate.objects.all().order_by('-vote')
	a={}
	data={}
	data['name']=c[0].name
	data['photo']=c[0].photo.url
	data['party']=c[0].party
	data['symbol']=c[0].symbol.url
	data['votes']=c[0].vote
	data['affitavit']=c[0].affitavid	
	a=data
	b=[]
	for candidate in c:
		data={}
		data['name']=candidate.name
		data['party']=candidate.party
		data['votes']=candidate.vote
		b.append(data)
	
	return JsonResponse( {"winner":a,"results":b} ,safe=False)	