import os
from azure.cosmos import CosmosClient, PartitionKey

COSMOS_URL = os.getenv("COSMOS_URL")
COSMOS_KEY = os.getenv("COSMOS_KEY")
DATABASE_NAME = "NetflixCatalog"
CONTAINER_NAME = "Catalog"

client = CosmosClient(COSMOS_URL, credential=COSMOS_KEY)

# Criar banco de dados e contêiner, caso não existam
def initialize_db():
    database = client.create_database_if_not_exists(id=DATABASE_NAME)
    container = database.create_container_if_not_exists(
        id=CONTAINER_NAME,
        partition_key=PartitionKey(path="/category"),
        offer_throughput=400
    )
    return container

container = initialize_db()
