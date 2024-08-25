from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from langchain.schema import HumanMessage
from langchain_openai import ChatOpenAI

def ask_openai(message):
    model = ChatOpenAI(api_key=settings.OPENAI_API_KEY)
    messages = [HumanMessage(content=message)]
    response = model.invoke(messages)
    return response.content

# Create your views here.
def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)
        return JsonResponse({'message': message, 'response': response})
    return render(request, 'chatbot.html')