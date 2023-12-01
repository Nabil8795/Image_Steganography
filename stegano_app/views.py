from django.shortcuts import render
import stepic
from PIL import Image
# Create your views here.

def hide_text_in_image(image,text):
    data = text.encode('utf-8')
    return stepic.encode(image, data)

def index(request):
    return render(request, 'index.html')

def encryption_view(request):
    if request.method == "POST":
        text = request.POST['text']
        image_file = request.FILES['image']
        image=Image.open(image_file)
        new_image = hide_text_in_image(image,text)

    return render(request, 'encryption.html')


def decryption_view(request):
    return render(request, 'decryption.html')

