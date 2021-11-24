from lice.models import AppUser
from lice.calculations.ldap_search import get_names_by_net_id


def user_license_auth_check(user):
    user_search = AppUser.objects.filter(
        net_id=user.username, LicenseSignAccess=True)
    if len(user_search) > 0:
        passed = True
    else:
        passed = False
    return passed


def create_user_if_not_exists(username):
    user_found = AppUser.objects.filter(net_id=username)
    if len(user_found) == 0:
        try:
            if '\\' in username:
                search_user = username.split('\\')[1]
            else:
                search_user = username
            search_res = get_names_by_net_id(search_user)
        except Exception:
            search_res = {'name': '', 'surname': ''}
        if "name" not in search_res.keys():
            search_res["name"] = "--"
        if "surname" not in search_res.keys():
            search_res["surname"] = ""
        AppUser.objects.create(net_id=username, Name=search_res["name"], Surname=search_res["surname"],
                               Active=False, FullAccess=False, LicenseSignAccess=False)
    return user_found
