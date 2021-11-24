# import clr
# import System
# clr.AddReference("System.DirectoryServices")


# def get_net_id_by_name_surname(name, surname):
#     searcher = System.DirectoryServices.DirectorySearcher()
#     searcher.SearchRoot = System.DirectoryServices.DirectoryEntry()
#     searcher.Filter = f"(&(objectCategory=person)(objectClass=user)(givenname={name})(sn={surname}))"
#     searcher.PropertiesToLoad.Add("sAMAccountName")
#     return sorted([a for item in searcher.FindAll() for a in item.Properties['sAMAccountName']])


# def get_names_by_net_id(net_id):
#     searcher = System.DirectoryServices.DirectorySearcher()
#     searcher.SearchRoot = System.DirectoryServices.DirectoryEntry()
#     searcher.Filter = f"(&(objectCategory=person)(objectClass=user)(sAMAccountName={net_id}))"
#     props = {'givenname': 'name', 'sn': 'surname'}
#     # props = PP
#     for prop in props:
#         searcher.PropertiesToLoad.Add(prop)

#     final_result = {'net_id': net_id}
#     result_search = searcher.FindAll()
#     for result in result_search:
#         for result_property in result.Properties.PropertyNames:
#             print(result_property)
#             if result_property in props.keys():
#                 for ob in result.Properties[result_property]:
#                     final_result[props[result_property]] = ob
#     if 'surname' not in final_result.keys():
#         final_result['surname'] = ''
#     return final_result


def get_names_by_net_id(net_id):
    return {'net_id': 'test', 'name': 'test', 'surname': 'test'}
