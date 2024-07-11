from django.shortcuts import render

# Create your views here.

def example_view(request) :
    return render(request, 'test_app/example.html')

def variable_view(request) :
    
    my_var = {
        'first_name' : 'BenJamin',
        'last_name' : 'frankLin',
        'some_list' : [0,1,2,3,4,5, 29, 71, 45, 61],
        'some_dict' : { 'inside_key' : 'inside_value'}
    }
    
    return render(request, 'test_app/variable.html', context=my_var)