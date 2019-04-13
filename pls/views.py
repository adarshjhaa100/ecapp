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
		img_str=str(base64.b64encode(station.picture.read()).decode('utf-8'))
	
		data={}
		data['id']=station.pid
		data['address']=station.address
		data['lat']=station.lat
		data['lon']=station.lon
		data['no']=station.no
		data['facilities']=b
		data['picture']=img_str
		a.append(data)
	return JsonResponse(a,safe=False)		

def searchStation(request):
	station=pollingStation.objects.get(pid=request.GET['pid'])
	x=station.fName.all()
	a=[]
	for i in x:
		a.append(i.fname)
	img_str=str(base64.b64encode(station.picture.read()).decode('utf-8'))
	data={}
	data['id']=station.pid
	data['address']=station.address
	data['lat']=station.lat
	data['lon']=station.lon
	data['no']=station.no
	data['facilities']=a
	data['picture']=img_str
	return JsonResponse(data,safe=False)

def ViewAllCandidate(request):
	candidates=Candidate.objects.all()
	a=[]
	for candidate in candidates:
		photo_str=str(base64.b64encode(candidate.photo.read()).decode('utf-8'))
		party_str=str(base64.b64encode(candidate.symbol.read()).decode('utf-8'))
		data={}
		data['name']=candidate.name
		data['photo']=candidate.photo.url
		data['party']=candidate.party
		data['symbol']=candidate.symbol.url
		data['affitavit']=candidate.affitavid
		a.append(data)
	return JsonResponse(a,safe=False)		

def getCandidate(request):
	candidate=Candidate.objects.get(party=request.GET['party'])
	photo_str=str(base64.b64encode(candidate.photo.read()).decode('utf-8'))
	party_str=str(base64.b64encode(candidate.symbol.read()).decode('utf-8'))
	data={}
	data['name']=candidate.name
	data['photo']=candidate.photo.url
	data['party']=candidate.party
	data['symbol']=candidate.symbol.url
	data['affitavit']=candidate.affitavid	
	return JsonResponse(data,safe=False)

@csrf_exempt
def getPwd(request):
	pd=pwd.objects.get(epic=request.POST['epic'])
	data={}
	data['epic']=pd.epic
	data['phone']=pd.phone
	data['pickupLat']=pd.pickupLat
	data['pickupLon']=pd.pickupLon
	data['pickupTime']=pd.pickupTime
	return JsonResponse(data,safe=False)
@csrf_exempt
def getThrd(request):
	pd=ThirdGender.objects.get(epic=request.POST['epic'])
	data={}
	data['epic']=pd.epic
	data['phone']=pd.phone
	data['pickupLat']=pd.pickupLat
	data['pickupLon']=pd.pickupLon
	data['pickupTime']=pd.pickupTime
	return JsonResponse(data,safe=False)	

def getSuggestion(request):
	text=request.GET['text']
	rating=request.GET['rating']
	m=Suggestion(text=text,rating=rating)
	m.save()
	return JsonResponse({'success':True})

def up(request):
	p=request.POST['pid']
	q=request.POST['no']
	m=pollingStation.objects.filter(pid=p).update(no=q)
	return JsonResponse({'success':True})	

def getResults(request):
	R=result.objects.all()
	a=[]
	for r in R:
		data={}
		data['candidate']=r.candidate
		data['party']=r.party
		data['votes']=r.votes
		a.append(data)	
	return JsonResponse(a,safe=False)	