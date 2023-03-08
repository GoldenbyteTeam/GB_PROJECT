from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages

# Create your views here.

from explorer.models import Explorer
from catalogue.models import Catalogue,Category,Keywords
from clicommands.models import Command

from clicommands.forms import DefineCommandForm


def index(request):
    list_explorer = Explorer.objects.all()
    catalogues = Catalogue.objects.all().order_by('category__name', 'title').filter(is_published=True)
    categories = Category.objects.all().order_by('name').filter(not_empty=True)


    context = {
        'list_explorer': list_explorer,
        'catalogues': catalogues,
        'categories': categories
    }
    return render(request, 'pages/index.html', context)

def catalogue(request, catalogue_id):
    catalogue = get_object_or_404(Catalogue, pk=catalogue_id)
    catalogue_cmds = Command.objects.all().order_by('cmd_date').filter(is_published=True,catalogue=catalogue)
    context = {
        'catalogue': catalogue,
        'catalogue_cmds': catalogue_cmds

    }
    return render(request, 'catalogue/catalogue.html',context)

def addcmd(request):
    if request.user.is_authenticated:
        form = DefineCommandForm()
        new = True
        readonly = False
        context = {
            'new': new,
            'form': form,
            'readonly':readonly
        }
        return render(request, 'catalogue/cmdref.html',context)
    else:
        messages.error(request, 'You must login to add commands!')
        return redirect('login')


def viewcmd(request,command_id):

    command = get_object_or_404(Command, pk=command_id)
    keywords = get_object_or_404(Keywords, name=command.environment)

    cmd_parsing_list = []
    for item in command.command.split(" "):
        cmd_parsing_list.append(item)

    urlref_list = []
    urlref_list.append(command.refurl_1)
    urlref_list.append(command.refurl_2)
    urlref_list.append(command.refurl_3)
    urlref_list.append(command.refurl_4)
    urlref_list.append(command.refurl_5)


    new = False
    readonly = True
    context = {
        'new': new,
        'command': command,
        'cmd_parsing_list':cmd_parsing_list,
        'keywords':keywords.keywords['keywords'],
        'color_keywords': keywords.keywords['color'],
        'readonly': readonly,
        'urlref_list':urlref_list
    }
    return render(request, 'catalogue/cmdref.html',context)

def editcmd(request,command_id):
    if request.user.is_authenticated:
        command = get_object_or_404(Command, pk=command_id)

        form = DefineCommandForm(instance=command)
        new = False
        readonly = False
        context = {
            'new': new,
            'form': form,
            'command':command,
            'readonly':readonly
        }
        return render(request, 'catalogue/cmdref.html',context)
    else:
        messages.error(request, 'You must login to edit commands!')
        return redirect('login')

def error_404_view(request, exception):
    return render(request, 'pages/404.html')
