from django.urls import path
from django.views.generic.base import TemplateView
#from . import views

urlpatterns = [
#    path('', views.index),
    path('', TemplateView.as_view(template_name="AboutMyself/index.html",
    	extra_context={"title": "AboutMyself",
    	"town": "Казань", 
    	"hobbies": "программирование, спорт, олимпиадное программирование, чтение(последняя прочитанная: 'Война и мир')",
        "experience": "Начинал в 7 классе с Turbo Pascal, после 2 года яндекс лицея и недавно начал заниматься олимпиадным программированием"}), 
        name='index')
]
