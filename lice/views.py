from django.shortcuts import render
# Create your views here.
from lice.models import License
from .forms import LicenseCreateForm
from calculations.ldap_search import get_names_by_net_id
from django.urls import reverse
from django.shortcuts import redirect
from lice.calculations.sign import sign_data_to_str
from lice.helpers import user_license_auth_check, create_user_if_not_exists
from django.contrib.auth.decorators import user_passes_test
# import mssql.base
# import mssql.compiler


def no_access(request):
    if request.method == 'POST':
        print(request.POST)
        for key in request.POST:
            if 'request_access_button' in key:
                user = request.user.username
                create_user_if_not_exists(user)

    return render(request, 'lice/no_access.html')


@user_passes_test(user_license_auth_check, login_url='/lic/no_access/')
def home(request):

    num_visits = request.session.get('num_visits', 0)
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

    queryset = License.objects.using('license').all()  # .order_by('-id')
    context['objects'] = queryset

    return render(request, 'lice/home.html', context)


@user_passes_test(user_license_auth_check, login_url='/lic/no_access/')
def license_detail_view(request, id):
    context = {}
    context['data'] = License.objects.using('license').get(id=id)

    return render(request, 'lice/license_detail.html', context)


@user_passes_test(user_license_auth_check, login_url='/lic/no_access/')
def sign_license_view(request, id):
    context = {}
    single_license = License.objects.using('license').get(id=id)
    my_license = sign_data_to_str(single_license.data)
    single_license.license = my_license
    single_license.save()
    context['data'] = single_license

    return redirect('lice:home')


@user_passes_test(user_license_auth_check, login_url='/lic/no_access/')
def license_clear_view(request, id):
    context = {}
    single_license = License.objects.using('license').get(id=id)

    single_license.license = ''
    single_license.save()
    context['data'] = single_license

    return redirect('lice:home')


@user_passes_test(user_license_auth_check, login_url='/lic/no_access/')
def license_create_view(request):
    context = {}
    form = LicenseCreateForm(request.POST or None)
    if form.is_valid():
        license_obj = License()
        license_obj.data = form.cleaned_data['data']
        license_obj.ipaddress = form.cleaned_data['ipaddress']
        license_obj.save(using='license')
        return redirect('/lic')

    context['form'] = form

    return render(request, 'lice/license_create_view.html', context)
