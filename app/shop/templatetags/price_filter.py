# src/app/shop/templatetags/price_filter.py

# Django dan third parties modules
from django import template 
from django.template.defaultfilters import stringfilter

register = template.Library()  

# Format harga dengan filter khusus (simbul mata uang)
@register.filter(name='format_price')
@stringfilter
def format_price(value):
	try:
		value = float(value)

		return 'Rp {:.2f}'.format(value)
	except:
		return value 


# Format harga prosentase pengurangan (xx % Off)
@register.filter(name='solde_rate')
def solde_rate(product):
	try:
		sold_price = float(product.sold_price)
		regular_price = float(product.regular_price)

		rate = ((regular_price - sold_price) / regular_price) * 100

		return f"{int(rate)} % Off"

	except Exception as err:
		# print(err)
		return f"{0} % Off"
