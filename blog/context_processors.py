from blog import services


def tags(request):
    return {
        'tags': services.tag_all()
    }


def rubrics(request):
    return {
        'rubrics': services.rubric_all()
    }
