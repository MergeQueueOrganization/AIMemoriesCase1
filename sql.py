import ast

from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET", "POST"])
def snippet_list(request):
    query = request.GET["query"]

    result = ast.literal_eval(query)
    return Response({"result": result})
