from django.shortcuts import render
from django.http import HttpResponse # 追記
from chatterbot import ChatBot # 追記
from chatterbot.ext.django_chatterbot import settings # 追記

app_name = 'sample_bot'
# Create your views here.
def home(request):
		return render (request, 'home.html')

		
def bot_response(request):
   
    chatbot = ChatBot(**settings.CHATTERBOT)

    input_data = request.POST.get('input_text')
    if not input_data:
        return HttpResponse('<h2>たいせい？それは「うんち」であっていますか？。</h2>', status=400)

    bot_response = chatbot.get_response(input_data)
    http_response = HttpResponse()
    http_response.write('{}: {}'.format(chatbot.name, bot_response))
    return http_response