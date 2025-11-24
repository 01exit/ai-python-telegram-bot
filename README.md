# Telegram bot using AI APIs
Telegram bot integrated with AI APIs, including Hugging Face for image generation and Mistral AI for text generation

**Task:**
Creating a full-featured Telegram bot for image generation, image editing, and text generation using AI.

# Solution:
Integration of third-party APIs for image generation and editing.
Image generation and editing: Hugging Face, Bria.ai
Text generation: Mistral.ai

# Result:
When the user sends specific commands to the bot, such as "/image", the bot generates an image based on the user's request.

# Launch:
Install all dependencies from requirements.txt and create a Telegram bot, adding its token to the TOKEN field in the .env file.
You must also have API tokens from the services listed above, as well as a payment system token from Cryptomus.
All required environment variables are described in the .example_env file.

# Stack:
Python, Aiogram, and the basic imports listed in requirements.txt.

# Important notes:
The bot was rewritten several times and deployed on different platforms (Heroku and Render). This specific version is adapted for deployment on Heroku.
