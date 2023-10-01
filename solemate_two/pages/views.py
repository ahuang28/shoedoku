from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from .utils import get_next_image


# Create your views here.
def index(request):
    image_path = request.GET.get('image_path')
    
    context = {'image_path': image_path}
    return render(request, 'pages/index.html', context)
    
def results(request):
    template = loader.get_template('pages/results.html')
    return HttpResponse(template.render(request=request))
    
# def load_first(request):
#     '''
#     get the first image to display
#     '''
#     if 'random_img_url' not in request.session:
#         image_path = get_first_image()
#         image_path = str(image_path)
#         request.session['random_img_url'] = image_path
#     else:
#         image_path = request.session['random_img_url']
    
#     return render(request, 'pages/index.html', {'image_path': image_path})


def change_image(request,button,current_image='images/103787.3.jpg'):
    '''Changes the image based on the button pressed''' 
    if request == 'POST':
        current_image = request.POST.get('image_path')
        
    if button == 'like':
        accept = True
        
    else :
        accept = False
        
   

    new_image_path = get_next_image(accept, current_image)
    return redirect(f'/index/?image_path={new_image_path}')

    