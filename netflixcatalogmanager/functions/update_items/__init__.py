import azure.functions as func
import json
from ..shared_code.db_helper import container

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        item_id = req.params.get('id')
        if not item_id:
            return func.HttpResponse("ID não fornecido.", status_code=400)
        
        data = req.get_json()
        item = container.read_item(item_id, partition_key=data['category'])
        for key, value in data.items():
            item[key] = value
        container.replace_item(item=item_id, body=item)
        return func.HttpResponse("Item atualizado com sucesso!", status_code=200)
    except Exception as e:
        return func.HttpResponse(f"Erro: {str(e)}", status_code=400)
