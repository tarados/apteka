from django.contrib import admin
from app.models import Product, Pharmacy, Order, OrderItem


class OrderItemInline(admin.TabularInline):
	model = OrderItem
	extra = 0


class OrderAdmin(admin.ModelAdmin):
	list_display = ("date", "pharmacy", "total_price", "customer_name", "customer_surname", "customer_phone", "status")
	inlines = [
		OrderItemInline,
	]


admin.site.register(Product)
admin.site.register(Pharmacy)
admin.site.register(Order, OrderAdmin)

