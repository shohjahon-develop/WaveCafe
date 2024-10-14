from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from cafe.forms import ContactForms, CommentForm
from cafe.models import Ice,Hot,Fruit,About,Contact,Item


# Create your views here.

def index(request):
    ice = Ice.objects.all()
    items = Item.objects.all()
    hots = Hot.objects.all()
    fruite = Fruit.objects.all()
    abouts = About.objects.all()
    contact = ContactForms(request.POST or None)
    if request.method == "POST" and contact.is_valid():
        contact.save()
        return HttpResponse("<h2> MA'LUMOTLAR MUVOFIQYIATLI YUBORILDI QO'NG'IROQNI KUTING  !!! <h2/> ")
    context = {
        'ice':ice,
        'items':items,
        'hots':hots,
        'fruite':fruite,
        'abouts':abouts
    }
    return render(request,'index.html',context)





def icedetailview(request, slug):
    ice = get_object_or_404(Ice ,slug=slug)
    comments = ice.comments.filter(active=True)
    new_comment = None
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.ice = ice
            new_comment.user = request.user
            new_comment.save()

    else:
        comment_form = CommentForm()
    context = {
        "ice": ice,
        'comments': comments,
        "new_comment": new_comment,
        "comment_form": comment_form
    }

    return render(request,"ice_Detail.html",context=context)

def hotdetailview(requset,slug):
    hot = get_object_or_404(Hot,slug=slug)
    context = {
        'hot':hot
    }
    return render(requset,"hot_Detail.html",context=context)


def fruitdetailview(requset,slug):
    fruit = get_object_or_404(Fruit,slug=slug)
    context = {
        'fruit':fruit
    }
    return render(requset,"fruit_Detail.html",context=context)



def aboutdetailview(requset,slug):
    about = get_object_or_404(About,slug=slug)
    context = {
        'about':about
    }
    return render(requset,"about_Detail.html",context=context)


def itemdetailview(requset,slug):
    item = get_object_or_404(Item,slug=slug)
    context = {
        'item':item
    }
    return render(requset,"item_Detail.html",context=context)

















































































