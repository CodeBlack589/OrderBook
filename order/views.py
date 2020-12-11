from random import random, randint, uniform

from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
rate1=uniform(1997,2300)
rate2=uniform(1954,2300)
share={'Reliance':rate1,'IBM':rate2}
ordershares={'Reliance':{'shareno':0,'price':0.0,'avg':0.0,'Type':'Market','buy':True},'IBM':{'shareno':0,'price':0.0,'avg':0.0,'Type':'Market','buy':True}}

l1=[]
l2=[]
l3=[]
l4=[]
stoplossRsell=[]
stoplossIsell=[]
LimitRSell=[]
LimitISell=[]
sellshare={'Reliance':{'shareno':0,'price':0.0,'avg':0.0,'Type':'Market'},'IBM':{'shareno':0,'price':0.0,'avg':0.0,'Type':'Market'}}
def home(request):
    return render(request,'home.html')

def ordershare(request):
    k=ordershares['Reliance']
    l=ordershares['IBM']

    data={'share':share,'l':l1,'l2':l2,'l3':l3,'l4':l4,'share1':ordershares['Reliance'],'share2':ordershares['IBM']}
    return render(request,'ordershare.html',data)

def chnageshareprice(request):
    r=uniform(-2,3)
    s=uniform(-4,5)
    share['Reliance']=share['Reliance']+r
    share['IBM']=share['IBM']+s
    data={'p1':share['Reliance'],'p2':share['IBM']}
    return JsonResponse(data)

def order(request):
    select=request.POST.get('select')
    shareno=request.POST.get('shareno')
    sharetype1=request.POST.get('sharetype1')
    Limit=request.POST.get('Limit')
    Stop=request.POST.get('Stop')
    if select=="Reliance":
        if sharetype1=="option1":
            ordershares['Reliance']['shareno']=int(ordershares['Reliance']['shareno'])+int(shareno)
            ordershares['Reliance']['price']=ordershares['Reliance']['price']+float(shareno)*share['Reliance']
            ordershares['Reliance']['avg']=ordershares['Reliance']['price']/share['Reliance']
            ordershares['Reliance']['Type']='Market'
            ordershares['Reliance']['buy']=True
            data={
                'ordershares':'ok'
            }
            if data['ordershares']:
                data['shareno']=ordershares['Reliance']['shareno']
                data['price']=ordershares['Reliance']['price']
                data['avg']=ordershares['Reliance']['avg']
                data['market']=ordershares['Reliance']['Type']
                data['buy']=ordershares['Reliance']['buy']
                data['name']='Reliance'
            return JsonResponse(data)

        if sharetype1=="option2":
            k=len(l1)+1
            ordershares1={'Reliance':{'shareno':0,'price':0.0},'IBM':{'shareno':0,'price':0.0}}
            ordershares1['Reliance']['id']=k
            ordershares1['Reliance']['shareno']=int(ordershares1['Reliance']['shareno'])+int(shareno)
            ordershares1['Reliance']['price']=float(shareno)*share['Reliance']
            ordershares1['Reliance']['avg']=share['Reliance']
            ordershares1['Reliance']['Type']='Limit order'
            ordershares1['Reliance']['buy']=False
            ordershares1['Reliance']['Limit']=Limit
            data={
                'ordershares1':'ok'
            }
            dictionary_copy = ordershares1['Reliance']. copy()
            l1.append(dictionary_copy)
            if data['ordershares1']:
                data['key']=k
                data['shareno']=ordershares1['Reliance']['shareno']
                data['price']=ordershares1['Reliance']['price']
                data['avg']=ordershares1['Reliance']['avg']
                data['market']=ordershares1['Reliance']['Type']
                data['buy']=ordershares1['Reliance']['buy']
                data['name']='Reliance'
                data['limit']=Limit
                return JsonResponse(data)
        else:
            m=len(l2)+1
            ordershares2={'Reliance':{'shareno':0,'price':0.0},'IBM':{'shareno':0,'price':0.0}}
            ordershares2['Reliance']['id']=m
            ordershares2['Reliance']['shareno']=int(shareno)
            ordershares2['Reliance']['price']=float(shareno)*share['Reliance']
            ordershares2['Reliance']['avg']=share['Reliance']
            ordershares2['Reliance']['Type']='Stop Order'
            ordershares2['Reliance']['Stoploss']=Stop
            ordershares2['Reliance']['buy']=True
            data={
                'ordershares2':'ok'
            }
            a_copy=ordershares2['Reliance'].copy()
            l2.append(a_copy)
            if data['ordershares2']:
                data['key']=m
                data['shareno']=ordershares2['Reliance']['shareno']
                data['price']=ordershares2['Reliance']['price']
                data['avg']=ordershares2['Reliance']['avg']
                data['market']=ordershares2['Reliance']['Type']
                data['buy']=ordershares2['Reliance']['buy']
                data['name']='Reliance'
                data['stop']=ordershares2['Reliance']['Stoploss']
                return JsonResponse(data)
    elif select=="IBM":

        if sharetype1=="option1":
            ordershares['IBM']['shareno']=int(ordershares['IBM']['shareno'])+int(shareno)
            ordershares['IBM']['price']=ordershares['IBM']['price']+float(shareno)*share['IBM']
            ordershares['IBM']['avg']=ordershares['IBM']['price']/share['IBM']
            ordershares['IBM']['Type']='Market'
            ordershares['IBM']['buy']=True
            data={
                'ordershares':'ok'
            }
            if data['ordershares']:
                data['shareno']=ordershares['IBM']['shareno']
                data['price']=ordershares['IBM']['price']
                data['avg']=ordershares['IBM']['avg']
                data['market']=ordershares['IBM']['Type']
                data['buy']=ordershares['IBM']['buy']
                data['name']='IBM'
            return JsonResponse(data)

        if sharetype1=="option2":
            k=len(l3)+1
            ordershares1={'Reliance':{'shareno':0,'price':0.0},'IBM':{'shareno':0,'price':0.0}}
            ordershares1['IBM']['id']=k
            ordershares1['IBM']['shareno']=int(shareno)
            ordershares1['IBM']['price']=float(shareno)*share['IBM']
            ordershares1['IBM']['avg']=share['IBM']
            ordershares1['IBM']['Type']='Limit order'
            ordershares1['IBM']['buy']=False
            ordershares1['IBM']['Limit']=Limit
            data={
                'ordershares1':'ok'
            }
            dictionary_copy = ordershares1['IBM']. copy()
            l3.append(dictionary_copy)
            if data['ordershares1']:
                data['key']=k
                data['shareno']=ordershares1['IBM']['shareno']
                data['price']=ordershares1['IBM']['price']
                data['avg']=ordershares1['IBM']['avg']
                data['market']=ordershares1['IBM']['Type']
                data['buy']=ordershares1['IBM']['buy']
                data['name']='IBM'
                data['limit']=Limit
                return JsonResponse(data)
        else:
            m=len(l4)+1
            ordershares2={'Reliance':{'shareno':0,'price':0.0},'IBM':{'shareno':0,'price':0.0}}
            ordershares2['IBM']['id']=m
            ordershares2['IBM']['shareno']=int(shareno)
            ordershares2['IBM']['price']=float(shareno)*share['IBM']
            ordershares2['IBM']['avg']=share['IBM']
            ordershares2['IBM']['Type']='Stop Order'
            ordershares2['IBM']['Stoploss']=Stop
            ordershares2['IBM']['buy']=True
            data={
                'ordershares2':'ok'
            }
            a_copy=ordershares2['IBM'].copy()
            l4.append(a_copy)
            if data['ordershares2']:
                data['key']=m
                data['shareno']=ordershares2['IBM']['shareno']
                data['price']=ordershares2['IBM']['price']
                data['avg']=ordershares2['IBM']['avg']
                data['market']=ordershares2['IBM']['Type']
                data['buy']=ordershares2['IBM']['buy']
                data['name']='IMB'
                data['stop']=ordershares2['IBM']['Stoploss']
                return JsonResponse(data)

def checkbuy(request):
    k=ordershares['Reliance']
    m=ordershares['IBM']
    Rshareno=k['shareno']
    Ishareno=m['shareno']
    Iprice=m['price']
    Rprice=k['price']
    Iavg=m['avg']
    Ravg=k['avg']
    a={}
    b={}
    c={}
    d={}
    z=0
    p=0
    len1=len(l1)
    len2=len(l2)
    len3=len(l3)
    len4=len(l4)
    for i in l1:
       if float(i['Limit'])>=share['Reliance'] and i['buy']==False:
           i['buy']=True

    for i in l3:
       if float(i['Limit'])>=share['IBM'] and i['buy']==False:
           i['buy']=True

    for i in l2:
        if float(i['Stoploss'])>share['Reliance']:
            stoplossRsell.append(i)
            del l2[p]
        p=p+1

    for i in l4:
        if float(i['Stoploss'])>share['IBM']:
            stoplossIsell.append(i)
            del l4[z]
        z=z+1
    data={'done':'done'}
    if data['done']:
        data['Rshareno']=Rshareno
        data['Ishareno']=Ishareno
        data['Rprice']=Rprice
        data['Iprice']=Iprice
        data['Ravg']=Ravg
        data['Iavg']=Iavg
    return JsonResponse(data)

def sellproduct(request):
    k=sellshare['Reliance']
    l=sellshare['IBM']

    data={'share':share,'sh1':ordershares['Reliance'],'sh2':ordershares['IBM'],'l11':l1,'l22':l2,'l33':l3,'l44':l4,'l':stoplossRsell,'l2':stoplossIsell,'l3':LimitRSell,'l4':LimitISell,'share1':sellshare['Reliance'],'share2':sellshare['IBM']}
    return render(request,'sellshare.html',data)

def sellmarketshare(request):
    if request.method=="POST":
        no=request.POST.get('no')
        btn=request.POST.get('but')
        if btn=="Reliance":
            if int(ordershares['Reliance']['shareno'])<=int(no):
                no=int(ordershares['Reliance']['shareno'])
            ordershares['Reliance']['shareno']=ordershares['Reliance']['shareno']-int(no)
            ordershares['Reliance']['price']=float(ordershares['Reliance']['price'])-float(ordershares['Reliance']['avg'])*float(no)
            ordershares['Reliance']['avg']=float(ordershares['Reliance']['price'])/float(no)
            sellshare['Reliance']['shareno']=int(sellshare['Reliance']['shareno'])+int(no)
            sellshare['Reliance']['price']=float(sellshare['Reliance']['price'])+float(no)*share['Reliance']
            sellshare['Reliance']['avg']=float(sellshare['Reliance']['price'])/float(sellshare['Reliance']['shareno'])
        if btn=="IBM":

            if int(ordershares['IBM']['shareno'])<=int(no):
                no=int(ordershares['IBM']['shareno'])
            ordershares['IBM']['shareno']=ordershares['IBM']['shareno']-int(no)
            ordershares['IBM']['price']=float(ordershares['IBM']['price'])-float(ordershares['IBM']['avg'])*float(no)
            ordershares['IBM']['avg']=float(ordershares['IBM']['price'])/float(no)
            sellshare['IBM']['shareno']=int(sellshare['IBM']['shareno'])+int(no)
            sellshare['IBM']['price']=float(sellshare['IBM']['price'])+float(no)*share['IBM']
            sellshare['IBM']['avg']=float(sellshare['IBM']['price'])/float(sellshare['IBM']['shareno'])
    return redirect('order:sellshare')

def sellLimitshare(request,id):
    if request.method=="POST":
        ordershares1={'Reliance':{'shareno':0,'price':0.0},'IBM':{'shareno':0,'price':0.0}}
        no=request.POST.get('no')
        btn=request.POST.get('but')
        if btn=="Reliance":
            i=l1[int(id)-1]
            print(i)
            if int(i['shareno'])<=int(no):
                no=int(i['shareno'])
            i['shareno']=int(i['shareno'])-int(no)
            i['price']=float(i['shareno'])*i['avg']
            i['avg']=float(i['shareno'])/float(no)
            i['Type']='Limit'
            i['Limit']=i['Limit']
            i['buy']=True
            ordershares1['Reliance']['id']=id
            ordershares1['Reliance']['shareno']=int(ordershares1['Reliance']['shareno'])+int(no)
            ordershares1['Reliance']['price']=float(no)*share['Reliance']
            ordershares1['Reliance']['avg']=share['Reliance']
            ordershares1['Reliance']['Type']='Limit order'
            ordershares1['Reliance']['buy']=True
            ordershares1['Reliance']['Limit']=i['Limit']
            dictionary_copy = ordershares1['Reliance']. copy()
            LimitRSell.append(dictionary_copy)
            if int(i['shareno'])<=int(no):
                del l1[int(id)-1]
        else:
            i=l3[int(id)-1]
            if int(i['shareno'])<=int(no):
                no=int(i['IBM']['shareno'])
            i['shareno']=int(i['shareno'])-int(no)
            i['price']=float(i['shareno'])*i['avg']
            i['avg']=float(i['shareno'])/float(no)
            i['Type']='Limit'
            i['Limit']=i['Limit']
            i['buy']=True
            ordershares1['IBM']['id']=id
            ordershares1['IBM']['shareno']=int(no)
            ordershares1['IBM']['price']=float(no)*share['IBM']
            ordershares1['IBM']['avg']=share['IBM']
            ordershares1['IBM']['Type']='Limit order'
            ordershares1['IBM']['buy']=True
            ordershares1['IBM']['Limit']=i['Limit']
            dictionary_copy = ordershares1['IBM']. copy()
            LimitISell.append(dictionary_copy)
            if int(i['shareno'])<=int(no):
                del l3[int(id)-1]
    return redirect('order:sellshare')


def sellStopshare(request,id):
    if request.method=="POST":
        ordershares2={'Reliance':{'shareno':0,'price':0.0},'IBM':{'shareno':0,'price':0.0}}

        no=request.POST.get('no')
        btn=request.POST.get('but')
        if btn=="Reliance":
            i=l2[int(id)-1]
            if int(i['shareno'])<=int(no):
                no=int(i['shareno'])
            i['shareno']=int(i['shareno'])-int(no)
            i['price']=float(i['shareno'])*i['avg']
            i['avg']=float(i['shareno'])/float(no)
            i['Type']='Stop Order'
            i['Stoploss']=i['Stoploss']
            i['buy']=True
            ordershares2['Reliance']['id']=id
            ordershares2['Reliance']['shareno']=int(no)
            ordershares2['Reliance']['price']=float(no)*share['Reliance']
            ordershares2['Reliance']['avg']=share['Reliance']
            ordershares2['Reliance']['Type']='Stop Order'
            ordershares2['Reliance']['Stoploss']=i['Stoploss']
            ordershares2['Reliance']['buy']=True
            a_copy=ordershares2['Reliance'].copy()
            stoplossRsell.append(a_copy)
            if int(i['shareno'])<=int(no):
                del l2[int(id)-1]
        else:
            i=l4[int(id)-1]
            if int(i['shareno'])<=int(no):
                no=int(i['shareno'])
            i['shareno']=int(i['shareno'])-int(no)
            i['price']=float(i['shareno'])*i['avg']
            i['avg']=float(i['shareno'])/float(no)
            i['Type']='Stop Order'
            i['Stoploss']=i['Stoploss']
            i['buy']=True
            ordershares2['IBM']['id']=id
            ordershares2['IBM']['shareno']=int(no)
            ordershares2['IBM']['price']=float(no)*share['IBM']
            ordershares2['IBM']['avg']=share['IBM']
            ordershares2['IBM']['Type']='Stop Order'
            ordershares2['IBM']['Stoploss']=i['Stoploss']
            ordershares2['IBM']['buy']=True
            a_copy=ordershares2['IBM'].copy()
            stoplossIsell.append(a_copy)
            if int(i['shareno'])<=int(no):
                del l4[int(id)-1]
    return redirect('order:sellshare')
