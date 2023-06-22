from django.views import generic

from portfolio import services


class WorkList(generic.ListView):
    model = services.models.Work

    def get_queryset(self):
        return services.work_all()


class WorkDetail(generic.DetailView):
    model = services.models.Work
