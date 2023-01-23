from django.shortcuts import render,HttpResponse,redirect
from .forms import RegistrationForm,LoginForm,UpdateForm,DeleteForm 
from .models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib import messages
from django.views import View

class Home(View):
    '''class based home'''
    def get(self, request):
        '''home get method'''
        template_name = 'home.html'
        return render(request,template_name)
    def post(self, request):
        '''home post method '''
        template_name = 'home.html'
        return render(request,template_name)

class Register(View):
    '''register class besed'''
    def get(self,request,*args,**kwargs):
        '''home page'''
        templates_name  = "register.html"
        form_class = RegistrationForm()
        return render(request,templates_name,{'form':form_class})
    # form = RegistrationForm()
    # if request.method == 'POST':
    #     form = RegistrationForm(request.POST)
    def post(self,request,*args,**kwargs):
        '''psot '''
        templates_name  = "register.html"
        form_class = RegistrationForm(request.POST  )
        if form_class.is_valid():
            form_class.user_active = False
            form_class.save()
            return redirect('home')
        else:
            return render(request,templates_name,{'form':form_class})
        # else:
        #     form = RegistrationForm()
        #     return render(request,"register.html",{'form':form})

class Login(View):
    '''login class '''
    def get (self,request):
        '''login get '''
        templates_name = 'login.html'
        form_class = LoginForm(request.POST)
        return render(request,templates_name,{'login':form_class})
    def post(self,request):
        '''login post'''
        templates_name = 'login.html'
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            return render(request,'login_home.html')
        else:
            form_class = LoginForm(request.POST)
            return render(request,templates_name,{'login':form_class})
    # def post(self,request):
    #     templates_name = 'login_home.html'
    #     if user is not None:
    #         return render(request,templates_name)
    #     else:
    #         form_class = LoginForm(request.POST)
    #         return render(request,"login.html",{'login':form_class})

# def login(request):
#     '''login view'''
#     if request.method == 'POST':
#         login_form = LoginForm(request.POST)
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)     
#         if user is not None:
#             return render(request,"login_home.html")
#         else:
#             messages.info(request,"Invalid Login Id and Password Please Enter Again")
#             return redirect("login")
#     else:
#         login_form = LoginForm()
#         return render(request,"login.html",{'login':login_form})

class ShowData(View):
    '''show user all data'''
    def get(self,request):
        '''shoe data get'''
        templates_name = 'show_data.html'
        users =User.objects.filter(is_deleted=False)
        context = {'user_data':users}
        return render (request,templates_name,context)

class Edit(View):
    '''edit user details'''
    def get(self,request,e_id):
        '''edit get data'''
        templates_name = 'edit.html'
        edit_data = User.objects.get(pk=e_id)
        form_class  = UpdateForm(instance=edit_data)
        return render(request,templates_name,context={'edit_form':form_class})

    
    def post(self,request,e_id):
        '''edit get data'''
        form_class  = UpdateForm(request.POST,instance=User.objects.get(pk=e_id))
        if form_class.is_valid():
            form_class.save()
            return redirect('show_data')
        
    # '''function base'''
# def edit(request,id):
    
#     edit_data = User.objects.get(pk=id)
#     if request.method == 'POST':
#         print("post request")
#         edit_user_form = UpdateForm(request.POST, instance=edit_data)
#         if edit_user_form.is_valid():
#             edit_user_form.save()
#             print("????save")
#             return redirect('show_data')
#     else:
#         edit_form = UpdateForm(instance=edit_data)
#         context = {'user_edit':edit_data, "edit_form":edit_form}
#         return render(request,"edit.html",context)

def delete(request,e_id):
    '''user account delete'''
    User.objects.get(id=e_id).soft_delete()

    return redirect('show_data')

class Logout(View):
    '''logout class'''y
    def get(self,request):
        '''logout function'''
        logout(request)
        messages.info(request,"Logged out successfulluy")
        return redirect('home')
