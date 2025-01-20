from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import GiftIdea
from .forms import GiftIdeaForm


# create a function
def buyer_view(request):
    
    content = GiftIdea.objects.filter(purchased=False)
    context = {
        'content': content
    }
    return render(request, "index.html", context=context)
def owner_view(request):
    
    content = GiftIdea.objects.all()
    context = {
        'content': content
    }
    return render(request, "owner.html", context=context)

def test(request):
    content = GiftIdea.objects.all()
    context = {
        'content': content
    }
    return render(request, "test.html", context=context)

def list_item_form(request):
    if request.method == 'POST':
        form = GiftIdeaForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("giftee_view")
        else:

            # uncomment the below line to see errors
            # in the form (if any)
            # print(form.errors)
            return redirect("list_item_form")
    else:
        context = {}
        context['form'] = GiftIdeaForm
        return render(request, "form.html", context=context)

def set_item_purchased(request, id):
    idea = GiftIdea.objects.get(id=id)
    idea.purchased = True
    idea.save()
    return redirect(buyer_view)

def edit_item(request, id):
    idea = get_object_or_404(GiftIdea, id = id)
    context ={}
    form = GiftIdeaForm(request.POST or None, instance = idea)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/self')
    
    context["form"] = form
 
    return render(request, "edit.html", context)

def delete_item(request, id):
    idea = GiftIdea.objects.get(id=id)
    idea.delete()
    
    return redirect(owner_view)