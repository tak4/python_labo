import re

# 練習に使用するAWS Cloud Formation StackID
# https://docs.aws.amazon.com/ja_jp/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stack.html#:~:text=The%20AWS::CloudFormation::Stack%20resource%20nests%20a%20stack%20as%20a

# 正規表現をコンパイルしておく
# RE_STACK_ID = re.compile(
#     r'arn:aws:cloudformation:(?P<region>[\w-]+):(?P<account_id>[\d]+)'
#      ':stack/(?P<stack_name>[\w-]+)/[\w-]+'
# )
# 正規表現をコンパイルしておく VERBOSE
RE_STACK_ID = re.compile(r"""
                         arn:aws:cloudformation:
                         (?P<region>[\w-]+):        # region
                         (?P<account_id>[\d]+)      # account_d
                         :stack/
                         (?P<stack_name>[\w-]+)     # stack_name
                         /[\w-]+""", re.VERBOSE
)

# チェック対象文字列
s1 = ('arn:aws:cloudformation:us-east-2:123456789012:stack/'
     'mystack-mynestedstack-sggfrhxhum7w/f449b250-b969-11e0-a185-5081d0136786')
s2 = ('arn:aws:cloudformation:us-east-1:888456789012:stack/'
     'mystack-mynestedstack-sggfrhxhum8w/8889b250-b969-11e0-a185-5081d0136786')

# マッチチェック
for s in [s1, s2]:
    m = RE_STACK_ID.match(s)
    if m:
        print(m.group('region'))
        print(m.group('account_id'))
        print(m.group('stack_name'))
    else:
        raise Exception('Error!')
