from django.shortcuts import render, get_object_or_404
from django.http import Http404

from contact.models import Contact

# Create your views here.
def index(request):

    contacts = Contact.objects.filter(show=True).order_by('-id')[10:20]

    context = {
        'contacts' : contacts,
    }

    return render(
        request,'contact/index.html', context
    )

def contact(request, contact_id):

    single_contact = Contact.objects.filter(pk=contact_id, show=True).first() # não estou utilizando get() pois ele retornaria um erro caso eu busque, na url, um valor que não exista ou um valor duplicado.

    if single_contact is None:
        raise Http404()
    
    # O trecho acima tb funcionaria assim:
    # single_contact = get_object_or_404(
    # Contact.objects.filter(pk=contact_id))
    
    # ou assim:
    # single_contact = get_object_or_404(
    # Contact.objects, pk=contact_id)

    # ou assim:
    # single_contact = get_object_or_404(
    # Contact, pk=contact_id)

    context = {
        'contact' : single_contact,
    }

    return render(
        request,'contact/contact.html', context
    )