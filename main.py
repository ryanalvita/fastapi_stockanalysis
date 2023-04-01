import uvicorn
from fastapi import FastAPI

import router

app = FastAPI(
    title="Stock Analysis API",
    version="0.0.1",
    contact={
        "name": "Ryan Alvita",
        "email": "ryanalvita@gmail.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)

origins = ["*"]

app.add_middleware(
    CORS,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
