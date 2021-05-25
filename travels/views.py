from django.shortcuts import render, redirect
from .models import Destination
from travels.documents import DestinationDocument
from django.core.paginator import Paginator
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Q
import time
# Create your views here.




def destination(request,country,city):
        #tik = time.time()
        # dests = DestinationDocument.search().query()
        #q = {"range": {"price": {"gte": 1000,"lte": 2000}}}
        #q = {"price": {"gte": 1000, "lte": 2000}}
        #q = {"must":[]}
        #q = Q("range",query=q,fields=['city','country','price','img1'])
        q_city = {"match": {"city": city}}
        #q = {"":}
        #q = Q(q)
        #q_city = Q({"multi_match": {"query": city, "fields": ["city"]}})
        q_country = {"match": {"country": country}}
        dest = DestinationDocument.search().query(q_country).query(q_city)
        print(type(dest))

        #dest = DestinationDocument.search().query('match',**{'country':country}).query('match',**{'city':city})
        # time taken: 0.0000000000000000001
        #dest = Destination.objects.filter(city__iexact=city,country__iexact=country)
        # time taken: 0.0010008811950683594
        #print("time taken:", time.time()-tik)
        return render(request, "destinations.html", {'dests': dest})

def destination_country(request,country):
    #dest = DestinationDocument.search().query("match", country=country)
    #time take: 0.0009975433349609375
    q = Q({"match": {"country": country}})
    t = time.time()
    dest = DestinationDocument.search().query(q)
    print("time take:", time.time()-t)
    return render(request,"destinations.html", {'dests':dest})
'''
def index(request):
    #q = Q({"match_all": {}})
    #dests = DestinationDocument.search().query(q)
    #q = {
    #    "query": {
    #        "bool": {
    #        "must": []
    #        }
    #    }
    #}
    #client = Elasticsearch()
    #dests = client.search(
    #    index="dests",
    #    body = q
    #)
    #print(type(dests))
    #print(dests["hits"])
    #input()

    # budget query
    budget = {
    "query": {
        "bool": {
            "filter": [{
                "range": {
                    "price": {
                        "gte": 1000
                    },
                    "price": {
                        "lte": 2000
                    }
                }
            }]
        }
    }
}
    

    #print(type(q))
    dests = Destination.objects.all()

    #dests = Destination(dictionary=dests)
    
    countries = Destination.objects.values('country').order_by('country').distinct('country')
    cities = Destination.objects.values('city').order_by('city').distinct('city')
    country_d = []
    city_d  = []
    for count in countries:
        country_d.append(count['country'])
    for count in cities:
            city_d.append(count['city'])
    
    city, country, budgetmin, budgetmax = None, None, None, None
    try:

        if request.POST['search'] == 'true':
            city = request.POST['city']
            country = request.POST['country']
            if city == "" and country == "":
                return redirect("")
            print("got some search",city,country,budgetmin,budgetmin)
            if country != "":

                dests = dests.filter(country=country)
            if city != "":
                dests = dests.filter(city__icontains=city)
            #if budgetmax != "":
            #    dests = dests.filter(price<=int(budgetmax))
            #if budgetmin != "":
            #    dests  = dests.filter(price>=int(budgetmin))
            paginator = Paginator(dests,20)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            return render(request, "index.html", {'dests':page_obj,'dropdown_countries':[], 'dropdown_cities':[]})
    except Exception as e:
        print(e)
    
    paginator = Paginator(dests, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, "index.html", {'dests': dests,'dropdown_countries':[], 'dropdown_cities':[]})
'''

def index(request):
    dests = Destination.objects.all()

    try:
        city = request.POST['city']
        country = request.POST['country']
        budgetmin = request.POST['min']
        budgetmax = request.POST['max']
        if city == "" and country == "" and budgetmax == "" and budgetmin == "":
            return redirect("")
        print("got some search", city, country, budgetmin, budgetmin)
        if country != "":
            dests = dests.filter(country__icontains=country)
        if city != "":
            q = {"match": {"city":{"query": city,"fuzziness": 1,"prefix_length": 1}}}
            dests = DestinationDocument.search().query(q)
            for dest in dests:
                print(dest)
            #dests = dests.filter(city__icontains=city)
            print("got here")
        if budgetmax != "":
            try:
                budgetmax = int(budgetmax)
                dests = dests.filter(price__range=(0,budgetmax))
            except: pass
        if budgetmin != "":
            try:
                budgetmin = int(budgetmin)
                dests = dests.filter(price__range=(budgetmin, 10000))
            except:
                pass
        '''
        page_number = request.GET.get('page')
        paginator = Paginator(dests,20)
        page_obj = paginator.get_page(page_number)
        '''
        return render(request, "index.html", {'dests':dests})


    except Exception as e:
        print(e)
    paginator = Paginator(dests, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "index.html", {'dests': page_obj})
