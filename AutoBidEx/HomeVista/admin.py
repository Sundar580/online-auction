from django.contrib import admin
from . models import UserModel,CarModel,CartModel,bids,Biddings

# Register your models here.
admin.site.register(UserModel)
admin.site.register(CarModel)
admin.site.register(CartModel)
admin.site.register(bids)
admin.site.register(Biddings)