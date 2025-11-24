HF_IMAGE_MODELS = [
    'black-forest-labs/FLUX.1-schnell',
    'stabilityai/stable-diffusion-xl-base-1.0',
    'stabilityai/stable-diffusion-3.5-large',
    'prithivMLmods/SD3.5-Large-Photorealistic-LoRA',
    'kudzueye/Boreal',
    'black-forest-labs/FLUX.1-dev'
]
HF_SUBSCRIPTION_MODELS = [
    'kudzueye/Boreal',
    'black-forest-labs/FLUX.1-dev'
]

info_dict = {
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
}
version = {
    'version': '''Bot version: "*Snaplix 1.5*"

Available functions:
— *Image generation, 2 methods*
— *Snap-AI text generation*
— *AI-Vision images*
— *AI Image Expand*
— *AI Image Upscaling*
— *AI Background Change*
— *AI Reference Image*
— *AI Web Search*


Changelog:
— The new command /search has been added.
'''
}