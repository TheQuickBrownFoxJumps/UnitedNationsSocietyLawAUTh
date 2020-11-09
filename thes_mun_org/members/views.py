from django.shortcuts import render
from .models import BoardMember
from django.views.generic import ListView


# Create your views here.

class BoardView(ListView):
    template_name = 'boardmember/board.html'
    model = BoardMember
    context_object_name = 'boardmember'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            boardmembers = self.model.objects.filter(title__icontains=query)
        else:
            boardmembers = self.model.objects.all()
        return boardmembers
