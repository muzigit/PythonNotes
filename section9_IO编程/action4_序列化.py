# 序列化(pickling)
# 定义:把变量从内存中变成可存储或传输的过程
# 反序列化(unpickling):
# 定义:把变量内容从序列化的对象重新读取到内存中

# python提供pickle模块来实现序列化

import pickle, os

# 示例:
# 把一个对象序列化后写入文件
d = dict(name='Bob', age=20, score=88)

# pickle.dumps():把任意对象序列化成一个bytes,然后就可以把这个bytes写入文件
print(pickle.dumps(d))
# 输出:b'\x80\x03}q\x00(X\x04\x00\x00\x00nameq\x01X\x03\x00\x00\x00Bobq\x02X\x03\x00\x00\x00ageq\x03K\x14X\x05\x00\x00\x00scoreq\x04KXu.'

# pickle.dump():直接把对象序列化后写入file-like object
f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()

# 将对象从磁盘中读取到内存中
f = open('dump.txt', 'rb')
d = pickle.load(f)
print(d)  # 输出:{'name': 'Bob', 'age': 20, 'score': 88}
f.close()

# Json
# 使用json进行数据传输

# 示例:利用python内置模块json 将python对象转换成json
import json

# dumps()方法返回一个str 内容就是标准的json
jsonStr = json.dumps(d)
print(jsonStr)  # 输出:{"name": "Bob", "age": 20, "score": 88}

# 将json反序列化成python对象
pythonObject = json.loads(jsonStr)
print(pythonObject)  # 输出:{'name': 'Bob', 'age': 20, 'score': 88}


# Json进阶
# 对class 的序列化 与 反序列化

# 示例:
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    # 将class的实例 序列化json 需要专门写一个转换函数
    def student2dict(self, std):
        return {
            'name': std.name,
            'age': std.age,
            'score': std.score

        }

        # 将json反序列成class对象的转换函数


def dict2student(d):
    return Student(d['name'], d['age'], d['score'])


s = Student('Tom', 20, 88)
# 再将转换函数 传入dumps()方法中
print(json.dumps(s, default=s.student2dict))  # 输出:{"name": "Tom", "age": 20, "score": 88}

# 为了简化每次在新的class实例都写转化函数  可以将任意class的实例变成dict
jsonStr = json.dumps(s, default=lambda obj: obj.__dict__)
print(jsonStr)  # 输出:{"name": "Tom", "age": 20, "score": 88}

# 把json反序列成Student对象
print(json.loads(jsonStr, object_hook=dict2student))  # 输出:<__main__.Student object at 0x102a831d0>


# 练习:
# 对中文进行JSON序列化时，json.dumps()提供了一个ensure_ascii参数，观察该参数对结果的影响：
obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=False)
s1 = json.dumps(obj, ensure_ascii=True)

print(s)  # 输出:{"name": "小明", "age": 20}
print(s1)  # 输出:{"name": "\u5c0f\u660e", "age": 20}
