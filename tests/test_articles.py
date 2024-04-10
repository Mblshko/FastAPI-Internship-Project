from httpx import AsyncClient


async def test_create_articles(client: AsyncClient):
    response = await client.post(
        "/articles",
        json={
            "title": "title",
            "content": "content",
            "is_published": True,
        },
    )
    assert response.status_code == 201
