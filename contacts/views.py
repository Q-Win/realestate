from django.shortcuts import render, redirect

def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
    return
