translations = {
    "en": {  # English
        "info_dict": {
            'snap': '''The /snap command is used for generating text.\nFor example: /snap what is java.

This command has a daily limit of *30* uses. For subscribers, the limit increases to *500* uses.

All languages are supported with this command.''',
            'image': '''The /image command generates images. After using the /image command, you need to input any request\nThe *more detailed* your request, the *better the result*. After submitting your request, you'll need to select a model and the number of images.

There are daily limits: *40* images per day and up to 4 images per generation. Not all models are available to free users.

For subscribers: *1000* images per day, 10 images per generation, and access to all models. This command supports all languages.''',
            'image2': '''The /image2 command is currently in a test phase and may be removed or replaced. After using /image2, you need to input any request\nThe *more detailed* your request, the *better the result*.

It generates 4 images for everyone and has a daily limit of *20* images. For subscribers: *40* images. This command supports all languages.''',
            'vision': '''The /vision command is used for recognizing objects in images. After using /vision, you must send the bot an image for recognition.

*Important!* When sending the image, you can *specify* a specific request in the "caption" field. For example, "what is in the upper-right corner of the image."\nIf no specific request is provided in the caption, *the bot will default to describing the image in English.*

This command has a daily limit of *10* uses. For subscribers: *300* uses. The request language can be any.''',
            'upscale': '''The /upscale command increases an image to *2X* resolution using Snap-AI to enhance the image quality.
After using the /upscale command, you must send a photo for upscaling.

*Important!* The minimum resolution supported for width and/or height is *216 pixels.*
This command has a daily limit of *5* uses. For subscribers: *20* uses. The request language can be any.''',
            'background': '''The /background command changes the background of a photo by highlighting the object or objects.
After using the /background command, you’ll need to enter a prompt describing the background you want to use.

Then, send the photo on which you'd like to change the background. The bot will send you *4* variations based on your request.

This command has daily limits: *20* photos for standard users and *40* photos for subscribers.''',
            'expand': '''The command /expand allows you to enlarge your image using AI. After issuing the /expand command, you need to send a photo.

*Important!* The area of the original image must be more than 15% of the canvas area.

This command has a daily limit of *20* images per day, while subscribers can process up to *60* images per day.''',
            'reimage': '''The /reimage command uses similar image generation. After using this command, you need to enter a prompt.

*Important!* For better results, describe what is depicted in the image you want to process. After that, send the image.

This command has daily limits: *20* images for regular users and *60* images for subscribers.''',
            'search': '''Search for information on the internet.
The command works by utilizing the resources of the /snap command.
And the limits are also applied from the /snap command.''',
            'v': '''The /v command displays the bot's current version and updates.''',
            'my_id': '''The /my_id command shows your user_id.''',
            'reg': '''The /reg command registers you in the Snaplix bot.''',
            'sub': '''The /sub command checks if you have an active subscription.''',
            'get_sub': '''The /get_sub command allows you to purchase a subscription.''',
            'limits': '''The /limits command displays your current command usage limits.''',
            'ping': '''The /ping command checks the bot's connection status.''',
            'info': '''The /info command shows a detailed description of the command ''',
        },
        "switch_lang": "You have switched to 🇺🇸 English.",
        "blocked_message": "You are temporarily blocked. Please try again in 10 minutes.",
        "registration_in_progress": "You are already in the process of registration. Please complete it.",
        "already_registered": "You are already registered.",
        "captcha": "Enter text from captcha",
        "successful_registration": "You have *successfully registered!*",
        "invitee_registered": "Your invitee has registered!",
        "failed_registration": "You have *failed registration* after 4 attempts.",
        "incorrect_attempts": "Incorrect. Attempts left: {attempts}.",
        "donate_amount": "Please specify the donation amount between 1 and 100 $USD. Usage: /donate <amount>",
        "invalid_donate_amount": "Please specify a valid donation amount between 1 and 100 dollars.",
        "donate_description": "By donating money, you help the Snaplix project develop.\nFor a donation, you receive Snap Coins. *1 $USD = 10 Snap Coins*\n\nYou can also get Snap Coins for inviting people. *5 people = 50 Snap Coins*\nSnap Coins are used in the *premium functions* of the project\n\nYour *Link* for donate:\n{link}",
        "donate_thank_you": "*Thank you very much for supporting the project*\nYou receive {amount} Snap Coins\nYour order id: *{order_id}*",
        "check_payment_later": "Retry later...",
        "order_not_paid": "The donation *has not* been paid yet.\nPlease, use \"*Check Payment Status*\" button *after* successful payment of the order.",
        "order_status": "Status: *{status}*",
        "info_command_usage": "This command is used to describe all the bot commands in detail. To find out information about a command, use /info <bot command>",
        "command_not_found": "This command does not exist.",
        "invite_link": "Your invite link - {link}",
        "my_invites": "Your invites - *{invites}*",
        "my_coins": "You have *{coins}* Snap Coins on your account",
        "invite_reward": "Congratulations! Your account has been increased by 50 Snap Coins for 5 invites",
        "less_than_5_invites": "You have less than *5* invited people",
        "donate_usage": "/donate <amount>",
        "invalid_amount": "Amount must be a positive integer between 1 and 1000.",
        "coins_given": "Given {amount} coins to user: {user_id}",
        "unfreeze_usage": "/unfreeze <user_id>",
        "user_unfreezed": "User {user_id} has been unfreezed",
        "my_id": "Your ID: {user_id}",
        "search_limit": "You can use the /search command only once per *minute.*",
        "snap_ai_usage": "To use Snap-AI, please enter /snap <your request>",
        "thinking": "*Thinking...*",
        "search_usage": "To use AI-Search, please enter /search <your request>",
        "checking_request": "*Checking request...*",
        "unethical_request": "*Sorry, I can't help with this request*",
        "searching": "*Searching...*",
        "send_image": "*Send only 1 image*",
        "enter_prompt": "*Enter prompt for generation*",
        "generating": "*Generating...*",
        "analyzing_image": "*Analyzing image...*",
        "whats_in_this_image": "What's in this image?",
        "choice_model": "*Choice the model of generation*",
        "choice_number": "*Choice the number of generation*",
        "msg_incorrect_use": "Incorrect use /msg",
        "messages_sent": "Messages sent to {count} users.",
        "stats_message": (
            "Total users: {total_users}\n"
            "Frozen users: {frozen_users}\n"
            "Processed users: {processing_users}\n"
            "Sub users: {paying_users}\n\n"
            "Limits:\n{limits_message}"
        ),
        "enter_prompt_background": "*Enter prompt for background*",
        "enter_prompt_reference": "*Enter prompt for reference-image*",
        "expanding": "*Expanding...*",
        "register_first": "To use bot commands, register with the /reg command",
        "already_registered": "You are already registered.",
        "request_processing": "Your request is being processed. Please wait.",
        "previous_donation_pending": "You have not yet paid for the previous donation.",
        "limit_reached": "You have reached the limit of {max_limit} for today.",
        "not_a_text": "This is not a text",
        "not_an_image": "This is not an image",
        "too_many_images": "Too many images",
        "image_generation_model": "Image Generation Model",
        "text_generation_model": "Text Generation Model",
        "config_menu": "Config menu:\nImage Model: {img_model}\nText Model: {txt_model}",
        "config_success": "Your configuration has been successfully set!"
    },
    "ru": {  # Русский
        "info_dict": {
            'snap': '''Команда /snap используется для генерации текста.\nНапример: /snap что такое java.

Эта команда имеет дневной лимит в *30* использований. Для подписчиков лимит увеличивается до *500* использований.

Все языки поддерживаются с этой командой.''',
            'image': '''Команда /image генерирует изображения. После использования команды /image вам нужно ввести любой запрос\nЧем *подробнее* ваш запрос, тем *лучше результат*. После отправки запроса вам нужно выбрать модель и количество изображений.

Существуют дневные лимиты: *40* изображений в день и до 4 изображений за генерацию. Не все модели доступны бесплатным пользователям.

Для подписчиков: *1000* изображений в день, 10 изображений за генерацию и доступ ко всем моделям. Эта команда поддерживает все языки.''',
            'image2': '''Команда /image2 в настоящее время находится в тестовой фазе и может быть удалена или заменена. После использования /image2 вам нужно ввести любой запрос\nЧем *подробнее* ваш запрос, тем *лучше результат*.

Она генерирует 4 изображения для всех и имеет дневной лимит в *20* изображений. Для подписчиков: *40* изображений. Эта команда поддерживает все языки.''',
            'vision': '''Команда /vision используется для распознавания объектов на изображениях. После использования /vision вам нужно отправить боту изображение для распознавания.

*Важно!* При отправке изображения вы можете *указать* конкретный запрос в поле "подпись". Например, "что находится в правом верхнем углу изображения."\nЕсли конкретный запрос не указан в подписи, *бот по умолчанию опишет изображение на английском языке.*

Эта команда имеет дневной лимит в *10* использований. Для подписчиков: *300* использований. Язык запроса может быть любым.''',
            'upscale': '''Команда /upscale увеличивает изображение в *2 раза* с помощью Snap-AI для улучшения качества изображения.
После использования команды /upscale вам нужно отправить фото для увеличения.

*Важно!* Минимальное поддерживаемое разрешение для ширины и/или высоты составляет *216 пикселей.*
Эта команда имеет дневной лимит в *5* использований. Для подписчиков: *20* использований. Язык запроса может быть любым.''',
            'background': '''Команда /background изменяет фон фотографии, выделяя объект или объекты.
После использования команды /background вам нужно ввести запрос, описывающий фон, который вы хотите использовать.

Затем отправьте фото, на котором хотите изменить фон. Бот отправит вам *4* варианта на основе вашего запроса.

Эта команда имеет дневные лимиты: *20* фото для обычных пользователей и *40* фото для подписчиков.''',
            'expand': '''Команда /expand позволяет увеличить ваше изображение с помощью ИИ. После использования команды /expand вам нужно отправить фото.

*Важно!* Площадь оригинального изображения должна быть более 15% от площади холста.

Эта команда имеет дневной лимит в *20* изображений в день, в то время как подписчики могут обработать до *60* изображений в день.''',
            'reimage': '''Команда /reimage использует подобную генерацию изображений. После использования этой команды вам нужно ввести запрос.

*Важно!* Для лучших результатов опишите, что изображено на изображении, которое вы хотите обработать. После этого отправьте изображение.

Эта команда имеет дневные лимиты: *20* изображений для обычных пользователей и *60* изображений для подписчиков.''',
            'search': '''Поиск информации в интернете.
Команда работает, используя ресурсы команды /snap.
И лимиты также применяются от команды /snap.''',
            'v': '''Команда /v отображает текущую версию бота и обновления.''',
            'my_id': '''Команда /my_id показывает ваш user_id.''',
            'reg': '''Команда /reg регистрирует вас в боте Snaplix.''',
            'sub': '''Команда /sub проверяет, есть ли у вас активная подписка.''',
            'get_sub': '''Команда /get_sub позволяет вам приобрести подписку.''',
            'limits': '''Команда /limits отображает ваши текущие лимиты использования команд.''',
            'ping': '''Команда /ping проверяет статус подключения бота.''',
            'info': '''Команда /info показывает подробное описание команды ''',
        },
        "switch_lang": "Вы переключились на 🇷🇺 русский язык.",
        "blocked_message": "Вы временно заблокированы. Пожалуйста, попробуйте снова через 10 минут.",
        "registration_in_progress": "Вы уже находитесь в процессе регистрации. Пожалуйста, завершите его.",
        "already_registered": "Вы уже зарегистрированы.",
        "captcha": "Введите текст с картинки",
        "successful_registration": "Вы успешно зарегистрировались!",
        "invitee_registered": "Ваш приглашенный зарегистрировался!",
        "failed_registration": "Вы не смогли зарегистрироваться после 4 попыток.",
        "incorrect_attempts": "Неправильно. Осталось попыток: {attempts}.",
        "donate_amount": "Пожалуйста, укажите сумму пожертвования от 1 до 100 $USD. Использование: /donate <amount>",
        "invalid_donate_amount": "Пожалуйста, укажите корректную сумму пожертвования от 1 до 100 долларов.",
        "donate_description": "Пожертвовав деньги, вы помогаете развитию проекта Snaplix.\nЗа пожертвование вы получаете Snap Coins. *1 $USD = 10 Snap Coins*\n\nВы также можете получать Snap Coins за приглашение людей. *5 человек = 50 Snap Coins*\nSnap Coins используются в *премиум-функциях* проекта\n\nВаша *ссылка* для пожертвования:\n{link}",
        "donate_thank_you": "*Большое спасибо за поддержку проекта*\nВы получаете {amount} Snap Coins\nВаш номер заказа: *{order_id}*",
        "check_payment_later": "Попробуйте позже...",
        "order_not_paid": "Пожертвование *не* было оплачено.\nПожалуйста, используйте кнопку \"*Check Payment Status*\" *после* успешной оплаты заказа.",
        "order_status": "Статус: *{status}*",
        "info_command_usage": "Эта команда используется для описания всех команд бота. Чтобы узнать информацию о команде, используйте /info <bot command>",
        "command_not_found": "Эта команда не существует.",
        "invite_link": "Ваша пригласительная ссылка - {link}",
        "my_invites": "Ваши приглашения - *{invites}*",
        "my_coins": "У вас *{coins}* Snap Coins на вашем аккаунте",
        "invite_reward": "Поздравляем! Ваш аккаунт был увеличен на 50 Snap Coins за 5 приглашений",
        "less_than_5_invites": "У вас меньше *5* приглашенных людей",
        "donate_usage": "/donate <amount>",
        "invalid_amount": "Сумма должна быть положительным целым числом от 1 до 1000.",
        "coins_given": "Выдано {amount} монет пользователю: {user_id}",
        "unfreeze_usage": "/unfreeze <user_id>",
        "user_unfreezed": "Пользователь {user_id} был разморожен",
        "my_id": "Ваш ID: {user_id}",
        "search_limit": "Вы можете использовать команду /search только раз в *минуту.*",
        "snap_ai_usage": "Чтобы использовать Snap-AI, введите /snap <ваш запрос>",
        "thinking": "*Думаю...*",
        "search_usage": "Чтобы использовать AI-Search, пожалуйста, введите /search <ваш запрос>",
        "checking_request": "*Проверка запроса...*",
        "unethical_request": "*Извините, я не могу помочь с этим запросом*",
        "searching": "*Поиск...*",
        "send_image": "*Отправьте только 1 изображение*",
        "enter_prompt": "*Введите запрос для генерации*",
        "generating": "*Генерация...*",
        "analyzing_image": "*Анализ изображения...*",
        "whats_in_this_image": "Что на этом изображении?",
        "choice_model": "*Выберите модель для генерации*",
        "choice_number": "*Выберите количество генерации*",
        "msg_incorrect_use": "Неправильное использование /msg",
        "messages_sent": "Сообщения отправлены {count} пользователям.",
        "stats_message": (
            "Всего пользователей: {total_users}\n"
            "Замороженные пользователи: {frozen_users}\n"
            "Обработанные пользователи: {processing_users}\n"
            "Пользователи с подпиской: {paying_users}\n\n"
            "Лимиты:\n{limits_message}"
        ),
        "enter_prompt_background": "*Введите запрос для фона*",
        "enter_prompt_reference": "*Введите запрос для референс-изображения*",
        "expanding": "*Расширение...*",
        "register_first": "Чтобы использовать команды бота, зарегистрируйтесь с помощью команды /reg",
        "already_registered": "Вы уже зарегистрированы.",
        "request_processing": "Ваш запрос обрабатывается. Пожалуйста, подождите.",
        "previous_donation_pending": "Вы еще не оплатили предыдущее пожертвование.",
        "limit_reached": "Вы достигли лимита {max_limit} на сегодня.",
        "not_a_text": "Это не текст",
        "not_an_image": "Это не изображение",
        "too_many_images": "Слишком много изображений",
        "image_generation_model": "Модель генерации изображений",
        "text_generation_model": "Модель генерации текста",
        "config_menu": "Меню настроек:\nМодель изображения: {img_model}\nМодель текста: {txt_model}",
        "config_success": "Ваша конфигурация успешно установлена!",
    },
    "zh": {  # 中文 (Chinese - Simplified)
        "info_dict": {
            'snap': '''/snap 命令用于生成文本。\n例如：/snap 什么是 Java。

该命令每日使用限制为 *30* 次。订阅用户的限制增加到 *500* 次。

该命令支持所有语言。''',
            'image': '''/image 命令生成图像。使用 /image 命令后，您需要输入任何请求\n请求越 *详细*，结果越 *好*。提交请求后，您需要选择模型和图像数量。

每日限制：*40* 张图像每天，每次生成最多 4 张图像。并非所有模型都对免费用户开放。

订阅用户：每日 *1000* 张图像，每次生成 10 张图像，并可访问所有模型。该命令支持所有语言。''',
            'image2': '''/image2 命令目前处于测试阶段，可能会被移除或替换。使用 /image2 后，您需要输入任何请求\n请求越 *详细*，结果越 *好*。

它为每个人生成 4 张图像，每日限制为 *20* 张图像。订阅用户：*40* 张图像。该命令支持所有语言。''',
            'vision': '''/vision 命令用于识别图像中的对象。使用 /vision 后，您需要向机器人发送一张图像进行识别。

*重要！* 发送图像时，您可以在“标题”字段中 *指定* 具体请求。例如，“图像右上角有什么。”\n如果标题中未提供具体请求，*机器人将默认用英语描述图像*。

该命令每日使用限制为 *10* 次。订阅用户：*300* 次。请求语言可以是任何语言。''',
            'upscale': '''/upscale 命令使用 Snap-AI 将图像放大到 *2X* 分辨率，以提高图像质量。
使用 /upscale 命令后，您需要发送一张照片进行放大。

*重要！* 支持的最小分辨率为宽度和/或高度 *216 像素*。
该命令每日使用限制为 *5* 次。订阅用户：*20* 次。请求语言可以是任何语言。''',
            'background': '''/background 命令通过突出显示对象或对象来更改照片的背景。
使用 /background 命令后，您需要输入一个提示，描述您想要使用的背景。

然后，发送您想要更改背景的照片。机器人将根据您的请求发送 *4* 个变体。

该命令的每日限制：标准用户 *20* 张照片，订阅用户 *40* 张照片。''',
            'expand': '''/expand 命令允许您使用 AI 放大图像。使用 /expand 命令后，您需要发送照片。

*重要！* 原始图像的面积必须超过画布面积的 15%。

该命令每日限制为 *20* 张图像，而订阅用户每天可处理多达 *60* 张图像。''',
            'reimage': '''/reimage 命令使用类似的图像生成。使用该命令后，您需要输入一个提示。

*重要！* 为获得更好的结果，请描述您想要处理的图像中的内容。然后，发送图像。

该命令的每日限制：普通用户 *20* 张图像，订阅用户 *60* 张图像。''',
            'search': '''在互联网上搜索信息。
该命令通过利用 /snap 命令的资源来工作。
并且限制也适用于 /snap 命令。''',
            'v': '''/v 命令显示机器人的当前版本和更新。''',
            'my_id': '''/my_id 命令显示您的 user_id。''',
            'reg': '''/reg 命令在 Snaplix 机器人中注册您。''',
            'sub': '''/sub 命令检查您是否有活动订阅。''',
            'get_sub': '''/get_sub 命令允许您购买订阅。''',
            'limits': '''/limits 命令显示您当前的命令使用限制。''',
            'ping': '''/ping 命令检查机器人的连接状态。''',
            'info': '''/info 命令显示命令的详细描述 ''',
        },
        "switch_lang": "您已切换到 🇨🇳 中文。",
        "blocked_message": "您已被暂时封锁，请在 10 分钟后重试。",
        "registration_in_progress": "您已经在注册过程中。请完成它。",
        "already_registered": "您已注册。",
        "captcha": "输入验证码文本",
        "successful_registration": "您已成功注册！",
        "invitee_registered": "您的邀请者已注册！",
        "failed_registration": "您在 4 次尝试后未能注册。",
        "incorrect_attempts": "不正确。剩余尝试次数：{attempts}。",
        "donate_amount": "请指定 1 到 100 美元之间的捐款金额。用法：/donate <amount>",
        "invalid_donate_amount": "请指定 1 到 100 美元之间的有效捐款金额。",
        "donate_description": "通过捐款，您帮助 Snaplix 项目发展。\n捐款后您将收到 Snap Coins。*1 美元 = 10 Snap Coins*\n\n您也可以通过邀请人获得 Snap Coins。*5 人 = 50 Snap Coins*\nSnap Coins 用于项目的 *高级功能*\n\n您的 *捐款链接*：\n{link}",
        "donate_thank_you": "*非常感谢您对项目的支持*\n您获得 {amount} Snap Coins\n您的订单号：*{order_id}*",
        "check_payment_later": "稍后重试...",
        "order_not_paid": "捐款 *尚未*支付。\n请在成功支付订单后使用“*检查支付状态*”按钮。",
        "order_status": "状态：*{status}*",
        "info_command_usage": "此命令用于详细描述所有机器人命令。要查找有关命令的信息，请使用 /info <bot command>",
        "command_not_found": "此命令不存在。",
        "invite_link": "您的邀请链接 - {link}",
        "my_invites": "您的邀请 - *{invites}*",
        "my_coins": "您有 *{coins}* Snap Coins 在您的账户上",
        "invite_reward": "恭喜！您的账户因 5 次邀请增加了 50 Snap Coins",
        "less_than_5_invites": "您邀请的人数少于 *5* 人",
        "donate_usage": "/donate <amount>",
        "invalid_amount": "金额必须是 1 到 1000 之间的正整数。",
        "coins_given": "已给予用户 {user_id} {amount} 枚币",
        "unfreeze_usage": "/unfreeze <user_id>",
        "user_unfreezed": "用户 {user_id} 已解冻",
        "my_id": "您的 ID: {user_id}",
        "search_limit": "您只能每 *分钟* 使用一次 /search 命令。",
        "search_usage": "要使用 AI-Search，请输入 /search <您的请求>",
        "snap_ai_usage": "要使用 Snap-AI，请输入 /snap <您的请求>",
        "thinking": "*思考中...*",
        "checking_request": "*检查请求...*",
        "unethical_request": "*抱歉，我无法帮助此请求*",
        "searching": "*搜索中...*",
        "send_image": "*只发送 1 张图片*",
        "enter_prompt": "*输入生成提示*",
        "generating": "*生成中...*",
        "analyzing_image": "*分析图像...*",
        "whats_in_this_image": "这张图片里有什么？",
        "choice_model": "*选择生成模型*",
        "choice_number": "*选择生成数量*",
        "msg_incorrect_use": "不正确的使用 /msg",
        "messages_sent": "消息已发送给 {count} 个用户。",
        "stats_message": (
            "总用户数: {total_users}\n"
            "被冻结的用户: {frozen_users}\n"
            "处理中的用户: {processing_users}\n"
            "订阅用户: {paying_users}\n\n"
            "限制:\n{limits_message}"
        ),
        "enter_prompt_background": "*输入背景提示*",
        "enter_prompt_reference": "*输入参考图像提示*",
        "expanding": "*扩展中...*",
        "register_first": "要使用机器人命令，请先使用 /reg 命令注册",
        "already_registered": "您已经注册。",
        "request_processing": "您的请求正在处理中。请稍候。",
        "previous_donation_pending": "您尚未支付上一次捐款。",
        "limit_reached": "您今天的限额已达到 {max_limit}。",
        "not_a_text": "这不是文本",
        "not_an_image": "这不是图像",
        "too_many_images": "图像过多",
        "image_generation_model": "图像生成模型",
        "text_generation_model": "文本生成模型",
        "config_menu": "配置菜单:\n图像模型: {img_model}\n文本模型: {txt_model}",
        "config_success": "您的配置已成功设置！",
    },
    "es": {  # Español (Spanish)
        "info_dict": {
            'snap': '''El comando /snap se usa para generar texto.\nPor ejemplo: /snap qué es java.

Este comando tiene un límite diario de *30* usos. Para suscriptores, el límite aumenta a *500* usos.

Todos los idiomas son compatibles con este comando.''',
            'image': '''El comando /image genera imágenes. Después de usar el comando /image, debe ingresar cualquier solicitud\nCuanto más *detallada* sea su solicitud, *mejor será el resultado*. Después de enviar su solicitud, deberá seleccionar un modelo y la cantidad de imágenes.

Hay límites diarios: *40* imágenes por día y hasta 4 imágenes por generación. No todos los modelos están disponibles para usuarios gratuitos.

Para suscriptores: *1000* imágenes por día, 10 imágenes por generación y acceso a todos los modelos. Este comando admite todos los idiomas.''',
            'image2': '''El comando /image2 está actualmente en fase de prueba y puede ser eliminado o reemplazado. Después de usar /image2, debe ingresar cualquier solicitud\nCuanto más *detallada* sea su solicitud, *mejor será el resultado*.

Genera 4 imágenes para todos y tiene un límite diario de *20* imágenes. Para suscriptores: *40* imágenes. Este comando admite todos los idiomas.''',
            'vision': '''El comando /vision se usa para reconocer objetos en imágenes. Después de usar /vision, debe enviar al bot una imagen para su reconocimiento.

*Importante!* Al enviar la imagen, puede *especificar* una solicitud específica en el campo "subtítulo". Por ejemplo, "qué hay en la esquina superior derecha de la imagen."\nSi no se proporciona una solicitud específica en el subtítulo, *el bot describirá la imagen en inglés de forma predeterminada*.

Este comando tiene un límite diario de *10* usos. Para suscriptores: *300* usos. El idioma de la solicitud puede ser cualquiera.''',
            'upscale': '''El comando /upscale aumenta una imagen a una resolución *2X* utilizando Snap-AI para mejorar la calidad de la imagen.
Después de usar el comando /upscale, debe enviar una foto para aumentar su tamaño.

*Importante!* La resolución mínima compatible para el ancho y/o la altura es de *216 píxeles.*
Este comando tiene un límite diario de *5* usos. Para suscriptores: *20* usos. El idioma de la solicitud puede ser cualquiera.''',
            'background': '''El comando /background cambia el fondo de una foto resaltando el objeto o los objetos.
Después de usar el comando /background, deberá ingresar un mensaje que describa el fondo que desea usar.

Luego, envíe la foto en la que desea cambiar el fondo. El bot le enviará *4* variaciones basadas en su solicitud.

Este comando tiene límites diarios: *20* fotos para usuarios estándar y *40* fotos para suscriptores.''',
            'expand': '''El comando /expand le permite ampliar su imagen usando IA. Después de emitir el comando /expand, debe enviar una foto.

*Importante!* El área de la imagen original debe ser más del 15% del área del lienzo.

Este comando tiene un límite diario de *20* imágenes por día, mientras que los suscriptores pueden procesar hasta *60* imágenes por día.''',
            'reimage': '''El comando /reimage usa una generación de imágenes similar. Después de usar este comando, debe ingresar un mensaje.

*Importante!* Para obtener mejores resultados, describa qué se muestra en la imagen que desea procesar. Después de eso, envíe la imagen.

Este comando tiene límites diarios: *20* imágenes para usuarios regulares y *60* imágenes para suscriptores.''',
            'search': '''Buscar información en Internet.
El comando funciona utilizando los recursos del comando /snap.
Y los límites también se aplican desde el comando /snap.''',
            'v': '''El comando /v muestra la versión actual del bot y las actualizaciones.''',
            'my_id': '''El comando /my_id muestra su user_id.''',
            'reg': '''El comando /reg lo registra en el bot Snaplix.''',
            'sub': '''El comando /sub verifica si tiene una suscripción activa.''',
            'get_sub': '''El comando /get_sub le permite comprar una suscripción.''',
            'limits': '''El comando /limits muestra sus límites de uso de comandos actuales.''',
            'ping': '''El comando /ping verifica el estado de la conexión del bot.''',
            'info': '''El comando /info muestra una descripción detallada del comando ''',
        },
        "switch_lang": "Has cambiado a 🇪🇸 español.",
        "blocked_message": "Está bloqueado temporalmente. Inténtelo de nuevo en 10 minutos.",
        "registration_in_progress": "Ya está en el proceso de registro. Por favor, complételo.",
        "already_registered": "Ya está registrado.",
        "captcha": "Introduzca el texto del captcha",
        "successful_registration": "¡Te has registrado *exitosamente*!",
        "invitee_registered": "¡Tu invitado se ha registrado!",
        "failed_registration": "Ha *fallado el registro* después de 4 intentos.",
        "incorrect_attempts": "Incorrecto. Intentos restantes: {attempts}.",
        "donate_amount": "Por favor, especifique la cantidad de donación entre 1 y 100 $USD. Uso: /donate <amount>",
        "invalid_donate_amount": "Por favor, especifique una cantidad de donación válida entre 1 y 100 dólares.",
        "donate_description": "Al donar dinero, ayudas al proyecto Snaplix a desarrollarse.\nPor una donación, recibes Snap Coins. *1 $USD = 10 Snap Coins*\n\nTambién puedes obtener Snap Coins invitando a personas. *5 personas = 50 Snap Coins*\nLas Snap Coins se usan en las *funciones premium* del proyecto\n\nTu *Link* para donar:\n{link}",
        "donate_thank_you": "*Muchas gracias por apoyar el proyecto*\nRecibes {amount} Snap Coins\nTu ID de pedido: *{order_id}*",
        "check_payment_later": "Inténtelo más tarde...",
        "order_not_paid": "La donación *no* ha sido pagada todavía.\nPor favor, use el botón \"*Check Payment Status*\" *después* de la exitosa realización del pago del pedido.",
        "order_status": "Estado: *{status}*",
        "info_command_usage": "Este comando se usa para describir todos los comandos del bot en detalle. Para encontrar información sobre un comando, use /info <bot command>",
        "command_not_found": "Este comando no existe.",
        "invite_link": "Tu enlace de invitación - {link}",
        "my_invites": "Tus invitaciones - *{invites}*",
        "my_coins": "Tienes *{coins}* Snap Coins en tu cuenta",
        "invite_reward": "¡Felicidades! Tu cuenta ha aumentado 50 Snap Coins por 5 invitaciones",
        "less_than_5_invites": "Tienes menos de *5* personas invitadas",
        "donate_usage": "/donate <amount>",
        "invalid_amount": "La cantidad debe ser un número entero positivo entre 1 y 1000.",
        "coins_given": "Dado {amount} monedas al usuario: {user_id}",
        "unfreeze_usage": "/unfreeze <user_id>",
        "user_unfreezed": "El usuario {user_id} ha sido descongelado",
        "my_id": "Tu ID: {user_id}",
        "search_limit": "Puedes usar el comando /search solo una vez por *minuto.*",
        "search_usage": "Para usar AI-Search, por favor ingresa /search <tu solicitud>",
        "snap_ai_usage": "Para usar Snap-AI, ingrese /snap <su solicitud>",
        "thinking": "*Pensando...*",
        "checking_request": "*Revisando solicitud...*",
        "unethical_request": "*Lo siento, no puedo ayudar con esta solicitud*",
        "searching": "*Buscando...*",
        "send_image": "*Envía solo 1 imagen*",
        "enter_prompt": "*Introduce el prompt para la generación*",
        "generating": "*Generando...*",
        "analyzing_image": "*Analizando imagen...*",
        "whats_in_this_image": "¿Qué hay en esta imagen?",
        "choice_model": "*Elige el modelo de generación*",
        "choice_number": "*Elige el número de generación*",
        "msg_incorrect_use": "Uso incorrecto /msg",
        "messages_sent": "Mensajes enviados a {count} usuarios.",
        "stats_message": (
            "Total de usuarios: {total_users}\n"
            "Usuarios congelados: {frozen_users}\n"
            "Usuarios procesados: {processing_users}\n"
            "Usuarios suscritos: {paying_users}\n\n"
            "Límites:\n{limits_message}"
        ),
        "enter_prompt_background": "*Introduce el prompt para el fondo*",
        "enter_prompt_reference": "*Introduce el prompt para la imagen de referencia*",
        "expanding": "*Expandiendo...*",
        "register_first": "Para usar los comandos del bot, regístrese con el comando /reg",
        "already_registered": "Ya está registrado.",
        "request_processing": "Su solicitud está siendo procesada. Por favor, espere.",
        "previous_donation_pending": "Aún no ha pagado la donación anterior.",
        "limit_reached": "Ha alcanzado el límite de {max_limit} para hoy.",
        "not_a_text": "Esto no es un texto",
        "not_an_image": "Esto no es una imagen",
        "too_many_images": "Demasiadas imágenes",
        "image_generation_model": "Modelo de Generación de Imágenes",
        "text_generation_model": "Modelo de Generación de Texto",
        "config_menu": "Menú de configuración:\nModelo de Imagen: {img_model}\nModelo de Texto: {txt_model}",
        "config_success": "¡Su configuración se ha establecido correctamente!",
    },
    "hi": {  # हिंदी (Hindi)
        "info_dict": {
            'snap': '''/snap कमांड टेक्स्ट उत्पन्न करने के लिए उपयोग किया जाता है।\nउदाहरण: /snap जावा क्या है।

इस कमांड की दैनिक लिमिट *30* उपयोग है। सदस्यों के लिए लिमिट *500* उपयोग तक बढ़ जाता है।

इस कमांड के साथ सभी भाषाएँ समर्थित हैं।''',
            'image': '''/image कमांड छवियाँ उत्पन्न करता है। /image कमांड का उपयोग करने के बाद, आपको किसी भी अनुरोध दर्ज करना होगा\nआपका अनुरोध जितना *विस्तृत* होगा, परिणाम उतना ही *बेहतर* होगा। अपने अनुरोध को सबमिट करने के बाद, आपको एक मॉडल और छवियों की संख्या चुननी होगी।

दैनिक लिमिट हैं: *40* छवियाँ प्रतिदिन और प्रति उत्पादन के लिए कम से कम 4 छवियाँ। सभी मॉडल मुफ्त उपयोगकर्ताओं के लिए उपलब्ध नहीं हैं।

सदस्यों के लिए: *1000* छवियाँ प्रतिदिन, प्रति उत्पादन 10 छवियाँ, और सभी मॉडल तक पहुँच। यह कमांड सभी भाषाओं का समर्थन करता है।''',
            'image2': '''/image2 कमांड वर्तमान में परीक्षण चरण में है और इसे हटाया या बदला जा सकता है। /image2 का उपयोग करने के बाद, आपको किसी भी अनुरोध दर्ज करना होगा\nआपका अनुरोध जितना *विस्तृत* होगा, परिणाम उतना ही *बेहतर* होगा।

यह हर किसी के लिए 4 छवियाँ उत्पन्न करता है और इसकी दैनिक लिमिट *20* छवियाँ है। सदस्यों के लिए: *40* छवियाँ। यह कमांड सभी भाषाओं का समर्थन करता है।''',
            'vision': '''/vision कमांड छवियों में वस्तुओं को पहचानने के लिए उपयोग किया जाता है। /vision का उपयोग करने के बाद, आपको पहचान के लिए बॉट को एक छवि भेजनी होगी।

*महत्वपूर्ण!* छवि भेजते समय, आप "कैप्शन" फ़ील्ड में एक विशिष्ट अनुरोध दर्ज कर सकते हैं। उदाहरण के लिए, "छवि के ऊपरी दाएँ कोने में क्या है।"\nअगर कैप्शन में कोई विशिष्ट अनुरोध नहीं दिया गया है, तो *बॉट छवि का वर्णन डिफ़ॉल्ट रूप से अंग्रेजी में करेगा*।

इस कमांड की दैनिक लिमिट *10* उपयोग है। सदस्यों के लिए: *300* उपयोग। अनुरोध भाषा कोई भी हो सकती है।''',
            'upscale': '''/upscale कमांड Snap-AI का उपयोग करके छवि की रिज़ॉल्यूशन को *2X* तक बढ़ाता है ताकि छवि की गुणवत्ता बेहतर हो सके।
/upscale कमांड का उपयोग करने के बाद, आपको अपस्केलिंग के लिए एक फोटो भेजना होगा।

*महत्वपूर्ण!* चौड़ाई और/या ऊँचाई के लिए समर्थित न्यूनतम रिज़ॉल्यूशन *216 पिक्सेल* है।
इस कमांड की दैनिक लिमिट *5* उपयोग है। सदस्यों के लिए: *20* उपयोग। अनुरोध भाषा कोई भी हो सकती है।''',
            'background': '''/background कमांड फोटो के पृष्ठभूमि को बदलने के लिए वस्तु या वस्तुओं को हाइलाइट करके काम करता है।
/background कमांड का उपयोग करने के बाद, आपको उस पृष्ठभूमि का वर्णन करने वाला एक प्रॉम्प्ट दर्ज करना होगा जिसे आप उपयोग करना चाहते हैं।

फिर, उस फोटो को भेजें जिस पर आप पृष्ठभूमि बदलना चाहते हैं। बॉट आपके अनुरोध के आधार पर आपको *4* विकल्प भेजेगा।

इस कमांड की दैनिक लिमिट हैं: मानक उपयोगकर्ताओं के लिए *20* फोटो और सदस्यों के लिए *40* फोटो।''',
            'expand': '''/expand कमांड आपको एआई का उपयोग करके अपनी छवि को बड़ाने देता है। /expand कमांड जारी करने के बाद, आपको एक फोटो भेजना होगा।

*महत्वपूर्ण!* मूल छवि का क्षेत्र कैनवास क्षेत्र के 15% से अधिक होना चाहिए।

इस कमांड की दैनिक लिमिट *20* छवियाँ प्रतिदिन है, जबकि सदस्य प्रतिदिन *60* छवियों तक प्रोसेस कर सकते हैं।''',
            'reimage': '''/reimage कमांड समान छवि उत्पादन का उपयोग करता है। इस कमांड का उपयोग करने के बाद, आपको एक प्रॉम्प्ट दर्ज करना होगा।

*महत्वपूर्ण!* बेहतर परिणाम के लिए, वर्णन करें कि छवि में क्या दिखाया गया है जिसे आप प्रोसेस करना चाहते हैं। उसके बाद, छवि भेजें।

इस कमांड की दैनिक लिमिट हैं: नियमित उपयोगकर्ताओं के लिए *20* छवियाँ और सदस्यों के लिए *60* छवियाँ।''',
            'search': '''इंटरनेट पर जानकारी खोजें।
यह कमांड /snap कमांड के संसाधनों का उपयोग करके काम करता है।
और लिमिट भी /snap कमांड से लागू होते हैं।''',
            'v': '''/v कमांड बॉट के वर्तमान संस्करण और अपडेट दिखाता है।''',
            'my_id': '''/my_id कमांड आपका user_id दिखाता है।''',
            'reg': '''/reg कमांड आपको Snaplix बॉट में पंजीकृत करता है।''',
            'sub': '''/sub कमांड चेक करता है कि क्या आपके पास एक सक्रिय सदस्यता है।''',
            'get_sub': '''/get_sub कमांड आपको सदस्यता खरीदने देता है।''',
            'limits': '''/limits कमांड आपके वर्तमान कमांड उपयोग लिमिट दिखाता है।''',
            'ping': '''/ping कमांड बॉट के कनेक्शन स्टेटस की जाँच करता है।''',
            'info': '''/info कमांड कमांड का विस्तृत वर्णन दिखाता है ''',
        },
        "switch_lang": "आपने 🇮🇳 हिंदी पर स्विच कर दिया है।",
        "blocked_message": "आप अस्थायी रूप से अवरुद्ध हैं। कृपया 10 मिनट में पुनः प्रयास करें।",
        "registration_in_progress": "आप पंजीकरण प्रक्रिया में पहले से ही हैं। कृपया इसे पूरा करें।",
        "already_registered": "आप पहले से ही पंजीकृत हैं।",
        "captcha": "कैप्चा से टेक्स्ट दर्ज करें",
        "successful_registration": "आपने *सफलतापूर्वक पंजीकरण* किया है!",
        "invitee_registered": "आपके आमंत्रित ने पंजीकरण कर लिया है!",
        "failed_registration": "आपने 4 प्रयासों के बाद *पंजीकरण विफल* कर दिया है।",
        "incorrect_attempts": "गलत। बचे प्रयास: {attempts}.",
        "donate_amount": "कृपया 1 से 100 $USD के बीच दान राशि निर्दिष्ट करें। उपयोग: /donate <amount>",
        "invalid_donate_amount": "कृपया 1 से 100 डॉलर के बीच एक वैध दान राशि निर्दिष्ट करें।",
        "donate_description": "दान करके, आप Snaplix परियोजना के विकास में मदद करते हैं।\nदान के लिए, आपको Snap Coins मिलेंगे। *1 $USD = 10 Snap Coins*\n\nआप लोगों को आमंत्रित करके भी Snap Coins प्राप्त कर सकते हैं। *5 लोगों = 50 Snap Coins*\nSnap Coins परियोजना की *प्रीमियम सुविधाओं* में उपयोग किए जाते हैं\n\nआपका *लिंक* दान के लिए:\n{link}",
        "donate_thank_you": "*परियोजना के समर्थन के लिए बहुत-बहुत धन्यवाद*\nआपको {amount} Snap Coins मिलते हैं\nआपका आदेश आईडी: *{order_id}*",
        "check_payment_later": "बाद में पुनः प्रयास करें...",
        "order_not_paid": "दान *अभी तक* अदायगी नहीं किया गया है।\nकृपया, ऑर्डर की सफल भुगतान के *बाद* \"*Check Payment Status*\" बटन का उपयोग करें।",
        "order_status": "स्थिति: *{status}*",
        "info_command_usage": "यह कमांड सभी बॉट कमांडों का विस्तृत वर्णन करने के लिए उपयोग की जाती है। किसी कमांड के बारे में जानकारी प्राप्त करने के लिए /info <bot command> उपयोग करें",
        "command_not_found": "यह कमांड मौजूद नहीं है।",
        "invite_link": "आपका आमंत्रण लिंक - {link}",
        "my_invites": "आपके आमंत्रण - *{invites}*",
        "my_coins": "आपके अकाउंट पर *{coins}* Snap Coins हैं",
        "invite_reward": "बधाई हो! 5 आमंत्रणों के लिए आपका अकाउंट 50 Snap Coins से बढ़ गया है",
        "less_than_5_invites": "आपके पास *5* से कम लोग आमंत्रित हैं",
        "donate_usage": "/donate <amount>",
        "invalid_amount": "राशि 1 से 1000 के बीच एक सकारात्मक पूर्णांक होनी चाहिए।",
        "coins_given": "उपयोगकर्ता: {user_id} को {amount} सिक्के दिए गए",
        "unfreeze_usage": "/unfreeze <user_id>",
        "user_unfreezed": "उपयोगकर्ता {user_id} को अनफ्रीज़ कर दिया गया है",
        "my_id": "आपका ID: {user_id}",
        "search_limit": "आप /search कमांड का उपयोग केवल एक बार *मिनट* में कर सकते हैं।",
        "search_usage": "AI-Search का उपयोग करने के लिए, कृपया /search <अपनी अनुरोध> दर्ज करें",
        "snap_ai_usage": "Snap-AI का उपयोग करने के लिए, कृपया दर्ज करें /snap <आपका अनुरोध>",
        "thinking": "*सोच रहा हूँ...*",
        "checking_request": "*अनुरोध जांच कर रहा है...*",
        "unethical_request": "*क्षमा करें, मैं इस अनुरोध में मदद नहीं कर सकता*",
        "searching": "*खोज रहा है...*",
        "send_image": "*केवल 1 छवि भेजें*",
        "enter_prompt": "*उत्पादन के लिए प्रोम्प्ट दर्ज करें*",
        "generating": "*उत्पादन हो रहा है...*",
        "analyzing_image": "*छवि का विश्लेषण कर रहा है...*",
        "whats_in_this_image": "इस इमेज में क्या है?",
        "choice_model": "*उत्पादन मॉडल चुनें*",
        "choice_number": "*उत्पादन संख्या चुनें*",
        "msg_incorrect_use": "गलत उपयोग /msg",
        "messages_sent": "{count} उपयोगकर्ताओं को संदेश भेजा गया।",
        "stats_message": (
            "कुल उपयोगकर्ता: {total_users}\n"
            "फ्रीज़ किए गए उपयोगकर्ता: {frozen_users}\n"
            "प्रोसेस किए गए उपयोगकर्ता: {processing_users}\n"
            "सदस्यता उपयोगकर्ता: {paying_users}\n\n"
            "सीमाएँ:\n{limits_message}"
        ),
        "enter_prompt_background": "*पृष्ठभूमि के लिए प्रोम्प्ट दर्ज करें*",
        "enter_prompt_reference": "*रेफरेंस-इमेज के लिए प्रोम्प्ट दर्ज करें*",
        "expanding": "*विस्तार हो रहा है...*",
        "register_first": "बॉट कमांड उपयोग करने के लिए, कृपया /reg कमांड के साथ पंजीकरण करें",
        "already_registered": "आप पहले से ही पंजीकृत हैं।",
        "request_processing": "आपका अनुरोध प्रोसेस किया जा रहा है। कृपया प्रतीक्षा करें।",
        "previous_donation_pending": "आपने अभी तक पिछले दान का भुगतान नहीं किया है।",
        "limit_reached": "आपने आज के लिए {max_limit} की सीमा तक पहुंच गए हैं।",
        "not_a_text": "यह टेक्स्ट नहीं है",
        "not_an_image": "यह एक छवि नहीं है",
        "too_many_images": "बहुत अधिक छवियाँ",
        "image_generation_model": "इमेज जनरेशन मॉडल",
        "text_generation_model": "टेक्स्ट जनरेशन मॉडल",
        "config_menu": "कॉन्फ़िगरेशन मेनू:\nइमेज मॉडल: {img_model}\nटेक्स्ट मॉडल: {txt_model}",
        "config_success": "आपकी कॉन्फ़िगरेशन सफलतापूर्वक सेट कर दी गई है!",
    },
    "ar": {  # العربية (Arabic)
        "info_dict": {
            'snap': '''تُستخدم الأمر /snap لتوليد النصوص.\nعلى سبيل المثال: /snap ما هو جافا.

يتمتع هذا الأمر بحد يومي يبلغ *30* استخدامًا. يزيد الحد للمشتركين إلى *500* استخدام.

جميع اللغات مدعومة مع هذا الأمر.''',
            'image': '''يقوم الأمر /image بإنشاء صور. بعد استخدام الأمر /image، يجب عليك إدخال أي طلب\nكلما كان الطلب *أكثر تفصيلاً*، كانت النتيجة *أفضل*. بعد إرسال طلبك، ستحتاج إلى تحديد نموذج وعدد الصور.

هناك حدود يومية: *40* صورة يوميًا وما يصل إلى 4 صور لكل توليد. ليست جميع النماذج متاحة للمستخدمين المجانيين.

للمشتركين: *1000* صورة يوميًا، 10 صور لكل توليد، والوصول إلى جميع النماذج. يدعم هذا الأمر جميع اللغات.''',
            'image2': '''الأمر /image2 حاليًا في مرحلة الاختبار وقد يتم إزالته أو استبداله. بعد استخدام /image2، يجب عليك إدخال أي طلب\nكلما كان الطلب *أكثر تفصيلاً*، كانت النتيجة *أفضل*.

يقوم بإنشاء 4 صور للجميع وله حد يومي يبلغ *20* صورة. للمشتركين: *40* صورة. يدعم هذا الأمر جميع اللغات.''',
            'vision': '''يُستخدم الأمر /vision للتعرف على الأشياء في الصور. بعد استخدام /vision، يجب عليك إرسال صورة للتعرف عليها إلى البوت.

*مهم!* عند إرسال الصورة، يمكنك *تحديد* طلب محدد في حقل "التعليق". على سبيل المثال، "ما الموجود في الزاوية العلوية اليمنى من الصورة."\nإذا لم يتم تقديم طلب محدد في التعليق، *سيقوم البوت بوصف الصورة باللغة الإنجليزية افتراضيًا*.

يتمتع هذا الأمر بحد يومي يبلغ *10* استخدامات. للمشتركين: *300* استخدام. يمكن أن تكون لغة الطلب أي لغة.''',
            'upscale': '''يزيد الأمر /upscale من دقة الصورة إلى *2X* باستخدام Snap-AI لتحسين جودة الصورة.
بعد استخدام الأمر /upscale، يجب عليك إرسال صورة للتكبير.

*مهم!* الدقة الدنيا المدعومة للعرض و/أو الارتفاع هي *216 بكسل*.
يتمتع هذا الأمر بحد يومي يبلغ *5* استخدامات. للمشتركين: *20* استخدام. يمكن أن تكون لغة الطلب أي لغة.''',
            'background': '''يقوم الأمر /background بتغيير خلفية الصورة من خلال تسليط الضوء على الكائن أو الكائنات.
بعد استخدام الأمر /background، ستحتاج إلى إدخال مُحفّز يصف الخلفية التي تريد استخدامها.

ثم، أرسل الصورة التي تريد تغيير خلفيتها. سيرسل لك البوت *4* اختلافات بناءً على طلبك.

يتمتع هذا الأمر بحدود يومية: *20* صورة للمستخدمين العاديين و*40* صورة للمشتركين.''',
            'expand': '''يتيح لك الأمر /expand تكبير صورتك باستخدام الذكاء الاصطناعي. بعد إصدار الأمر /expand، يجب عليك إرسال صورة.

*مهم!* يجب أن تكون مساحة الصورة الأصلية أكثر من 15% من مساحة القماش.

يتمتع هذا الأمر بحد يومي يبلغ *20* صورة يوميًا، بينما يمكن للمشتركين معالجة ما يصل إلى *60* صورة يوميًا.''',
            'reimage': '''يستخدم الأمر /reimage توليد الصور المماثلة. بعد استخدام هذا الأمر، يجب عليك إدخال مُحفّز.

*مهم!* للحصول على نتائج أفضل، وصف ما يُظهر في الصورة التي تريد معالجتها. بعد ذلك، أرسل الصورة.

يتمتع هذا الأمر بحدود يومية: *20* صورة للمستخدمين العاديين و*60* صورة للمشتركين.''',
            'search': '''ابحث عن معلومات على الإنترنت.
يعمل الأمر عن طريق استخدام موارد الأمر /snap.
ويتم تطبيق الحدود أيضًا من الأمر /snap.''',
            'v': '''يعرض الأمر /v الإصدار الحالي للبوت والتحديثات.''',
            'my_id': '''يعرض الأمر /my_id معرف المستخدم الخاص بك.''',
            'reg': '''يقوم الأمر /reg بتسجيلك في بوت Snaplix.''',
            'sub': '''يتحقق الأمر /sub من وجود اشتراك نشط لديك.''',
            'get_sub': '''يتيح لك الأمر /get_sub شراء اشتراك.''',
            'limits': '''يعرض الأمر /limits حدود استخدام الأوامر الحالية لديك.''',
            'ping': '''يتحقق الأمر /ping من حالة اتصال البوت.''',
            'info': '''يعرض الأمر /info وصفًا مفصلاً للأمر ''',
        },
        "switch_lang": "لقد قمت بالتبديل إلى اللغة العربية 🇦🇪.",
        "blocked_message": "أنت محظور مؤقتًا. يرجى المحاولة مرة أخرى بعد 10 دقائق.",
        "registration_in_progress": "أنت بالفعل في عملية التسجيل. يرجى إكمالها.",
        "already_registered": "أنت بالفعل مسجل.",
        "captcha": "أدخل نص التحقق",
        "successful_registration": "لقد تم *تسجيلك* بنجاح!",
        "invitee_registered": "لقد سجل مدعوك!",
        "failed_registration": "لقد *فشلت* في التسجيل بعد 4 محاولات.",
        "incorrect_attempts": "غير صحيح. المحاولات المتبقية: {attempts}.",
        "donate_amount": "يرجى تحديد مبلغ التبرع بين 1 و 100 دولار أمريكي. الاستخدام: /donate <amount>",
        "invalid_donate_amount": "يرجى تحديد مبلغ تبرع صالح بين 1 و 100 دولار.",
        "donate_description": "عن طريق التبرع بالأموال، تساعد مشروع Snaplix على التطور.\nمقابل التبرع، ستحصل على Snap Coins. *1 $USD = 10 Snap Coins*\n\nيمكنك أيضًا الحصول على Snap Coins من خلال دعوة الأشخاص. *5 أشخاص = 50 Snap Coins*\nتستخدم Snap Coins في الوظائف *المتقدمة* للمشروع\n\nرابطك للتبرع:\n{link}",
        "donate_thank_you": "*شكراً جزيلاً لدعمك للمشروع*\nستحصل على {amount} Snap Coins\nرقم طلبك: *{order_id}*",
        "check_payment_later": "حاول مرة أخرى لاحقًا...",
        "order_not_paid": "لم يتم *دفع* التبرع بعد.\nيرجى استخدام زر \"*Check Payment Status*\" *بعد* دفع الطلب بنجاح.",
        "order_status": "الحالة: *{status}*",
        "info_command_usage": "تُستخدم هذه الأمر لوصف جميع أوامر البوت بالتفصيل. لمعرفة معلومات حول أمر، استخدم /info <bot command>",
        "command_not_found": "هذا الأمر غير موجود.",
        "invite_link": "رابط الدعوة الخاص بك - {link}",
        "my_invites": "دعواتك - *{invites}*",
        "my_coins": "لديك *{coins}* Snap Coins في حسابك",
        "invite_reward": "تهانينا! تم زيادة حسابك بـ 50 Snap Coins لـ 5 دعوات",
        "less_than_5_invites": "لديك أقل من *5* أشخاص مدعوين",
        "donate_usage": "/donate <amount>",
        "invalid_amount": "يجب أن يكون المبلغ عددًا صحيحًا موجبًا بين 1 و 1000.",
        "coins_given": "تم منح المستخدم: {user_id} {amount} عملات",
        "unfreeze_usage": "/unfreeze <user_id>",
        "user_unfreezed": "تم إلغاء تجميد المستخدم {user_id}",
        "my_id": "معرفك: {user_id}",
        "search_limit": "يمكنك استخدام أمر /search مرة واحدة فقط كل *دقيقة.*",
        "search_usage": "لاستخدام AI-Search، يرجى إدخال /search <طلبك>",
        "snap_ai_usage": "لاستخدام Snap-AI، يرجى إدخال /snap <طلبك>",
        "thinking": "*في تفكير...*",
        "checking_request": "*جاري التحقق من الطلب...*",
        "unethical_request": "*عذراً، لا يمكنني المساعدة في هذا الطلب*",
        "searching": "*جاري البحث...*",
        "send_image": "*أرسل صورة واحدة فقط*",
        "enter_prompt": "*أدخل التلميح للتوليد*",
        "generating": "*جاري التوليد...*",
        "analyzing_image": "*جاري تحليل الصورة...*",
        "whats_in_this_image": "ما الموجود في هذه الصورة؟",
        "choice_model": "*اختر نموذج التوليد*",
        "choice_number": "*اختر عدد التوليد*",
        "msg_incorrect_use": "استخدام غير صحيح /msg",
        "messages_sent": "تم إرسال الرسائل إلى {count} من المستخدمين.",
        "stats_message": (
            "إجمالي المستخدمين: {total_users}\n"
            "المستخدمين المجمدين: {frozen_users}\n"
            "المستخدمين المعالجين: {processing_users}\n"
            "المستخدمين المشتركين: {paying_users}\n\n"
            "الحدود:\n{limits_message}"
        ),
        "enter_prompt_background": "*أدخل التلميح للخلفية*",
        "enter_prompt_reference": "*أدخل التلميح لصورة المرجع*",
        "expanding": "*جاري التوسيع...*",
        "register_first": "لاستخدام أوامر البوت، يرجى التسجيل باستخدام الأمر /reg",
        "already_registered": "أنت مسجل بالفعل.",
        "request_processing": "طلبك قيد المعالجة. يرجى الانتظار.",
        "previous_donation_pending": "لم تقم بدفع التبرع السابق بعد.",
        "limit_reached": "لقد وصلت إلى الحد الأقصى {max_limit} اليوم.",
        "not_a_text": "هذا ليس نصًا",
        "not_an_image": "هذا ليس صورة",
        "too_many_images": "الكثير من الصور",
        "image_generation_model": "نموذج توليد الصور",
        "text_generation_model": "نموذج توليد النصوص",
        "config_menu": "قائمة الإعدادات:\nنموذج الصورة: {img_model}\nنموذج النص: {txt_model}",
        "config_success": "تم ضبط الإعدادات الخاصة بك بنجاح!",
    },
    "pt": {  # Português (Portuguese)
        "info_dict": {
            'snap': '''O comando /snap é usado para gerar texto.\nPor exemplo: /snap o que é java.

Este comando tem um limite diário de *30* usos. Para assinantes, o limite aumenta para *500* usos.

Todos os idiomas são suportados com este comando.''',
            'image': '''O comando /image gera imagens. Após usar o comando /image, você deve inserir qualquer solicitação\nQuanto mais *detalhada* for sua solicitação, *melhor será o resultado*. Após enviar sua solicitação, você precisará selecionar um modelo e a quantidade de imagens.

Há limites diários: *40* imagens por dia e até 4 imagens por geração. Nem todos os modelos estão disponíveis para usuários gratuitos.

Para assinantes: *1000* imagens por dia, 10 imagens por geração e acesso a todos os modelos. Este comando suporta todos os idiomas.''',
            'image2': '''O comando /image2 está atualmente em fase de teste e pode ser removido ou substituído. Após usar /image2, você deve inserir qualquer solicitação\nQuanto mais *detalhada* for sua solicitação, *melhor será o resultado*.

Ele gera 4 imagens para todos e tem um limite diário de *20* imagens. Para assinantes: *40* imagens. Este comando suporta todos os idiomas.''',
            'vision': '''O comando /vision é usado para reconhecer objetos em imagens. Após usar /vision, você deve enviar ao bot uma imagem para reconhecimento.

*Importante!* Ao enviar a imagem, você pode *especificar* uma solicitação específica no campo "legenda". Por exemplo, "o que está no canto superior direito da imagem."\nSe nenhuma solicitação específica for fornecida na legenda, *o bot descreverá a imagem em inglês por padrão*.

Este comando tem um limite diário de *10* usos. Para assinantes: *300* usos. O idioma da solicitação pode ser qualquer um.''',
            'upscale': '''O comando /upscale aumenta uma imagem para resolução *2X* usando Snap-AI para melhorar a qualidade da imagem.
Após usar o comando /upscale, você deve enviar uma foto para aumentar.

*Importante!* A resolução mínima suportada para largura e/ou altura é de *216 pixels.*
Este comando tem um limite diário de *5* usos. Para assinantes: *20* usos. O idioma da solicitação pode ser qualquer um.''',
            'background': '''O comando /background altera o fundo de uma foto destacando o objeto ou objetos.
Após usar o comando /background, você precisará inserir um prompt descrevendo o fundo que deseja usar.

Em seguida, envie a foto na qual deseja alterar o fundo. O bot enviará *4* variações com base na sua solicitação.

Este comando tem limites diários: *20* fotos para usuários padrão e *40* fotos para assinantes.''',
            'expand': '''O comando /expand permite ampliar sua imagem usando IA. Após emitir o comando /expand, você deve enviar uma foto.

*Importante!* A área da imagem original deve ser mais de 15% da área da tela.

Este comando tem um limite diário de *20* imagens por dia, enquanto os assinantes podem processar até *60* imagens por dia.''',
            'reimage': '''O comando /reimage usa geração de imagem semelhante. Após usar este comando, você deve inserir um prompt.

*Importante!* Para melhores resultados, descreva o que está representado na imagem que você deseja processar. Depois disso, envie a imagem.

Este comando tem limites diários: *20* imagens para usuários regulares e *60* imagens para assinantes.''',
            'search': '''Pesquisar informações na Internet.
O comando funciona utilizando os recursos do comando /snap.
E os limites também são aplicados do comando /snap.''',
            'v': '''O comando /v exibe a versão atual do bot e as atualizações.''',
            'my_id': '''O comando /my_id mostra seu user_id.''',
            'reg': '''O comando /reg registra você no bot Snaplix.''',
            'sub': '''O comando /sub verifica se você tem uma assinatura ativa.''',
            'get_sub': '''O comando /get_sub permite que você compre uma assinatura.''',
            'limits': '''O comando /limits mostra seus limites de uso de comandos atuais.''',
            'ping': '''O comando /ping verifica o status da conexão do bot.''',
            'info': '''O comando /info mostra uma descrição detalhada do comando ''',
        },
        "switch_lang": "Você mudou para 🇵🇹 português.",
        "blocked_message": "Você está temporariamente bloqueado. Tente novamente em 10 minutos.",
        "registration_in_progress": "Você já está no processo de registro. Por favor, complete-o.",
        "already_registered": "Você já está registrado.",
        "captcha": "Digite o texto do captcha",
        "successful_registration": "Você se *registrou com sucesso*!",
        "invitee_registered": "Seu convidado se registrou!",
        "failed_registration": "Você *falhou no registro* após 4 tentativas.",
        "incorrect_attempts": "Incorreto. Tentativas restantes: {attempts}.",
        "donate_amount": "Por favor, especifique o valor da doação entre 1 e 100 $USD. Uso: /donate <amount>",
        "invalid_donate_amount": "Por favor, especifique um valor de doação válido entre 1 e 100 dólares.",
        "donate_description": "Ao doar dinheiro, você ajuda o projeto Snaplix a se desenvolver.\nPor uma doação, você recebe Snap Coins. *1 $USD = 10 Snap Coins*\n\nVocê também pode obter Snap Coins convidando pessoas. *5 pessoas = 50 Snap Coins*\nAs Snap Coins são usadas nas *funções premium* do projeto\n\nSeu *Link* para doação:\n{link}",
        "donate_thank_you": "*Muito obrigado por apoiar o projeto*\nVocê recebe {amount} Snap Coins\nSeu ID de pedido: *{order_id}*",
        "check_payment_later": "Tente novamente mais tarde...",
        "order_not_paid": "A doação *não* foi paga ainda.\nPor favor, use o botão \"*Check Payment Status*\" *após* o pagamento bem-sucedido do pedido.",
        "order_status": "Status: *{status}*",
        "info_command_usage": "Este comando é usado para descrever todos os comandos do bot em detalhes. Para encontrar informações sobre um comando, use /info <bot command>",
        "command_not_found": "Este comando não existe.",
        "invite_link": "Seu link de convite - {link}",
        "my_invites": "Seus convites - *{invites}*",
        "my_coins": "Você tem *{coins}* Snap Coins em sua conta",
        "invite_reward": "Parabéns! Sua conta foi aumentada em 50 Snap Coins por 5 convites",
        "less_than_5_invites": "Você tem menos de *5* pessoas convidadas",
        "donate_usage": "/donate <amount>",
        "invalid_amount": "O valor deve ser um número inteiro positivo entre 1 e 1000.",
        "coins_given": "Dado {amount} moedas ao usuário: {user_id}",
        "unfreeze_usage": "/unfreeze <user_id>",
        "user_unfreezed": "O usuário {user_id} foi descongelado",
        "my_id": "Seu ID: {user_id}",
        "search_limit": "Você pode usar o comando /search apenas uma vez por *minuto.*",
        "search_usage": "Para usar AI-Search, por favor digite /search <seu pedido>",
        "snap_ai_usage": "Para usar o Snap-AI, digite /snap <seu pedido>",
        "thinking": "*Pensando...*",
        "checking_request": "*Verificando pedido...*",
        "unethical_request": "*Desculpe, não posso ajudar com este pedido*",
        "searching": "*Pesquisando...*",
        "send_image": "*Envie apenas 1 imagem*",
        "enter_prompt": "*Digite o prompt para geração*",
        "generating": "*Gerando...*",
        "analyzing_image": "*Analisando imagem...*",
        "whats_in_this_image": "O que há nesta imagem?",
        "choice_model": "*Escolha o modelo de geração*",
        "choice_number": "*Escolha o número de geração*",
        "msg_incorrect_use": "Uso incorreto /msg",
        "messages_sent": "Mensagens enviadas a {count} usuários.",
        "stats_message": (
            "Total de usuários: {total_users}\n"
            "Usuários congelados: {frozen_users}\n"
            "Usuários processados: {processing_users}\n"
            "Usuários assinantes: {paying_users}\n\n"
            "Limites:\n{limits_message}"
        ),
        "enter_prompt_background": "*Digite o prompt para o fundo*",
        "enter_prompt_reference": "*Digite o prompt para a imagem de referência*",
        "expanding": "*Expandindo...*",
        "register_first": "Para usar os comandos do bot, registre-se com o comando /reg",
        "already_registered": "Você já está registrado.",
        "request_processing": "Seu pedido está sendo processado. Por favor, aguarde.",
        "previous_donation_pending": "Você ainda não pagou a doação anterior.",
        "limit_reached": "Você atingiu o limite de {max_limit} para hoje.",
        "not_a_text": "Isso não é um texto",
        "not_an_image": "Isso não é uma imagem",
        "too_many_images": "Muitas imagens",
        "image_generation_model": "Modelo de Geração de Imagem",
        "text_generation_model": "Modelo de Geração de Texto",
        "config_menu": "Menu de configuração:\nModelo de Imagem: {img_model}\nModelo de Texto: {txt_model}",
        "config_success": "Sua configuração foi definida com sucesso!",
    },
    "ua": {  # Українська (Ukrainian)
        "info_dict": {
            'snap': '''Команда /snap використовується для генерації тексту.\nНаприклад: /snap що таке java.

Ця команда має щоденний ліміт у *30* використань. Для передплатників ліміт збільшується до *500* використань.

Усі мови підтримуються цією командою.''',
            'image': '''Команда /image генерує зображення. Після використання команди /image вам потрібно ввести будь-який запит\nЧим *детальнішим* буде ваш запит, тим *кращим* буде результат. Після надсилання запиту вам потрібно буде вибрати модель і кількість зображень.

Є щоденні ліміти: *40* зображень на день і до 4 зображень за генерацію. Не всі моделі доступні безкоштовним користувачам.

Для передплатників: *1000* зображень на день, 10 зображень за генерацію та доступ до всіх моделей. Ця команда підтримує всі мови.''',
            'image2': '''Команда /image2 наразі перебуває на етапі тестування і може бути видалена або замінена. Після використання /image2 вам потрібно ввести будь-який запит\nЧим *детальнішим* буде ваш запит, тим *кращим* буде результат.

Вона генерує 4 зображення для всіх і має щоденний ліміт у *20* зображень. Для передплатників: *40* зображень. Ця команда підтримує всі мови.''',
            'vision': '''Команда /vision використовується для розпізнавання об’єктів на зображеннях. Після використання /vision вам потрібно надіслати боту зображення для розпізнавання.

*Важливо!* При надсиланні зображення ви можете *вказати* конкретний запит у полі "підпис". Наприклад, "що знаходиться у правому верхньому куті зображення."\nЯкщо конкретний запит не вказано в підписі, *бот за замовчуванням опише зображення англійською мовою*.

Ця команда має щоденний ліміт у *10* використань. Для передплатників: *300* використань. Мова запиту може бути будь-якою.''',
            'upscale': '''Команда /upscale збільшує зображення до роздільної здатності *2X* за допомогою Snap-AI для покращення якості зображення.
Після використання команди /upscale вам потрібно надіслати фото для збільшення.

*Важливо!* Мінімальна підтримувана роздільна здатність для ширини та/або висоти становить *216 пікселів.*
Ця команда має щоденний ліміт у *5* використань. Для передплатників: *20* використань. Мова запиту може бути будь-якою.''',
            'background': '''Команда /background змінює фон фотографії, виділяючи об’єкт або об’єкти.
Після використання команди /background вам потрібно ввести підказку, яка описує фон, який ви хочете використовувати.

Потім надішліть фото, на якому ви хочете змінити фон. Бот надішле вам *4* варіанти на основі вашого запиту.

Ця команда має щоденні ліміти: *20* фото для стандартних користувачів і *40* фото для передплатників.''',
            'expand': '''Команда /expand дозволяє збільшити ваше зображення за допомогою ШІ. Після видачі команди /expand вам потрібно надіслати фото.

*Важливо!* Площа оригінального зображення повинна бути більше 15% від площі полотна.

Ця команда має щоденний ліміт у *20* зображень на день, тоді як передплатники можуть обробляти до *60* зображень на день.''',
            'reimage': '''Команда /reimage використовує схожу генерацію зображень. Після використання цієї команди вам потрібно ввести підказку.

*Важливо!* Для кращих результатів опишіть, що зображено на зображенні, яке ви хочете обробити. Після цього надішліть зображення.

Ця команда має щоденні ліміти: *20* зображень для звичайних користувачів і *60* зображень для передплатників.''',
            'search': '''Пошук інформації в Інтернеті.
Команда працює, використовуючи ресурси команди /snap.
І ліміти також застосовуються від команди /snap.''',
            'v': '''Команда /v відображає поточну версію бота та оновлення.''',
            'my_id': '''Команда /my_id показує ваш user_id.''',
            'reg': '''Команда /reg реєструє вас у боті Snaplix.''',
            'sub': '''Команда /sub перевіряє, чи у вас є активна підписка.''',
            'get_sub': '''Команда /get_sub дозволяє вам придбати підписку.''',
            'limits': '''Команда /limits відображає ваші поточні ліміти використання команд.''',
            'ping': '''Команда /ping перевіряє стан з’єднання бота.''',
            'info': '''Команда /info показує детальний опис команди ''',
        },
        "switch_lang": "Ви переключилися на 🇺🇦 українську мову.",
        "blocked_message": "Вас тимчасово заблоковано. Будь ласка, спробуйте ще раз через 10 хвилин.",
        "registration_in_progress": "Ви вже знаходитесь в процесі реєстрації. Будь ласка, завершіть його.",
        "already_registered": "Ви вже зареєстровані.",
        "captcha": "Введіть текст з капчі",
        "successful_registration": "Ви успішно зареєструвалися!",
        "invitee_registered": "Ваш запрошений зареєструвався!",
        "failed_registration": "Ви *не змогли зареєструватися* після 4 спроб.",
        "incorrect_attempts": "Неправильно. Залишилося спроб: {attempts}.",
        "donate_amount": "Будь ласка, вкажіть суму пожертви від 1 до 100 $USD. Використання: /donate <amount>",
        "invalid_donate_amount": "Будь ласка, вкажіть коректну суму пожертви від 1 до 100 доларів.",
        "donate_description": "Пожертвувавши гроші, ви допомагаєте розвитку проекту Snaplix.\nЗа пожертву ви отримаєте Snap Coins. *1 $USD = 10 Snap Coins*\n\nВи також можете отримати Snap Coins за запрошення людей. *5 людей = 50 Snap Coins*\nSnap Coins використовуються в *преміум-функціях* проекту\n\nВаше *посилання* для пожертви:\n{link}",
        "donate_thank_you": "*Дуже дякуємо за підтримку проекту*\nВи отримуєте {amount} Snap Coins\nВаш номер замовлення: *{order_id}*",
        "check_payment_later": "Спробуйте пізніше...",
        "order_not_paid": "Пожертва *не* була оплачена ще.\nБудь ласка, використовуйте кнопку \"*Check Payment Status*\" *після* успішної оплати замовлення.",
        "order_status": "Статус: *{status}*",
        "info_command_usage": "Ця команда використовується для детального опису всіх команд бота. Щоб дізнатися інформацію про команду, використовуйте /info <bot command>",
        "command_not_found": "Ця команда не існує.",
        "invite_link": "Ваше запрошення - {link}",
        "my_invites": "Ваші запрошення - *{invites}*",
        "my_coins": "У вас *{coins}* Snap Coins на вашому рахунку",
        "invite_reward": "Вітаємо! Ваш рахунок був збільшений на 50 Snap Coins за 5 запрошень",
        "less_than_5_invites": "У вас менше *5* запрошених людей",
        "donate_usage": "/donate <amount>",
        "invalid_amount": "Сума повинна бути позитивним цілим числом від 1 до 1000.",
        "coins_given": "Видано {amount} монет користувачу: {user_id}",
        "unfreeze_usage": "/unfreeze <user_id>",
        "user_unfreezed": "Користувач {user_id} був розморожений",
        "my_id": "Ваш ID: {user_id}",
        "search_limit": "Ви можете використовувати команду /search тільки раз на *хвилину.*",
        "search_usage": "Щоб використовувати AI-Search, будь ласка, введіть /search <ваш запит>",
        "snap_ai_usage": "Щоб використовувати Snap-AI, введіть /snap <ваш запит>",
        "thinking": "*Думаю...*",
        "checking_request": "*Перевірка запиту...*",
        "unethical_request": "*Вибачте, я не можу допомогти з цим запитом*",
        "searching": "*Пошук...*",
        "send_image": "*Відправте тільки 1 зображення*",
        "enter_prompt": "*Введіть запит для генерації*",
        "generating": "*Генерація...*",
        "analyzing_image": "*Аналіз зображення...*",
        "whats_in_this_image": "Що на цьому зображенні?",
        "choice_model": "*Виберіть модель генерації*",
        "choice_number": "*Виберіть кількість генерації*",
        "msg_incorrect_use": "Неправильне використання /msg",
        "messages_sent": "Повідомлення відправлено {count} користувачам.",
        "stats_message": (
            "Загальна кількість користувачів: {total_users}\n"
            "Заморожені користувачі: {frozen_users}\n"
            "Оброблені користувачі: {processing_users}\n"
            "Підписки користувачів: {paying_users}\n\n"
            "Ліміти:\n{limits_message}"
        ),
        "enter_prompt_background": "*Введіть запит для фону*",
        "enter_prompt_reference": "*Введіть запит для референс-зображення*",
        "expanding": "*Розширення...*",
        "register_first": "Щоб використовувати команди бота, зареєструйтеся за допомогою команди /reg",
        "already_registered": "Ви вже зареєстровані.",
        "request_processing": "Ваш запит обробляється. Будь ласка, зачекайте.",
        "previous_donation_pending": "Ви ще не сплатили попереднє пожертву.",
        "limit_reached": "Ви досягли ліміту {max_limit} на сьогодні.",
        "not_a_text": "Це не текст",
        "not_an_image": "Це не зображення",
        "too_many_images": "Забагато зображень",
        "image_generation_model": "Модель генерації зображень",
        "text_generation_model": "Модель генерації тексту",
        "config_menu": "Меню налаштувань:\nМодель зображення: {img_model}\nМодель тексту: {txt_model}",
        "config_success": "Ваші налаштування успішно встановлені!",
    },
    "fr": {  # Français (French)
        "info_dict": {
            'snap': '''La commande /snap est utilisée pour générer du texte.\nPar exemple : /snap qu'est-ce que java.

Cette commande a une limite quotidienne de *30* utilisations. Pour les abonnés, la limite augmente à *500* utilisations.

Toutes les langues sont prises en charge avec cette commande.''',
            'image': '''La commande /image génère des images. Après avoir utilisé la commande /image, vous devez entrer une requête\nPlus votre requête est *détaillée*, meilleur sera le *résultat*. Après avoir soumis votre requête, vous devrez sélectionner un modèle et le nombre d'images.

Il y a des limites quotidiennes : *40* images par jour et jusqu'à 4 images par génération. Tous les modèles ne sont pas disponibles pour les utilisateurs gratuits.

Pour les abonnés : *1000* images par jour, 10 images par génération, et accès à tous les modèles. Cette commande prend en charge toutes les langues.''',
            'image2': '''La commande /image2 est actuellement en phase de test et peut être supprimée ou remplacée. Après avoir utilisé /image2, vous devez entrer une requête\nPlus votre requête est *détaillée*, meilleur sera le *résultat*.

Elle génère 4 images pour tout le monde et a une limite quotidienne de *20* images. Pour les abonnés : *40* images. Cette commande prend en charge toutes les langues.''',
            'vision': '''La commande /vision est utilisée pour reconnaître des objets dans des images. Après avoir utilisé /vision, vous devez envoyer au bot une image à reconnaître.

*Important!* Lors de l'envoi de l'image, vous pouvez *spécifier* une requête spécifique dans le champ "légende". Par exemple, "qu'y a-t-il dans le coin supérieur droit de l'image."\nSi aucune requête spécifique n'est fournie dans la légende, *le bot décrira l'image en anglais par défaut*.

Cette commande a une limite quotidienne de *10* utilisations. Pour les abonnés : *300* utilisations. La langue de la requête peut être n'importe laquelle.''',
            'upscale': '''La commande /upscale augmente la résolution d'une image à *2X* en utilisant Snap-AI pour améliorer la qualité de l'image.
Après avoir utilisé la commande /upscale, vous devez envoyer une photo à agrandir.

*Important!* La résolution minimale prise en charge pour la largeur et/ou la hauteur est de *216 pixels.*
Cette commande a une limite quotidienne de *5* utilisations. Pour les abonnés : *20* utilisations. La langue de la requête peut être n'importe laquelle.''',
            'background': '''La commande /background change l'arrière-plan d'une photo en mettant en évidence l'objet ou les objets.
Après avoir utilisé la commande /background, vous devrez entrer une invite décrivant l'arrière-plan que vous souhaitez utiliser.

Ensuite, envoyez la photo sur laquelle vous souhaitez changer l'arrière-plan. Le bot vous enverra *4* variations basées sur votre requête.

Cette commande a des limites quotidiennes : *20* photos pour les utilisateurs standard et *40* photos pour les abonnés.''',
            'expand': '''La commande /expand vous permet d'agrandir votre image en utilisant l'IA. Après avoir émis la commande /expand, vous devez envoyer une photo.

*Important!* La zone de l'image originale doit être supérieure à 15% de la zone de la toile.

Cette commande a une limite quotidienne de *20* images par jour, tandis que les abonnés peuvent traiter jusqu'à *60* images par jour.''',
            'reimage': '''La commande /reimage utilise une génération d'image similaire. Après avoir utilisé cette commande, vous devez entrer une invite.

*Important!* Pour de meilleurs résultats, décrivez ce qui est représenté sur l'image que vous souhaitez traiter. Ensuite, envoyez l'image.

Cette commande a des limites quotidiennes : *20* images pour les utilisateurs réguliers et *60* images pour les abonnés.''',
            'search': '''Rechercher des informations sur Internet.
La commande fonctionne en utilisant les ressources de la commande /snap.
Et les limites sont également appliquées à partir de la commande /snap.''',
            'v': '''La commande /v affiche la version actuelle du bot et les mises à jour.''',
            'my_id': '''La commande /my_id affiche votre user_id.''',
            'reg': '''La commande /reg vous inscrit dans le bot Snaplix.''',
            'sub': '''La commande /sub vérifie si vous avez un abonnement actif.''',
            'get_sub': '''La commande /get_sub vous permet d'acheter un abonnement.''',
            'limits': '''La commande /limits affiche vos limites d'utilisation des commandes actuelles.''',
            'ping': '''La commande /ping vérifie l'état de la connexion du bot.''',
            'info': '''La commande /info affiche une description détaillée de la commande ''',
        },
        "switch_lang": "Vous avez basculé en 🇫🇷 français.",
        "blocked_message": "Vous êtes temporairement bloqué. Veuillez réessayer dans 10 minutes.",
        "registration_in_progress": "Vous êtes déjà en cours d'inscription. Veuillez la terminer.",
        "already_registered": "Vous êtes déjà inscrit.",
        "captcha": "Entrez le texte du captcha",
        "successful_registration": "Vous vous êtes *inscrit avec succès*!",
        "invitee_registered": "Votre invité s'est inscrit!",
        "failed_registration": "Vous avez *échoué à vous inscrire* après 4 tentatives.",
        "incorrect_attempts": "Incorrect. Tentatives restantes: {attempts}.",
        "donate_amount": "Veuillez spécifier le montant du don entre 1 et 100 $USD. Utilisation: /donate <amount>",
        "invalid_donate_amount": "Veuillez spécifier un montant de don valide entre 1 et 100 dollars.",
        "donate_description": "En donnant de l'argent, vous aidez le projet Snaplix à se développer.\nPour un don, vous recevez des Snap Coins. *1 $USD = 10 Snap Coins*\n\nVous pouvez également obtenir des Snap Coins en invitant des personnes. *5 personnes = 50 Snap Coins*\nLes Snap Coins sont utilisés dans les *fonctions premium* du projet\n\nVotre *lien* pour faire un don:\n{link}",
        "donate_thank_you": "*Merci beaucoup pour votre soutien au projet*\nVous recevez {amount} Snap Coins\nVotre ID de commande: *{order_id}*",
        "check_payment_later": "Réessayez plus tard...",
        "order_not_paid": "Le don *n'a pas* encore été payé.\nVeuillez utiliser le bouton \"*Check Payment Status*\" *après* le paiement réussi de la commande.",
        "order_status": "Statut: *{status}*",
        "info_command_usage": "Cette commande est utilisée pour décrire en détail toutes les commandes du bot. Pour obtenir des informations sur une commande, utilisez /info <bot command>",
        "command_not_found": "Cette commande n'existe pas.",
        "invite_link": "Votre lien d'invitation - {link}",
        "my_invites": "Vos invitations - *{invites}*",
        "my_coins": "Vous avez *{coins}* Snap Coins sur votre compte",
        "invite_reward": "Félicitations! Votre compte a été augmenté de 50 Snap Coins pour 5 invitations",
        "less_than_5_invites": "Vous avez moins de *5* personnes invitées",
        "donate_usage": "/donate <amount>",
        "invalid_amount": "Le montant doit être un nombre entier positif entre 1 et 1000.",
        "coins_given": "Donné {amount} pièces à l'utilisateur: {user_id}",
        "unfreeze_usage": "/unfreeze <user_id>",
        "user_unfreezed": "L'utilisateur {user_id} a été débloqué",
        "my_id": "Votre ID: {user_id}",
        "search_limit": "Vous pouvez utiliser la commande /search une seule fois par *minute.*",
        "search_usage": "Pour utiliser AI-Search, veuillez entrer /search <votre demande>",
        "snap_ai_usage": "Pour utiliser Snap-AI, veuillez entrer /snap <votre demande>",
        "thinking": "*Réflexion...*",
        "checking_request": "*Vérification de la demande...*",
        "unethical_request": "*Désolé, je ne peux pas aider avec cette demande*",
        "searching": "*Recherche...*",
        "send_image": "*Envoyez seulement 1 image*",
        "enter_prompt": "*Entrez l'invite pour la génération*",
        "generating": "*Génération...*",
        "analyzing_image": "*Analyse de l'image...*",
        "whats_in_this_image": "Qu'y a-t-il sur cette image ?",
        "choice_model": "*Choisissez le modèle de génération*",
        "choice_number": "*Choisissez le nombre de génération*",
        "msg_incorrect_use": "Utilisation incorrecte /msg",
        "messages_sent": "Messages envoyés à {count} utilisateurs.",
        "stats_message": (
            "Nombre total d'utilisateurs: {total_users}\n"
            "Utilisateurs gelés: {frozen_users}\n"
            "Utilisateurs traités: {processing_users}\n"
            "Utilisateurs abonnés: {paying_users}\n\n"
            "Limites:\n{limits_message}"
        ),
        "enter_prompt_background": "*Entrez l'invite pour le fond*",
        "enter_prompt_reference": "*Entrez l'invite pour l'image de référence*",
        "expanding": "*Expansion...*",
        "register_first": "Pour utiliser les commandes du bot, enregistrez-vous avec la commande /reg",
        "already_registered": "Vous êtes déjà inscrit.",
        "request_processing": "Votre demande est en cours de traitement. Veuillez patienter.",
        "previous_donation_pending": "Vous n'avez pas encore payé le don précédent.",
        "limit_reached": "Vous avez atteint la limite de {max_limit} pour aujourd'hui.",
        "not_a_text": "Ce n'est pas un texte",
        "not_an_image": "Ce n'est pas une image",
        "too_many_images": "Trop d'images",
        "image_generation_model": "Modèle de Génération d'Image",
        "text_generation_model": "Modèle de Génération de Texte",
        "config_menu": "Menu de configuration:\nModèle d'Image: {img_model}\nModèle de Texte: {txt_model}",
        "config_success": "Votre configuration a été définie avec succès!",
    },
    "jp": {  # 日本語 (Japanese)
        "info_dict": {
            'snap': '''/snap コマンドはテキストを生成するために使用されます。\n例: /snap ジャバとは何ですか。

このコマンドは 1 日 *30* 回の使用制限があります。サブスクライバーの場合、制限は *500* 回に増加します。

このコマンドではすべての言語がサポートされています。''',
            'image': '''/image コマンドは画像を生成します。/image コマンドを使用した後、任意のリクエストを入力する必要があります\nリクエストが *詳細*であるほど、結果は *良く*なります。リクエストを送信した後、モデルと画像の数を選択する必要があります。

毎日の制限: 1 日あたり *40* 枚の画像と 1 回の生成につき最大 4 枚の画像。すべてのモデルが無料ユーザーに利用可能なわけではありません。

サブスクライバー: 1 日あたり *1000* 枚の画像、1 回の生成につき 10 枚の画像、およびすべてのモデルへのアクセス。このコマンドはすべての言語をサポートしています。''',
            'image2': '''/image2 コマンドは現在テスト段階にあり、削除または置き換えられる可能性があります。/image2 を使用した後、任意のリクエストを入力する必要があります\nリクエストが *詳細*であるほど、結果は *良く*なります。

これはすべての人に対して 4 枚の画像を生成し、毎日の制限は *20* 枚の画像です。サブスクライバーの場合: *40* 枚の画像。このコマンドはすべての言語をサポートしています。''',
            'vision': '''/vision コマンドは画像内のオブジェクトを認識するために使用されます。/vision を使用した後、認識するためにボットに画像を送信する必要があります。

*重要!* 画像を送信する際に、「キャプション」フィールドに *特定のリクエスト*を指定できます。例えば、「画像の右上隅に何がありますか。」\nキャプションに特定のリクエストが提供されていない場合、*ボットはデフォルトで英語で画像を説明します*。

このコマンドは 1 日 *10* 回の使用制限があります。サブスクライバーの場合: *300* 回。リクエストの言語は任意の言語です。''',
            'upscale': '''/upscale コマンドは Snap-AI を使用して画像の解像度を *2X* に拡大し、画像の品質を向上させます。
/upscale コマンドを使用した後、拡大するための写真を送信する必要があります。

*重要!* サポートされる最小解像度は幅または高さの *216 ピクセル*です。
このコマンドは 1 日 *5* 回の使用制限があります。サブスクライバーの場合: *20* 回。リクエストの言語は任意の言語です。''',
            'background': '''/background コマンドはオブジェクトまたはオブジェクトを強調表示することで、写真の背景を変更します。
/background コマンドを使用した後、使用する背景を説明するプロンプトを入力する必要があります。

次に、背景を変更したい写真を送信します。ボットはリクエストに基づいて *4* つのバリエーションを送信します。

このコマンドの毎日の制限: 標準ユーザーは *20* 枚の写真、サブスクライバーは *40* 枚の写真。''',
            'expand': '''/expand コマンドを使用すると、AI を使用して画像を拡大できます。/expand コマンドを発行した後、写真を送信する必要があります。

*重要!* オリジナル画像の面積はキャンバス面積の 15% を超える必要があります。

このコマンドは 1 日 *20* 枚の画像の使用制限がありますが、サブスクライバーは 1 日に最大 *60* 枚の画像を処理できます。''',
            'reimage': '''/reimage コマンドは類似画像生成を使用します。このコマンドを使用した後、プロンプトを入力する必要があります。

*重要!* より良い結果を得るために、処理したい画像に何が描かれているかを説明してください。その後、画像を送信します。

このコマンドの毎日の制限: 通常ユーザーは *20* 枚の画像、サブスクライバーは *60* 枚の画像。''',
            'search': '''インターネットで情報を検索します。
このコマンドは /snap コマンドのリソースを使用して動作します。
また、制限も /snap コマンドから適用されます。''',
            'v': '''/v コマンドはボットの現在のバージョンと更新を表示します。''',
            'my_id': '''/my_id コマンドはあなたの user_id を表示します。''',
            'reg': '''/reg コマンドは Snaplix ボットに登録します。''',
            'sub': '''/sub コマンドはアクティブなサブスクリプションがあるかどうかを確認します。''',
            'get_sub': '''/get_sub コマンドを使用すると、サブスクリプションを購入できます。''',
            'limits': '''/limits コマンドは現在のコマンド使用制限を表示します。''',
            'ping': '''/ping コマンドはボットの接続ステータスを確認します。''',
            'info': '''/info コマンドはコマンドの詳細な説明を表示します ''',
        },
        "switch_lang": "日本語に切り替えました 🇯🇵.",
        "blocked_message": "一時的にブロックされています。10分後に再試行してください。",
        "registration_in_progress": "既に登録手続き中です。完了させてください。",
        "already_registered": "既に登録済みです。",
        "captcha": "キャプチャのテキストを入力してください",
        "successful_registration": "登録が*成功*しました！",
        "invitee_registered": "招待された方が登録しました！",
        "failed_registration": "4回の試行後、登録に*失敗*しました。",
        "incorrect_attempts": "不正確です。残りの試行回数: {attempts}。",
        "donate_amount": "寄付金額を1ドルから100ドルの間で指定してください。使用法: /donate <amount>",
        "invalid_donate_amount": "有効な寄付金額を1ドルから100ドルの間で指定してください。",
        "donate_description": "寄付金を提供することで、Snaplixプロジェクトの発展を支援します。\n寄付に対してSnap Coinsを受け取ります。*1 $USD = 10 Snap Coins*\n\n人を招待することでもSnap Coinsを獲得できます。*5人 = 50 Snap Coins*\nSnap Coinsはプロジェクトの*プレミアム機能*で使用されます\n\n寄付用の*リンク*:\n{link}",
        "donate_thank_you": "*プロジェクトのサポートありがとうございました*\n{amount} Snap Coinsを受け取ります\n注文ID: *{order_id}*",
        "check_payment_later": "後で再試行してください...",
        "order_not_paid": "寄付はまだ*支払われていません*。\n注文の支払いが成功した*後*、\"*Check Payment Status*\"ボタンを使用してください。",
        "order_status": "ステータス: *{status}*",
        "info_command_usage": "このコマンドは、すべてのボットコマンドを詳しく説明するために使用されます。コマンドについての情報を得るには、/info <bot command>を使用してください",
        "command_not_found": "このコマンドは存在しません。",
        "invite_link": "招待リンク - {link}",
        "my_invites": "招待 - *{invites}*",
        "my_coins": "アカウントに *{coins}* Snap Coinsがあります",
        "invite_reward": "おめでとうございます！5回の招待でアカウントが50 Snap Coins増えました",
        "less_than_5_invites": "*5*人未満しか招待していません",
        "donate_usage": "/donate <amount>",
        "invalid_amount": "金額は1から1000の間の正の整数でなければなりません。",
        "coins_given": "ユーザー: {user_id} に {amount} コインを与えました",
        "unfreeze_usage": "/unfreeze <user_id>",
        "user_unfreezed": "ユーザー {user_id} が解凍されました",
        "my_id": "あなたのID: {user_id}",
        "search_limit": "/searchコマンドは1 *分*に1回だけ使用できます。",
        "search_usage": "AI-Searchを使用するには、/search <あなたのリクエスト>を入力してください",
        "snap_ai_usage": "Snap-AIを使用するには、/snap <リクエスト> を入力してください",
        "thinking": "*考え中...*",
        "checking_request": "*リクエストを確認しています...*",
        "unethical_request": "*申し訳ありませんが、このリクエストには対応できません*",
        "searching": "*検索中...*",
        "send_image": "*1枚の画像のみを送信してください*",
        "enter_prompt": "*生成用のプロンプトを入力してください*",
        "generating": "*生成中...*",
        "analyzing_image": "*画像を分析しています...*",
        "whats_in_this_image": "この画像には何がありますか？",
        "choice_model": "*生成モデルを選択してください*",
        "choice_number": "*生成数を選択してください*",
        "msg_incorrect_use": "不正な使用 /msg",
        "messages_sent": "{count} ユーザーにメッセージが送信されました。",
        "stats_message": (
            "総ユーザー数: {total_users}\n"
            "凍結ユーザー: {frozen_users}\n"
            "処理中のユーザー: {processing_users}\n"
            "サブスクリプションユーザー: {paying_users}\n\n"
            "制限:\n{limits_message}"
        ),
        "enter_prompt_background": "*背景用のプロンプトを入力してください*",
        "enter_prompt_reference": "*参考画像用のプロンプトを入力してください*",
        "expanding": "*拡張中...*",
        "register_first": "ボットコマンドを使用するには、/reg コマンドで登録してください",
        "already_registered": "すでに登録されています。",
        "request_processing": "ご要望は処理中です。しばらくお待ちください。",
        "previous_donation_pending": "前回の寄付がまだ支払われていません。",
        "limit_reached": "今日の制限 {max_limit} に達しました。",
        "not_a_text": "これはテキストではありません",
        "not_an_image": "これは画像ではありません",
        "too_many_images": "画像が多すぎます",
        "image_generation_model": "画像生成モデル",
        "text_generation_model": "テキスト生成モデル",
        "config_menu": "設定メニュー:\n画像モデル: {img_model}\nテキストモデル: {txt_model}",
        "config_success": "設定が正常に完了しました！",
    }
}