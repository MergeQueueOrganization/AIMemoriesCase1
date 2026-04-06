from rest_framework.decorators import api_view


@api_view(["GET", "POST"])
def snippet_list(request):
    tainted = request.GET["query"]

    # ruleid: tainted-code-stdlib-django
    eval(tainted)
