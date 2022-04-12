from django.shortcuts import render
from . import translate

# Create your views here.

def translator_view(request): 
    if request.method == 'POST':
        original_text = request.POST['my_textarea']
        destinationLanguage = request.POST.get('dest_language', 'de')
        translation = translate.translateTwo(original_text, destinationLanguage )
        output = translation[0]
        language = translation[1]
        
        return render(request, 'translate.html', {'output_text' : output, 'original_text' : original_text, 'language' : language})
    else:
        return render(request, 'translate.html')