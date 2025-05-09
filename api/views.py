from django.http import JsonResponse

def authors_view(request):
    autores = [
        {"nombre": "Manuel Jose Cardozo Vanegas ", "codigo": "303159"},
        {"nombre": "Amy Jeanine Nossa Ramirez", "codigo": "296077"},
	{"nombre": "Esteban David Hernandez Parra", "codigo": "307597"},
    ]
    return JsonResponse({"autores": autores})

