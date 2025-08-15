import logging
import httpx
from typing import List, Any

logger = logging.getLogger(__name__)


class KaitenApiClient:
    def __init__(self, base_url: str, token: str):
        self.base_url = base_url.rstrip("/")
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        self._client = httpx.AsyncClient(base_url=self.base_url, headers=self.headers)

    async def close(self):
        await self._client.aclose()

    async def _request(self, method: str, url: str, **kwargs) -> Any:
        try:
            resp = await self._client.request(method, url, **kwargs)
            resp.raise_for_status()
            logger.info(f"{method} {url} succeeded with status {resp.status_code}")
            data = resp.json()
            logger.debug(f"Response JSON: {data}")
            return data
        except httpx.HTTPStatusError as e:
            logger.error(f"HTTP error {e.response.status_code} during {method} {url}: {e.response.text}")
            raise
        except httpx.RequestError as e:
            logger.error(f"Network error during {method} {url}: {e}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error during {method} {url}: {e}")
            raise

    # Пространства
    async def spaces_list(self) -> List[Any]:
        return await self._request("GET", "/api/v1/spaces")

    async def spaces_get(self, space_id: str) -> Any:
        return await self._request("GET", f"/api/v1/spaces/{space_id}")

    async def spaces_create(self, data: dict) -> Any:
        return await self._request("POST", "/api/v1/spaces", json=data)

    async def spaces_update(self, space_id: str, data: dict) -> Any:
        return await self._request("PATCH", f"/api/v1/spaces/{space_id}", json=data)

    async def spaces_delete(self, space_id: str) -> bool:
        return await self._request("DELETE", f"/api/v1/spaces/{space_id}")

    # Доски
    async def boards_list(self, space_id: str) -> List[Any]:
        return await self._request("GET", f"/api/v1/spaces/{space_id}/boards")

    async def boards_get(self, board_id: str) -> Any:
        return await self._request("GET", f"/api/v1/boards/{board_id}")

    async def boards_create(self, space_id: str, data: dict) -> Any:
        return await self._request("POST", f"/api/v1/spaces/{space_id}/boards", json=data)

    async def boards_update(self, board_id: str, space_id: str, data: dict) -> Any:
        return await self._request("PATCH", f"/api/v1/spaces/{space_id}/boards/{board_id}", json=data)

    async def boards_delete(self, board_id: str, space_id: str) -> bool:
        try:
            resp = await self._client.request(
                method="DELETE",
                url=f"/api/v1/spaces/{space_id}/boards/{board_id}",
                json={"force": True}
            )
            resp.raise_for_status()
            logger.info(f"DELETE /spaces/{space_id}/boards/{board_id} succeeded with status {resp.status_code}")
            data = resp.json()
            logger.debug(f"Response JSON: {data}")
            return data
        except httpx.HTTPStatusError as e:
            logger.error(
                f"HTTP error {e.response.status_code} on deleting board {board_id} in space {space_id}: {e.response.text}")
            raise
        except httpx.RequestError as e:
            logger.error(f"Network error on deleting board {board_id} in space {space_id}: {e}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error on deleting board {board_id} in space {space_id}: {e}")
            raise

    # Карты
    async def cards_list(self) -> List[Any]:
        return await self._request("GET", "/api/v1/cards")

    async def cards_get(self, card_id: str) -> Any:
        return await self._request("GET", f"/api/v1/cards/{card_id}")

    async def cards_create(self, data: dict) -> Any:
        return await self._request("POST", "/api/v1/cards", json=data)

    async def cards_update(self, card_id: str, data: dict) -> Any:
        return await self._request("PATCH", f"/api/v1/cards/{card_id}", json=data)

    async def cards_delete(self, card_id: str) -> bool:
        return await self._request("DELETE", f"/api/v1/cards/{card_id}")
