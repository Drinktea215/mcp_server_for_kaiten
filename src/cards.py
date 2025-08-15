import logging
from mcp.server.fastmcp import Context
from typing import Any, List, Union
from httpx import HTTPStatusError, RequestError

logger = logging.getLogger(__name__)


async def cards_list(context: Context) -> List[Any]:
    client = context.request_context.lifespan_context.client
    try:
        result = await client.cards_list()
        logger.info("cards_list: Retrieved cards list")
        return result
    except HTTPStatusError as e:
        logger.error(f"cards_list HTTP error {e.response.status_code}: {e.response.text}")
        raise
    except RequestError as e:
        logger.error(f"cards_list Network error: {str(e)}")
        raise
    except Exception as e:
        logger.error(f"cards_list Unexpected error: {str(e)}")
        raise


async def cards_get(context: Context, id: Union[int, str]) -> Any:
    client = context.request_context.lifespan_context.client
    try:
        if id is not None:
            id = str(id)
        result = await client.cards_get(id)
        logger.info(f"cards_get: Retrieved card with id={id}")
        return result
    except HTTPStatusError as e:
        logger.error(f"cards_get HTTP error {e.response.status_code}: {e.response.text}")
        raise
    except RequestError as e:
        logger.error(f"cards_get Network error: {str(e)}")
        raise
    except Exception as e:
        logger.error(f"cards_get Unexpected error: {str(e)}")
        raise


async def cards_create(context: Context, data: dict) -> Any:
    client = context.request_context.lifespan_context.client
    try:
        result = await client.cards_create(data)
        logger.info("cards_create: Created new card")
        return result
    except HTTPStatusError as e:
        logger.error(f"cards_create HTTP error {e.response.status_code}: {e.response.text}")
        raise
    except RequestError as e:
        logger.error(f"cards_create Network error: {str(e)}")
        raise
    except Exception as e:
        logger.error(f"cards_create Unexpected error: {str(e)}")
        raise


async def cards_update(context: Context, id: Union[int, str], data: dict) -> Any:
    client = context.request_context.lifespan_context.client
    try:
        if id is not None:
            id = str(id)
        result = await client.cards_update(id, data)
        logger.info(f"cards_update: Updated card with id={id}")
        return result
    except HTTPStatusError as e:
        logger.error(f"cards_update HTTP error {e.response.status_code}: {e.response.text}")
        raise
    except RequestError as e:
        logger.error(f"cards_update Network error: {str(e)}")
        raise
    except Exception as e:
        logger.error(f"cards_update Unexpected error: {str(e)}")
        raise


async def cards_delete(context: Context, id: Union[int, str]) -> Any:
    client = context.request_context.lifespan_context.client
    try:
        if id is not None:
            id = str(id)
        result = await client.cards_delete(id)
        logger.info(f"cards_delete: Deleted card with id={id}")
        return result
    except HTTPStatusError as e:
        logger.error(f"cards_delete HTTP error {e.response.status_code}: {e.response.text}")
        raise
    except RequestError as e:
        logger.error(f"cards_delete Network error: {str(e)}")
        raise
    except Exception as e:
        logger.error(f"cards_delete Unexpected error: {str(e)}")
        raise
