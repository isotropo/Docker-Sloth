
labels = ["car", "var", "truck", "pedestrian", "person_sitting", "cyclist", "tram", "misc", "dont_care" ]
parameters = [{"name": "occluded", "levels": [0,1,2,3]}, {"name":"truncated", "levels": [0,1]}]


# [1,2,3]
# [[1],[2],[3]]
# [[["car.occluded", "car.occluded"], ["car.trunc", "car.trunc"]]]
# all_labels_not_flat = []
# for label in labels:
#     output_1 = []
#     for parameter in parameters:
#         output_2 = []
#         for level in parameter["level"]:
#             output_2.append("{0}.{1}.{2}".format(label,parameter["name"],level))
#         output_1.append(output_2)
#     all_labels_not_flat.append(output_1)

# array = [item for item in my_list]

# array = []
# for item in my_list:
#     array.append(item)

all_labels_not_flat = [[["{0}.{1}.{2}".format(label,parameter["name"],level) for level in parameter["levels"]] for parameter in parameters] for label in labels]
all_labels_flat = flat_list = [level_3_item for level_1 in all_labels_not_flat for level_2 in level_1 for level_3_item in level_2]
print(all_labels_flat)
f = open("template.txt","r")
template = f.read()
f.close()
# print(template)
# print(template.replace("{0}", "car"))

# def template_for_key(key):

f = open("config.py", "w")
f.write("LABELS = (\n")
for label in all_labels_flat:
    f.write(template.replace("{0}", label))
f.write(")")

print(len(all_labels_flat))