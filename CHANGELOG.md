# CHANGELOG

## explorer 全量轨道（2026-09-13）

新增 0 · 移除 0 · 定义变更 5（全量共 1640 个接口）

### 定义变更
- `POST /open-apis/drive/v1/permissions/{token}/public/password`「启用云文档密码」（drive/v1/permission.public.password/create）
- `DELETE /open-apis/drive/v1/permissions/{token}/public/password`「停用云文档密码」（drive/v1/permission.public.password/delete）
- `PUT /open-apis/drive/v1/permissions/{token}/public/password`「刷新云文档密码」（drive/v1/permission.public.password/update）
- `GET /open-apis/drive/v1/permissions/{token}/public`「获取云文档权限设置」（drive/v1/permission.public/get）
- `PATCH /open-apis/drive/v1/permissions/{token}/public`「更新云文档权限设置」（drive/v1/permission.public/patch）

## explorer 全量轨道（2026-09-12）

新增 0 · 移除 0 · 定义变更 1（全量共 1640 个接口）

### 定义变更
- `POST /open-apis/contact/v3/users/basic_batch`「通过 ID 获取用户姓名」（contact/v3/user/basic_batch）

## explorer 全量轨道（2026-09-11）

新增 0 · 移除 0 · 定义变更 6（全量共 1640 个接口）

### 定义变更
- `GET /open-apis/corehr/v2/signature_template_info_with_thumbnails`「获取电子签模板列表」（corehr/v2/signature_template_info_with_thumbnail/list）
- `GET /open-apis/im/v1/files/{file_key}`「下载文件」（im/v1/file/get）
- `GET /open-apis/im/v1/images/{image_key}`「下载图片」（im/v1/image/get）
- `POST /open-apis/im/v1/messages/merge_forward`「合并转发消息」（im/v1/message/merge_forward）
- `PUT /open-apis/im/v1/messages/{message_id}`「编辑消息」（im/v1/message/update）
- `POST /open-apis/vc/v1/meetings/{meeting_id}/kickout`「移除参会人」（vc/v1/meeting/kickout）

## explorer 全量轨道（2026-09-10）

新增 0 · 移除 0 · 定义变更 75（全量共 1640 个接口）

### 定义变更
- `DELETE /open-apis/board/v1/whiteboards/{whiteboard_id}/nodes/batch_delete`「批量删除节点」（board/v1/whiteboard.node/batch_delete）
- `POST /open-apis/board/v1/whiteboards/{whiteboard_id}/nodes`「创建节点」（board/v1/whiteboard.node/create）
- `POST /open-apis/board/v1/whiteboards/{whiteboard_id}/nodes/plantuml`「解析画板语法」（board/v1/whiteboard.node/create_plantuml）
- `GET /open-apis/board/v1/whiteboards/{whiteboard_id}/nodes`「获取所有节点」（board/v1/whiteboard.node/list）
- `GET /open-apis/board/v1/whiteboards/{whiteboard_id}/download_as_image`「获取画板缩略图片」（board/v1/whiteboard/download_as_image）
- `GET /open-apis/board/v1/whiteboards/{whiteboard_id}/theme`「获取画板主题」（board/v1/whiteboard/theme）
- `POST /open-apis/board/v1/whiteboards/{whiteboard_id}/update_theme`「更新画板主题」（board/v1/whiteboard/update_theme）
- `POST /open-apis/drive/v1/files/{file_token}/copy`「复制文件」（drive/v1/file/copy）
- `POST /open-apis/mail/v1/multi_entity/search`「多实体搜索」（mail/v1/multi_entity/search）
- `POST /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/messages/{message_id}/cancel_scheduled_send`「取消定时发送」（mail/v1/user_mailbox.draft/cancel_scheduled_send）
- `POST /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/drafts`「创建草稿」（mail/v1/user_mailbox.draft/create）
- `DELETE /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/drafts/{draft_id}`「删除草稿」（mail/v1/user_mailbox.draft/delete）
- `GET /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/drafts/{draft_id}`「获取草稿内容」（mail/v1/user_mailbox.draft/get）
- `GET /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/drafts`「列出草稿列表」（mail/v1/user_mailbox.draft/list）
- `POST /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/drafts/{draft_id}/send`「发送草稿」（mail/v1/user_mailbox.draft/send）
- `PUT /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/drafts/{draft_id}`「更新草稿」（mail/v1/user_mailbox.draft/update）
- `POST /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/folders`「创建邮箱文件夹」（mail/v1/user_mailbox.folder/create）
- `DELETE /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/folders/{folder_id}`「删除邮箱文件夹」（mail/v1/user_mailbox.folder/delete）
- `GET /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/folders/{folder_id}`「获取邮箱文件信息」（mail/v1/user_mailbox.folder/get）
- `GET /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/folders`「列出邮箱文件夹」（mail/v1/user_mailbox.folder/list）
- `PATCH /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/folders/{folder_id}`「修改邮箱文件夹」（mail/v1/user_mailbox.folder/patch）
- `POST /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/labels`「创建标签」（mail/v1/user_mailbox.label/create）
- `DELETE /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/labels/{label_id}`「删除标签」（mail/v1/user_mailbox.label/delete）
- `GET /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/labels/{label_id}`「获取标签信息」（mail/v1/user_mailbox.label/get）
- `GET /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/labels`「列出标签」（mail/v1/user_mailbox.label/list）
- `PATCH /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/labels/{label_id}`「更新标签」（mail/v1/user_mailbox.label/patch）
- `POST /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/mail_contacts`「创建邮箱联系人」（mail/v1/user_mailbox.mail_contact/create）
- `DELETE /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/mail_contacts/{mail_contact_id}`「删除邮箱联系人」（mail/v1/user_mailbox.mail_contact/delete）
- `GET /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/mail_contacts`「列出邮箱联系人」（mail/v1/user_mailbox.mail_contact/list）
- `PATCH /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/mail_contacts/{mail_contact_id}`「修改邮箱联系人信息」（mail/v1/user_mailbox.mail_contact/patch）
- `GET /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/messages/{message_id}/attachments/download_url`「获取附件下载链接」（mail/v1/user_mailbox.message.attachment/download_url）
- `POST /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/messages/batch_get`「批量获取邮件详情」（mail/v1/user_mailbox.message/batch_get）
- `POST /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/messages/batch_modify`「批量修改邮件」（mail/v1/user_mailbox.message/batch_modify）
- `POST /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/messages/batch_trash`「批量删除邮件」（mail/v1/user_mailbox.message/batch_trash）
- `GET /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/messages/{message_id}`「获取邮件详情」（mail/v1/user_mailbox.message/get）
- `GET /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/messages/get_by_card`「获取邮件卡片的邮件列表」（mail/v1/user_mailbox.message/get_by_card）
- `GET /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/messages`「列出邮件」（mail/v1/user_mailbox.message/list）
- `GET /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/threads/{thread_id}/messages`「查询会话下邮件信息」（mail/v1/user_mailbox.message/list_thread_message）
- `PUT /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/messages/{message_id}/modify`「修改邮件」（mail/v1/user_mailbox.message/modify）
- `POST /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/messages/send`「发送邮件」（mail/v1/user_mailbox.message/send）
- `GET /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/messages/{message_id}/send_status`「查询邮件发送状态」（mail/v1/user_mailbox.message/send_status）
- `POST /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/messages/{message_id}/trash`「删除邮件」（mail/v1/user_mailbox.message/trash）
- `POST /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/rules`「创建收信规则」（mail/v1/user_mailbox.rule/create）
- `DELETE /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/rules/{rule_id}`「删除收信规则」（mail/v1/user_mailbox.rule/delete）
- `GET /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/rules`「列出收信规则」（mail/v1/user_mailbox.rule/list）
- `POST /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/rules/reorder`「对收信规则进行排序」（mail/v1/user_mailbox.rule/reorder）
- `PUT /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/rules/{rule_id}`「更新收信规则」（mail/v1/user_mailbox.rule/update）
- `GET /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/messages/{message_id}/recall`「获取邮件撤回进度」（mail/v1/user_mailbox.sent_message/get_recall_detail）
- `POST /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/messages/{message_id}/recall`「撤回已发送邮件」（mail/v1/user_mailbox.sent_message/recall）
- `GET /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/settings/signatures`「列出邮件签名」（mail/v1/user_mailbox.setting/get_signatures）
- `GET /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/settings/send_as`「列出可发信邮箱」（mail/v1/user_mailbox.setting/send_as）
- `GET /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/templates/{template_id}/attachments/download_url`「获取模板附件下载链接」（mail/v1/user_mailbox.template.attachment/download_url）
- `POST /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/templates`「创建邮件模板」（mail/v1/user_mailbox.template/create）
- `DELETE /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/templates/{template_id}`「删除邮件模板」（mail/v1/user_mailbox.template/delete）
- `GET /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/templates/{template_id}`「获取邮件模板」（mail/v1/user_mailbox.template/get）
- `GET /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/templates`「列出邮件模板」（mail/v1/user_mailbox.template/list）
- `PUT /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/templates/{template_id}`「更新邮件模板」（mail/v1/user_mailbox.template/update）
- `POST /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/threads/batch_modify`「批量修改邮件会话」（mail/v1/user_mailbox.thread/batch_modify）
- `POST /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/threads/batch_trash`「批量删除邮件会话」（mail/v1/user_mailbox.thread/batch_trash）
- `GET /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/threads/{thread_id}`「获取邮件会话详情」（mail/v1/user_mailbox.thread/get）
- `GET /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/threads`「列出邮件会话」（mail/v1/user_mailbox.thread/list）
- `POST /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/threads/{thread_id}/modify`「修改邮件会话」（mail/v1/user_mailbox.thread/modify）
- `POST /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/threads/{thread_id}/trash`「删除邮件会话」（mail/v1/user_mailbox.thread/trash）
- `GET /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/accessible_mailboxes`「列出可访问的邮箱」（mail/v1/user_mailbox/accessible_mailboxes）
- `GET /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/profile`「获取用户邮箱信息」（mail/v1/user_mailbox/profile）
- `POST /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/search`「搜索邮件」（mail/v1/user_mailbox/search）
- `POST /open-apis/spark/v1/apps`「创建妙搭应用」（spark/v1/app/create）
- `GET /open-apis/task/v2/attachments`「列取附件」（task/v2/attachment/list）
- `POST /open-apis/task/v2/attachments/upload`「上传附件」（task/v2/attachment/upload）
- `POST /open-apis/task/v2/comments`「创建评论」（task/v2/comment/create）
- `GET /open-apis/task/v2/comments`「获取评论列表」（task/v2/comment/list）
- `POST /open-apis/task/v2/tasks`「创建任务」（task/v2/task/create）
- `GET /open-apis/task/v2/tasks/{task_guid}`「获取任务详情」（task/v2/task/get）
- `PATCH /open-apis/task/v2/tasks/{task_guid}`「更新任务」（task/v2/task/patch）
- `GET /open-apis/vc/v1/bots/events`「获取会议事件列表」（vc/v1/bot/events）

## explorer 全量轨道（2026-09-09）

新增 0 · 移除 0 · 定义变更 135（全量共 1640 个接口）

### 定义变更
- `PUT /open-apis/cardkit/v1/cards/{card_id}/elements/{element_id}/content`「流式更新文本」（cardkit/v1/card.element/content）
- `POST /open-apis/cardkit/v1/cards/{card_id}/elements`「新增组件」（cardkit/v1/card.element/create）
- `DELETE /open-apis/cardkit/v1/cards/{card_id}/elements/{element_id}`「删除组件」（cardkit/v1/card.element/delete）
- `PATCH /open-apis/cardkit/v1/cards/{card_id}/elements/{element_id}`「更新组件属性」（cardkit/v1/card.element/patch）
- `PUT /open-apis/cardkit/v1/cards/{card_id}/elements/{element_id}`「更新组件」（cardkit/v1/card.element/update）
- `POST /open-apis/cardkit/v1/cards/{card_id}/batch_update`「局部更新卡片实体」（cardkit/v1/card/batch_update）
- `POST /open-apis/cardkit/v1/cards`「创建卡片实体」（cardkit/v1/card/create）
- `POST /open-apis/cardkit/v1/cards/id_convert`「转换 ID」（cardkit/v1/card/id_convert）
- `PATCH /open-apis/cardkit/v1/cards/{card_id}/settings`「更新卡片实体配置」（cardkit/v1/card/settings）
- `PUT /open-apis/cardkit/v1/cards/{card_id}`「全量更新卡片实体」（cardkit/v1/card/update）
- `POST /open-apis/compensation/v1/recurring_payment/batch_create`「批量创建经常性支付记录」（compensation/v1/recurring_payment/batch_create）
- `POST /open-apis/compensation/v1/recurring_payment/batch_update`「批量更正经常性支付记录」（compensation/v1/recurring_payment/batch_update）
- `POST /open-apis/compensation/v1/recurring_payment/query`「查询经常性支付记录」（compensation/v1/recurring_payment/query）
- `POST /open-apis/hire/v1/background_check_orders/batch_query`「查询背调信息列表」（hire/v1/background_check_order/batch_query）
- `GET /open-apis/hire/v1/background_check_orders`「获取背调信息列表」（hire/v1/background_check_order/list）
- `GET /open-apis/im/v1/chats/{chat_id}/announcement`「获取群公告信息」（im/v1/chat.announcement/get）
- `PATCH /open-apis/im/v1/chats/{chat_id}/announcement`「更新群公告信息」（im/v1/chat.announcement/patch）
- `POST /open-apis/im/v1/chats/{chat_id}/managers/add_managers`「指定群管理员」（im/v1/chat.managers/add_managers）
- `POST /open-apis/im/v1/chats/{chat_id}/managers/delete_managers`「删除群管理员」（im/v1/chat.managers/delete_managers）
- `POST /open-apis/im/v1/chats/{chat_id}/members`「将用户或机器人拉入群聊」（im/v1/chat.members/create）
- `DELETE /open-apis/im/v1/chats/{chat_id}/members`「将用户或机器人移出群聊」（im/v1/chat.members/delete）
- `GET /open-apis/im/v1/chats/{chat_id}/members`「获取群成员列表」（im/v1/chat.members/get）
- `GET /open-apis/im/v1/chats/{chat_id}/members/is_in_chat`「判断用户或机器人是否在群里」（im/v1/chat.members/is_in_chat）
- `PATCH /open-apis/im/v1/chats/{chat_id}/members/me_join`「用户或机器人主动加入群聊」（im/v1/chat.members/me_join）
- `GET /open-apis/im/v1/chats/{chat_id}/moderation`「获取群成员发言权限」（im/v1/chat.moderation/get）
- `PUT /open-apis/im/v1/chats/{chat_id}/moderation`「更新群发言权限」（im/v1/chat.moderation/update）
- `POST /open-apis/im/v1/chats/{chat_id}/chat_tabs`「添加会话标签页」（im/v1/chat.tab/create）
- `DELETE /open-apis/im/v1/chats/{chat_id}/chat_tabs/delete_tabs`「删除会话标签页」（im/v1/chat.tab/delete_tabs）
- `GET /open-apis/im/v1/chats/{chat_id}/chat_tabs/list_tabs`「拉取会话标签页」（im/v1/chat.tab/list_tabs）
- `POST /open-apis/im/v1/chats/{chat_id}/chat_tabs/sort_tabs`「会话标签页排序」（im/v1/chat.tab/sort_tabs）
- `POST /open-apis/im/v1/chats/{chat_id}/chat_tabs/update_tabs`「更新会话标签页」（im/v1/chat.tab/update_tabs）
- `POST /open-apis/im/v1/chats/{chat_id}/top_notice/delete_top_notice`「撤销群置顶」（im/v1/chat.top_notice/delete_top_notice）
- `POST /open-apis/im/v1/chats/{chat_id}/top_notice/put_top_notice`「更新群置顶」（im/v1/chat.top_notice/put_top_notice）
- `POST /open-apis/im/v1/chats`「创建群」（im/v1/chat/create）
- `DELETE /open-apis/im/v1/chats/{chat_id}`「解散群」（im/v1/chat/delete）
- `GET /open-apis/im/v1/chats/{chat_id}`「获取群信息」（im/v1/chat/get）
- `POST /open-apis/im/v1/chats/{chat_id}/link`「获取群分享链接」（im/v1/chat/link）
- `GET /open-apis/im/v1/chats`「获取用户或机器人所在的群列表」（im/v1/chat/list）
- `GET /open-apis/im/v1/chats/search`「搜索对用户或机器人可见的群列表」（im/v1/chat/search）
- `PUT /open-apis/im/v1/chats/{chat_id}`「更新群信息」（im/v1/chat/update）
- `POST /open-apis/im/v1/files`「上传文件」（im/v1/file/create）
- `POST /open-apis/im/v1/images`「上传图片」（im/v1/image/create）
- `POST /open-apis/im/v1/messages/reactions/batch_query`「批量获取消息表情回复」（im/v1/message.reaction/batch_query）
- `POST /open-apis/im/v1/messages/{message_id}/reactions`「添加消息表情回复」（im/v1/message.reaction/create）
- `DELETE /open-apis/im/v1/messages/{message_id}/reactions/{reaction_id}`「删除消息表情回复」（im/v1/message.reaction/delete）
- `GET /open-apis/im/v1/messages/{message_id}/reactions`「获取消息表情回复」（im/v1/message.reaction/list）
- `GET /open-apis/im/v1/messages/{message_id}/resources/{file_key}`「获取消息中的资源文件」（im/v1/message.resource/get）
- `POST /open-apis/im/v1/messages`「发送消息」（im/v1/message/create）
- `DELETE /open-apis/im/v1/messages/{message_id}`「撤回消息」（im/v1/message/delete）
- `POST /open-apis/im/v1/messages/{message_id}/forward`「转发消息」（im/v1/message/forward）
- `GET /open-apis/im/v1/messages/{message_id}`「获取指定消息的内容」（im/v1/message/get）
- `GET /open-apis/im/v1/messages`「获取会话历史消息」（im/v1/message/list）
- `PATCH /open-apis/im/v1/messages/{message_id}`「更新已发送的消息卡片」（im/v1/message/patch）
- `GET /open-apis/im/v1/messages/{message_id}/read_users`「消息发送者查询消息已读状态」（im/v1/message/read_users）
- `POST /open-apis/im/v1/messages/{message_id}/reply`「回复消息」（im/v1/message/reply）
- `POST /open-apis/im/v1/messages/search`「搜索消息」（im/v1/message/search）
- `POST /open-apis/im/v1/pins`「Pin 消息」（im/v1/pin/create）
- `DELETE /open-apis/im/v1/pins/{message_id}`「移除 Pin 消息」（im/v1/pin/delete）
- `GET /open-apis/im/v1/pins`「获取群内 Pin 消息」（im/v1/pin/list）
- `POST /open-apis/im/v1/threads/{thread_id}/forward`「转发话题」（im/v1/thread/forward）
- `GET /open-apis/minutes/v1/minutes/{minute_token}/media`「下载妙记音视频文件」（minutes/v1/minute.media/get）
- `GET /open-apis/minutes/v1/minutes/{minute_token}/statistics`「获取妙记统计数据」（minutes/v1/minute.statistics/get）
- `GET /open-apis/minutes/v1/minutes/{minute_token}/transcript`「导出妙记文字记录」（minutes/v1/minute.transcript/get）
- `GET /open-apis/minutes/v1/minutes/{minute_token}/artifacts`「获取妙记AI产物」（minutes/v1/minute/artifacts）
- `POST /open-apis/minutes/v1/minutes/{minute_token}/clip`「创建妙记片段」（minutes/v1/minute/clip）
- `GET /open-apis/minutes/v1/minutes/{minute_token}`「获取妙记信息」（minutes/v1/minute/get）
- `POST /open-apis/minutes/v1/minutes/search`「搜索妙记」（minutes/v1/minute/search）
- `POST /open-apis/minutes/v1/minutes/subscription`「订阅妙记变更事件」（minutes/v1/minute/subscription）
- `POST /open-apis/minutes/v1/minutes/unsubscription`「取消订阅妙记变更事件」（minutes/v1/minute/unsubscription）
- `POST /open-apis/minutes/v1/minutes/upload`「云空间文件生成妙记」（minutes/v1/minute/upload）
- `POST /open-apis/search/v2/doc_wiki/search`「搜索文档」（search/v2/doc_wiki/search）
- `POST /open-apis/sheets/v3/spreadsheets/{spreadsheet_token}/sheets/{sheet_id}/filter`「创建筛选」（sheets/v3/spreadsheet.sheet.filter/create）
- `DELETE /open-apis/sheets/v3/spreadsheets/{spreadsheet_token}/sheets/{sheet_id}/filter`「删除筛选」（sheets/v3/spreadsheet.sheet.filter/delete）
- `GET /open-apis/sheets/v3/spreadsheets/{spreadsheet_token}/sheets/{sheet_id}/filter`「获取筛选」（sheets/v3/spreadsheet.sheet.filter/get）
- `PUT /open-apis/sheets/v3/spreadsheets/{spreadsheet_token}/sheets/{sheet_id}/filter`「更新筛选」（sheets/v3/spreadsheet.sheet.filter/update）
- `POST /open-apis/sheets/v3/spreadsheets/{spreadsheet_token}/sheets/{sheet_id}/filter_views/{filter_view_id}/conditions`「创建筛选条件」（sheets/v3/spreadsheet.sheet.filter_view.condition/create）
- `DELETE /open-apis/sheets/v3/spreadsheets/{spreadsheet_token}/sheets/{sheet_id}/filter_views/{filter_view_id}/conditions/{condition_id}`「删除筛选条件」（sheets/v3/spreadsheet.sheet.filter_view.condition/delete）
- `GET /open-apis/sheets/v3/spreadsheets/{spreadsheet_token}/sheets/{sheet_id}/filter_views/{filter_view_id}/conditions/{condition_id}`「获取筛选条件」（sheets/v3/spreadsheet.sheet.filter_view.condition/get）
- `GET /open-apis/sheets/v3/spreadsheets/{spreadsheet_token}/sheets/{sheet_id}/filter_views/{filter_view_id}/conditions/query`「查询筛选条件」（sheets/v3/spreadsheet.sheet.filter_view.condition/query）
- `PUT /open-apis/sheets/v3/spreadsheets/{spreadsheet_token}/sheets/{sheet_id}/filter_views/{filter_view_id}/conditions/{condition_id}`「更新筛选条件」（sheets/v3/spreadsheet.sheet.filter_view.condition/update）
- `POST /open-apis/sheets/v3/spreadsheets/{spreadsheet_token}/sheets/{sheet_id}/filter_views`「创建筛选视图」（sheets/v3/spreadsheet.sheet.filter_view/create）
- `DELETE /open-apis/sheets/v3/spreadsheets/{spreadsheet_token}/sheets/{sheet_id}/filter_views/{filter_view_id}`「删除筛选视图」（sheets/v3/spreadsheet.sheet.filter_view/delete）
- `GET /open-apis/sheets/v3/spreadsheets/{spreadsheet_token}/sheets/{sheet_id}/filter_views/{filter_view_id}`「获取筛选视图」（sheets/v3/spreadsheet.sheet.filter_view/get）
- `PATCH /open-apis/sheets/v3/spreadsheets/{spreadsheet_token}/sheets/{sheet_id}/filter_views/{filter_view_id}`「更新筛选视图」（sheets/v3/spreadsheet.sheet.filter_view/patch）
- `GET /open-apis/sheets/v3/spreadsheets/{spreadsheet_token}/sheets/{sheet_id}/filter_views/query`「查询筛选视图」（sheets/v3/spreadsheet.sheet.filter_view/query）
- `POST /open-apis/sheets/v3/spreadsheets/{spreadsheet_token}/sheets/{sheet_id}/float_images`「创建浮动图片」（sheets/v3/spreadsheet.sheet.float_image/create）
- `DELETE /open-apis/sheets/v3/spreadsheets/{spreadsheet_token}/sheets/{sheet_id}/float_images/{float_image_id}`「删除浮动图片」（sheets/v3/spreadsheet.sheet.float_image/delete）
- `GET /open-apis/sheets/v3/spreadsheets/{spreadsheet_token}/sheets/{sheet_id}/float_images/{float_image_id}`「获取浮动图片」（sheets/v3/spreadsheet.sheet.float_image/get）
- `PATCH /open-apis/sheets/v3/spreadsheets/{spreadsheet_token}/sheets/{sheet_id}/float_images/{float_image_id}`「更新浮动图片」（sheets/v3/spreadsheet.sheet.float_image/patch）
- `GET /open-apis/sheets/v3/spreadsheets/{spreadsheet_token}/sheets/{sheet_id}/float_images/query`「查询浮动图片」（sheets/v3/spreadsheet.sheet.float_image/query）
- `POST /open-apis/sheets/v3/spreadsheets/{spreadsheet_token}/sheets/{sheet_id}/find`「查找单元格」（sheets/v3/spreadsheet.sheet/find）
- `GET /open-apis/sheets/v3/spreadsheets/{spreadsheet_token}/sheets/{sheet_id}`「查询工作表」（sheets/v3/spreadsheet.sheet/get）
- `POST /open-apis/sheets/v3/spreadsheets/{spreadsheet_token}/sheets/{sheet_id}/move_dimension`「移动行列」（sheets/v3/spreadsheet.sheet/move_dimension）
- `GET /open-apis/sheets/v3/spreadsheets/{spreadsheet_token}/sheets/query`「获取工作表」（sheets/v3/spreadsheet.sheet/query）
- `POST /open-apis/sheets/v3/spreadsheets/{spreadsheet_token}/sheets/{sheet_id}/replace`「替换单元格」（sheets/v3/spreadsheet.sheet/replace）
- `POST /open-apis/sheets/v3/spreadsheets`「创建电子表格」（sheets/v3/spreadsheet/create）
- `GET /open-apis/sheets/v3/spreadsheets/{spreadsheet_token}`「获取电子表格信息」（sheets/v3/spreadsheet/get）
- `PATCH /open-apis/sheets/v3/spreadsheets/{spreadsheet_token}`「修改电子表格属性」（sheets/v3/spreadsheet/patch）
- `POST /open-apis/vc/v1/bots/countdown`「会中倒计时」（vc/v1/bot/countdown）
- `GET /open-apis/vc/v1/bots/events`「获取会议事件列表」（vc/v1/bot/events）
- `POST /open-apis/vc/v1/bots/join`「加入会议」（vc/v1/bot/join）
- `POST /open-apis/vc/v1/bots/leave`「离开会议」（vc/v1/bot/leave）
- `POST /open-apis/vc/v1/bots/message`「发送会中消息」（vc/v1/bot/message）
- `GET /open-apis/vc/v1/bots/user_active_meeting`「获取用户活跃会议列表」（vc/v1/bot/user_active_meeting）
- `GET /open-apis/vc/v1/exports/download`「下载导出文件」（vc/v1/export/download）
- `GET /open-apis/vc/v1/exports/{task_id}`「查询导出任务结果」（vc/v1/export/get）
- `POST /open-apis/vc/v1/exports/meeting_list`「导出会议明细」（vc/v1/export/meeting_list）
- `POST /open-apis/vc/v1/exports/participant_list`「导出参会人明细」（vc/v1/export/participant_list）
- `POST /open-apis/vc/v1/exports/participant_quality_list`「导出参会人会议质量数据」（vc/v1/export/participant_quality_list）
- `POST /open-apis/vc/v1/exports/resource_reservation_list`「导出会议室预定数据」（vc/v1/export/resource_reservation_list）
- `GET /open-apis/vc/v1/meetings/{meeting_id}/recording`「获取录制文件」（vc/v1/meeting.recording/get）
- `PATCH /open-apis/vc/v1/meetings/{meeting_id}/recording/set_permission`「授权录制文件」（vc/v1/meeting.recording/set_permission）
- `PATCH /open-apis/vc/v1/meetings/{meeting_id}/recording/start`「开始录制」（vc/v1/meeting.recording/start）
- `PATCH /open-apis/vc/v1/meetings/{meeting_id}/recording/stop`「停止录制」（vc/v1/meeting.recording/stop）
- `PATCH /open-apis/vc/v1/meetings/{meeting_id}/end`「结束会议」（vc/v1/meeting/end）
- `GET /open-apis/vc/v1/meetings/{meeting_id}`「获取会议详情」（vc/v1/meeting/get）
- `PATCH /open-apis/vc/v1/meetings/{meeting_id}/invite`「邀请参会人」（vc/v1/meeting/invite）
- `GET /open-apis/vc/v1/meetings/list_by_no`「获取与会议号关联的会议列表」（vc/v1/meeting/list_by_no）
- `POST /open-apis/vc/v1/meetings/search`「搜索会议记录」（vc/v1/meeting/search）
- `PATCH /open-apis/vc/v1/meetings/{meeting_id}/set_host`「设置主持人」（vc/v1/meeting/set_host）
- `POST /open-apis/vc/v1/meetings/subscription`「订阅会议变更事件」（vc/v1/meeting/subscription）
- `POST /open-apis/vc/v1/meetings/unsubscription`「取消订阅会议变更事件」（vc/v1/meeting/unsubscription）
- `GET /open-apis/vc/v1/meeting_list`「查询会议明细」（vc/v1/meeting_list/get）
- `GET /open-apis/vc/v1/notes/{note_id}`「获取纪要详情」（vc/v1/note/get）
- `POST /open-apis/vc/v1/notes/subscription`「订阅纪要变更事件」（vc/v1/note/subscription）
- `POST /open-apis/vc/v1/notes/unsubscription`「取消订阅纪要变更事件」（vc/v1/note/unsubscription）
- `GET /open-apis/vc/v1/participant_list`「查询参会人明细」（vc/v1/participant_list/get）
- `GET /open-apis/vc/v1/participant_quality_list`「查询参会人会议质量数据」（vc/v1/participant_quality_list/get）
- `POST /open-apis/vc/v1/reserves/apply`「预约会议」（vc/v1/reserve/apply）
- `DELETE /open-apis/vc/v1/reserves/{reserve_id}`「删除预约」（vc/v1/reserve/delete）
- `GET /open-apis/vc/v1/reserves/{reserve_id}`「获取预约」（vc/v1/reserve/get）
- `GET /open-apis/vc/v1/reserves/{reserve_id}/get_active_meeting`「获取活跃会议」（vc/v1/reserve/get_active_meeting）
- `PUT /open-apis/vc/v1/reserves/{reserve_id}`「更新预约」（vc/v1/reserve/update）
- `GET /open-apis/vc/v1/resource_reservation_list`「查询会议室预定数据」（vc/v1/resource_reservation_list/get）
- `POST /open-apis/vc/v1/rooms/search`「搜索会议室」（vc/v1/room/search）

## explorer 全量轨道（2026-09-08）

新增 0 · 移除 0 · 定义变更 99（全量共 1640 个接口）

### 定义变更
- `GET /open-apis/docs/v1/content`「获取云文档内容」（docs/v1/content/get）
- `DELETE /open-apis/docx/v1/chats/{chat_id}/announcement/blocks/{block_id}/children/batch_delete`「删除群公告中的块」（docx/v1/chat.announcement.block.children/batch_delete）
- `POST /open-apis/docx/v1/chats/{chat_id}/announcement/blocks/{block_id}/children`「在群公告中创建块」（docx/v1/chat.announcement.block.children/create）
- `GET /open-apis/docx/v1/chats/{chat_id}/announcement/blocks/{block_id}/children`「获取所有子块」（docx/v1/chat.announcement.block.children/get）
- `PATCH /open-apis/docx/v1/chats/{chat_id}/announcement/blocks/batch_update`「批量更新群公告块的内容」（docx/v1/chat.announcement.block/batch_update）
- `GET /open-apis/docx/v1/chats/{chat_id}/announcement/blocks/{block_id}`「获取群公告块的内容」（docx/v1/chat.announcement.block/get）
- `GET /open-apis/docx/v1/chats/{chat_id}/announcement/blocks`「获取群公告所有块」（docx/v1/chat.announcement.block/list）
- `GET /open-apis/docx/v1/chats/{chat_id}/announcement`「获取群公告基本信息」（docx/v1/chat.announcement/get）
- `DELETE /open-apis/docx/v1/documents/{document_id}/blocks/{block_id}/children/batch_delete`「删除块」（docx/v1/document.block.children/batch_delete）
- `POST /open-apis/docx/v1/documents/{document_id}/blocks/{block_id}/children`「创建块」（docx/v1/document.block.children/create）
- `GET /open-apis/docx/v1/documents/{document_id}/blocks/{block_id}/children`「获取所有子块」（docx/v1/document.block.children/get）
- `POST /open-apis/docx/v1/documents/{document_id}/blocks/{block_id}/descendant`「创建嵌套块」（docx/v1/document.block.descendant/create）
- `PATCH /open-apis/docx/v1/documents/{document_id}/blocks/batch_update`「批量更新块的内容」（docx/v1/document.block/batch_update）
- `GET /open-apis/docx/v1/documents/{document_id}/blocks/{block_id}`「获取块的内容」（docx/v1/document.block/get）
- `GET /open-apis/docx/v1/documents/{document_id}/blocks`「获取文档所有块」（docx/v1/document.block/list）
- `PATCH /open-apis/docx/v1/documents/{document_id}/blocks/{block_id}`「更新块的内容」（docx/v1/document.block/patch）
- `POST /open-apis/docx/v1/documents/blocks/convert`「Markdown/HTML 内容转换为文档块」（docx/v1/document/convert）
- `POST /open-apis/docx/v1/documents`「创建文档」（docx/v1/document/create）
- `GET /open-apis/docx/v1/documents/{document_id}`「获取文档基本信息」（docx/v1/document/get）
- `GET /open-apis/docx/v1/documents/{document_id}/raw_content`「获取文档纯文本内容」（docx/v1/document/raw_content）
- `POST /open-apis/drive/v1/export_tasks`「创建导出任务」（drive/v1/export_task/create）
- `GET /open-apis/drive/v1/export_tasks/file/{file_token}/download`「下载导出文件」（drive/v1/export_task/download）
- `GET /open-apis/drive/v1/export_tasks/{ticket}`「查询导出任务结果」（drive/v1/export_task/get）
- `POST /open-apis/drive/v1/files/{file_token}/comments/{comment_id}/replies`「添加回复」（drive/v1/file.comment.reply/create）
- `DELETE /open-apis/drive/v1/files/{file_token}/comments/{comment_id}/replies/{reply_id}`「删除回复」（drive/v1/file.comment.reply/delete）
- `GET /open-apis/drive/v1/files/{file_token}/comments/{comment_id}/replies`「获取回复信息」（drive/v1/file.comment.reply/list）
- `PUT /open-apis/drive/v1/files/{file_token}/comments/{comment_id}/replies/{reply_id}`「更新回复的内容」（drive/v1/file.comment.reply/update）
- `POST /open-apis/drive/v1/files/{file_token}/comments/batch_query`「批量获取评论」（drive/v1/file.comment/batch_query）
- `POST /open-apis/drive/v1/files/{file_token}/comments`「添加全文评论」（drive/v1/file.comment/create）
- `GET /open-apis/drive/v1/files/{file_token}/comments/{comment_id}`「获取全文评论」（drive/v1/file.comment/get）
- `GET /open-apis/drive/v1/files/{file_token}/comments`「获取云文档所有评论」（drive/v1/file.comment/list）
- `PATCH /open-apis/drive/v1/files/{file_token}/comments/{comment_id}`「解决/恢复评论」（drive/v1/file.comment/patch）
- `GET /open-apis/drive/v1/files/{file_token}/statistics`「获取文件统计信息」（drive/v1/file.statistics/get）
- `POST /open-apis/drive/v1/files/{file_token}/subscriptions`「创建订阅」（drive/v1/file.subscription/create）
- `GET /open-apis/drive/v1/files/{file_token}/subscriptions/{subscription_id}`「获取订阅状态」（drive/v1/file.subscription/get）
- `PATCH /open-apis/drive/v1/files/{file_token}/subscriptions/{subscription_id}`「更新订阅状态」（drive/v1/file.subscription/patch）
- `POST /open-apis/drive/v1/files/{file_token}/versions`「创建文档版本」（drive/v1/file.version/create）
- `DELETE /open-apis/drive/v1/files/{file_token}/versions/{version_id}`「删除文档版本」（drive/v1/file.version/delete）
- `GET /open-apis/drive/v1/files/{file_token}/versions/{version_id}`「获取文档版本信息」（drive/v1/file.version/get）
- `GET /open-apis/drive/v1/files/{file_token}/versions`「获取文档版本列表」（drive/v1/file.version/list）
- `GET /open-apis/drive/v1/files/{file_token}/view_records`「获取文件访问记录」（drive/v1/file.view_record/list）
- `POST /open-apis/drive/v1/files/{file_token}/copy`「复制文件」（drive/v1/file/copy）
- `POST /open-apis/drive/v1/files/create_folder`「新建文件夹」（drive/v1/file/create_folder）
- `POST /open-apis/drive/v1/files/create_shortcut`「创建文件快捷方式」（drive/v1/file/create_shortcut）
- `DELETE /open-apis/drive/v1/files/{file_token}`「删除文件或文件夹」（drive/v1/file/delete）
- `DELETE /open-apis/drive/v1/files/{file_token}/delete_subscribe`「取消云文档事件订阅」（drive/v1/file/delete_subscribe）
- `GET /open-apis/drive/v1/files/{file_token}/download`「下载文件」（drive/v1/file/download）
- `GET /open-apis/drive/v1/files/{file_token}/get_subscribe`「查询云文档事件订阅状态」（drive/v1/file/get_subscribe）
- `GET /open-apis/drive/v1/files`「获取文件夹中的文件清单」（drive/v1/file/list）
- `POST /open-apis/drive/v1/files/{file_token}/move`「移动文件或文件夹」（drive/v1/file/move）
- `POST /open-apis/drive/v1/files/{file_token}/subscribe`「订阅云文档事件」（drive/v1/file/subscribe）
- `GET /open-apis/drive/v1/files/task_check`「查询异步任务状态」（drive/v1/file/task_check）
- `POST /open-apis/drive/v1/files/upload_all`「上传文件」（drive/v1/file/upload_all）
- `POST /open-apis/drive/v1/files/upload_finish`「分片上传文件-完成上传」（drive/v1/file/upload_finish）
- `POST /open-apis/drive/v1/files/upload_part`「分片上传文件-上传分片」（drive/v1/file/upload_part）
- `POST /open-apis/drive/v1/files/upload_prepare`「分片上传文件-预上传」（drive/v1/file/upload_prepare）
- `POST /open-apis/drive/v1/import_tasks`「创建导入任务」（drive/v1/import_task/create）
- `GET /open-apis/drive/v1/import_tasks/{ticket}`「查询导入任务结果」（drive/v1/import_task/get）
- `GET /open-apis/drive/v1/medias/batch_get_tmp_download_url`「获取素材临时下载链接」（drive/v1/media/batch_get_tmp_download_url）
- `GET /open-apis/drive/v1/medias/{file_token}/download`「下载素材」（drive/v1/media/download）
- `POST /open-apis/drive/v1/medias/upload_all`「上传素材」（drive/v1/media/upload_all）
- `POST /open-apis/drive/v1/medias/upload_finish`「分片上传素材-完成上传」（drive/v1/media/upload_finish）
- `POST /open-apis/drive/v1/medias/upload_part`「分片上传素材-上传分片」（drive/v1/media/upload_part）
- `POST /open-apis/drive/v1/medias/upload_prepare`「分片上传素材-预上传」（drive/v1/media/upload_prepare）
- `POST /open-apis/drive/v1/metas/batch_query`「获取文件元数据」（drive/v1/meta/batch_query）
- `GET /open-apis/drive/v1/permissions/{token}/members/auth`「判断用户云文档权限」（drive/v1/permission.member/auth）
- `POST /open-apis/drive/v1/permissions/{token}/members/batch_create`「批量增加协作者权限」（drive/v1/permission.member/batch_create）
- `POST /open-apis/drive/v1/permissions/{token}/members`「增加协作者权限」（drive/v1/permission.member/create）
- `DELETE /open-apis/drive/v1/permissions/{token}/members/{member_id}`「移除云文档协作者权限」（drive/v1/permission.member/delete）
- `GET /open-apis/drive/v1/permissions/{token}/members`「获取云文档协作者」（drive/v1/permission.member/list）
- `POST /open-apis/drive/v1/permissions/{token}/members/transfer_owner`「转移云文档所有者」（drive/v1/permission.member/transfer_owner）
- `PUT /open-apis/drive/v1/permissions/{token}/members/{member_id}`「更新协作者权限」（drive/v1/permission.member/update）
- `POST /open-apis/drive/v1/permissions/{token}/public/password`「启用云文档密码」（drive/v1/permission.public.password/create）
- `DELETE /open-apis/drive/v1/permissions/{token}/public/password`「停用云文档密码」（drive/v1/permission.public.password/delete）
- `PUT /open-apis/drive/v1/permissions/{token}/public/password`「刷新云文档密码」（drive/v1/permission.public.password/update）
- `GET /open-apis/drive/v1/permissions/{token}/public`「获取云文档权限设置」（drive/v1/permission.public/get）
- `PATCH /open-apis/drive/v1/permissions/{token}/public`「更新云文档权限设置」（drive/v1/permission.public/patch）
- `DELETE /open-apis/drive/v1/user/remove_subscription`「取消用户云文档事件订阅」（drive/v1/user/remove_subscription）
- `POST /open-apis/drive/v1/user/subscription`「订阅用户云文档事件」（drive/v1/user/subscription）
- `GET /open-apis/drive/v1/user/subscription_status`「查询用户云文档事件订阅状态」（drive/v1/user/subscription_status）
- `POST /open-apis/drive/v2/files/{file_token}/comments/reaction`「添加/取消表情回应」（drive/v2/comment_reaction/update_reaction）
- `GET /open-apis/drive/v2/files/{file_token}/likes`「获取云文档的点赞者列表」（drive/v2/file.like/list）
- `GET /open-apis/drive/v2/permissions/{token}/public`「获取云文档权限设置」（drive/v2/permission.public/get）
- `PATCH /open-apis/drive/v2/permissions/{token}/public`「更新云文档权限设置」（drive/v2/permission.public/patch）
- `POST /open-apis/wiki/v2/spaces/{space_id}/members`「添加知识空间成员」（wiki/v2/space.member/create）
- `DELETE /open-apis/wiki/v2/spaces/{space_id}/members/{member_id}`「删除知识空间成员」（wiki/v2/space.member/delete）
- `GET /open-apis/wiki/v2/spaces/{space_id}/members`「获取知识空间成员列表」（wiki/v2/space.member/list）
- `POST /open-apis/wiki/v2/spaces/{space_id}/nodes/{node_token}/copy`「创建知识空间节点副本」（wiki/v2/space.node/copy）
- `POST /open-apis/wiki/v2/spaces/{space_id}/nodes`「创建知识空间节点」（wiki/v2/space.node/create）
- `GET /open-apis/wiki/v2/spaces/{space_id}/nodes`「获取知识空间子节点列表」（wiki/v2/space.node/list）
- `POST /open-apis/wiki/v2/spaces/{space_id}/nodes/{node_token}/move`「移动知识空间节点」（wiki/v2/space.node/move）
- `POST /open-apis/wiki/v2/spaces/{space_id}/nodes/move_docs_to_wiki`「移动云空间文档至知识空间」（wiki/v2/space.node/move_docs_to_wiki）
- `POST /open-apis/wiki/v2/spaces/{space_id}/nodes/{node_token}/update_title`「更新知识空间节点标题」（wiki/v2/space.node/update_title）
- `PUT /open-apis/wiki/v2/spaces/{space_id}/setting`「更新知识空间设置」（wiki/v2/space.setting/update）
- `POST /open-apis/wiki/v2/spaces`「创建知识空间」（wiki/v2/space/create）
- `GET /open-apis/wiki/v2/spaces/{space_id}`「获取知识空间信息」（wiki/v2/space/get）
- `GET /open-apis/wiki/v2/spaces/get_node`「获取知识空间节点信息」（wiki/v2/space/get_node）
- `GET /open-apis/wiki/v2/spaces`「获取知识空间列表」（wiki/v2/space/list）
- `GET /open-apis/wiki/v2/tasks/{task_id}`「获取任务结果」（wiki/v2/task/get）

## explorer 全量轨道（2026-09-05）

新增 0 · 移除 0 · 定义变更 42（全量共 1640 个接口）

### 定义变更
- `POST /open-apis/calendar/v4/calendars/{calendar_id}/acls`「创建访问控制」（calendar/v4/calendar.acl/create）
- `DELETE /open-apis/calendar/v4/calendars/{calendar_id}/acls/{acl_id}`「删除访问控制」（calendar/v4/calendar.acl/delete）
- `GET /open-apis/calendar/v4/calendars/{calendar_id}/acls`「获取访问控制列表」（calendar/v4/calendar.acl/list）
- `POST /open-apis/calendar/v4/calendars/{calendar_id}/acls/subscription`「订阅日历访问控制变更事件」（calendar/v4/calendar.acl/subscription）
- `POST /open-apis/calendar/v4/calendars/{calendar_id}/acls/unsubscription`「取消订阅日历访问控制变更事件」（calendar/v4/calendar.acl/unsubscription）
- `GET /open-apis/calendar/v4/calendars/{calendar_id}/events/{event_id}/attendees/{attendee_id}/chat_members`「获取日程参与群成员列表」（calendar/v4/calendar.event.attendee.chat_member/list）
- `POST /open-apis/calendar/v4/calendars/{calendar_id}/events/{event_id}/attendees/batch_delete`「删除日程参与人」（calendar/v4/calendar.event.attendee/batch_delete）
- `POST /open-apis/calendar/v4/calendars/{calendar_id}/events/{event_id}/attendees`「添加日程参与人」（calendar/v4/calendar.event.attendee/create）
- `GET /open-apis/calendar/v4/calendars/{calendar_id}/events/{event_id}/attendees`「获取日程参与人列表」（calendar/v4/calendar.event.attendee/list）
- `POST /open-apis/calendar/v4/calendars/{calendar_id}/events/{event_id}/meeting_chat`「创建会议群」（calendar/v4/calendar.event.meeting_chat/create）
- `DELETE /open-apis/calendar/v4/calendars/{calendar_id}/events/{event_id}/meeting_chat`「解绑会议群」（calendar/v4/calendar.event.meeting_chat/delete）
- `POST /open-apis/calendar/v4/calendars/{calendar_id}/events/{event_id}/meeting_minute`「创建会议纪要」（calendar/v4/calendar.event.meeting_minute/create）
- `POST /open-apis/calendar/v4/calendars/{calendar_id}/events`「创建日程」（calendar/v4/calendar.event/create）
- `DELETE /open-apis/calendar/v4/calendars/{calendar_id}/events/{event_id}`「删除日程」（calendar/v4/calendar.event/delete）
- `GET /open-apis/calendar/v4/calendars/{calendar_id}/events/{event_id}`「获取日程」（calendar/v4/calendar.event/get）
- `GET /open-apis/calendar/v4/calendars/{calendar_id}/events/instance_view`「查询日程视图」（calendar/v4/calendar.event/instance_view）
- `GET /open-apis/calendar/v4/calendars/{calendar_id}/events/{event_id}/instances`「获取重复日程实例」（calendar/v4/calendar.event/instances）
- `GET /open-apis/calendar/v4/calendars/{calendar_id}/events`「获取日程列表」（calendar/v4/calendar.event/list）
- `PATCH /open-apis/calendar/v4/calendars/{calendar_id}/events/{event_id}`「更新日程」（calendar/v4/calendar.event/patch）
- `POST /open-apis/calendar/v4/calendars/{calendar_id}/events/{event_id}/reply`「回复日程」（calendar/v4/calendar.event/reply）
- `POST /open-apis/calendar/v4/calendars/{calendar_id}/events/search`「搜索日程」（calendar/v4/calendar.event/search）
- `POST /open-apis/calendar/v4/calendars/{calendar_id}/events/subscription`「订阅日程变更事件」（calendar/v4/calendar.event/subscription）
- `POST /open-apis/calendar/v4/calendars/{calendar_id}/events/unsubscription`「取消订阅日程变更事件」（calendar/v4/calendar.event/unsubscription）
- `POST /open-apis/calendar/v4/calendars`「创建共享日历」（calendar/v4/calendar/create）
- `DELETE /open-apis/calendar/v4/calendars/{calendar_id}`「删除共享日历」（calendar/v4/calendar/delete）
- `GET /open-apis/calendar/v4/calendars/{calendar_id}`「查询日历信息」（calendar/v4/calendar/get）
- `GET /open-apis/calendar/v4/calendars`「查询日历列表」（calendar/v4/calendar/list）
- `POST /open-apis/calendar/v4/calendars/mget`「批量查询日历信息」（calendar/v4/calendar/mget）
- `PATCH /open-apis/calendar/v4/calendars/{calendar_id}`「更新日历信息」（calendar/v4/calendar/patch）
- `POST /open-apis/calendar/v4/calendars/primary`「查询主日历信息」（calendar/v4/calendar/primary）
- `POST /open-apis/calendar/v4/calendars/primarys`「批量获取主日历信息」（calendar/v4/calendar/primarys）
- `POST /open-apis/calendar/v4/calendars/search`「搜索日历」（calendar/v4/calendar/search）
- `POST /open-apis/calendar/v4/calendars/{calendar_id}/subscribe`「订阅日历」（calendar/v4/calendar/subscribe）
- `POST /open-apis/calendar/v4/calendars/subscription`「订阅日历变更事件」（calendar/v4/calendar/subscription）
- `POST /open-apis/calendar/v4/calendars/{calendar_id}/unsubscribe`「取消订阅日历」（calendar/v4/calendar/unsubscribe）
- `POST /open-apis/calendar/v4/calendars/unsubscription`「取消订阅日历变更事件」（calendar/v4/calendar/unsubscription）
- `POST /open-apis/calendar/v4/freebusy/batch`「批量查询主日历日程忙闲信息」（calendar/v4/freebusy/batch）
- `POST /open-apis/calendar/v4/freebusy/list`「查询主日历日程忙闲信息」（calendar/v4/freebusy/list）
- `GET /open-apis/vc/v1/bots/events`「获取会议事件列表」（vc/v1/bot/events）
- `POST /open-apis/vc/v1/bots/join`「加入会议」（vc/v1/bot/join）
- `POST /open-apis/vc/v1/bots/leave`「离开会议」（vc/v1/bot/leave）
- `GET /open-apis/vc/v1/bots/user_active_meeting`「获取用户活跃会议列表」（vc/v1/bot/user_active_meeting）

## explorer 全量轨道（2026-09-03）

新增 1 · 移除 0 · 定义变更 2（全量共 1640 个接口）

### 新增接口
- `POST /open-apis/vc/v1/bots/countdown`「会中倒计时」（vc/v1/bot/countdown）

### 定义变更
- `POST /open-apis/corehr/v2/employees/batch_get`「批量查询员工信息」（corehr/v2/employee/batch_get）
- `POST /open-apis/corehr/v2/employees/search`「搜索员工信息」（corehr/v2/employee/search）

## explorer 全量轨道（2026-09-02）

新增 0 · 移除 0 · 定义变更 4（全量共 1639 个接口）

### 定义变更
- `POST /open-apis/corehr/v2/pre_hires`「直接创建待入职」（corehr/v2/pre_hire/create）
- `PATCH /open-apis/corehr/v2/pre_hires/{pre_hire_id}`「更新待入职信息」（corehr/v2/pre_hire/patch）
- `POST /open-apis/corehr/v2/pre_hires/query`「查询待入职信息」（corehr/v2/pre_hire/query）
- `POST /open-apis/corehr/v2/pre_hires/search`「搜索待入职信息」（corehr/v2/pre_hire/search）

## explorer 全量轨道（2026-09-01）

新增 5 · 移除 0 · 定义变更 1（全量共 1639 个接口）

### 新增接口
- `GET /open-apis/spark/v1/available_scope`「获取妙搭产品使用权限」（spark/v1/app.available_scope/open_api_get_miaoda_available_scope）
- `PUT /open-apis/spark/v1/available_scope`「修改妙搭产品使用权限」（spark/v1/app.available_scope/open_api_update_miaoda_available_scope）
- `GET /open-apis/spark/v1/apps/{app_id}/analytics/overview`「获取妙搭应用运营数据总览」（spark/v1/app/open_api_analytics_overview）
- `GET /open-apis/spark/v1/apps/{app_id}/credit_usage`「获取妙搭应用消耗 AI 额度」（spark/v1/app/open_api_credit_usage）
- `POST /open-apis/spark/v1/apps/{app_id}/query_analytics_data`「获取妙搭应用运营数据趋势」（spark/v1/app/query_analytics_data）

### 定义变更
- `POST /open-apis/corehr/v2/pre_hires/search`「搜索待入职信息」（corehr/v2/pre_hire/search）

## explorer 全量轨道（2026-08-31）

新增 0 · 移除 0 · 定义变更 3（全量共 1634 个接口）

### 定义变更
- `GET /open-apis/vc/v1/meetings/{meeting_id}`「获取会议详情」（vc/v1/meeting/get）
- `GET /open-apis/vc/v1/meetings/list_by_no`「获取与会议号关联的会议列表」（vc/v1/meeting/list_by_no）
- `GET /open-apis/vc/v1/reserves/{reserve_id}/get_active_meeting`「获取活跃会议」（vc/v1/reserve/get_active_meeting）

## explorer 全量轨道（2026-08-28）

新增 0 · 移除 0 · 定义变更 12（全量共 1634 个接口）

### 定义变更
- `POST /open-apis/corehr/v2/pre_hires`「直接创建待入职」（corehr/v2/pre_hire/create）
- `PATCH /open-apis/corehr/v2/pre_hires/{pre_hire_id}`「更新待入职信息」（corehr/v2/pre_hire/patch）
- `POST /open-apis/corehr/v2/pre_hires/query`「查询待入职信息」（corehr/v2/pre_hire/query）
- `POST /open-apis/corehr/v2/pre_hires/search`「搜索待入职信息」（corehr/v2/pre_hire/search）
- `GET /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/threads`「列出邮件会话」（mail/v1/user_mailbox.thread/list）
- `GET /open-apis/okr/v2/key_results/{key_result_id}/progresses`「获取关键结果下的进展记录」（okr/v2/okr.key_result.progress/list）
- `POST /open-apis/spark/v1/apps`「创建妙搭应用」（spark/v1/app/create）
- `GET /open-apis/spark/v1/apps`「批量获取妙搭应用」（spark/v1/app/list）
- `PATCH /open-apis/spark/v1/apps/{app_id}`「更新妙搭应用信息」（spark/v1/app/patch）
- `POST /open-apis/task/v2/tasks/search`「搜索任务」（task/v2/task/search）
- `POST /open-apis/task/v2/tasklists/search`「搜索清单」（task/v2/tasklist/search）
- `GET /open-apis/vc/v1/bots/events`「获取会议事件列表」（vc/v1/bot/events）

## explorer 全量轨道（2026-08-27）

新增 1 · 移除 0 · 定义变更 6（全量共 1634 个接口）

### 新增接口
- `POST /open-apis/approval/v4/approvals/search_launchable`「搜索可发起的审批定义」（approval/v4/approval/search_launchable）

### 定义变更
- `POST /open-apis/approval/v4/instances/add_cc`「抄送审批实例（用户级）」（approval/v4/instance/add_cc）
- `GET /open-apis/approval/v4/instances/detail`「获取单个审批实例详情（用户级）」（approval/v4/instance/detail）
- `GET /open-apis/approval/v4/instances/initiated`「查询用户的已发起审批列表」（approval/v4/instance/initiated）
- `POST /open-apis/approval/v4/tasks/add_sign`「审批任务加签（用户级）」（approval/v4/task/add_sign）
- `POST /open-apis/approval/v4/tasks/forward`「转交审批任务（用户级）」（approval/v4/task/forward）
- `GET /open-apis/approval/v4/tasks`「查询审批任务列表」（approval/v4/task/list）

## explorer 全量轨道（2026-08-26）

新增 2 · 移除 0 · 定义变更 10（全量共 1633 个接口）

### 新增接口
- `POST /open-apis/minutes/v1/minutes/{minute_token}/clip`「创建妙记片段」（minutes/v1/minute/clip）
- `POST /open-apis/minutes/v1/minutes/upload`「云空间文件生成妙记」（minutes/v1/minute/upload）

### 定义变更
- `POST /open-apis/approval/v4/instances/add_cc`「抄送审批实例（用户级）」（approval/v4/instance/add_cc）
- `GET /open-apis/approval/v4/instances/detail`「获取单个审批实例详情（用户级）」（approval/v4/instance/detail）
- `GET /open-apis/approval/v4/instances/initiated`「查询用户的已发起审批列表」（approval/v4/instance/initiated）
- `POST /open-apis/approval/v4/tasks/add_sign`「审批任务加签（用户级）」（approval/v4/task/add_sign）
- `POST /open-apis/approval/v4/tasks/forward`「转交审批任务（用户级）」（approval/v4/task/forward）
- `GET /open-apis/approval/v4/tasks`「查询审批任务列表」（approval/v4/task/list）
- `POST /open-apis/hire/v1/background_check_orders/batch_query`「查询背调信息列表」（hire/v1/background_check_order/batch_query）
- `GET /open-apis/hire/v1/background_check_orders`「获取背调信息列表」（hire/v1/background_check_order/list）
- `POST /open-apis/hire/v1/eco_background_checks/update_progress`「更新背调订单进度」（hire/v1/eco_background_check/update_progress）
- `POST /open-apis/hire/v1/eco_background_checks/update_result`「回传背调订单的最终结果」（hire/v1/eco_background_check/update_result）

## explorer 全量轨道（2026-08-25）

新增 0 · 移除 0 · 定义变更 14（全量共 1631 个接口）

### 定义变更
- `POST /open-apis/corehr/v2/employees/batch_get`「批量查询员工信息」（corehr/v2/employee/batch_get）
- `POST /open-apis/corehr/v2/employees/search`「搜索员工信息」（corehr/v2/employee/search）
- `POST /open-apis/corehr/v2/persons`「创建个人信息」（corehr/v2/person/create）
- `PATCH /open-apis/corehr/v2/persons/{person_id}`「更新个人信息」（corehr/v2/person/patch）
- `POST /open-apis/corehr/v2/pre_hires/query`「查询待入职信息」（corehr/v2/pre_hire/query）
- `POST /open-apis/corehr/v2/pre_hires/search`「搜索待入职信息」（corehr/v2/pre_hire/search）
- `POST /open-apis/im/v1/messages`「发送消息」（im/v1/message/create）
- `POST /open-apis/im/v1/messages/{message_id}/forward`「转发消息」（im/v1/message/forward）
- `GET /open-apis/im/v1/messages/{message_id}`「获取指定消息的内容」（im/v1/message/get）
- `GET /open-apis/im/v1/messages`「获取会话历史消息」（im/v1/message/list）
- `POST /open-apis/im/v1/messages/merge_forward`「合并转发消息」（im/v1/message/merge_forward）
- `POST /open-apis/im/v1/messages/{message_id}/reply`「回复消息」（im/v1/message/reply）
- `PUT /open-apis/im/v1/messages/{message_id}`「编辑消息」（im/v1/message/update）
- `POST /open-apis/im/v1/threads/{thread_id}/forward`「转发话题」（im/v1/thread/forward）

## explorer 全量轨道（2026-08-20）

新增 0 · 移除 0 · 定义变更 3（全量共 1631 个接口）

### 定义变更
- `GET /open-apis/vc/v1/bots/events`「获取会议事件列表」（vc/v1/bot/events）
- `POST /open-apis/vc/v1/bots/join`「加入会议」（vc/v1/bot/join）
- `POST /open-apis/vc/v1/meetings/search`「搜索会议记录」（vc/v1/meeting/search）

## explorer 全量轨道（2026-08-19）

新增 0 · 移除 0 · 定义变更 1（全量共 1631 个接口）

### 定义变更
- `PATCH /open-apis/corehr/v1/employments/{employment_id}`「更新雇佣信息」（corehr/v1/employment/patch）

## explorer 全量轨道（2026-08-18）

新增 3 · 移除 0 · 定义变更 0（全量共 1631 个接口）

### 新增接口
- `POST /open-apis/vc/v1/bots/join`「加入会议」（vc/v1/bot/join）
- `POST /open-apis/vc/v1/bots/leave`「离开会议」（vc/v1/bot/leave）
- `POST /open-apis/vc/v1/bots/message`「发送会中消息」（vc/v1/bot/message）

## explorer 全量轨道（2026-08-14）

新增 0 · 移除 0 · 定义变更 2（全量共 1628 个接口）

### 定义变更
- `POST /open-apis/drive/v1/medias/upload_all`「上传素材」（drive/v1/media/upload_all）
- `POST /open-apis/drive/v1/medias/upload_prepare`「分片上传素材-预上传」（drive/v1/media/upload_prepare）

## explorer 全量轨道（2026-08-13）

新增 0 · 移除 0 · 定义变更 1（全量共 1628 个接口）

### 定义变更
- `GET /open-apis/wiki/v2/spaces/get_node`「获取知识空间节点信息」（wiki/v2/space/get_node）

## explorer 全量轨道（2026-08-12）

新增 0 · 移除 0 · 定义变更 5（全量共 1628 个接口）

### 定义变更
- `POST /open-apis/drive/v1/files/upload_all`「上传文件」（drive/v1/file/upload_all）
- `POST /open-apis/drive/v1/medias/upload_all`「上传素材」（drive/v1/media/upload_all）
- `GET /open-apis/drive/v1/permissions/{token}/members/auth`「判断用户云文档权限」（drive/v1/permission.member/auth）
- `POST /open-apis/drive/v1/permissions/{token}/members/batch_create`「批量增加协作者权限」（drive/v1/permission.member/batch_create）
- `POST /open-apis/drive/v1/permissions/{token}/members`「增加协作者权限」（drive/v1/permission.member/create）

## explorer 全量轨道（2026-08-11）

新增 0 · 移除 0 · 定义变更 9（全量共 1628 个接口）

### 定义变更
- `PATCH /open-apis/corehr/v1/employments/{employment_id}`「更新雇佣信息」（corehr/v1/employment/patch）
- `POST /open-apis/corehr/v2/pre_hires/query`「查询待入职信息」（corehr/v2/pre_hire/query）
- `POST /open-apis/corehr/v2/pre_hires/search`「搜索待入职信息」（corehr/v2/pre_hire/search）
- `DELETE /open-apis/drive/v1/files/{file_token}`「删除文件或文件夹」（drive/v1/file/delete）
- `GET /open-apis/drive/v1/files/{file_token}/download`「下载文件」（drive/v1/file/download）
- `GET /open-apis/drive/v1/medias/{file_token}/download`「下载素材」（drive/v1/media/download）
- `GET /open-apis/im/v1/messages/{message_id}/read_users`「消息发送者查询消息已读状态」（im/v1/message/read_users）
- `GET /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/mail_contacts`「列出邮箱联系人」（mail/v1/user_mailbox.mail_contact/list）
- `GET /open-apis/wiki/v2/spaces/{space_id}/nodes`「获取知识空间子节点列表」（wiki/v2/space.node/list）

## explorer 全量轨道（2026-08-07）

新增 0 · 移除 0 · 定义变更 1（全量共 1628 个接口）

### 定义变更
- `GET /open-apis/drive/v1/permissions/{token}/members/auth`「判断用户云文档权限」（drive/v1/permission.member/auth）

## explorer 全量轨道（2026-08-06）

新增 0 · 移除 0 · 定义变更 8（全量共 1628 个接口）

### 定义变更
- `POST /open-apis/calendar/v4/calendars/{calendar_id}/events`「创建日程」（calendar/v4/calendar.event/create）
- `GET /open-apis/calendar/v4/calendars/{calendar_id}/events/{event_id}`「获取日程」（calendar/v4/calendar.event/get）
- `PATCH /open-apis/calendar/v4/calendars/{calendar_id}/events/{event_id}`「更新日程」（calendar/v4/calendar.event/patch）
- `POST /open-apis/corehr/v1/leaves/work_calendar_date`「获取工作日历日期详情」（corehr/v1/leave/work_calendar_date）
- `POST /open-apis/im/v1/messages/search`「搜索消息」（im/v1/message/search）
- `GET /open-apis/vc/v1/bots/events`「获取会议事件列表」（vc/v1/bot/events）
- `GET /open-apis/vc/v1/notes/{note_id}`「获取纪要详情」（vc/v1/note/get）
- `GET /open-apis/wiki/v2/spaces/{space_id}/nodes`「获取知识空间子节点列表」（wiki/v2/space.node/list）

## explorer 全量轨道（2026-08-05）

新增 0 · 移除 0 · 定义变更 9（全量共 1628 个接口）

### 定义变更
- `GET /open-apis/approval/v4/tasks`「查询审批任务列表」（approval/v4/task/list）
- `POST /open-apis/board/v1/whiteboards/{whiteboard_id}/nodes`「创建节点」（board/v1/whiteboard.node/create）
- `POST /open-apis/compensation/v1/lump_sum_payment/batch_create`「批量创建一次性支付记录」（compensation/v1/lump_sum_payment/batch_create）
- `POST /open-apis/compensation/v1/lump_sum_payment/batch_remove`「批量删除一次性支付记录」（compensation/v1/lump_sum_payment/batch_remove）
- `POST /open-apis/compensation/v1/lump_sum_payment/batch_update`「批量更正一次性支付记录」（compensation/v1/lump_sum_payment/batch_update）
- `POST /open-apis/compensation/v1/lump_sum_payment/query`「查询一次性支付授予记录」（compensation/v1/lump_sum_payment/query）
- `POST /open-apis/compensation/v1/lump_sum_payment/query_detail`「查询一次性支付授予明细」（compensation/v1/lump_sum_payment/query_detail）
- `GET /open-apis/minutes/v1/minutes/{minute_token}/artifacts`「获取妙记AI产物」（minutes/v1/minute/artifacts）
- `POST /open-apis/minutes/v1/minutes/search`「搜索妙记」（minutes/v1/minute/search）

## explorer 全量轨道（2026-07-30）

新增 0 · 移除 0 · 定义变更 4（全量共 1628 个接口）

### 定义变更
- `POST /open-apis/corehr/v2/departments/batch_get`「批量查询部门」（corehr/v2/department/batch_get）
- `POST /open-apis/corehr/v2/departments/query_multi_timeline`「批量查询部门版本信息」（corehr/v2/department/query_multi_timeline）
- `POST /open-apis/corehr/v2/departments/query_timeline`「查询指定生效日期的部门基本信息」（corehr/v2/department/query_timeline）
- `POST /open-apis/corehr/v2/departments/search`「搜索部门信息」（corehr/v2/department/search）

## explorer 全量轨道（2026-07-29）

新增 0 · 移除 0 · 定义变更 16（全量共 1628 个接口）

### 定义变更
- `DELETE /open-apis/board/v1/whiteboards/{whiteboard_id}/nodes/batch_delete`「批量删除节点」（board/v1/whiteboard.node/batch_delete）
- `POST /open-apis/board/v1/whiteboards/{whiteboard_id}/nodes`「创建节点」（board/v1/whiteboard.node/create）
- `POST /open-apis/board/v1/whiteboards/{whiteboard_id}/nodes/plantuml`「解析画板语法」（board/v1/whiteboard.node/create_plantuml）
- `GET /open-apis/board/v1/whiteboards/{whiteboard_id}/nodes`「获取所有节点」（board/v1/whiteboard.node/list）
- `GET /open-apis/board/v1/whiteboards/{whiteboard_id}/download_as_image`「获取画板缩略图片」（board/v1/whiteboard/download_as_image）
- `GET /open-apis/board/v1/whiteboards/{whiteboard_id}/theme`「获取画板主题」（board/v1/whiteboard/theme）
- `POST /open-apis/board/v1/whiteboards/{whiteboard_id}/update_theme`「更新画板主题」（board/v1/whiteboard/update_theme）
- `GET /open-apis/drive/v1/permissions/{token}/members/auth`「判断用户云文档权限」（drive/v1/permission.member/auth）
- `POST /open-apis/drive/v1/permissions/{token}/members/batch_create`「批量增加协作者权限」（drive/v1/permission.member/batch_create）
- `POST /open-apis/drive/v1/permissions/{token}/members`「增加协作者权限」（drive/v1/permission.member/create）
- `DELETE /open-apis/drive/v1/permissions/{token}/members/{member_id}`「移除云文档协作者权限」（drive/v1/permission.member/delete）
- `GET /open-apis/drive/v1/permissions/{token}/members`「获取云文档协作者」（drive/v1/permission.member/list）
- `POST /open-apis/drive/v1/permissions/{token}/members/transfer_owner`「转移云文档所有者」（drive/v1/permission.member/transfer_owner）
- `PUT /open-apis/drive/v1/permissions/{token}/members/{member_id}`「更新协作者权限」（drive/v1/permission.member/update）
- `GET /open-apis/drive/v2/permissions/{token}/public`「获取云文档权限设置」（drive/v2/permission.public/get）
- `PATCH /open-apis/drive/v2/permissions/{token}/public`「更新云文档权限设置」（drive/v2/permission.public/patch）

## explorer 全量轨道（2026-07-28）

新增 1 · 移除 0 · 定义变更 0（全量共 1628 个接口）

### 新增接口
- `PUT /open-apis/passport/v1/password`「重置登录密码」（passport/v1/password/update）

## explorer 全量轨道（2026-07-24）

新增 0 · 移除 0 · 定义变更 2（全量共 1627 个接口）

### 定义变更
- `POST /open-apis/bitable/v1/apps/{app_token}/tables/{table_id}/fields`「新增字段」（bitable/v1/app.table.field/create）
- `PUT /open-apis/bitable/v1/apps/{app_token}/tables/{table_id}/fields/{field_id}`「更新字段」（bitable/v1/app.table.field/update）

## explorer 全量轨道（2026-07-22）

新增 0 · 移除 0 · 定义变更 7（全量共 1627 个接口）

### 定义变更
- `POST /open-apis/corehr/v2/cost_centers/tree`「查询指定生效日期的成本中心架构树」（corehr/v2/cost_center/tree）
- `POST /open-apis/corehr/v2/departments/parents`「获取父部门信息」（corehr/v2/department/parents）
- `POST /open-apis/corehr/v2/departments/search`「搜索部门信息」（corehr/v2/department/search）
- `POST /open-apis/corehr/v2/departments/tree`「查询指定生效日期的部门架构树」（corehr/v2/department/tree）
- `GET /open-apis/corehr/v2/workforce_plans`「查询编制规划方案」（corehr/v2/workforce_plan/list）
- `POST /open-apis/spark/v1/apps`「创建妙搭应用」（spark/v1/app/create）
- `POST /open-apis/spark/v1/directory/user/id_convert`「妙搭和飞书用户 ID 转换」（spark/v1/directory.user/id_convert）

## explorer 全量轨道（2026-07-21）

新增 0 · 移除 0 · 定义变更 14（全量共 1627 个接口）

### 定义变更
- `POST /open-apis/calendar/v4/calendars/{calendar_id}/events`「创建日程」（calendar/v4/calendar.event/create）
- `GET /open-apis/calendar/v4/calendars/{calendar_id}/events/{event_id}`「获取日程」（calendar/v4/calendar.event/get）
- `GET /open-apis/calendar/v4/calendars/{calendar_id}/events/instance_view`「查询日程视图」（calendar/v4/calendar.event/instance_view）
- `GET /open-apis/calendar/v4/calendars/{calendar_id}/events/{event_id}/instances`「获取重复日程实例」（calendar/v4/calendar.event/instances）
- `GET /open-apis/calendar/v4/calendars/{calendar_id}/events`「获取日程列表」（calendar/v4/calendar.event/list）
- `PATCH /open-apis/calendar/v4/calendars/{calendar_id}/events/{event_id}`「更新日程」（calendar/v4/calendar.event/patch）
- `POST /open-apis/calendar/v4/calendars/{calendar_id}/events/search`「搜索日程」（calendar/v4/calendar.event/search）
- `POST /open-apis/corehr/v1/job_datas`「创建任职信息」（corehr/v1/job_data/create）
- `GET /open-apis/corehr/v1/job_datas/{job_data_id}`「查询单个任职信息」（corehr/v1/job_data/get）
- `GET /open-apis/corehr/v1/job_datas`「批量查询任职信息」（corehr/v1/job_data/list）
- `PATCH /open-apis/corehr/v1/job_datas/{job_data_id}`「更新任职信息」（corehr/v1/job_data/patch）
- `POST /open-apis/corehr/v2/persons`「创建个人信息」（corehr/v2/person/create）
- `PATCH /open-apis/corehr/v2/persons/{person_id}`「更新个人信息」（corehr/v2/person/patch）
- `POST /open-apis/spark/v1/directory/user/id_convert`「妙搭和飞书用户 ID 转换」（spark/v1/directory.user/id_convert）

## Go 源码轨道上线（2026-07-19）

新增第三数据源：lark-cli 快捷命令的 **Go 源码实现**（`shortcuts/` 目录）。这些
`common.Shortcut` 结构体带有描述、风险分级、权限 scopes、调用身份、flag 定义和
使用提示，并硬编码了实际调用的 HTTP 方法和路径。首次提取（lark-cli v1.0.72）：
**18 个服务、228 个接口**，产物位于 `openapi-go/`。

其中 **102 个接口路径官方 API Explorer 未收录**——包括几乎整套未文档化的
Base v3 家族（约 45 个端点）、`docs_ai`、`slides_ai`、`sheet_ai`、`spark`，以及
drive/im/calendar/vc/sheets 等域的零散内部端点。

说明：提取为启发式（正则解析而非完整 AST），flag → 参数的映射是近似推断，
响应体为通用信封；每条操作带有 `x-lark-source: lark-cli-go` 与
`x-lark-cli-command` 标记。少量深度抽象的命令（sheets/mail 的部分辅助层）
暂未覆盖。

## 仓库结构调整（2026-07-19）

- 全量轨道目录由 `openapi-full/` 更名为 **`openapi/`**（项目主体：55 个项目、1627 个接口）；
- 精选轨道目录由 `openapi/` 更名为 **`openapi-curated/`**（15 个服务、239 个接口）；
- 精选轨道同步移除 `x-lark-generated-at` 构建时间戳（`info.version` 即上游注册表版本），与全量轨道一致实现字节级确定性重建。

## explorer 全量轨道（2026-07-19，数据规范化）

修复上游 `scopesOfFieldRequired` 数组顺序随机导致的变更误报：抓取时对该字段排序后再计算内容哈希，此前两次 "定义变更 79/81" 条目为同一原因产生的误报，已移除，无实际接口变动。同时全量文档的 `info.version` 改为内容哈希（`1.0.0+<hash>`），移除构建时间戳，未变更的文档重建后字节级不变。

## explorer 全量轨道上线（2026-07-19）

新增第二数据源：飞书官方 API Explorer（`/api_explorer/v1`，开放平台在线调试工具的
数据接口）。首次导入 **55 个项目、1627 个接口**，产物位于 `openapi-full/`。

与 lark-cli 轨道（`openapi/`，239 个精选接口）的差异：

- 覆盖面：1627 vs 239，包含 lark-cli 未收录的接口（如发消息 `POST /open-apis/im/v1/messages`）；
- 字段：额外包含错误码表（x-lark-error-mappings）、限流档位（x-lark-rate-limit）、分页标记；
- 变更检测：上游无版本号，改为每日全量抓取 + 内容 hash 比对，有变化才提交。

## registry v1.0.0（2026-07-19）

新增 239 · 移除 0 · 变更 0

### 新增接口
- `GET /open-apis/approval/v4/approvals/{approval_code}/detail`（approval / approvals.get）
- `POST /open-apis/approval/v4/approvals/search_launchable`（approval / approvals.search）
- `POST /open-apis/approval/v4/instances/recall`（approval / instances.cancel）
- `POST /open-apis/approval/v4/instances/add_cc`（approval / instances.cc）
- `POST /open-apis/approval/v4/instances/initiate`（approval / instances.create）
- `GET /open-apis/approval/v4/instances/detail`（approval / instances.get）
- `GET /open-apis/approval/v4/instances/initiated`（approval / instances.initiated）
- `POST /open-apis/approval/v4/tasks/add_sign`（approval / tasks.add_sign）
- `POST /open-apis/approval/v4/tasks/pass`（approval / tasks.approve）
- `GET /open-apis/approval/v4/tasks`（approval / tasks.query）
- `POST /open-apis/approval/v4/tasks/refuse`（approval / tasks.reject）
- `POST /open-apis/approval/v4/instances/remind`（approval / tasks.remind）
- `POST /open-apis/approval/v4/tasks/rollback`（approval / tasks.rollback）
- `POST /open-apis/approval/v4/tasks/forward`（approval / tasks.transfer）
- `POST /open-apis/attendance/v1/user_tasks/query`（attendance / user_tasks.query）
- `POST /open-apis/calendar/v4/calendars`（calendar / calendars.create）
- `DELETE /open-apis/calendar/v4/calendars/{calendar_id}`（calendar / calendars.delete）
- `GET /open-apis/calendar/v4/calendars/{calendar_id}`（calendar / calendars.get）
- `GET /open-apis/calendar/v4/calendars`（calendar / calendars.list）
- `PATCH /open-apis/calendar/v4/calendars/{calendar_id}`（calendar / calendars.patch）
- `POST /open-apis/calendar/v4/calendars/primary`（calendar / calendars.primary）
- `POST /open-apis/calendar/v4/calendars/search`（calendar / calendars.search）
- `POST /open-apis/calendar/v4/calendars/{calendar_id}/events/{event_id}/attendees/batch_delete`（calendar / event.attendees.batch_delete）
- `POST /open-apis/calendar/v4/calendars/{calendar_id}/events/{event_id}/attendees`（calendar / event.attendees.create）
- `GET /open-apis/calendar/v4/calendars/{calendar_id}/events/{event_id}/attendees`（calendar / event.attendees.list）
- `POST /open-apis/calendar/v4/calendars/{calendar_id}/events`（calendar / events.create）
- `DELETE /open-apis/calendar/v4/calendars/{calendar_id}/events/{event_id}`（calendar / events.delete）
- `GET /open-apis/calendar/v4/calendars/{calendar_id}/events/{event_id}`（calendar / events.get）
- `GET /open-apis/calendar/v4/calendars/{calendar_id}/events/instance_view`（calendar / events.instance_view）
- `PATCH /open-apis/calendar/v4/calendars/{calendar_id}/events/{event_id}`（calendar / events.patch）
- `POST /open-apis/calendar/v4/calendars/{calendar_id}/events/search_event`（calendar / events.search_event）
- `POST /open-apis/calendar/v4/calendars/{calendar_id}/events/{event_id}/share_info`（calendar / events.share_info）
- `POST /open-apis/calendar/v4/freebusy/list`（calendar / freebusys.list）
- `POST /open-apis/profile/v2/user_profiles/batch_query`（contact / user_profiles.batch_query）
- `POST /open-apis/drive/v2/files/{file_token}/comments/reaction`（drive / file.comment.reply.reactions.update_reaction）
- `POST /open-apis/drive/v1/files/{file_token}/comments/{comment_id}/replies`（drive / file.comment.replys.create）
- `DELETE /open-apis/drive/v1/files/{file_token}/comments/{comment_id}/replies/{reply_id}`（drive / file.comment.replys.delete）
- `GET /open-apis/drive/v1/files/{file_token}/comments/{comment_id}/replies`（drive / file.comment.replys.list）
- `PUT /open-apis/drive/v1/files/{file_token}/comments/{comment_id}/replies/{reply_id}`（drive / file.comment.replys.update）
- `POST /open-apis/drive/v1/files/{file_token}/comments/batch_query`（drive / file.comments.batch_query）
- `POST /open-apis/drive/v1/files/{file_token}/new_comments`（drive / file.comments.create_v2）
- `GET /open-apis/drive/v1/files/{file_token}/comments`（drive / file.comments.list）
- `PATCH /open-apis/drive/v1/files/{file_token}/comments/{comment_id}`（drive / file.comments.patch）
- `GET /open-apis/drive/v1/files/{file_token}/statistics`（drive / file.statistics.get）
- `GET /open-apis/drive/v1/files/{file_token}/view_records`（drive / file.view_records.list）
- `POST /open-apis/drive/v1/files/{file_token}/copy`（drive / files.copy）
- `POST /open-apis/drive/v1/files/create_folder`（drive / files.create_folder）
- `GET /open-apis/drive/v1/files`（drive / files.list）
- `PATCH /open-apis/drive/v1/files/{file_token}`（drive / files.patch）
- `POST /open-apis/drive/v1/metas/batch_query`（drive / metas.batch_query）
- `GET /open-apis/drive/v1/permissions/{token}/members/auth`（drive / permission.members.auth）
- `POST /open-apis/drive/v1/permissions/{token}/members`（drive / permission.members.create）
- `POST /open-apis/drive/v1/permissions/{token}/members/transfer_owner`（drive / permission.members.transfer_owner）
- `GET /open-apis/drive/v1/permissions/{token}/public`（drive / permission.public.get）
- `PATCH /open-apis/drive/v1/permissions/{token}/public`（drive / permission.public.patch）
- `GET /open-apis/drive/v2/quota_details/{quota_detail_id}`（drive / quota_details.get）
- `DELETE /open-apis/drive/v1/user/remove_subscription`（drive / user.remove_subscription）
- `POST /open-apis/drive/v1/user/subscription`（drive / user.subscription）
- `GET /open-apis/drive/v1/user/subscription_status`（drive / user.subscription_status）
- `POST /open-apis/im/v1/chats/{chat_id}/managers/add_managers`（im / chat.managers.add_managers）
- `POST /open-apis/im/v1/chats/{chat_id}/managers/delete_managers`（im / chat.managers.delete_managers）
- `GET /open-apis/im/v1/chats/{chat_id}/members/bots`（im / chat.members.bots）
- `POST /open-apis/im/v1/chats/{chat_id}/members`（im / chat.members.create）
- `DELETE /open-apis/im/v1/chats/{chat_id}/members`（im / chat.members.delete）
- `GET /open-apis/im/v1/chats/{chat_id}/members`（im / chat.members.get）
- `GET /open-apis/im/v1/chats/{chat_id}/moderation`（im / chat.moderation.get）
- `PUT /open-apis/im/v1/chats/{chat_id}/moderation`（im / chat.moderation.update）
- `DELETE /open-apis/im/v1/chats/{chat_id}/nickname`（im / chat.nickname.delete）
- `GET /open-apis/im/v1/chats/{chat_id}/nickname`（im / chat.nickname.get）
- `PUT /open-apis/im/v1/chats/{chat_id}/nickname`（im / chat.nickname.update）
- `POST /open-apis/im/v1/chat_user_setting/batch_query`（im / chat.user_setting.batch_query）
- `POST /open-apis/im/v1/chat_user_setting/batch_update`（im / chat.user_setting.batch_update）
- `POST /open-apis/im/v1/chats`（im / chats.create）
- `GET /open-apis/im/v1/chats/{chat_id}`（im / chats.get）
- `POST /open-apis/im/v1/chats/{chat_id}/link`（im / chats.link）
- `PUT /open-apis/im/v1/chats/{chat_id}`（im / chats.update）
- `POST /open-apis/im/v1/groups/{feed_group_id}/batch_add_item`（im / feed.groups.batch_add_item）
- `POST /open-apis/im/v1/groups/batch_query`（im / feed.groups.batch_query）
- `POST /open-apis/im/v1/groups/{feed_group_id}/batch_remove_item`（im / feed.groups.batch_remove_item）
- `POST /open-apis/im/v1/groups`（im / feed.groups.create）
- `DELETE /open-apis/im/v1/groups/{feed_group_id}`（im / feed.groups.delete）
- `PUT /open-apis/im/v1/groups/{feed_group_id}`（im / feed.groups.update）
- `POST /open-apis/im/v1/images`（im / images.create）
- `DELETE /open-apis/im/v1/messages/{message_id}`（im / messages.delete）
- `POST /open-apis/im/v1/messages/{message_id}/forward`（im / messages.forward）
- `POST /open-apis/im/v1/messages/merge_forward`（im / messages.merge_forward）
- `GET /open-apis/im/v1/messages/{message_id}/read_users`（im / messages.read_users）
- `PATCH /open-apis/im/v1/messages/{message_id}/urgent_app`（im / messages.urgent_app）
- `PATCH /open-apis/im/v1/messages/{message_id}/urgent_phone`（im / messages.urgent_phone）
- `PATCH /open-apis/im/v1/messages/{message_id}/urgent_sms`（im / messages.urgent_sms）
- `POST /open-apis/im/v1/pins`（im / pins.create）
- `DELETE /open-apis/im/v1/pins/{message_id}`（im / pins.delete）
- `GET /open-apis/im/v1/pins`（im / pins.list）
- `POST /open-apis/im/v1/messages/reactions/batch_query`（im / reactions.batch_query）
- `POST /open-apis/im/v1/messages/{message_id}/reactions`（im / reactions.create）
- `DELETE /open-apis/im/v1/messages/{message_id}/reactions/{reaction_id}`（im / reactions.delete）
- `GET /open-apis/im/v1/messages/{message_id}/reactions`（im / reactions.list）
- `POST /open-apis/im/v1/threads/{thread_id}/forward`（im / threads.forward）
- `POST /open-apis/mail/v1/multi_entity/search`（mail / multi_entity.search）
- `POST /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/messages/{message_id}/cancel_scheduled_send`（mail / user_mailbox.drafts.cancel_scheduled_send）
- `POST /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/drafts`（mail / user_mailbox.drafts.create）
- `DELETE /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/drafts/{draft_id}`（mail / user_mailbox.drafts.delete）
- `GET /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/drafts/{draft_id}`（mail / user_mailbox.drafts.get）
- `GET /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/drafts`（mail / user_mailbox.drafts.list）
- `POST /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/drafts/{draft_id}/send`（mail / user_mailbox.drafts.send）
- `PUT /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/drafts/{draft_id}`（mail / user_mailbox.drafts.update）
- `POST /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/event/subscribe`（mail / user_mailbox.event.subscribe）
- `GET /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/event/subscription`（mail / user_mailbox.event.subscription）
- `POST /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/event/unsubscribe`（mail / user_mailbox.event.unsubscribe）
- `POST /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/folders`（mail / user_mailbox.folders.create）
- `DELETE /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/folders/{folder_id}`（mail / user_mailbox.folders.delete）
- `GET /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/folders/{folder_id}`（mail / user_mailbox.folders.get）
- `GET /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/folders`（mail / user_mailbox.folders.list）
- `PATCH /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/folders/{folder_id}`（mail / user_mailbox.folders.patch）
- `POST /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/labels`（mail / user_mailbox.labels.create）
- `DELETE /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/labels/{label_id}`（mail / user_mailbox.labels.delete）
- `GET /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/labels/{label_id}`（mail / user_mailbox.labels.get）
- `GET /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/labels`（mail / user_mailbox.labels.list）
- `PATCH /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/labels/{label_id}`（mail / user_mailbox.labels.patch）
- `POST /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/mail_contacts`（mail / user_mailbox.mail_contacts.create）
- `DELETE /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/mail_contacts/{mail_contact_id}`（mail / user_mailbox.mail_contacts.delete）
- `GET /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/mail_contacts`（mail / user_mailbox.mail_contacts.list）
- `PATCH /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/mail_contacts/{mail_contact_id}`（mail / user_mailbox.mail_contacts.patch）
- `GET /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/messages/{message_id}/attachments/download_url`（mail / user_mailbox.message.attachments.download_url）
- `POST /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/messages/batch_get`（mail / user_mailbox.messages.batch_get）
- `POST /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/messages/batch_modify`（mail / user_mailbox.messages.batch_modify）
- `POST /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/messages/batch_trash`（mail / user_mailbox.messages.batch_trash）
- `GET /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/messages/{message_id}`（mail / user_mailbox.messages.get）
- `GET /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/messages`（mail / user_mailbox.messages.list）
- `PUT /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/messages/{message_id}/modify`（mail / user_mailbox.messages.modify）
- `GET /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/messages/{message_id}/send_status`（mail / user_mailbox.messages.send_status）
- `POST /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/messages/{message_id}/trash`（mail / user_mailbox.messages.trash）
- `POST /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/rules`（mail / user_mailbox.rules.create）
- `DELETE /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/rules/{rule_id}`（mail / user_mailbox.rules.delete）
- `GET /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/rules`（mail / user_mailbox.rules.list）
- `POST /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/rules/reorder`（mail / user_mailbox.rules.reorder）
- `PUT /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/rules/{rule_id}`（mail / user_mailbox.rules.update）
- `GET /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/messages/{message_id}/recall`（mail / user_mailbox.sent_messages.get_recall_detail）
- `POST /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/messages/{message_id}/recall`（mail / user_mailbox.sent_messages.recall）
- `GET /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/settings/send_as`（mail / user_mailbox.settings.send_as）
- `GET /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/templates/{template_id}/attachments/download_url`（mail / user_mailbox.template.attachments.download_url）
- `POST /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/templates`（mail / user_mailbox.templates.create）
- `DELETE /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/templates/{template_id}`（mail / user_mailbox.templates.delete）
- `GET /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/templates/{template_id}`（mail / user_mailbox.templates.get）
- `GET /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/templates`（mail / user_mailbox.templates.list）
- `PUT /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/templates/{template_id}`（mail / user_mailbox.templates.update）
- `POST /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/threads/batch_modify`（mail / user_mailbox.threads.batch_modify）
- `POST /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/threads/batch_trash`（mail / user_mailbox.threads.batch_trash）
- `GET /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/threads/{thread_id}`（mail / user_mailbox.threads.get）
- `GET /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/threads`（mail / user_mailbox.threads.list）
- `POST /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/threads/{thread_id}/modify`（mail / user_mailbox.threads.modify）
- `POST /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/threads/{thread_id}/trash`（mail / user_mailbox.threads.trash）
- `GET /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/accessible_mailboxes`（mail / user_mailboxes.accessible_mailboxes）
- `GET /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/profile`（mail / user_mailboxes.profile）
- `POST /open-apis/mail/v1/user_mailboxes/{user_mailbox_id}/search`（mail / user_mailboxes.search）
- `POST /open-apis/mindnote/v1/mindnotes/{mindnote_id}/nodes`（mindnotes / nodes.create）
- `GET /open-apis/mindnote/v1/mindnotes/{mindnote_id}/nodes`（mindnotes / nodes.list）
- `GET /open-apis/minutes/v1/minutes/{minute_token}`（minutes / minutes.get）
- `DELETE /open-apis/okr/v2/alignments/{alignment_id}`（okr / alignments.delete）
- `GET /open-apis/okr/v2/alignments/{alignment_id}`（okr / alignments.get）
- `GET /open-apis/okr/v2/categories`（okr / categories.list）
- `POST /open-apis/okr/v2/cycles/{cycle_id}/objectives`（okr / cycle.objectives.create）
- `GET /open-apis/okr/v2/cycles/{cycle_id}/objectives`（okr / cycle.objectives.list）
- `GET /open-apis/okr/v2/cycles`（okr / cycles.list）
- `PUT /open-apis/okr/v2/cycles/{cycle_id}/objectives_position`（okr / cycles.objectives_position）
- `PUT /open-apis/okr/v2/cycles/{cycle_id}/objectives_weight`（okr / cycles.objectives_weight）
- `PATCH /open-apis/okr/v2/indicators/{indicator_id}`（okr / indicators.patch）
- `GET /open-apis/okr/v2/key_results/{key_result_id}/indicators`（okr / key_result.indicators.list）
- `DELETE /open-apis/okr/v2/key_results/{key_result_id}`（okr / key_results.delete）
- `GET /open-apis/okr/v2/key_results/{key_result_id}`（okr / key_results.get）
- `PATCH /open-apis/okr/v2/key_results/{key_result_id}`（okr / key_results.patch）
- `POST /open-apis/okr/v2/objectives/{objective_id}/alignments`（okr / objective.alignments.create）
- `GET /open-apis/okr/v2/objectives/{objective_id}/alignments`（okr / objective.alignments.list）
- `GET /open-apis/okr/v2/objectives/{objective_id}/indicators`（okr / objective.indicators.list）
- `POST /open-apis/okr/v2/objectives/{objective_id}/key_results`（okr / objective.key_results.create）
- `GET /open-apis/okr/v2/objectives/{objective_id}/key_results`（okr / objective.key_results.list）
- `DELETE /open-apis/okr/v2/objectives/{objective_id}`（okr / objectives.delete）
- `GET /open-apis/okr/v2/objectives/{objective_id}`（okr / objectives.get）
- `PUT /open-apis/okr/v2/objectives/{objective_id}/key_results_position`（okr / objectives.key_results_position）
- `PUT /open-apis/okr/v2/objectives/{objective_id}/key_results_weight`（okr / objectives.key_results_weight）
- `PATCH /open-apis/okr/v2/objectives/{objective_id}`（okr / objectives.patch）
- `POST /open-apis/sheets/v3/spreadsheets/{spreadsheet_token}/sheets/{sheet_id}/filter`（sheets / spreadsheet.sheet.filters.create）
- `DELETE /open-apis/sheets/v3/spreadsheets/{spreadsheet_token}/sheets/{sheet_id}/filter`（sheets / spreadsheet.sheet.filters.delete）
- `GET /open-apis/sheets/v3/spreadsheets/{spreadsheet_token}/sheets/{sheet_id}/filter`（sheets / spreadsheet.sheet.filters.get）
- `PUT /open-apis/sheets/v3/spreadsheets/{spreadsheet_token}/sheets/{sheet_id}/filter`（sheets / spreadsheet.sheet.filters.update）
- `POST /open-apis/sheets/v3/spreadsheets/{spreadsheet_token}/sheets/{sheet_id}/find`（sheets / spreadsheet.sheets.find）
- `POST /open-apis/sheets/v3/spreadsheets`（sheets / spreadsheets.create）
- `GET /open-apis/sheets/v3/spreadsheets/{spreadsheet_token}`（sheets / spreadsheets.get）
- `PATCH /open-apis/sheets/v3/spreadsheets/{spreadsheet_token}`（sheets / spreadsheets.patch）
- `POST /open-apis/slides_ai/v1/xml_presentations/{xml_presentation_id}/slide`（slides / xml_presentation.slide.create）
- `DELETE /open-apis/slides_ai/v1/xml_presentations/{xml_presentation_id}/slide`（slides / xml_presentation.slide.delete）
- `GET /open-apis/slides_ai/v1/xml_presentations/{xml_presentation_id}/slide`（slides / xml_presentation.slide.get）
- `POST /open-apis/slides_ai/v1/xml_presentations/{xml_presentation_id}/slide/replace`（slides / xml_presentation.slide.replace）
- `GET /open-apis/slides_ai/v1/xml_presentations/{xml_presentation_id}`（slides / xml_presentations.get）
- `POST /open-apis/task/v2/agent/register_agent`（task / agent.register_agent）
- `POST /open-apis/task/v2/agent/update_agent_profile`（task / agent.update_agent_profile）
- `POST /open-apis/task/v2/agent_task_step_info/append_task_steps`（task / agent_task_step_info.append_task_steps）
- `POST /open-apis/task/v2/custom_fields/{custom_field_guid}/options`（task / custom_field_options.create）
- `PATCH /open-apis/task/v2/custom_fields/{custom_field_guid}/options/{option_guid}`（task / custom_field_options.patch）
- `POST /open-apis/task/v2/custom_fields/{custom_field_guid}/add`（task / custom_fields.add）
- `POST /open-apis/task/v2/custom_fields`（task / custom_fields.create）
- `GET /open-apis/task/v2/custom_fields/{custom_field_guid}`（task / custom_fields.get）
- `GET /open-apis/task/v2/custom_fields`（task / custom_fields.list）
- `PATCH /open-apis/task/v2/custom_fields/{custom_field_guid}`（task / custom_fields.patch）
- `POST /open-apis/task/v2/custom_fields/{custom_field_guid}/remove`（task / custom_fields.remove）
- `POST /open-apis/task/v2/tasks/{task_guid}/add_members`（task / members.add）
- `POST /open-apis/task/v2/tasks/{task_guid}/remove_members`（task / members.remove）
- `POST /open-apis/task/v2/sections`（task / sections.create）
- `DELETE /open-apis/task/v2/sections/{section_guid}`（task / sections.delete）
- `GET /open-apis/task/v2/sections/{section_guid}`（task / sections.get）
- `GET /open-apis/task/v2/sections`（task / sections.list）
- `PATCH /open-apis/task/v2/sections/{section_guid}`（task / sections.patch）
- `GET /open-apis/task/v2/sections/{section_guid}/tasks`（task / sections.tasks）
- `POST /open-apis/task/v2/tasks/{task_guid}/subtasks`（task / subtasks.create）
- `GET /open-apis/task/v2/tasks/{task_guid}/subtasks`（task / subtasks.list）
- `POST /open-apis/task/v2/tasklists/{tasklist_guid}/add_members`（task / tasklists.add_members）
- `POST /open-apis/task/v2/tasklists`（task / tasklists.create）
- `DELETE /open-apis/task/v2/tasklists/{tasklist_guid}`（task / tasklists.delete）
- `GET /open-apis/task/v2/tasklists/{tasklist_guid}`（task / tasklists.get）
- `GET /open-apis/task/v2/tasklists`（task / tasklists.list）
- `PATCH /open-apis/task/v2/tasklists/{tasklist_guid}`（task / tasklists.patch）
- `POST /open-apis/task/v2/tasklists/{tasklist_guid}/remove_members`（task / tasklists.remove_members）
- `GET /open-apis/task/v2/tasklists/{tasklist_guid}/tasks`（task / tasklists.tasks）
- `POST /open-apis/task/v2/tasks`（task / tasks.create）
- `DELETE /open-apis/task/v2/tasks/{task_guid}`（task / tasks.delete）
- `GET /open-apis/task/v2/tasks/{task_guid}`（task / tasks.get）
- `GET /open-apis/task/v2/tasks`（task / tasks.list）
- `PATCH /open-apis/task/v2/tasks/{task_guid}`（task / tasks.patch）
- `GET /open-apis/vc/v1/meetings/{meeting_id}`（vc / meeting.get）
- `POST /open-apis/wiki/v2/spaces/{space_id}/members`（wiki / members.create）
- `DELETE /open-apis/wiki/v2/spaces/{space_id}/members/{member_id}`（wiki / members.delete）
- `GET /open-apis/wiki/v2/spaces/{space_id}/members`（wiki / members.list）
- `POST /open-apis/wiki/v2/spaces/{space_id}/nodes/{node_token}/copy`（wiki / nodes.copy）
- `POST /open-apis/wiki/v2/spaces/{space_id}/nodes`（wiki / nodes.create）
- `GET /open-apis/wiki/v2/spaces/{space_id}/nodes`（wiki / nodes.list）
- `POST /open-apis/wiki/v2/spaces`（wiki / spaces.create）
- `GET /open-apis/wiki/v2/spaces/{space_id}`（wiki / spaces.get）
- `GET /open-apis/wiki/v2/spaces/get_node`（wiki / spaces.get_node）
- `GET /open-apis/wiki/v2/spaces`（wiki / spaces.list）

每次上游注册表（registry）版本变化时，由 CI 自动在顶部前置接口级 diff
（新增 / 移除 / 变更的接口及字段级详情）。首次导入的全量条目由 CI 引导
运行（bootstrap）自动生成。
