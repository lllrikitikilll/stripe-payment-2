import stripe
from django.http import JsonResponse, HttpRequest
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from stripe_payment.config import STRIPE_SECRET_KEY, STRIPE_PUBLIC_KEY

from payment_app.models import Order, Item

stripe.api_key = STRIPE_SECRET_KEY
YOUR_DOMAIN = 'http://127.0.0.1:8000'
# Create your views here.
class CreateCheckoutOrderSessionView(View):
    def get(self, request: HttpRequest, *args, **kwargs):
        order = Order.objects.get(id=self.kwargs['pk'])
        if order.discount:
            coupon = stripe.Coupon.create(
                                        duration="repeating",
                                        duration_in_months=order.discount.duration_in_months,
                                        percent_off=order.discount.percent_dis,
            )
        else:
            coupon = None
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': item.currency,
                        'unit_amount': item.price,
                        'product_data': {
                            'name': item.name,
                        },
                    },
                    'quantity': 1,
                } for item in order.items.all()],
            metadata={
                "product_id": order.id
            },
            mode='payment',
            discounts=[{
                'coupon': coupon.id}],
            success_url=YOUR_DOMAIN + '/success/',
            cancel_url=YOUR_DOMAIN + '/cancel/',
        )



        return JsonResponse({'id': checkout_session.id})


class CreateCheckoutItemSessionView(View):
    def get(self, request: HttpRequest, *args, **kwargs):
        item = Item.objects.get(id=self.kwargs['pk'])
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': item.currency,
                        'unit_amount': item.price,
                        'product_data': {
                            'name': item.name,
                        },
                    },
                    'quantity': 1,
                }],
            metadata={
                "product_id": item.id
            },
            mode='payment',
            success_url=YOUR_DOMAIN + '/success/',
            cancel_url=YOUR_DOMAIN + '/cancel/',
        )
        return JsonResponse({'id': checkout_session.id})

class OrderIndexPageView(TemplateView):
    template_name = "order.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order'] = Order.objects.get(pk=self.kwargs['pk']).items.all()
        context['order_id'] = self.kwargs['pk']
        context['public_key'] = STRIPE_PUBLIC_KEY
        return context


class ItemIndexPageView(TemplateView):
    template_name = "item.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['item'] = Item.objects.get(pk=self.kwargs['pk'])
        context['public_key'] = STRIPE_PUBLIC_KEY
        return context