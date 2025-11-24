from .database import get_limits, has_subscription

async def limits_get(user_id: str):
    limits = get_limits(user_id)
    image_limit, image2_limit, snap_limit, vision_limit, upscale_limit, background_limit, expand_limit, reimage_limit, inpaint_limit = limits
    if has_subscription(user_id):
        response = (
            f"Your daily *Snap-Pro* limits:\n"
            f"Image Generation: *{image_limit}/1000*\n"
            f"Image Generation 2: *{image2_limit}/60*\n"
            f"Snap-AI: *{snap_limit}/500*\n"
            f"AI-Vision: *{vision_limit}/300*\n"
            f"AI-Upscale: *{upscale_limit}/30*\n"
            f"AI-Background-Change: *{background_limit}/60*\n"
            f"AI-Expand-Image: *{expand_limit}/60*\n"
            f"AI-Reference-Image: *{reimage_limit}/60*\n"
            f"AI-Inpaint-Image: *{inpaint_limit}/60*\n"
            )
        return response
    else:
        response = (
        f"Your daily *Free* limits:\n"
        f"Image Generation: *{image_limit}/40*\n"
        f"Image Generation 2: *{image2_limit}/20*\n"
        f"Snap-AI: *{snap_limit}/30*\n"
        f"AI-Vision: *{vision_limit}/20*\n"
        f"AI-Upscale: *{upscale_limit}/10*\n"
        f"AI-Background-Change: *{background_limit}/20*\n"
        f"AI-Expand-Image: *{expand_limit}/20*\n"
        f"AI-Reference-Image: *{reimage_limit}/20*\n"
        f"AI-Inpaint-Image: *{inpaint_limit}/20*\n"
        )
        return response