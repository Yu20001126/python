# 通过占位形式拼接字符串
name = "Jack"
message = "my name is %s" % name
print(message)
tel = 400000
message = "my name is %s,my tel is %s" % (name, tel)
print(message)
# python中 %s,%d,%f都可以占位
message = "my name is %s,my tel is %d" % (name, tel)
