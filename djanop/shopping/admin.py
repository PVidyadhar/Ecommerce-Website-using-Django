from django.contrib import admin

# Register your models here.
from .models import Productnew,Contact,Orders,OrderUpdate

admin.site.register(Productnew)
admin.site.register(Contact)
admin.site.register(Orders)
admin.site.register(OrderUpdate)