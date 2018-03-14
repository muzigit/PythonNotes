# XML

# 操作XML的两种方式:DOM 和 SAX
# DOM解析:
#   缺点:DOM会将整个XML读入内存,解析为树,因此占用内存大,解析慢
#   优点:可以任意遍历树的节点

# SAX解析:
#   缺点:需要自己处理事件
#   优点:SAX是流模式,边读边解析,占用内存小,解析快

# 在Python中使用SAX解析非常简洁,通常
# 只需要关心start_element,end_element和char_data这三个事件:
#   1.start_element : 在读取 <a href="/">时
#   2.char_data     : 在读取python时
#   3.end_element   : 在读取</a>时

# 示例:

from xml.parsers.expat import ParserCreate


class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        print('sax:start_element:%s,attrs:%s' % (name, str(attrs)))

    def char_data(self, text):
        print('sax:char_data:%s' % text)

    def end_element(self, name):
        print('sax:end_element:%s' % name)


xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

# 测试:
handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.CharacterDataHandler = handler.char_data
parser.EndElementHandler = handler.end_element
parser.Parse(xml)
