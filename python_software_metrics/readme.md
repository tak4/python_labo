# Flake8

## offcial
https://flake8.pycqa.org/en/latest/

## github
https://github.com/pycqa/flake8
https://github.com/Melevir/flake8-cognitive-complexity

## PyPi
https://pypi.org/project/flake8/
https://pypi.org/project/flake8-cognitive-complexity/

## output

flake8 --max-cognitive-complexity=0 target_software_metrics.py

target_software_metrics.py:4:1: CCR001 Cognitive complexity is too high (2 > 0)
target_software_metrics.py:4:1: E302 expected 2 blank lines, found 1
target_software_metrics.py:10:1: CCR001 Cognitive complexity is too high (3 > 0)
target_software_metrics.py:10:1: E302 expected 2 blank lines, found 1
target_software_metrics.py:18:1: CCR001 Cognitive complexity is too high (1 > 0)
target_software_metrics.py:18:1: E302 expected 2 blank lines, found 1
target_software_metrics.py:19:4: E111 indentation is not a multiple of 4
target_software_metrics.py:22:1: E302 expected 2 blank lines, found 1
target_software_metrics.py:23:4: E111 indentation is not a multiple of 4
target_software_metrics.py:24:7: E111 indentation is not a multiple of 4
target_software_metrics.py:26:1: CCR001 Cognitive complexity is too high (4 > 0)
target_software_metrics.py:26:1: E302 expected 2 blank lines, found 1
target_software_metrics.py:27:3: E111 indentation is not a multiple of 4
target_software_metrics.py:29:3: E111 indentation is not a multiple of 4
target_software_metrics.py:32:7: E111 indentation is not a multiple of 4

# radon

## oficial
https://radon.readthedocs.io/en/latest/

## github
https://github.com/rubik/radon

## PyPi
https://pypi.org/project/radon/


## output
radon cc -a -s target_software_metrics.py

target_software_metrics.py
    F 10:0 test_function3 - A (3)
    F 26:0 calculate_average - A (3)
    F 4:0 test_function2 - A (2)
    F 18:0 test_function4 - A (2)
    F 1:0 test_function1 - A (1)
    F 22:0 test_function5 - A (1)

6 blocks (classes, functions, methods) analyzed.
Average complexity: A (2.0)
