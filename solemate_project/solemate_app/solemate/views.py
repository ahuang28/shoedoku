from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .utils import get_next_image
from .utils import get_first_image


# def index(request):
#     template = loader.get_template("solemate/index.html")
#     return HttpResponse(template.render(request=request))

def results(request):
    template = loader.get_template("solemate/results.html")
    return HttpResponse(template.render(request=request))

def index(request):
    '''
    get the first image to display
    '''
    image_path = get_first_image()
    image_path = {'image_path': str(image_path)}
    return render(request, 'solemate/index.html', image_path)


def change_image(request,button,current_image):
    '''Changes the image based on the button pressed'''
    if request.method == 'POST':
        
        if button == 'accept':
            accept = True
        else :
            accept = False
        new_image_path = get_next_image(accept, current_image)
        return render(request, 'change_image.html', {'image_path': new_image_path})
    else:
        initial_image_path = get_first_image()
        return render(request, 'change_image.html', {'image_path': initial_image_path}) 