from django.shortcuts import render
from django.db.models.functions import Length
from django.db.models import Q
from app.models import *
# Create your views here.
def display_topics(request):
    LOT=Topic.objects.all()
    d={'topics':LOT}
    return render(request,'display_topics.html',context=d)


def display_webpages(request):
    LOW=Webpage.objects.all()
    LOW=Webpage.objects.filter(topic_name='Cricket')
    LOW=Webpage.objects.exclude(topic_name='Cricket')
    LOW=Webpage.objects.all()[1:2:]
    LOW=Webpage.objects.all().order_by('name')
    LOW=Webpage.objects.all().order_by('-name')
    LOW=Webpage.objects.filter(name__startswith='r') 
    LOW=Webpage.objects.filter(email__endswith='.com')
    LOW=Webpage.objects.filter(name__contains='l')
    LOW=Webpage.objects.filter(name__in=('rohith','dhoni')) 
    LOW=Webpage.objects.filter(name__regex='[a-zA-Z]{5}')  
    LOW=Webpage.objects.filter(Q(topic_name='Cricket') & Q(name='dhoni'))
    LOW=Webpage.objects.filter(Q(topic_name='Cricket'))
    LOW=Webpage.objects.filter(Q(topic_name='Cricket') & Q(name='dhoni')) 
    LOW=Webpage.objects.all()
    

  
    d={'webpages':LOW}
    return render(request,'display_webpages.html',d)

def display_access(request):
    LOA=AccessRecord.objects.all()
    LOA=AccessRecord.objects.all()
    LOA=AccessRecord.objects.filter(date__gt='2021-08-11')
    LOA=AccessRecord.objects.filter(date__lt='2022-08-11')
    LOA=AccessRecord.objects.filter(date__month='21')
    LOA=AccessRecord.objects.filter(date__year__gt='2021')
    LOA=AccessRecord.objects.filter(date__month__lt='10')




    d={'access':LOA}
    return render(request,'display_access.html',d)


