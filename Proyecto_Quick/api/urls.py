from django.urls import URLPattern, path
from .views import ProductView, UserView, ClientView, BillView, CSView, CSVUploadView

urlpatterns = [
    path('products', ProductView.as_view(), name="products"),
    path('users', UserView.as_view(), name="login"),
    path('clients', ClientView.as_view(), name="clients"),
    path('bills', BillView.as_view(), name="bills"),
    path('csv', CSView.as_view(), name="csv"),
    path('upload', CSVUploadView.as_view(), name="upload_csv")
]