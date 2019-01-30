import re

pattern = r"(\w)+:(\d+)"
s = "张:1994,李:1995"

#直接用ｒｅ调用
# l = re.findall(pattern,s)
# print(l)

#compile对象调用
regex = re.compile(pattern)
l = regex.findall(s,pos=0,endpos=8)
print(l)


l = re.split(r'\s+',"Hello    world nihao   Kitty")
print(l)


s = re.sub(r'\s+','##',"hello world  nihao Kitty",2)
print(s)

s = re.subn(r'\s+','##',"hello world  nihao Kitty",2)
print(s)

#####