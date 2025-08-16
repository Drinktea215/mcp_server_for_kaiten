import os
import sys
from dotenv import load_dotenv
from contextlib import asynccontextmanager
from collections.abc import AsyncIterator
from dataclasses import dataclass
from pydantic import AnyHttpUrl
from mcp.server.fastmcp import FastMCP
from mcp.server.auth.settings import AuthSettings
from mcp.server.auth.provider import TokenVerifier, AccessToken
from kaiten_api_client import KaitenApiClient
from spaces import *
from boards import *
from cards import *

load_dotenv()

DOMAIN = os.getenv("DOMAIN")
TOKEN = os.getenv("TOKEN")

if not DOMAIN or not TOKEN:
    raise RuntimeError("Переменные окружения DOMAIN и TOKEN обязательны")

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler("log.log"),
        logging.StreamHandler(sys.stderr)
    ]
)


# Класс токен-верификатора
class SimpleTokenVerifier(TokenVerifier):
    async def verify_token(self, token: str) -> AccessToken | None:
        if token == TOKEN:
            return AccessToken(token=token, client_id="static-client", scopes=["authenticated"])
        return None


# Контекст lifespan
@dataclass
class AppContext:
    client: KaitenApiClient


@asynccontextmanager
async def lifespan(server: FastMCP) -> AsyncIterator[AppContext]:
    client = KaitenApiClient(base_url=DOMAIN, token=TOKEN)
    try:
        yield AppContext(client=client)
    finally:
        await client.close()


auth_settings = AuthSettings(
    issuer_url=AnyHttpUrl(DOMAIN),
    resource_server_url=AnyHttpUrl("http://localhost:8080"),
)

# Создаем MCP сервер
app = FastMCP(
    name="Kaiten MCP Server",
    auth=auth_settings,
    token_verifier=SimpleTokenVerifier(),
    lifespan=lifespan,
)

# Добавляем инструменты
tool_functions = [
    spaces_list,
    spaces_get,
    spaces_create,
    spaces_update,
    spaces_delete,
    boards_list,
    boards_get,
    boards_create,
    boards_update,
    boards_delete,
    cards_list,
    cards_get,
    cards_create,
    cards_update,
    cards_delete,
]

for tool_func in tool_functions:
    app.add_tool(tool_func)

if __name__ == "__main__":
    app.settings.host = "0.0.0.0"
    app.settings.port = 8080
    app.run(transport="streamable-http")
