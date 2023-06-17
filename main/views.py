from django.views import generic


class HomeView(generic.base.TemplateResponseMixin ,generic.View):
    template_name = 'main/home.html'

    def get(self, request):
        return self.render_to_response({})