from django.shortcuts import render, redirect


# Create your views here.
from frame.clientdb import ClientDB
from frame.error import ErrorCode


def index(request):
    return render(request, 'index.html')

def according(request):
    return render(request, 'according.html')

def ace_code_editor(request):
    return render(request, 'ace-code-editor.html')

def add_post(request):
    return render(request, 'add-post.html')

def alert(request):
    return render(request, 'alert.html')

def animate(request):
    return render(request, 'animate.html')

def AOS(request):
    return render(request, 'AOS.html')

def avatars(request):
    return render(request, 'avatars.html')

def base_input(request):
    return render(request, 'base-input.html')

def basic_card(request):
    return render(request, 'basic-card.html')

def basic_template(request):
    return render(request, 'basic-template.html')

def blog(request):
    return render(request, 'blog.html')

def blog_single(request):
    return render(request, 'blog-single.html')

def bookmark(request):
    return render(request, 'bookmark.html')

def bootstrap_basic_table(request):
    return render(request, 'bootstrap-basic-table.html')

def bootstrap_border_table(request):
    return render(request, 'bootstrap-border-table.html')

def bootstrap_notify(request):
    return render(request, 'bootstrap-notify.html')

def box_layout(request):
    return render(request, 'box-layout.html')


def login(request):
    return render(request, 'login.html')
def login_bs_tt_validation(request):
    return render(request, 'login-bs-tt-validation.html')
def login_bs_validation(request):
    return render(request, 'login-bs-validation-layout.html')
def login_sa_validation(request):
    return render(request, 'login-sa-validation.html')
def login_one(request):
    return render(request, 'login_one.html')
def login_two(request):
    return render(request, 'login_two.html')
def loginimpl(request):
    email = request.POST['email']
    pwd = request.POST['pwd']
    # ㅡㅡㅡㅡㅡㅡㅡㅡㅡ 여기까진 ok
    try:
        client = ClientDB().selectOne(pwd, email)
        if pwd == client.getPwd():
            request.session['logininfo'] = {'id': client.getId(), 'name': client.getName(), 'pwd': client.getPwd(),
                                            'email': client.getEmail()}
            print(request.session['logininfo'])
            return redirect('index')
        else:
            raise Exception
    except:
        context = {'msg': ErrorCode.e02}
        return render(request,'login_two.html' , context)

def logout(request):
    if request.session['logininfo'] != None:
        del request.session['logininfo']
    return redirect('index')

def forget_password(request):
    return render(request, 'forget-password.html')
def sign_up(request):
    return render(request, 'sign-up.html')
def sign_up_one(request):
    return render(request, 'sign-up-one.html')
def sign_up_two(request):
    return render(request, 'sign-up-two.html')
def signupimpl(request):
    try:
        email = request.POST['email']
        pwd = request.POST['pwd']
        name = request.POST['name']
        phone_num = request.POST['phone_num']
        ClientDB().insert(pwd, name, email, phone_num)
        return render(request, 'login_two.html')
    except Exception as err:
        print(err)
        context = {'msg': ErrorCode.e03}
        return render(request, 'sign-up.html', context)

def search(request):
    return render(request, 'search.html')

def general_widget(request):
    return render(request, 'general-widget.html')

def update(request):
    pwd = request.session['logininfo']['pwd']
    email = request.session['logininfo']['email']
    print(pwd, email)
    client = ClientDB().selectOne(pwd, email)
    context = {'client': client}
    return render(request, 'update.html', context)
def infoupdate(request):
    try:
        email = request.POST['email']
        pwd = request.POST['pwd']
        name = request.POST['name']
        phone_num = request.POST['phone_num']
        ClientDB().update(pwd, name, phone_num, email)
        return redirect('index')
    except Exception as err:
        print('에러:', err)
        context= {'msg': ErrorCode.e03}
        return render(request, 'update.html', context)

