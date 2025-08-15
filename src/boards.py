import logging
from mcp.server.fastmcp import Context
from typing import Any, List, Union
from httpx import HTTPStatusError, RequestError

logger = logging.getLogger(__name__)


async def boards_list(context: Context, space_id: Union[int, str]) -> List[Any]:
    client = context.request_context.lifespan_context.client
    try:
        if space_id is not None:
            space_id = str(space_id)
        result = await client.boards_list(space_id)
        logger.info(f"boards_list: Retrieved boards list for space_id={space_id}")
        return result
    except HTTPStatusError as e:
        logger.error(f"boards_list HTTP error {e.response.status_code}: {e.response.text}")
        raise
    except RequestError as e:
        logger.error(f"boards_list Network error: {str(e)}")
        raise
    except Exception as e:
        logger.error(f"boards_list Unexpected error: {str(e)}")
        raise


async def boards_get(context: Context, id: Union[int, str]) -> Any:
    client = context.request_context.lifespan_context.client
    try:
        if id is not None:
            id = str(id)
        result = await client.boards_get(id)
        logger.info(f"boards_get: Retrieved board with id={id}")
        return result
    except HTTPStatusError as e:
        logger.error(f"boards_get HTTP error {e.response.status_code}: {e.response.text}")
        raise
    except RequestError as e:
        logger.error(f"boards_get Network error: {str(e)}")
        raise
    except Exception as e:
        logger.error(f"boards_get Unexpected error: {str(e)}")
        raise


async def boards_create(context: Context, space_id: Union[int, str], data: dict) -> Any:
    client = context.request_context.lifespan_context.client
    try:
        if space_id is not None:
            space_id = str(space_id)
        result = await client.boards_create(space_id, data)
        logger.info(f"boards_create: Created board in space_id={space_id}")
        return result
    except HTTPStatusError as e:
        logger.error(f"boards_create HTTP error {e.response.status_code}: {e.response.text}")
        raise
    except RequestError as e:
        logger.error(f"boards_create Network error: {str(e)}")
        raise
    except Exception as e:
        logger.error(f"boards_create Unexpected error: {str(e)}")
        raise


async def boards_update(context: Context, board_id: Union[int, str], space_id: Union[int, str], data: dict) -> Any:
    client = context.request_context.lifespan_context.client
    try:
        if board_id is not None:
            board_id = str(board_id)
        if space_id is not None:
            space_id = str(space_id)
        result = await client.boards_update(board_id, space_id, data)
        logger.info(f"boards_update: Updated board {board_id} in space {space_id}")
        return result
    except HTTPStatusError as e:
        logger.error(f"boards_update HTTP error {e.response.status_code}: {e.response.text}")
        raise
    except RequestError as e:
        logger.error(f"boards_update Network error: {str(e)}")
        raise
    except Exception as e:
        logger.error(f"boards_update Unexpected error: {str(e)}")
        raise


async def boards_delete(context: Context, board_id: Union[int, str], space_id: Union[int, str]) -> Any:
    client = context.request_context.lifespan_context.client
    try:
        if board_id is not None:
            board_id = str(board_id)
        if space_id is not None:
            space_id = str(space_id)
        result = await client.boards_delete(board_id, space_id)
        logger.info(f"boards_delete: Deleted board {board_id} in space {space_id}")
        return result
    except HTTPStatusError as e:
        logger.error(f"boards_delete HTTP error {e.response.status_code}: {e.response.text}")
        raise
    except RequestError as e:
        logger.error(f"boards_delete Network error: {str(e)}")
        raise
    except Exception as e:
        logger.error(f"boards_delete Unexpected error: {str(e)}")
        raise
