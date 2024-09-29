import inspect
import importlib
import os
import sys
base_path = os.path.dirname(
                    os.path.dirname(
                        os.path.abspath(__file__)))
sys.path.append(base_path)
from SmartCamera import BoundingBox
from SmartCamera import BoundingBox2d
from SmartCamera import ObjectDetectionTop
import SmartCamera

modules = inspect.getmembers(SmartCamera, inspect.ismodule)
for m in modules:
    module = importlib.import_module('SmartCamera.' + m[0])
    print(module.__name__)
    classes = inspect.getmembers(module, inspect.isclass)
    for class_name, class_obj in classes:
        print(f"Class: {class_name}")
        methods = inspect.getmembers(class_obj, inspect.isfunction)
        for method_name, _ in methods:
            print(f"  Method: {method_name}")

# classes = inspect.getmembers(ObjectDetectionTop, inspect.isclass)
# for class_name, class_obj in classes:
#     print(f"Class: {class_name}")
#     methods = inspect.getmembers(class_obj, inspect.isfunction)
#     for method_name, _ in methods:
#         print(f"  Method: {method_name}")