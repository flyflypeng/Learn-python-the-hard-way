#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

sentence = ['I','Love','Python','Very','Much']
print "Before shuffle: ", sentence

# random.shuffle() 函数的乱序操作是在传入的 list 之上进行的，并没有做一个拷贝操作
random.shuffle(sentence)
print "After shuffle: ", sentence

print '*' * 10
a='123456789'
b=[1,2,3,4,5,6,7,8,9]
c=['a','b','c','d','e']
sample_a = random.sample(a,3)
sample_b = random.sample(b,3)
sample_c = random.sample(c,3)  #随机取三个元素最为一个片段返回[6,4,3]
print sample_a
print sample_b
print sample_c
print a
print b
print c    #a,b,c值不变

print '*' * 10
# for test in b,c 这句话起始可以等价于 for test in (b,c)
# 也就是是说 b,c 会被组合成一个 tuple 类型的对象，所以下面的这个循环会指向两次
# test 会被分别赋值为 b, c 
for test in b,c:
    print test

print '*' * 10
for test in b:
    print test

for test in c:
    print test