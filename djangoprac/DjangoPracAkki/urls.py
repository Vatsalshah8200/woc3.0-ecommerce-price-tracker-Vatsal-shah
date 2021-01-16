from django.urls import path
from . import views
urlpatterns =[
    path('', views.hello_world),
    path('amazon', views.amazon),
    path('amazonsel', views.amazonselenium),
    path('flipkart', views.flipkart),
    path('ebay', views.ebay),
]