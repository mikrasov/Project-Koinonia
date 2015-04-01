from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic

from manager.models import Pack, Character

# Create your views here.

class PackListView(generic.ListView):
    def get_queryset(self):
        return Pack.objects.order_by('-date_created')



class PackDetailView(generic.DetailView):
    model = Pack


class PackResultsView(generic.DetailView):
    model = Pack
    template_name = 'manager/results.html'

def vote(request, pack_id):
    p = get_object_or_404(Pack, pk=pack_id)
    try:
        selected_character = p.character_set.get(pk=request.POST['character'])
    except (KeyError, Character.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'manager/pack_detail.html', {
            'pack': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_character.votes += 1
        selected_character.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('manager:results', args=(p.id,)))
