from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.views import generic
from users.forms import *
from users.models import Post
from django.contrib.auth.decorators import user_passes_test

def main_page(request):
    return render(request, "users/main_page.html")

def logout_request(request):
    logout(request)
    return redirect("login")

def contacts(request):
    return render(request, "users/contacts.html")

#def feedback(request):
#    return render(request, "users/feedback.html")

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

class PostList(generic.ListView):
    template_name = 'users/my.html'  # Шаблон для отображения списка постов
    
    def get_queryset(self):#получение записей из базы данных для вставки в форму
        # Фильтруем посты по текущему автору (текущему пользователю)
        if self.request.user.is_authenticated:
            return Post.objects.filter(author=self.request.user).order_by('-created_on')
        else: return

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PostForm()  # Добавляем форму для создания нового поста
        return context

def delete_post(request, pk): #удаление задач
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('my')

def create_post(request): # добавление задач в список
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # важная строка!
            post.save()
    return redirect('my')  # если не POST или форма невалидна

def add_feedback(request): #обработка формы обратной связи
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
        # после добавления, можно сделать редирект или другую обработку
    return redirect('contacts')

#@user_passes_test(lambda u: u.is_superuser)
def feedback_list(request):#страница с выводом обратной связи, доступна только админу
    feedbacks = Feedback_Post.objects.all().order_by('-created_on')
    return render(request, 'users/feedback_list.html', {'feedbacks': feedbacks})