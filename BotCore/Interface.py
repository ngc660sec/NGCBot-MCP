from config import NGCBOT_API
import aiohttp


async def sendPostReq(api: str, data: dict):
    """
    发送POST请求通用函数
    :param api:
    :param data:
    :return:
    """
    sendApi = f'{NGCBOT_API}{api}'
    try:
        async with aiohttp.ClientSession() as session:
            resp = await session.post(sendApi, json=data, timeout=20)
            jsonData = await resp.json()
            return jsonData
    except Exception as e:
        raise ConnectionError(f'NGCBot接口服务出现错误, 错误信息: {e}')


async def sendGetReq(api: str, params: dict):
    """

    :param api:
    :param params:
    :return:
    """
    sendApi = f'{NGCBOT_API}{api}'
    try:
        async with aiohttp.ClientSession() as session:
            resp = await session.get(sendApi, params=params, timeout=20)
            jsonData = await resp.json()
            return jsonData
    except Exception as e:
        raise ConnectionError(f'NGCBot接口服务出现错误, 错误信息: {e}')
