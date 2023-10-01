from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from .utils import get_first_image
from .utils import get_next_image

# Create your views here.
def index(request):
    template = loader.get_template('pages/index.html')
    return HttpResponse(template.render(request=request))
    
def results(request):
    template = loader.get_template('pages/results.html')
    return HttpResponse(template.render(request=request))
    
def load_first(request):
    '''
    get the first image to display
    '''
    if 'random_img_url' not in request.session:
        image_path = get_first_image()
        image_path = str(image_path)
        request.session['random_img_url'] = image_path
    else:
        image_path = request.session['random_img_url']
    
    return render(request, 'pages/index.html', {'image_path': image_path})


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