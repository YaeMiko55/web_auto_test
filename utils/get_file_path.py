import os


def get_file_path(name):
    return os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'some_file', name)


# print(get_file_path('1.png'))

'''
os.path.realpath(__file__) 返回当前文件的绝对路径
os.path.dirname(os.path.realpath(__file__)) 返回当前文件所在目录的绝对路径
os.path.dirname(os.path.dirname(os.path.realpath(__file__))) 返回当前文件所在目录的上一级目录的绝对路径
os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'file', '1.png') 
返回当前文件所在目录的上一级目录下的file目录下的1.png文件的绝对路径

realpath(__file__) 该文件绝对路径
dirname() 该文件上一级绝对路径
join(路径1, 路径2, 路径3) 拼接路径 => 路径1/路径2/路径3

'''
