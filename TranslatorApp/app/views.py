from django.shortcuts import render
from django.http import JsonResponse
from deep_translator import GoogleTranslator
# Create your views here.


def index(request):
    return render(request,"app/index.html")


def translate(request):
    if request.method=="POST":
        from_lang=request.POST['fm_lang']
        to_lang=request.POST['toLang']
        content=request.POST['con']
        translated_text = GoogleTranslator(source=from_lang, target=to_lang).translate(content)
        trans_data={"text":translated_text}
        return JsonResponse({"success":200,'content':trans_data})
   