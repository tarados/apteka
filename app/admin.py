from django.contrib import admin
from app.models import Product, Pharmacy, Order, OrderItem


class OrderItemAdmin(admin.ModelAdmin):
	list_display = ("product_name", "price", "quantity", "cost_product", "date_order", "pharmacy", "customer", "phone")

	def product_name(self, obj):
		product_name = Product.objects.get(id=obj.id).product_name
		return product_name

	def date_order(self, obj):
		date_order = Order.objects.get(id=obj.id).date
		return date_order

	def pharmacy(self, obj):
		pharmacy = Order.objects.get(id=obj.id).pharmacy
		return pharmacy.pharmacy_name

	def customer(self, obj):
		customer_name = Order.objects.get(id=obj.id).customer_name
		customer_surname = Order.objects.get(id=obj.id).customer_surname
		customer = customer_name + ' ' + customer_surname
		return customer

	def phone(self, obj):
		phone = Order.objects.get(id=obj.id).customer_phone
		return phone


class OrderAdmin(admin.ModelAdmin):
	list_display = ("date", "pharmacy_name", "total_price", "customer_name", "customer_surname", "customer_phone")

	def pharmacy_name(self, obj):
		pharmacy = Order.objects.get(id=obj.id).pharmacy
		return pharmacy.pharmacy_name


admin.site.register(Product)
admin.site.register(Pharmacy)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
