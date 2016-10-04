from django.shortcuts import render
from django.views.generic import View


class IndexView(View):

    def get(self, request):
        context = 'personal/home.html'
        return render(request, context)


class ContactView(View):
    def get(self, request):
        context = 'personal/basic.html'
        content = {'content': {'If you would like to learn how this blog was made please follow '
                              'https://www.youtube.com/user/sentdex/'}}
        return render(request, context, content)
