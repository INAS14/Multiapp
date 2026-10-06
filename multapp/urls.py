from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse


def home(request):
    return HttpResponse("""
    <html>
    <head>
        <title>Multi App Django</title>

        <style>
            body {
                font-family: Arial;
                text-align: center;
                background: linear-gradient(135deg, #667eea, #764ba2);
                color: white;
                padding-top: 80px;
            }

            h1 {
                font-size: 45px;
            }

            .container {
                display: flex;
                justify-content: center;
                gap: 25px;
                margin-top: 50px;
            }

            a {
                text-decoration: none;
                background: white;
                color: #667eea;
                padding: 20px 35px;
                border-radius: 15px;
                font-size: 20px;
                font-weight: bold;
            }
        </style>
    </head>

    <body>

        <h1>🚀 Multi-App Django Project</h1>

        <p>Welcome to my Django Practical 1</p>

        <div class="container">

            <a href="/accounts/">👤 Accounts</a>

            <a href="/products/">🛍️ Products</a>

            <a href="/orders/">📦 Orders</a>

        </div>

    </body>
    </html>
    """)


urlpatterns = [
    path('', home, name='home'),

    path('admin/', admin.site.urls),

    path('accounts/', include('accounts.urls')),

    path('products/', include('products.urls')),

    path('orders/', include('orders.urls')),
]