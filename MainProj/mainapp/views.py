from django.views.generic import ListView, DetailView, CreateView
from .models import TelegrafModel
from .forms import MainForm
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import MainSerializer


class AllEntries(APIView):
    '''List of all entries'''
    def get(self, request):
        entries = TelegrafModel.objects.all()
        serializer = MainSerializer(entries, many=True)
        return Response(serializer.data)


class OneEntry(APIView):
    '''One entry'''
    def get(self, request, uri):
        entry = TelegrafModel.objects.get(uri=uri)
        serializer = MainSerializer(entry)
        return Response(serializer.data)


class List(ListView):
    model = TelegrafModel
    template_name = 'mainapp/list.html'
    context_object_name = 'obj'
    # allow_empty = False # objects.filter() returns empty QuerySet when no match found, we can use "allow_empty" to show HTTP404

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'List of all entries'
        return context

    def get_queryset(self):
        return TelegrafModel.objects.all()


class Pub(DetailView):
    model = TelegrafModel
    template_name = 'mainapp/pub.html'
    context_object_name = 'obj'
    pk_url_kwarg = 'uri'  # otherwise need <pk:uri> or <slug:uri> in route

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = TelegrafModel.objects.get(uri=self.kwargs['uri'])
        return context

    def get_queryset(self):
        return TelegrafModel.objects.filter(uri=self.kwargs['uri'])


class Add(CreateView):
    form_class = MainForm
    template_name = 'mainapp/add.html'
    # success_url = reverse_lazy('add')
