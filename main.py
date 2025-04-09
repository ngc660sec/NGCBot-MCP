import logging
from sys import stdin, stdout
from fastmcp import FastMCP
from Tools.tools import register_tools

stdin.reconfigure(encoding='utf-8')
stdout.reconfigure(encoding='utf-8')
# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# 创建FastMCP实例
mcp = FastMCP("NGCBot-MCP-Server", dependencies=["requests", "fastmcp", "aiohttp"], description='NGCBotMCP服务', version='0.1.0')
register_tools(mcp)

