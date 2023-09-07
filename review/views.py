from django.shortcuts import render, redirect, reverse
from .models import Review
from .forms import ReviewForm
from products.models import Product


# Create your views here.
from django.shortcuts import render, redirect
from django.urls import reverse


def rate(request, id):
    product = Product.objects.get(id=id)
    form = ReviewForm(request.POST or None)

    if form.is_valid():
        user = request.user
        comment = request.POST.get('comment')
        rating = request.POST.get('rating')
        review = Review(user=user, product=product,
                        comment=comment, rating=rating)
        review.save()
        return redirect('success')

    context = {
        "form": form,
        "product": product
    }

    return render(request, 'review/rate.html', context)


def success(request):
    return render(request, 'review/success.html')
