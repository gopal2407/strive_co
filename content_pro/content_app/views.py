from django.shortcuts import redirect, render
from .models import Content
from .forms import ContentForm
import datetime


def content_form(request):
    template_name = 'content_app/form.html'
    form = ContentForm()
    if request.method == 'POST':
        form = ContentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('data_url')
    context = {'form': form}
    return render(request, template_name, context)


def content_data(request):
    template_name = 'content_app/data.html'
    objs = Content.objects.all()
    context = {'objs': objs}
    return render(request, template_name, context)


def content_update(request, pk):
    obj = Content.objects.get(pk=pk)
    template_name = 'content_app/form.html'
    form = ContentForm(instance=obj)
    if request.method == 'POST':
        instance = obj
        instance.updated_at = datetime.datetime.now()
        form = ContentForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('data_url')
    context = {'form': form}
    return render(request, template_name, context)


def content_delete(request, pk):
    obj = Content.objects.get(pk=pk)
    template_name = 'content_app/delete.html'
    if request.method == 'POST':
        obj.delete()
        return redirect('data_url')
    context = {'obj': obj}
    return render(request, template_name, context)
