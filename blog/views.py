from django.views import generic
from blog import services as blog_services


class PostDetail(generic.DetailView):
    model = blog_services.models.Post
