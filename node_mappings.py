try:
    from .nodes.nodes_core import *
    from .nodes.nodes_aspect_ratio import *
    from .nodes.nodes_list import *
    from .nodes.nodes_lora import *
    from .nodes.nodes_controlnet import *
    from .nodes.nodes_pipe import *
    from .nodes.nodes_sdxl import *
    from .nodes.nodes_model_merge import *
    from .nodes.nodes_upscale import *
    from .nodes.nodes_xygrid import *
    from .nodes.nodes_legacy import *
except ImportError:
    print("\033[34mComfyroll Studio: \033[92mFailed to load Essential nodes\033[0m")

try:
    from .nodes.nodes_graphics_matplot import *
    from .nodes.nodes_graphics_text import *
    from .nodes.nodes_graphics_layout import *
    from .nodes.nodes_graphics_filter import *
    from .nodes.nodes_graphics_template import *
    from .nodes.nodes_graphics_pattern import *
except ImportError:
    print("\033[34mComfyroll Studio: \033[92mFailed to load Graphics nodes\033[0m")

try:
    from .nodes.nodes_animation_interpolation import *
    from .nodes.nodes_animation_io import *
    from .nodes.nodes_animation_prompt import *
    from .nodes.nodes_animation_schedulers import *
    from .nodes.nodes_animation_schedules import *
    from .nodes.nodes_animation_lists import *
    from .nodes.nodes_animation_utils import *
    from .nodes.nodes_animation_cyclers import *
except ImportError:
    print("\033[34mComfyroll Studio: \033[92mFailed to load Animation nodes\033[0m")
    
try:
    from .nodes.nodes_utils_logic import *
    from .nodes.nodes_utils_index import *
    from .nodes.nodes_utils_conversion import *
    from .nodes.nodes_utils_random import *
    from .nodes.nodes_utils_text import *
    from .nodes.nodes_utils_other import *
except ImportError:
    print("\033[34mComfyroll Studio: \033[92mFailed to load Utility nodes\033[0m")

NODE_CLASS_MAPPINGS = { 
    "CR Color Panel": CR_ColorPanel,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "CR Color Panel": "🌁 CR Color Panel",
}
