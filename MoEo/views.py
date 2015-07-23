from django.shortcuts import get_object_or_404,render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Leciono, Teksto, Vorto, Noto

def getLessonLinks(url,leciono):
	# set up links to next lessons
	previous_lesson = "<a class=\"link\" href=\"" + reverse(url,args=(leciono.id-1,)) +"\"><<</a>"
	next_lesson = "<a class=\"link\" href=\"" + reverse(url,args=(leciono.id+1,)) +"\">>></a>"
	if leciono.leciono == 1:
		previous_lesson = ''
	if not Leciono.objects.filter(pk=leciono.id+1):
		next_lesson = ""
	return (previous_lesson,next_lesson)

# index of lessons
def index(request):
	leciono_listo = Leciono.objects.order_by('leciono')
	kunteksto	= {'leciono_listo': leciono_listo}
	return render(request, 'MoEo/index.html',kunteksto)

# view a specific lesson
def lesson(request, leciono_id):
	leciono = Leciono.objects.get(pk=leciono_id)
	previous_lesson,next_lesson = getLessonLinks('moeo:lesson',leciono)
	try:
		noto = leciono.noto_set.get(leciono=leciono_id)
		noto = noto.noto.replace("\r\n","</br>")
		notoj = noto.split('</br></br>')
	except:
		notoj = ''
	# get words list and split into left and right
	vortoj = leciono.vorto_set.filter(frazo=False)
	size = vortoj.count()/2
	vortoj_left = vortoj[:size]
	vortoj_right = vortoj[size:]
	vortoj = zip(vortoj_left,vortoj_right)
	# get phrase list
	frazoj = leciono.vorto_set.filter(frazo=True)
	if frazoj:
		size = int(frazoj.count()/2)
		frazoj_left = frazoj[:size]
		frazoj_right = frazoj[size:]
		frazoj = zip(frazoj_left,frazoj_right)

	tekstoj = leciono.teksto_set.all()
	kunteksto	= {'leciono': leciono,
					'notoj': notoj,
					'vortoj': vortoj,
					'frazoj': frazoj,
					'previous': previous_lesson,
					'next': next_lesson,
					}
	return render(request, 'MoEo/moeo.html',kunteksto)

# choose a lesson to edit
def edit(request):
	leciono_listo = Leciono.objects.order_by('leciono')
	kunteksto	= {'leciono_listo': leciono_listo}
	return render(request, 'MoEo/edit.html',kunteksto)
	
# edit a specific lesson
def edit_lesson(request,leciono_id):
	# save lesson
	if request.method == 'POST':
		leciono = get_object_or_404(Leciono, pk=leciono_id)
		for tekstoNum in range(1,4):
			frazoj = request.POST['teksto'+str(tekstoNum)]
			try:
				teksto = leciono.teksto_set.get(number=tekstoNum)
			except:
				teksto = leciono.teksto_set.create(number=tekstoNum)
			# delete phrases
			frazListo = teksto.frazo_set.filter(teksto=teksto.id)
			if frazListo:
				frazListo.delete()
			# divide phrases into lines and save
			for frazo in frazoj.split('\r\n'):
				teksto.frazo_set.create(frazo=frazo,leciono_id=leciono_id)
			# save notes
			try:
				noto = leciono.noto_set.get(leciono = leciono_id)
			except:
				noto = leciono.noto_set.create()
			noto.noto = request.POST['notoj']
			noto.save()
			# delete old words
			vortListo = leciono.vorto_set.filter(leciono=leciono_id)
			if vortListo:
				vortListo.delete()
			# save vortojn
			vortoj = request.POST['vortoj']
			vorto_list = vortoj.split('\r\n')
			cxuFrazo = False
			for vorto in vorto_list:
				if vorto == "**":
					cxuFrazo = True
					continue
				vorto,rimarko,traduko = vorto.split('\t')
				leciono.vorto_set.create(vorto=vorto, rimarko=rimarko, traduko=traduko, leciono=leciono_id, frazo=cxuFrazo)
		return HttpResponseRedirect(reverse('moeo:edit_lesson',args=(leciono.id,)))
	# edit lesson
	else:
		leciono = Leciono.objects.get(pk=leciono_id)
		# set up links to next lessons
		previous_lesson,next_lesson = getLessonLinks('moeo:edit_lesson',leciono)
		
		teksto_group = leciono.teksto_set.filter(leciono=leciono_id)
		i = 0
		teksto_list = []
		for teksto in teksto_group:
			teksto_list.append('')
			for frazo in teksto.frazo_set.filter(teksto=teksto.id):
				teksto_list[i] += frazo.frazo + '\n'
			teksto_list[i] = teksto_list[i].strip('\n')
			i+=1
		# load up words
		vortoj = leciono.vorto_set.filter(leciono=leciono_id)
		vorto_list = ''
		cxuFrazo = False
		for vorto in vortoj:
			if vorto.frazo and not cxuFrazo:
				vorto_list += "**\n"
				cxuFrazo = True
			vorto_list += "{}\t{}\t{}\n".format(vorto.vorto,vorto.rimarko,vorto.traduko)
		vorto_list = vorto_list.strip('\n')
		kunteksto	= {'leciono': leciono,
						'teksto_list': teksto_list,
						'vorto_list': vorto_list,
						'previous': previous_lesson,
						'next': next_lesson,
						}
		return render(request, 'MoEo/edit_lesson.html',kunteksto)
