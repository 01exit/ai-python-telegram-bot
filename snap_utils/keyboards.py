from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from .config import HF_IMAGE_MODELS


result = []
for i in HF_IMAGE_MODELS:
    result.append([InlineKeyboardButton(text=i.split('/')[1], callback_data=i)])
inline_models = InlineKeyboardMarkup(inline_keyboard=result)

result2 = []
row = []
for i in range(1, 11):
    row.append(InlineKeyboardButton(text=str(i), callback_data=str(i)))
    if len(row) == 5:
        result2.append(row)
        row = []
if row:
    result2.append(row)
Generation_numbers = InlineKeyboardMarkup(inline_keyboard=result2)

result3 = [
    [
        InlineKeyboardButton(text="🇺🇸English", callback_data='en'),
        InlineKeyboardButton(text="🇷🇺Русский", callback_data='ru')
    ],
    [
        InlineKeyboardButton(text="🇨🇳简体中文", callback_data='zh'),
        InlineKeyboardButton(text="🇮🇳हिन्दी", callback_data='hi')
    ],
    [
        InlineKeyboardButton(text="🇦🇪العربية", callback_data='ar'),
        InlineKeyboardButton(text="🇪🇸Español", callback_data='es')
    ],
    [
        InlineKeyboardButton(text="🇵🇹Português", callback_data='pt'),
        InlineKeyboardButton(text="🇺🇦Українська", callback_data='ua')
    ],
    [
        InlineKeyboardButton(text="🇫🇷Français", callback_data='fr'),
        InlineKeyboardButton(text="🇯🇵日本語", callback_data='jp')
    ]
]
lang_kb = InlineKeyboardMarkup(inline_keyboard=result3)

result4 = [
    [
        InlineKeyboardButton(text="Mistral Large", callback_data='mistral-large-latest'),
        InlineKeyboardButton(text="Codestral", callback_data='codestral-latest')
    ],
    [
        InlineKeyboardButton(text="Pixtral Large", callback_data='pixtral-large-latest'),
        InlineKeyboardButton(text="Mistral Small", callback_data='mistral-small-latest')
    ],
    [
        InlineKeyboardButton(text="Mistral Saba", callback_data='mistral-saba-latest'),
    ]
]
text_model = InlineKeyboardMarkup(inline_keyboard=result4)