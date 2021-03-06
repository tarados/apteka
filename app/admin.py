from django.contrib import admin
from django.core.mail import send_mail
from import_export import resources
from django.conf import settings
from import_export.admin import ImportExportModelAdmin
from app.models import Product, Pharmacy, Order, OrderItem


class OrderItemInline(admin.TabularInline):
	model = OrderItem
	extra = 0


class OrderItemResource(resources.ModelResource):
	class Meta:
		model = OrderItem


def make_published(modeladmin, request, queryset):
	queryset.update(status='2')
	for i in range(len(queryset)):
		order_id = queryset[i].id
		message = settings.ORDER_URL + str(order_id)
		send_mail(
			'Subject here',
			message,
			'lith2009@mail.ru',
			['zvadaserg@yandex.ru', 'zvada53@gmail.com'],
			fail_silently=False,
		)


make_published.short_description = "Отправить в аптеку"


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
	list_display = (
	"idOrder", "date", "pharmacy", "total_price", "customer_name", "customer_surname", "customer_phone", "status")
	list_filter = ("status",)
	inlines = [
		OrderItemInline,
	]
	actions = [make_published]

	def idOrder(self, obj):
		return 'Заказ № %s' % str(obj.id)

	idOrder.short_description = "Номер заказа"

	def save_model(self, request, obj, form, change):
		obj.save()


class OrderItemAdmin(ImportExportModelAdmin):
	resource_class = OrderItemResource


admin.site.register(Product)
admin.site.register(Pharmacy)
admin.site.register(OrderItem, OrderItemAdmin)
