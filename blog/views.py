from django.views import generic
from blog import services as blog_services


class PostList(generic.ListView):
    model = blog_services.models.Post

    def get_queryset(self):
        return blog_services.post_all().filter(visible=True)


class PostDetail(generic.DetailView):
    model = blog_services.models.Post
