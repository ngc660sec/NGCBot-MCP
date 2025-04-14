from config import NGCBOT_API, NGCBot_KEY
import aiohttp
import base64
import asyncio

headers = {
    'BotKey': NGCBot_KEY
}


async def uploadFile(filePath: str):
    """
    上传文件到NGCBot接口服务器
    :param filePath:
    :return:
    """
    sendApi = f'{NGCBOT_API}/upload-file'
    try:
        data = aiohttp.FormData()
        data.add_field(
            "file",  # 字段名（对应后端的 key）
            open(filePath, "rb"),  # 文件对象
            filename=filePath.split("/")[-1],  # 文件名
            content_type="application/octet-stream"  # 文件 MIME 类型
        )
        async with aiohttp.ClientSession() as session:
            resp = await session.post(sendApi, headers=headers, data=data, timeout=20)
            jsonData = await resp.json()
            status = jsonData.get('status')
            if status == 0:
                return jsonData.get('filePath')
            raise ConnectionError(f'NGCBot接口服务出现错误, 错误信息: 未成功上传文件！')
    except Exception as e:
        raise ConnectionError(f'NGCBot接口服务出现错误, 错误信息: {e}')


async def getImgBase64Data(imgPath: str):
    """
    获取图片的base64编码
    :param imgPath: 
    :return: 
    """
    if 'http://' in imgPath or 'https://' in imgPath:
        imgContent = await sendGetContent(imgPath)
        imgBase64Data = base64.b64encode(imgContent).decode()
    else:
        imgBase64Data = base64.b64encode(open(imgPath, 'rb').read()).decode()
    return imgBase64Data


async def sendGetContent(sendApi: str):
    """
    发送字节资源GET请求通用函数
    :param sendApi: 
    :return: 
    """
    try:
        async with aiohttp.ClientSession() as session:
            resp = await session.get(sendApi, headers=headers, timeout=20)
            content = await resp.content.read()
            return content
    except Exception as e:
        raise ConnectionError(f'发送GET通用请求出现错误, 错误信息: {e}')


async def sendPostReq(api: str, data: dict):
    """
    发送POST请求NGCBot专用函数
    :param api:
    :param data:
    :return:
    """
    sendApi = f'{NGCBOT_API}{api}'
    try:
        async with aiohttp.ClientSession() as session:
            resp = await session.post(sendApi, headers=headers, json=data, timeout=20)
            jsonData = await resp.json()
            return jsonData
    except Exception as e:
        raise ConnectionError(f'NGCBot接口服务出现错误, 错误信息: {e}')


async def sendGetReq(api: str, params: dict):
    """
    发送GET请求NGCBot专用函数
    :param api:
    :param params:
    :return:
    """
    sendApi = f'{NGCBOT_API}{api}'
    try:
        async with aiohttp.ClientSession() as session:
            resp = await session.get(sendApi, headers=headers, params=params, timeout=20)
            jsonData = await resp.json()
            return jsonData
    except Exception as e:
        raise ConnectionError(f'NGCBot接口服务出现错误, 错误信息: {e}')


async def main():
    result = await uploadFile('/Users/exm/Python/MCP/NGCBot-MCP-Server/test.py')
    print(result)


asyncio.run(main())
