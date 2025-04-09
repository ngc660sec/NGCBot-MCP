import BotCore.botCore as bc


def register_tools(mcp):
    @mcp.tool("send_text", description='给微信好友或群聊发消息')
    async def send_message(text: str, receiver: str):
        """
        :param text: 要发送的文本内容
        :param receiver: wxId 或者 群聊wxId
        :return: 
        """
        if not text:
            raise ValueError('请输入要发送的内容!')
        elif not receiver:
            raise ValueError('请输入要接收的对象!')
        elif 'wxid_' not in receiver:
            if '@chatroom' not in receiver:
                raise ValueError('请先获取 wxId!')
        message = await bc.send_text(text, receiver)
        return message

    @mcp.tool('get_wxid', description='获取微信好友或群聊的wxId')
    async def get_wxId(wxName: str):
        wxId = await bc.get_wxId(wxName)
        if wxId:
            return wxId
        else:
            raise ValueError('未找到该wxId! 请重试！')

    @mcp.tool('push_room', description='向黑名单(black)|白名单(white)|推送(push)群聊推送消息')
    async def push_room_msg(text: str, msgType: str):
        if not text:
            raise ValueError('请输入要发送的内容!')
        if msgType not in ['black', 'white', 'push']:
            raise ValueError('请输入正确的消息类型!')
        message = await bc.push_msg(text, msgType)
        return message