## This python script is used to generate a custom Sloth config file.
## Change the labels to change the annotation object,
## Parameters specifies the possible values for each parameter.
## all_labels_not_flat  



## Enter in whatever object labels you want to use here.
labels = [
    "car", 
    "var", 
]

## Enter whatever object parameters you want to use here (w/ specified levels), whether they be
#   occlusion,
#   truncation,
#   alpha,
#   etc.
parameters = [
    {   
        "name": "occluded", 
        "levels": [0,1,2,3]
    }, 
    {   
        "name":"truncated", 
        "levels": [0,1]
    }
]


## Creates a list that runs through every permutation of key possible given the parameters specified.
all_labels_not_flat = [
    [
        [
            "{0}.{1}.{2}".format(
                label,
                parameter["name"],
                level
            ) 
            for level in parameter["levels"]
        ] 
        for parameter in parameters
    ] 
    for label in labels
]


all_labels_flat = flat_list = [
    level_3_item 
    for level_1 in all_labels_not_flat 
    for level_2 in level_1 
    for level_3_item in level_2
]

## Prints all the keys produced to the console 
## (so the user can check if everything processed properly)
print("\n"+str(all_labels_flat)+"\n")


# Open the reference template, assign it to f
f = open("template.txt","r")
template = f.read()
f.close()


## Displays to the console how the keys were formatted (for easy editing.)
# print(template)
# print(template.replace("{0}", "car"))

# def template_for_key(key):

f = open("config.py", "w")
f.write("LABELS = (\n")
for label in all_labels_flat:
    ## Parses for and replaces instances of "{0}" in file
    ## template.txt by running through the cascading for loop above.
    f.write(template.replace("{0}", label))
f.write(")")

print(str(len(all_labels_flat))+" keys generated.")