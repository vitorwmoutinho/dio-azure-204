import azure.functions as func
from ..shared_code.db_helper import container
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        category = req.params.get('category')
        query = "SELECT * FROM c WHERE c.category = @category" if category else "SELECT * FROM c"
        items = list(container.query_items(
            query=query,
            parameters=[{"name": "@category", "value": category}] if category else [],
            enable_cross_partition_query=True
        ))
        return func.HttpResponse(json.dumps(items), mimetype="application/json", status_code=200)
    except Exception as e:
        return func.HttpResponse(f"Erro: {str(e)}", status_code=400)
