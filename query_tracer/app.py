from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from query_tracer.api.config import Tags

app = FastAPI(
    description='Query Tracer API',
    servers=[{'url': 'http://localhost:8001'}],
    contact={'email': 'max@rokitsky.ru'},
    openapi_tags=[
        {
            'name': Tags.REQUEST_RECORD,
            'description': 'Operations with Requests',
        },
    ],
)
origins = [
    '*',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)
