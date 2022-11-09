import subprocess
import json
import sys
import os
import re
from pathlib import Path

import gradio as gr
import numpy as np
from tqdm import tqdm

from modules.ui import create_refresh_button, folder_symbol
from modules.shared import opts, OptionInfo
from modules import shared, paths, script_callbacks

def on_ui_tabs():

    with gr.Blocks(analytics_enabled=False) as model_kitchen:

        # structure
        gr.HTML("<h1>Model Kitchen!!!</h1>", css="{ display: flex; align-items: center; justify-items: center }")

    return (model_kitchen, "Model Kitchen", "model-kitchen"),

def on_ui_settings():
    picker_path = Path(paths.script_path) / "model-kitchen"
    section = ('model-kitchen', "Model Kitchen")

script_callbacks.on_ui_settings(on_ui_settings)
script_callbacks.on_ui_tabs(on_ui_tabs)