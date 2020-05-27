from django.shortcuts import render
from django.shortcuts import redirect
from . import models
from . import forms
# Create your views here.
def index(request):
    pass
    return render(request, 'login/index.html')


def login(request):
    if request.method == "POST":
        login_form = forms.UserForm(request.POST)
        message = '请检查填写的内容！'
        # 使用表单类自带的is_valid()方法一步完成数据验证工作
        if login_form.isvalid():
            # 验证成功后可以从表单对象的cleaned_data数据字典中获取表单的具体值
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
        # # 用户名密码不为空，strip方法将用户名前后无效的空格剪除
        # if username.strip() and password:
            try:
                user = models.User.objects.get(name=username)
            except:
                message = '用户不存在！'
                # return render(request, 'login/login.html', {'message': message})
                return render(request, 'login/login.html', locals())
                # Python内置locals()函数，返回当前所有的本地变量字典
                # 我们可以偷懒的将这作为render函数的数据字典参数值，就不用费劲去构造一个
                # 形如{'message': message, 'login_form': login_form}的字典了，但可能造成数据冗余降低效率

            if user.password == password:
                # print(username, password)
                return redirect('/index/')
            else:
                message = '密码不正确！'
                return render(request, 'login/login.html', locals())
        else:
            return render(request, 'login/login.html', locals())
    # 对于非POST方法发送数据时（比如GET方法请求页面），返回空的表单，让用户可以填入数据
    login_form = forms.UserForm()
    return render(request, 'login/login.html', locals())


def register(request):
    pass
    return render(request, 'login/register.html')


def logout(request):
    pass
    return redirect("/login/")