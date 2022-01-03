from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render

from django.shortcuts import render, redirect

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import FormView, ListView

from main_app.models import Ad, Category


class BasicView(View):
    def get(self, request):
        categories = Category.objects.all()
        context = {'categories': categories}
        return render(request,'main_app/basic_view.html', context)

    def post(self, request):
        categories = request.POST.getlist('category')
        keyword = request.POST.get('keyword')
        ads_by_category = []
        for category in categories:
            filtered_ads = Ad.objects.filter(category=category)
            for ad in filtered_ads:
                ads_by_category.append(ad)

        if not keyword:
            ads = ads_by_category
        else:
            ads = []
            filtered_ads = Ad.objects.filter(content__icontains=keyword)
            for ad in filtered_ads:
                if ad in ads_by_category:
                    ads.append(ad)

        context = {'ads' : ads}
        return render(request, 'main_app/chosen_ads.html', context)



class NewAd(View):
    pass


class AllAds(ListView):
    queryset = Ad.objects.all()
    context_object_name = 'ads'
    template_name = 'main_app/chosen_ads.html'


class RemoveAd(View):
    pass

#
# class Login(View):
#     def get(self, request):
#         return render(request, 'main_app/login.html')
#
#     def post(self,request):
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         user1 = authenticate(email=email,password=password)
#         if user1:
#             login(request,user1)
#             return HttpResponseRedirect('/index/')
#         else:
#             return HttpResponseRedirect('/register/')
#
#
# class Logout(View):
#     def get(self,request):
#         return render(request, 'main_app/logout.html')
#
#     def post(self, request):
#         logout(request)
#         return HttpResponseRedirect('/index/')


# class Register(FormView):
#     template_name =
#     form_class =
#     success_url = reverse_lazy('Login')
#     def from_valid(self, form):
#         cd = form.cleaned_data
#         user = TableUser.objects.create(username=cd['username'])
#         user.set_password(cd['password'])
#         user.save()
#         return super().form_valid(form)