from django.http import HttpResponse
from django.shortcuts import render
from DjangoPracAkki.amazonselenium import script
from DjangoPracAkki.flipkartselenium import flipkartscript
from DjangoPracAkki.ebayselenium import ebayscript


def hello_world(request):
    return render(request, 'home.html')
def amazon(request):
    return render(request, 'amazon.html')
def flipkart(request):
    return render(request, 'flipkart.html')
def ebay(request):
    return render(request, 'ebay.html')
def flipkartselenium(request):
    if request.method == 'GET':
        link = request.GET.get('Link')
        price = request.GET.get('price')
        email = request.GET.get('email')
        flipkartscript(link, price, email)
        html = "<html><body>Thank you</body></html>"
        return HttpResponse(html)
    else:
        html2="<html><body>Failed!</body></html>"
        return HttpResponse(html2)
def ebayselenium(request):
    if request.method == 'GET':
        link = request.GET.get('Link')
        price = request.GET.get('price')
        email = request.GET.get('email')
        ebayscript(link, price, email)
        html = "<html><body>Thank you</body></html>"
        return HttpResponse(html)
    else:
        html2="<html><body>Failed!</body></html>"
        return HttpResponse(html2)
def amazonselenium(request):
    if request.method == 'GET':
        link = request.GET.get('Link')
        price = request.GET.get('price')
        email = request.GET.get('email')
        script(link, price, email)
        html = "<html><body>Thank you</body></html>"
        return HttpResponse(html)
    else:
        html2="<html><body>Failed!</body></html>"
        return HttpResponse(html2)
# Create your views here.

# def script(link, price, email):
#     field_names = ['link', 'price', 'email',
#                    'new_price']
#     dictcsv = {'link': link, 'price': price, 'email': email, 'new_price': price}
#     with open('amazon.csv', 'a') as f_object:
#         dictwriter_object = csv.DictWriter(f_object, fieldnames=field_names)
#         dictwriter_object.writerow(dictcsv)
#         f_object.close()

# def script(link, price, email):
#     rows = [[',',link, price, email, price]]
#     filename = "D:\woc python\djangoprac\DjangoPracAkki\amazon.csv"
#     with open(filename, 'a') as csvfile:
#         csvwriter = csv.writer(csvfile)
#         # csvwriter.writerow(fields)
#         csvwriter.writerows(rows)
