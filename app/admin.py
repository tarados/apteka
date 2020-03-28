from django.contrib import admin
from django.conf import settings
import os
import json
from django.core.files import File
from app.models import Product, Pharmacy, Order, OrderItem


class OrderItemInline(admin.TabularInline):
	model = OrderItem
	extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
	list_display = ("date", "pharmacy", "total_price", "customer_name", "customer_surname", "customer_phone", "status")
	list_filter = ("status",)
	inlines = [
		OrderItemInline,
	]

	def save_model(self, request, obj, form, change):
		result = Order.objects.get(id=obj.id)
		print(result)
		# file_name = "order.json"
		# path_file = os.path.join(settings.MEDIA_ROOT, file_name)
		# with open(file_name, "w") as write_file:
		# 	json.dump(result, write_file)
		obj.save()


admin.site.register(Product)
admin.site.register(Pharmacy)
# admin.site.register(Order, OrderAdmin)
