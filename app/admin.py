from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from app.models import Product, Pharmacy, Order, OrderItem


class OrderItemInline(admin.TabularInline):
	model = OrderItem
	extra = 0


class OrderItemResource(resources.ModelResource):

	class Meta:
		model = OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
	list_display = ("idOrder", "date", "pharmacy", "total_price", "customer_name", "customer_surname", "customer_phone", "status")
	list_filter = ("status",)
	list_display_links = ("pharmacy",)
	inlines = [
		OrderItemInline,
	]

	def idOrder(self, obj):
		return obj.id
	idOrder.short_description = "Номер заказа"

	def save_model(self, request, obj, form, change):
		obj.save()


class OrderItemAdmin(ImportExportModelAdmin):
	resource_class = OrderItemResource


admin.site.register(Product)
admin.site.register(Pharmacy)
admin.site.register(OrderItem, OrderItemAdmin)
