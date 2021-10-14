from django.shortcuts import render
from .forms import ImageForm

# Create your views here.
from django.http import HttpResponse
from PIL import Image

#from .models import Book

def index(request):
    #from PIL import Image
    #image1 = Image.open(r'C:\Users\Clinton Cunha\Desktop\Desktop\Weekly Activities\Week17\Django\mysite\myapp\mak.jpg')
    #im1 = image1.convert('RGB')
    #im1.save(r'C:\Users\Clinton Cunha\Desktop\Desktop\Weekly Activities\Week17\Django\mysite\myapp\mak.pdf')
    return HttpResponse("Hello, world!")

#def book_by_id(request, book_id):
#    book = Book.objects.get(pk=book_id)
    #return HttpResponse(f"Book: {book.title}, published on {book.pub_date}")
#    return render(request, 'book_details.html', {'book':book})



def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        #if form.is_valid():
            #form.save()
            # Get the current instance object to display in the template
            #img_obj = form.instance
        return HttpResponse("Your image has been saved!")
    else:
        form = ImageForm()
    return render(request, 'index.html', {'form': form})