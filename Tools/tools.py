import BotCore.botCore as bc
from typing import Optional, List, Dict, Any


def register_tools(mcp):
    @mcp.tool('send_file', description='给微信好友或群聊发送文件')
    async def send_file(filePath: str, receiver: str):
        """
        给微信好友或群聊发送文件
        :param filePath:
        :param receiver: 接收者的wxId(个人)或群聊wxId(群聊) 如: wxid_123 或 123@chatroom
        :return:
        """
        if not filePath or filePath.strip() == "":
            raise ValueError('文件路径不能为空!')

        if not receiver or receiver.strip() == "":
            raise ValueError('接收者不能为空!')

        if 'wxid_' not in receiver and '@chatroom' not in receiver:
            receiver = bc.get_wxId(wxName=receiver)
            if 'wxid_' not in receiver and '@chatroom' not in receiver:
                raise ValueError('请提供有效的wxId或群聊ID! 可以使用get_wxid工具获取')
        try:
            message = await bc.send_file(filePath, receiver)
            return {"status": "success", "message": message}
        except Exception as e:
            return {"status": "error", "message": f"发送失败: {str(e)}"}

    @mcp.tool('send_image', description='给微信好友或群聊发送图片')
    async def send_image(imgPath: str, receiver: str):
        """
        给微信好友或群聊发送图片

        :param imgPath: 图片路径或图片链接
        :param receiver: 接收者的wxId(个人)或群聊wxId(群聊) 如: wxid_123 或 123@chatroom
        :return: 发送结果
        """
        if not imgPath or imgPath.strip() == "":
            raise ValueError('图片路径不能为空!')

        if not receiver or receiver.strip() == "":
            raise ValueError('接收者不能为空!')

        if 'wxid_' not in receiver and '@chatroom' not in receiver:
            receiver = bc.get_wxId(wxName=receiver)
            if 'wxid_' not in receiver and '@chatroom' not in receiver:
                raise ValueError('请提供有效的wxId或群聊ID! 可以使用get_wxid工具获取')

        try:
            message = await bc.send_image(imgPath, receiver)
            return {"status": "success", "message": message}
        except Exception as e:
            return {"status": "error", "message": f"发送失败: {str(e)}"}

    @mcp.tool("send_text", description='给微信好友或群聊发送文本消息')
    async def send_message(text: str, receiver: str):
        """
        给指定的微信好友或群聊发送文本消息
        
        :param text: 要发送的文本内容
        :param receiver: 接收者的wxId(个人)或群聊wxId(群聊) 如: wxid_123 或 123@chatroom
        :return: 发送结果
        """

        if not text or text.strip() == "":
            raise ValueError('消息内容不能为空!')

        if not receiver or receiver.strip() == "":
            raise ValueError('接收者不能为空!')

        if 'wxid_' not in receiver and '@chatroom' not in receiver:
            receiver = bc.get_wxId(wxName=receiver)
            if 'wxid_' not in receiver and '@chatroom' not in receiver:
                raise ValueError('请提供有效的wxId或群聊ID! 可以使用get_wxid工具获取')

        try:
            message = await bc.send_text(text, receiver)
            return {"status": "success", "message": message}
        except Exception as e:
            return {"status": "error", "message": f"发送失败: {str(e)}"}

    @mcp.tool('get_wxid', description='获取微信好友或群聊的wxId')
    async def get_wxId(wxName: str):
        """
        根据微信名称获取对应的wxId
        
        :param wxName: 微信好友昵称或群聊名称
        :return: 对应的wxId
        """
        if not wxName or wxName.strip() == "":
            raise ValueError('微信名称不能为空!')

        try:
            wxId = await bc.get_wxId(wxName)
            if wxId:
                return {"status": "success", "wxId": wxId}
            else:
                return {"status": "error", "message": f"未找到名为 '{wxName}' 的联系人或群聊"}
        except Exception as e:
            return {"status": "error", "message": f"获取wxId失败: {str(e)}"}

    @mcp.tool('push_room', description='向指定类型的群聊推送消息')
    async def push_room_msg(text: str, msgType: str):
        """
        向黑名单(black)、白名单(white)或推送列表(push)中的群聊推送消息
        
        :param text: 要推送的文本内容
        :param msgType: 消息类型，可选值: 'black'(黑名单), 'white'(白名单), 'push'(推送列表)
        :return: 推送结果
        """
        valid_types = ['black', 'white', 'push']

        if not text or text.strip() == "":
            raise ValueError('推送内容不能为空!')

        if not msgType or msgType not in valid_types:
            raise ValueError(f'消息类型必须是以下之一: {", ".join(valid_types)}')

        try:
            message = await bc.push_msg(text, msgType)
            return {"status": "success", "message": message}
        except Exception as e:
            return {"status": "error", "message": f"推送失败: {str(e)}"}
