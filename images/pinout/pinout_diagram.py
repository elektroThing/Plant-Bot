###########################################
#
# Example script to build a
# pinout diagram. Includes basic
# features and convenience classes.
#
###########################################

from pinout.core import Group, Image
from pinout.components.layout import Diagram_2Rows
from pinout.components.pinlabel import PinLabelGroup, PinLabel
from pinout.components.text import TextBlock
from pinout.components import leaderline as lline
from pinout.components.legend import Legend
from pinout.components.annotation import AnnotationLabel

# Import data for the diagram
import data

# Create a new diagram
# The Diagram_2Rows class provides 2 panels,
# 'panel_01' and 'panel_02', to insert components into.
diagram = Diagram_2Rows(1250, 1050, 900, "diagram")

# Add a stylesheet
diagram.add_stylesheet("styles.css", embed=True)

# Create a group to hold the pinout-diagram components.
graphic = diagram.panel_01.add(Group(400, 42))

# Add and embed an image
hardware = graphic.add(Image("hardware.png", embed=True))

# Measure and record key locations with the hardware Image instance
hardware.add_coord("gpio0", 231, 106)
hardware.add_coord("gpio8", 231, 265)
hardware.add_coord("esp32", 280, 225)
hardware.add_coord("reset", 139, 262)
hardware.add_coord("vcc", 206, 100)
hardware.add_coord("ch340", 140, 107)
hardware.add_coord("usb", 140, 30)
hardware.add_coord("ldo", 204, 214)
hardware.add_coord("button", 350, 53)
hardware.add_coord("j7", 212, 30)
hardware.add_coord("j6", 278, 30)
hardware.add_coord("ne555", 201, 315)
hardware.add_coord("opamp", 285, 322)
hardware.add_coord("sht20", 202, 257)
hardware.add_coord("ws2812", 212, 157)
hardware.add_coord("drv", 192, 104)
# Other (x,y) pairs can also be stored here
hardware.add_coord("pin_pitch_v", 0, 18)
hardware.add_coord("pin_pitch_h", 18, 0)

# Create a single pin label
graphic.add(
    PinLabel(
        content="Micro USB",
        x= hardware.coord("usb").x,
        y=hardware.coord("usb").y,
        tag="conn",
        body={"x": 117, "y": 30, "width":100, "height":25},
        scale=(-1,-1),
        leaderline={"direction": "vh"},
    )
)

graphic.add(
    PinLabel(
        content="Reset",
        x= hardware.coord("reset").x,
        y=hardware.coord("reset").y,
        tag="btn",
        body={"x": 160, "y": 30, "width":100, "height":25},
        scale=(-1,1),
        leaderline={"direction": "vh"},
    )
)

graphic.add(
    PinLabel(
        content="CH340 USB-to-UART",
        x= hardware.coord("ch340").x,
        y=hardware.coord("ch340").y,
        tag="mcu",
        body={"x": 117, "y": 25, "width":180, "height":25},
        scale=(-1,-1),
        leaderline={"direction": "vh"},
    )
)

graphic.add(
    PinLabel(
        content="3.3V 800mA LDO",
        x= hardware.coord("ldo").x,
        y=hardware.coord("ldo").y,
        tag="pwr",
        body={"x": 180, "y": 30, "width":180, "height":25},
        scale=(-1,-1),
        leaderline={"direction": "vh"},
    )
)


graphic.add(
    PinLabel(
        content="ESP32-C3-MINI",
        x= hardware.coord("esp32").x,
        y=hardware.coord("esp32").y,
        tag="mcu",
        body={"x": 117, "y": 30, "width":180, "height":25},
        scale=(1,-1),
        leaderline={"direction": "vh"},
    )
)

graphic.add(
    PinLabel(
        content="Button",
        x= hardware.coord("button").x,
        y=hardware.coord("button").y,
        tag="btn",
        body={"x": 117, "y": 30, "width":100, "height":25},
        scale=(1,1),
        leaderline={"direction": "vh"},
    )
)

graphic.add(
    PinLabel(
        content="Motor",
        x= hardware.coord("j7").x,
        y=hardware.coord("j7").y,
        tag="conn",
        body={"x": 240, "y": 30, "width":100, "height":25},
        scale=(1,-1),
        leaderline={"direction": "vh"},
    )
)

graphic.add(
    PinLabel(
        content="Grow LED",
        x= hardware.coord("j6").x,
        y=hardware.coord("j6").y,
        tag="conn",
        body={"x": 180, "y": 0, "width":100, "height":25},
        scale=(1,-1),
        leaderline={"direction": "vh"},
    )
)

graphic.add(
    PinLabel(
        content="NE555 Timer",
        x= hardware.coord("ne555").x,
        y=hardware.coord("ne555").y,
        tag="sns",
        body={"x": 210, "y": 30, "width":120, "height":25},
        scale=(-1,1),
        leaderline={"direction": "vh"},
    )
)

graphic.add(
    PinLabel(
        content="Op Amp",
        x= hardware.coord("opamp").x,
        y=hardware.coord("opamp").y,
        tag="sns",
        body={"x": 280, "y": 60, "width":100, "height":25},
        scale=(-1,1),
        leaderline={"direction": "vh"},
    )
)

graphic.add(
    PinLabel(
        content="SHT20",
        x= hardware.coord("sht20").x,
        y=hardware.coord("sht20").y,
        tag="sns",
        body={"x": 180, "y": 30, "width":100, "height":25},
        scale=(-1,-1),
        leaderline={"direction": "vh"},
    )
)

graphic.add(
    PinLabel(
        content="DRV8837CDSGR",
        x= hardware.coord("drv").x,
        y=hardware.coord("drv").y,
        tag="pwr",
        body={"x": 180, "y": 60, "width":180, "height":25},
        scale=(-1,-1),
        leaderline={"direction": "vh"},
    )
)

graphic.add(
    PinLabel(
        content="WS2812 LED",
        x= hardware.coord("ws2812").x,
        y=hardware.coord("ws2812").y,
        tag="mcu",
        body={"x": 210, "y": 20, "width":120, "height":25},
        scale=(-1,-1),
        leaderline={"direction": "vh"},
    )
)

# Create pinlabels on the upper header
graphic.add(
    PinLabelGroup(
        x=hardware.coord("gpio0").x,
        y=hardware.coord("gpio0").y,
        scale=(1, 1),
        pin_pitch=hardware.coord("pin_pitch_h", raw=True),
        label_start=(300, 450),
        label_pitch=(0, -30),
        labels=data.upper_header,
        leaderline=lline.Curved(direction="vh"),
    )
)
# Create pinlabels on the lower header
graphic.add(
    PinLabelGroup(
        x=hardware.coord("gpio8").x,
        y=hardware.coord("gpio8").y,
        scale=(1, 1),
        pin_pitch=hardware.coord("pin_pitch_h", raw=True),
        label_start=(300, 550),
        label_pitch=(0, -30),
        labels=data.lower_header,
        #body={"x": 200, "y": 100},
        leaderline=lline.Curved(direction="vh"),
    )
)

# Create a title and description text-blocks
title_block = diagram.panel_02.add(
    TextBlock(
        data.title,
        x=20,
        y=30,
        line_height=18,
        tag="panel title_block",
    )
)
diagram.panel_02.add(
    TextBlock(
        data.description,
        x=20,
        y=60,
        width=title_block.width,
        height=diagram.panel_02.height - title_block.height,
        line_height=18,
        tag="panel text_block",
    )
)

# Create a legend
legend = diagram.panel_02.add(
    Legend(
        data.legend,
        x=340,
        y=8,
        max_height=132,
    )
)

# Export the diagram via commandline:
# >>> py -m pinout.manager --export pinout_diagram.py diagram.svg
