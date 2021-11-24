from django.shortcuts import render
from django.views import View
from calculations.ldap_search import get_names_by_net_id


class About(View):
    context = {}

    def get(self, request):
        return render(request, 'loader/about.html', self.context)

class Home(View):
    context = {}

    def get(self, request):

        num_visits = request.session.get('num_visits', 0)
        print(num_visits)
        request.session['num_visits'] = num_visits + 1
        try:
            if '\\' in request.user.username:
                search_user = request.user.username.split('\\')[1]
            else:
                search_user = request.user.username
            search_res = get_names_by_net_id(search_user)
            text_name = f'{search_res["name"]} {search_res["surname"]}'
            self.context['text_name'] = text_name
        except Exception:
            pass

        return render(request, 'loader/home.html', self.context)


def home(request):

    num_visits = request.session.get('num_visits', 0)
    print(num_visits)
    request.session['num_visits'] = num_visits + 1
    context = {}
    try:
        if '\\' in request.user.username:
            search_user = request.user.username.split('\\')[1]
        else:
            search_user = request.user.username
        search_res = get_names_by_net_id(search_user)
        text_name = f'{search_res["name"]} {search_res["surname"]}'
        context['text_name'] = text_name
    except Exception:
        pass
    return render(request, 'loader/home.html', context)
