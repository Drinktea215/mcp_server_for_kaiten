import logging
from mcp.server.fastmcp import Context
from typing import Any, List, Union
from httpx import HTTPStatusError, RequestError

logger = logging.getLogger(__name__)


async def spaces_list(context: Context) -> List[Any]:
    client = context.request_context.lifespan_context.client
    try:
        result = await client.spaces_list()
        logger.info("spaces_list: Retrieved spaces list")
        return result
    except HTTPStatusError as e:
        logger.error(f"spaces_list HTTP error {e.response.status_code}: {e.response.text}")
        raise
    except RequestError as e:
        logger.error(f"spaces_list Network error: {str(e)}")
        raise
    except Exception as e:
        logger.error(f"spaces_list Unexpected error: {str(e)}")
        raise


async def spaces_get(context: Context, id: Union[int, str]) -> Any:
    client = context.request_context.lifespan_context.client
    try:
        if id is not None:
            id = str(id)
        result = await client.spaces_get(id)
        logger.info(f"spaces_get: Retrieved space with id={id}")
        return result
    except HTTPStatusError as e:
        logger.error(f"spaces_get HTTP error {e.response.status_code}: {e.response.text}")
        raise
    except RequestError as e:
        logger.error(f"spaces_get Network error: {str(e)}")
        raise
    except Exception as e:
        logger.error(f"spaces_get Unexpected error: {str(e)}")
        raise


async def spaces_create(context: Context, data: dict) -> Any:
    client = context.request_context.lifespan_context.client
    try:
        result = await client.spaces_create(data)
        logger.info("spaces_create: Created new space")
        return result
    except HTTPStatusError as e:
        logger.error(f"spaces_create HTTP error {e.response.status_code}: {e.response.text}")
        raise
    except RequestError as e:
        logger.error(f"spaces_create Network error: {str(e)}")
        raise
    except Exception as e:
        logger.error(f"spaces_create Unexpected error: {str(e)}")
        raise


async def spaces_update(context: Context, id: Union[int, str], data: dict) -> Any:
    client = context.request_context.lifespan_context.client
    try:
        if id is not None:
            id = str(id)
        result = await client.spaces_update(id, data)
        logger.info(f"spaces_update: Updated space with id={id}")
        return result
    except HTTPStatusError as e:
        logger.error(f"spaces_update HTTP error {e.response.status_code}: {e.response.text}")
        raise
    except RequestError as e:
        logger.error(f"spaces_update Network error: {str(e)}")
        raise
    except Exception as e:
        logger.error(f"spaces_update Unexpected error: {str(e)}")
        raise


async def spaces_delete(context: Context, id: Union[int, str]) -> Any:
    client = context.request_context.lifespan_context.client
    try:
        if id is not None:
            id = str(id)
        result = await client.spaces_delete(id)
        logger.info(f"spaces_delete: Deleted space with id={id}")
        return result
    except HTTPStatusError as e:
        logger.error(f"spaces_delete HTTP error {e.response.status_code}: {e.response.text}")
        raise
    except RequestError as e:
        logger.error(f"spaces_delete Network error: {str(e)}")
        raise
    except Exception as e:
        logger.error(f"spaces_delete Unexpected error: {str(e)}")
        raise
