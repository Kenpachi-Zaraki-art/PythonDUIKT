from django.contrib import admin
from django.urls import path

# 1. Імпортуємо нашу нову view-функцію з 'myapp'
from myapp.views import main_page_view

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # 2. Вказуємо Django, щоб на головний URL ('')
    # він викликав нашу функцію 'main_page_view'
    path('', main_page_view, name='main-page'),
]