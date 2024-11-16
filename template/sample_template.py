import string

# withブロック内の変数はwithブロック外でも使える
with open('./input/email_template.txt') as f:
    t = string.Template(f.read())

contents = t.substitute(name='Mike', contents='How are you?')
print(contents)
