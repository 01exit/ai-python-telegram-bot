# Telegram bot using AI APIs
Telegram bot integrated with AI APIs, including Hugging Face for image generation and Mistral AI for text generation

### Task:
Creating a full-featured Telegram bot for image generation, image editing, and text generation using AI.

### Solution:
Integration of third-party APIs for image generation and editing.
Image generation and editing: Hugging Face, Bria.ai
Text generation: Mistral.ai

### Result:
When the user sends specific commands to the bot, such as "/image", the bot generates an image based on the user's request.

### Launch:
1. Clone the repository:

```bash
git clone <repo_url>
cd project
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file based on `.example_env` and add your API keys.

4. Run the bot:

```bash
python app.py
```


## Environment variables
The following tokens are required in your `.env` file:

- `TOKEN` – Telegram bot token  
- `HF_API_KEY` – Hugging Face API token  
- `BRIA_API_KEY` – Bria.ai API token  
- `MISTRAL_API_KEY` – Mistral.ai API token  
- `CRYPTOMUS_KEY` – Cryptomus payment API token  

All required variables are listed in `.example_env`.

### Stack:
Python, Aiogram, and the basic imports listed in requirements.txt.

### Important notes:
The bot was rewritten several times and deployed on different platforms (Heroku and Render). This specific version is adapted for deployment on Heroku.

## Project structure

```bash
project/
├── app.py
├── Procfile
├── requirements.txt
├── runtime.txt
├── comicbd.ttf
├── .env     # local, .example_env
├── handlers.py
│
├── snap_actions/
│   ├── bria_background_change.py
│   ├── bria_expand.py
│   ├── bria_inpaint.py
│   ├── bria_inpaint_create_mask.py
│   ├── bria_reimage.py
│   ├── bria_upscaling.py
│   ├── image_generator_BRIA.py
│   ├── image_generator_HF.py
│   ├── search.py
│   ├── snap_generate.py
│   ├── snap_vision.py
│   └── __init__.py
│
└── snap_utils/
    ├── captcha.py
    ├── checker.py
    ├── config.py
    ├── cryptomus.py
    ├── database.py
    ├── keyboards.py
    ├── limits.py
    ├── multilang.py
    ├── utils.py
    └── __init__.py
```
## Bot commands:
`/reg` - Start the registration process for new users

`/info` - Get full information about the command

`/lang` - Change your language

`/config` - selection of different models for generation

`/image` - Create a unique image using Snap-AI

`/image2` - Another method for generating images with Snap-AI

`/reimage` - Generates a similar image (reference)

`/upscale` - Improve image quality and size

`/expand` - Image enlargement through AI generation

`/snap` - Generate text with Snap-AI

`/search` - Search for information on the internet with Snap-AI

`/vision` - Get a description of an image provided

`/background` - Change the background in a photo

`/donate` - Donate to the project

`/my_coins` - View Snap Coin Balance

`/my_id` - Get your user ID in the bot

`/invite` - Generate an invitation link

`/my_invites` - View the number of invited users

`/invite_reward` - Get a reward for invitations

`/v` - Display the current bot version and updates

