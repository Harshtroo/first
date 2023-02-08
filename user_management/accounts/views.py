from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from .forms import RegistrationForm,UpdateForm,DeleteForm,LoginForm 
from .models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib import messages
from django.views import View
from django.views.generic import TemplateView,CreateView,DeleteView,DetailView,UpdateView
from django.urls import reverse,reverse_lazy

class Home(TemplateView):
    '''class based home'''
    def get(self, request):
        '''home get method'''
        template_name = 'home.html'
        return render(request,template_name)
    def post(self, request):
        '''home post method '''
        template_name = 'home.html'
        return render(request,template_name)

class Register(CreateView):
    '''generic based register view'''
    model = User
    form_class=RegistrationForm
    template_name = "register.html"
    # success_url= reverse_lazy('/home/')
    def get_success_url(self):
        return reverse_lazy('home')

    # def register_user(self,request):
        #     return render (request,"register.html")
# class Register(View):
#     '''register class besed'''
#     def get(self,request,*args,**kwargs):
#         '''home page'''
#         templates_name  = "register.html"
#         form_class = RegistrationForm()
#         return render(request,templates_name,{'form':form_class})
#     # form = RegistrationForm()
#     # if request.method == 'POST':
#     #     form = RegistrationForm(request.POST)
#     def post(self,request,*args,**kwargs):
#         '''psot '''
#         templates_name  = "register.html"
#         form_class = RegistrationForm(request.POST  )
#         if form_class.is_valid():
#             form_class.user_active = False
#             form_class.save()
#             return redirect('home')
#         else:
#             return render(request,templates_name,{'form':form_class})
        # else:
        #     form = RegistrationForm()
        #     return render(request,"register.html",{'form':form})

class Login(CreateView):
    '''login class '''
    model = User
    form_class  = LoginForm
    template_name = "login.html"
    success_url = "logout"

    def get_success_url(self,request):
        return render (request,'login_home.html')

    # def form_valid(self,form,request):
    #     return HttpResponseRedirect(self.get_success_url())

    # def get (self,request):
    #     '''login get '''
    #     templates_name = 'login.html'
    #     form_class = LoginForm(request.POST)
    #     return render(request,templates_name,{'login':form_class})
    # def post(self,request):
    #     '''login post'''
    #     templates_name = 'login.html'
    #     username = request.POST.get('username')
    #     password = request.POST.get('password')
    #     user = authenticate(request, username=username, password=password)
    #     if user is not None:
    #         return render(request,'login_home.html')
    #     else:
    #         form_class = LoginForm(request.POST)
    #         return render(request,templates_name,{'login':form_class})
    # def post(self,request):
    #     templates_name = 'login_home.html'
    #     if user is not None:
    #         return render(request,templates_name)
    #     else:
    #         form_class = LoginForm(request.POST)
    #         return render(request,"login.html",{'login':form_class})

#''''''''function based views '''''''''''''
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

class ShowData(TemplateView):
    '''show user all data'''
    template_name = 'show_data.html'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['user_data'] =  User.objects.filter(is_deleted=False)
        return context
    # def get(self,request):
    #     '''shoe data get'''
    #     templates_name = 'show_data.html'
    #     users =User.objects.filter(is_deleted=False)
    #     context = {'user_data':users}
    #     return render (request,templates_name,context)

class Edit(DetailView,UpdateView):
    '''edit user details'''
    template_name   = 'edit.html'
    form_class = UpdateForm
    model = User
    success_url = 'show_data'
    # context_object_name = 'my_edit_form'
    # queryset = User.objects.get()

    def get(self,request,e_id,*args,**kwagrs):
        context = {}
        context['user_form'] = UpdateForm(instance=User.objects.get(id=e_id))
        return render(request,"edit.html",context)
    
    def post(self,request,e_id, *args, **kwargs):
        # context = {}
        form = self.get_form()
        form = UpdateForm(request.POST,instance=User.objects.get(id=e_id))
        if form.is_valid():
            form.save()
        return redirect('show_data')

    # def get_success_url(self):
    #     return reverse_lazy('show_data',kwargs = {'pk':self.get_object().id})

    #class based views
    # def get(self,request,pk):
    #     '''edit get data'''
    #     templates_name = 'edit.html'
    #     edit_data = User.objects.get(id=pk)
    #     form_class  = UpdateForm(instance=edit_data)
    #     return render(request,templates_name,context={'edit_form':form_class})

    # def post(self,request,e_id):
    #     '''edit get data'''
    #     form_class  = UpdateForm(request.POST,instance=User.objects.get(pk=e_id))
    #     if form_class.is_valid():
    #         form_class.save()
    #         return redirect('show_data')
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
class Delete(DeleteView):
    '''delete classs'''
    model = User
    template_name = 'delete.html'
    success_url = reverse_lazy('show_data')

    # class based views
    # def get(self,request,e_id):
    #     '''user account delete'''
    #     User.objects.get(id=e_id).soft_delete()
    #     return redirect('show_data')

class Logout(View):
    '''logout class'''
    def get(self,request):
        '''logout function'''
        logout(request)
        messages.info(request,"Logged out successfulluy")
        return redirect('home')
