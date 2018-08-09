import json
jsonInput = {}
with open("daptationJSONfile.json", "r") as f:
    inputData = f.read()
    jsonInput = json.loads(inputData)

jsonOutput = []

def typeFromClass(classString):
    return classString.split('.')[0]

def parameterTypeAndLevelFromClass(classString):
    components = classString.split('.')
    return (components[1], components[2])

def bboxFromAnnotation(annotationObject):
    bbox = {}
    bbox['x1'] = annotationObject['x']
    bbox['y1'] = annotationObject['y']
    bbox['x2'] = annotationObject['x'] + annotationObject['width']
    bbox['y2'] = annotationObject['y'] + annotationObject['height']
       
    return bbox

def outputForInputImage(imageObject):
    return [outputForAnnotation(annotation) for annotation in imageObject['annotations']]

def outputForAnnotation(annotationObject):
    
    parameter_index_map = {}
    parameter_index_map['occluded'] = 1
    parameter_index_map['truncated'] = 2
    # output = [type, truncated, occluded, alpha, bbox, dc1, dc1, dc1, dc2, dc2, dc2, dc3, dc4]
    
    annotation_class = annotationObject['class']
    (annotation_parameter, annotation_level) = parameterTypeAndLevelFromClass(annotationObject['class'])
    bbox = bboxFromAnnotation(annotationObject)
    output = [typeFromClass(annotation_class), 0, 0, 0, bbox['x1'], bbox['y1'], bbox['x2'], bbox['y2'], 0, 0, 0, 0, 0, 0, 0, 0]
    output[parameter_index_map[annotation_parameter]] = int(annotation_level)

    return output

output = [outputForInputImage(image) for image in jsonInput]
# print(outputForInputImage(jsonInput[0]))
# print(output)
outputjson = json.dumps(output, indent=2)
with open('output.json','w') as f:
    f.write(outputjson)