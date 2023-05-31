from django.shortcuts import render,get_object_or_404
from django.db.models import Q

from .models import Catalogue
from clicommands.models import Command


def search(request,catalogue_id):

    catalogue = get_object_or_404(Catalogue, pk=catalogue_id)
    catalogue_cmds = Command.objects.all().order_by('cmd_date').filter(is_published=True,catalogue=catalogue)

    #Search 4 Keywords into command OR description:

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if len(keywords) > 0:
            catalogue_cmds = catalogue_cmds.filter(Q(command__icontains=keywords)|Q(description__icontains=keywords))
        else:
            pass

    #Search 4 tags in Tags:
    if 'tags' in request.GET:
        input_tag = request.GET['tags']
        if len(input_tag) > 0:
            catalogue_cmds = catalogue_cmds.filter(tags__name__in=[input_tag])
        else:
            pass

    context = {
        'catalogue': catalogue,
        'catalogue_cmds': catalogue_cmds,
        'values': request.GET  # pass request to configure persistent values during search

    }
    return render(request, 'catalogue/catalogue.html',context)
