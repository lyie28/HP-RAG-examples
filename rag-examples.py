from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
)

# Import HP extract from data
documents = SimpleDirectoryReader("data").load_data()
index = VectorStoreIndex.from_documents(documents)

queries=["How many faces do teachers have?", "How do you catch a train?", "What is music used for?", "What is the purpose of a hat?"]

for x, query in enumerate(queries):
    print(f"Query {x}: {query}")
    query_engine = index.as_query_engine()
    response = query_engine.query(query)
    print(f"Response: {response}")