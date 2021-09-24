from django.shortcuts import render
import main.similar_font as similar_font
# Create your views here.


def index(request):
    
    ls = similar_font.similar_list_top4
    
    return render(request, 'main/index.html', { 'similar_list': ls })