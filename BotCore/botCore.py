from BotCore.Interface import *
import base64


async def send_text(text: str, receiver: str):
    """
    给微信好友或群聊发送消息
    :param text:
    :param receiver:
    :return:
    """
    jsonData = await sendPostReq('/text', {'msg': text, 'receiver': receiver})
    message = jsonData.get('message')
    return message


async def send_image(imgPath: str, receiver: str):
    """
    给微信好友或群聊发送图片
    :param imgPath:
    :param receiver:
    :return:
    """
    imgBase64Data = base64.b64encode(open(imgPath, 'rb').read()).decode()
    jsonData = await sendPostReq('/send-image', {'base64ImgData': imgBase64Data, 'receiver': receiver})
    message = jsonData.get('message')
    return message


async def push_msg(text: str, roomType: str):
    """
    给黑名单,白名单,推送群聊发消息
    :param text:
    :param roomType:
    :return:
    """
    jsonData = await sendPostReq('/send-room-text', {'msg': text, 'roomType': roomType})
    message = jsonData.get('message')
    return message


async def get_wxId(wxName: str):
    """
    获取微信名或群聊名对应的wxId
    :param wxName:
    :return:
    """
    if 'wxid_' in wxName or '@chatroom' in wxName:
        return wxName
    jsonData = await sendGetReq('/get-name-wxid', {'wxName': wxName})
    status = jsonData.get('status')
    if status == 0:
        wxId = jsonData.get('data').get('wxId')
        return wxId
    return None
