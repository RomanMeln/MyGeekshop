from django import forms

from mainapp.models import Product
from ordersapp.models import Order, OrderItem


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class OrderItemForm(forms.ModelForm):
    price = forms.CharField(label='цена', required=False)

    class Meta:
        model = OrderItem
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

        #Оптимизация кода. Для теста я должен поставить решётку. Изменение заказов.
        self.fields['product'].queryset = Product.objects.filter(is_active=True).select_related()
            