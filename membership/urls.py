from django.urls import path

from .views import MembershipSelectView, PaymentView, updateTransactions

urlpatterns = [
    path('', MembershipSelectView.as_view(), name='select'),
    path('payment/', PaymentView, name='payment'),
    path('update-transaction/<subscription_id>/', updateTransactions, name='update-transaction'),
]
