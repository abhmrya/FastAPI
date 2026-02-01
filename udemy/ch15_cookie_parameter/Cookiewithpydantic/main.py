from fastapi import FastAPI, Cookie, Depends
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()

class ProductCookies(BaseModel):
    session_id: str
    preferred_category: str | None = None
    tracking_id: str | None = None


def get_product_cookies(
    session_id: Annotated[str, Cookie()],
    preferred_category: Annotated[str | None, Cookie()] = None,
    tracking_id: Annotated[str | None, Cookie()] = None,
) -> ProductCookies:
    return ProductCookies(
        session_id=session_id,
        preferred_category=preferred_category,
        tracking_id=tracking_id
    )


@app.get("/products/recommendations")
async def get_recommendations(
    cookies: Annotated[ProductCookies, Depends(get_product_cookies)]
):
    response = {"session_id": cookies.session_id}

    if cookies.preferred_category:
        response["message"] = f"Recommendation for {cookies.preferred_category} products"
    else:
        response["message"] = f"Default recommendation for session {cookies.session_id}"

    if cookies.tracking_id:
        response["tracking_id"] = cookies.tracking_id

    return response
