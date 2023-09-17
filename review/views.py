from django.shortcuts import render, redirect, reverse
from .models import Review
from .forms import ReviewForm
from products.models import Product
from django.contrib.auth.decorators import login_required


# Create your views here.
from django.shortcuts import render, redirect
from django.urls import reverse


@login_required
def rate(request, id):
    product = Product.objects.get(id=id)
    form = ReviewForm(request.POST or None)

    if form.is_valid():
        user = request.user
        username = str(request.user)
        comment = request.POST.get('comment')
        rating = request.POST.get('rating')
        review = Review(user=user, product=product,
                        comment=comment, rating=rating, username=username)
        review.save()
        return redirect('success')

    context = {
        "form": form,
        "product": product
    }

    return render(request, 'review/rate.html', context)


def success(request):
    return render(request, 'review/success.html')
