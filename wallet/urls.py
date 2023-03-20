from django.urls import path
from .views import DepositFunds, Login, Register, VerifyDeposit, WalletInfo


urlpatterns = [
    path('register/', Register.as_view()),
    path('login/', Login.as_view()),
    path('wallet_info/', WalletInfo.as_view()),
    path('deposit/', DepositFunds.as_view()),
    path('deposit/verify/<str:reference>/', VerifyDeposit.as_view()),
]