import omni
import omni.usd
import omni.appwindow
import carb
from carb.input import KeyboardEventType

app_window = omni.appwindow.get_default_app_window()
keyboard = app_window.get_keyboard()
input = carb.input.acquire_input_interface()
stage = omni.usd.get_context().get_stage()

text = stage.GetPrimAtPath("/World/Text")

TextNode_01 = stage.GetPrimAtPath("/World/Text/ActionGraph/generate_3d_text")
attr_01 = TextNode_01.GetAttribute("inputs:text")

def on_keyboard_input(e):
    #current_input = str(e.input)
    #print(current_input)
    #attr_01.Set(attr_01.Get() + ("" if current_input.contains("KeyboardInput.") else current_input)
    attr_01.Set(attr_01.Get() + str(e.input).replace("KeyboardInput.", ""))

keyboard_sub_id = input.subscribe_to_keyboard_events(keyboard, on_keyboard_input)

