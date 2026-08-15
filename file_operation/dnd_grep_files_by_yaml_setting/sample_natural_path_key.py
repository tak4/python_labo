import re
from pathlib import PurePosixPath

def natural_path_key(path_like):
    if isinstance(path_like, str):
        path_text = path_like.replace("\\", "/")
        path = PurePosixPath(path_text)
    else:
        path = PurePosixPath(path_like.as_posix())

    key = []
    for part in path.parts:
        m = re.search(r'(?i)(N)(\d+)', part)
        if m:
            prefix, number = m.groups()
            key.append((prefix or "", int(number), part.lower()))
        else:
            key.append(("", 0, part.lower()))
    return tuple(key)

records = [
    r'log_a\a_test_01.txt:1:test_str_a*',
    r'log_a\N1\a_test_01.txt:1:test_str_a*',
    r'log_a\N2\a_test_01.txt:1:test_str_a*',
    r'log_a\N3\a_test_01.txt:1:test_str_a*',
    r'log_a\test_1.log:5:Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:',
    r'log_b\test_2.log:21:The precise terms and conditions for copying, distribution and modification follow.',
    r'log_b\test_2.log:58:All rights granted under this License are granted for the term of copyright on the Program, and are irrevocable provided the stated conditions are met. This License explicitly affirms your unlimited permission to run the unmodified Program. The output from running a covered work is covered by this License only if the output, given its content, constitutes a covered work. This License acknowledges your rights of fair use or other equivalent, as provided by copyright law.',
    r'log_b\test_2.log:60:You may make, run and propagate covered works that you do not convey, without conditions so long as your license otherwise remains in force. You may convey covered works to others for the sole purpose of having them make modifications exclusively for you, or provide you with facilities for running those works, provided that you comply with the terms of this License in conveying all material for which you do not control copyright. Those thus making or running the covered works for you must do so exclusively on your behalf, under your direction and control, on terms that prohibit them from making any copies of your copyrighted material outside their relationship with you.',
    r'log_b\test_2.log:62:Conveying under any other circumstances is permitted solely under the conditions stated below. Sublicensing is not allowed; section 10 makes it unnecessary.',
    r'log_b\test_2.log:78:You may convey a work based on the Program, or the modifications to produce it from the Program, in the form of source code under the terms of section 4, provided that you also meet all of these conditions:',
    r'log_b\test_2.log:81:b) The work must carry prominent notices stating that it is released under this License and any conditions added under section 7. This requirement modifies the requirement in section 4 to “keep intact all notices”.',
    r'log_b\test_2.log:109:“Additional permissions” are terms that supplement the terms of this License by making exceptions from one or more of its conditions. Additional permissions that are applicable to the entire Program shall be treated as though they were included in this License, to the extent that they are valid under applicable law. If additional permissions apply only to part of the Program, that part may be used separately under those permissions, but the entire Program remains governed by this License without regard to the additional permissions.',
    r'log_b\test_2.log:169:If conditions are imposed on you (whether by court order, agreement or otherwise) that contradict the conditions of this License, they do not excuse you from the conditions of this License. If you cannot convey a covered work so as to satisfy simultaneously your obligations under this License and any other pertinent obligations, then as a consequence you may not convey it at all. For example, if you agree to terms that obligate you to collect a royalty for further conveying from those to whom you convey the Program, the only way you could satisfy both those terms and this License would be to refrain entirely from conveying the Program.',
    r'log_b\test_2.log:179:Each version is given a distinguishing version number. If the Program specifies that a certain numbered version of the GNU General Public License “or any later version” applies to it, you have the option of following the terms and conditions either of that numbered version or of any later version published by the Free Software Foundation. If the Program does not specify a version number of the GNU General Public License, you may choose any version ever published by the Free Software Foundation.',
    r'log_b\test_2.log:211:<program> Copyright (C) <year> <name of author> This program comes with ABSOLUTELY NO WARRANTY; for details type `show w’. This is free software, and you are welcome to redistribute it under certain conditions; type `show c’ for details.',
]

# for record in sorted(records, key=lambda r: natural_pasam       th_key(r.split(":")[0])):
#     print(record)


print(natural_path_key(records[1]))