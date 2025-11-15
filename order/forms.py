# order/forms.py
from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
	# ✅ دیگر نیازی به تعریف فیلدهای اضافی نیست

	class Meta:
		model = Order
		# ✅ تغییر: فقط فیلدهای مورد نیاز را در فرم نگه می‌داریم
		fields = ['name', 'email', 'phone']

		# ✅ برای فارسی‌سازی لیبل‌ها (اختیاری اما پیشنهادی)
		labels = {
            'name': 'نام و نام خانوادگی',
            'email': 'آدرس ایمیل',
            'phone': 'شماره تماس',
        }