import azure.functions as func
import json
from ..shared_code.db_helper import container

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        data = req.get_json()
        container.create_item(data)
        return func.HttpResponse("Item adicionado com sucesso!", status_code=201)
    except Exception as e:
        return func.HttpResponse(f"Erro: {str(e)}", status_code=400)
