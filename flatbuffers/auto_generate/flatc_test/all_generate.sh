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
)

# 配列の要素をループで取り出す
for element in "${array[@]}"
do
  ./generate.sh "$element"
done