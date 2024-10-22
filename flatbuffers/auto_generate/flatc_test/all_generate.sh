#!/bin/bash

# 配列の定義
array=(
sample01
sample02
sample03
sample04
sample05
sample06
sample07
sample08
sample09
sample10
sample11
sample12
sample13
sample14
sample15
sample16
sample17
sample18
sample19
sample20
sample21
sample100
sample101
sample102
sample103
sample104
sample105
sample106
sample107
sample108
sample109
sample110
sample111
sample112
sample113
sample114
sample115
)

# 配列の要素をループで取り出す
for element in "${array[@]}"
do
  ./generate.sh "$element"
done