import azure.functions as func
from ..shared_code.db_helper import container

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        item_id = req.params.get('id')
        category = req.params.get('category')
        if not item_id or not category:
            return func.HttpResponse("ID ou Categoria não fornecidos.", status_code=400)
        
        container.delete_item(item=item_id, partition_key=category)
        return func.HttpResponse("Item excluído com sucesso!", status_code=200)
    except Exception as e:
        return func.HttpResponse(f"Erro: {str(e)}", status_code=400)
