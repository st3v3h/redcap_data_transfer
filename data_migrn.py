from redcap import Project

# Projects being used : "api_out" & "api_in"
api_url = ''
api_key_out = ''
api_key_in = ''

project_out = Project(api_url,api_key_out)
project_in = Project(api_url,api_key_in)

##################################################################################################################
##### This section finds the matching variable names from each project ###########################################
##################################################################################################################

# Gets field names from the metadata. NOTE: this does NOT include record_status codes. Will probably have to scrap
# this and use a dummy record from each project in order to get the status codes unless I can think of something else
field_list_out = project_out.field_names
field_list_in = project_in.field_names

# Compares fields based on a data pull from each project. Input project may need to have a dummy record (as least for
# the first import). In this case, both records have a '001' ID.
id_chk = ['001']
fields_rec_out = project_out.export_records(id_chk)
field_rec_list_out = fields_rec_out[0].keys()

fields_rec_in = project_in.export_records(id_chk)
field_rec_list_in = fields_rec_in[0].keys()

# print(fields_rec_out)
# print(field_list_in)

# Finds the matching fields between each project
intersect = set(field_rec_list_out).intersection(field_rec_list_in)
intersect = list(intersect)
print(intersect)

# Pulls the data from the record in "ids" and imports the matching fields to the new project
ids= ['002']
export_out = project_out.export_records(records=ids, fields=intersect)
# export_out = project_out.export_records(records=ids)
print(export_out)
# import_in = project_in.import_records(export_out)


##################################################################################################################
##### This section is where variable names are remapped ##########################################################
##################################################################################################################

# # Pull out the data of the record of interest
# dict_out = project_out.export_records(records=ids)
# # converts list to dictionary
# dict_out = dict_out[0]
# # dictionary of all variable the need to be remapped --> OLD:NEW
# var_remap = {'q5':'q5i','q6':'q6i','q7':'q7i'}
#
# # This removes everything from the old dictionary that isn't going to be remapped
# temp = list(dict_out.keys())
# for key in temp:
#     if key not in var_remap:
#         dict_out.pop(key,None)
#
# # This uses var_remap to rename all the remaining variables
# for oldkey, newkey in var_remap.items():
#     dict_out[newkey] = dict_out.pop(oldkey)
#
# dict_out['record_id'] = ids[0]
#
# dict_out =[dict_out]
#
# import_remap = project_in.import_records(dict_out)
#
# print(dict_out)











#--> below is from the code I was working on with Dawn

# dest_ids = ['001']
# ids = ['PNS_CMH_0014']
# forms_of_int = ['demographics']
# data = project_out.export_records(records=ids)

# for k, v in data[0].items():
#     print(k,":",v)

# project_out_vars = data[0].keys()
#
# data_in = project_in.export_records(records=dest_ids)
# project_in_vars = data_in[0].keys()
#
# vars_intersection = filter(lambda x: x in project_in_vars, project_out_vars)
#
# data = project_out.export_records(records=ids, fields=vars_intersection)
# response = project_in.import_records(data)
