# # Declare a list variable
# cities = ["Mumbai", "Thane","Kurla", "Malad", "Nashik"]
# print(cities)
# #  Print the length of the list
# print(len(cities))
#
# # Append a new city to the existing list
# cities.append("Ghatkopar")
# print(cities)
# #  Print the length of the list
# print(len(cities))
#
# # Remove an element at index '2’ from the list and print
# cities.pop(2)
# print(cities)
# print("Process_Completed")

# # Printing Country Names
# countries_and_capitals = {"India": "Delhi", "USA": "Washington_DC", "Japan": "Tokyo", "Australia": "Canberra"}
# print("Countries_Name:")
# for Countries in countries_and_capitals.keys():
#     print(Countries)
#
# # Inserting One Country and its Capital
# new_country = "Italy"
# new_capital = "Rome"
#
# countries_and_capitals[new_country] = new_capital
# print(countries_and_capitals)
#
# # Print the length of the dictionary
# print(len(countries_and_capitals))
#
# # # Remove an element from the dictionary
# countries_and_capitals.pop("USA")
# print(countries_and_capitals)
# print("Process Completed")

# Task 2
# import arcpy
# import os
#
# file_GDB_path = r"D:\Sem 3\programming for GIS 2\Assignment_2\ProProject_Practical_Two\ProProject_Practical_Two\World_data.gdb"
# fc_name = ["lakes"]
#
# for fc in fc_name:
#     fc_path = os.path.join(file_GDB_path, fc)
#     desc_obj = arcpy.Describe(fc_path)
#
#     sr_obj = desc_obj.spatialReference
#     print(sr_obj.name)
#     print(sr_obj.type)
#
# shape_type = desc_obj.shapeType
# print("The geometry type of feature class: {} is {}".format(fc, shape_type))
#
# field_list = desc_obj.fields
# for field in field_list:
#         print("The field name is {} and the type is {}".format(field.name,field.type))

# Task 3
import arcpy

raster_path = r"C:\Users\anike\Downloads\ProProject_Practical_Two\ProProject_Practical_Two\RASTER_DATA\erelev"
desc_obj = arcpy.Describe(raster_path)
print(desc_obj.bandCount)

print(desc_obj.format)

print(desc_obj.height)
print(desc_obj.width)
print(desc_obj.basename)
print("Process Completed")

