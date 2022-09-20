string1 = 'hello'
string2 = 'my name is '
name = 'alice'
string3 = 'my age is '
age = 17
prt = [string1 + '\n', string2, name + '\n', string3, str(age) + '\n']
print(string1 + '\n' + string2 + name + '\n' + string3 + str(age))
# 直接拼接字符串输出
print("%s\n%s%s\n%s%d" % (string1, string2, name, string3, age))
# 利用格式化进行输出
print(*prt, sep='')
# 利用列表进行输出
print(string1, string2, name, string3, str(age))
# 利用参数进行输出
