from django.shortcuts import render

def home_view(request) :
    return render(request, 'home.html')

def my_custom_error_view_to_handle_404(request, exception):
    return render(request, 'custom_error.html', status=404)
