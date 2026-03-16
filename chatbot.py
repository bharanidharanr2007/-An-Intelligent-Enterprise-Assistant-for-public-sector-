from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

knowledge = [
    "Employees get 20 annual leave days per year",
    "IT support email is it_support@company.com",
    "Company annual event is conducted every December"
]

embeddings = model.encode(knowledge)

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(np.array(embeddings))


def get_response(query):

    query_embedding = model.encode([query])

    D,I = index.search(np.array(query_embedding),1)

    return knowledge[I[0][0]]
