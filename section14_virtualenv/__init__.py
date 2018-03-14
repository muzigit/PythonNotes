# virtualenv:是用来给一个应用创建一个独立的python运行环境

# 使用步骤:
# 1.用pip安装virtualenv：
# $ pip3 install virtualenv

# 2.创建目录
# Mac:~ michael$ mkdir myproject
# Mac:~ michael$ cd myproject/
# Mac:myproject michael$

# 3.创建一个独立的Python运行环境，命名为venv：
# Mac:myproject michael$ virtualenv --no-site-packages venv
# Using base prefix '/usr/local/.../Python.framework/Versions/3.4'
# New python executable in venv/bin/python3.4
# Also creating executable in venv/bin/python
# Installing setuptools, pip, wheel...done.

# 4.有了venv这个Python环境，可以用source进入该环境：
# Mac:myproject michael$ source venv/bin/activate
# (venv)Mac:myproject michael$

# 完成环境安装 可以正常安装第三包
# (venv)Mac:myproject michael$ pip install jinja2
# ...
# Successfully installed jinja2-2.7.3 markupsafe-0.23
# (venv)Mac:myproject michael$ python myapp.py
# ...

# 退出当前venv环境,使用deactivate命令：
# (venv)Mac:myproject michael$ deactivate
# Mac:myproject michael$

# 在windows中使用virtualenv:  https://www.cnblogs.com/chaosimple/p/4475958.html
