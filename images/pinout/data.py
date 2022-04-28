legend = [
    ("Sensor", "sns"),
    ("Button", "btn"),
    ("Ground", "gnd"),
    ("GPIO", "gpio"),
    ("Connector", "conn"),
    ("Power", "pwr"),
    ("Microcontroller", "mcu"),
]

# Pinlabels

upper_header = [
    [
        ("5V", "pwr"),
    ],
    [
         ("GND", "gnd"),
    ],
    [
         ("3.3V", "pwr"),
    ],
    [
         ("0", "gpio"),
    ],
    [
         ("1", "gpio"),
    ],
    [
         ("10", "gpio"),
    ],
    [
         ("3", "gpio"),
    ],
    [
         ("2", "gpio"),
    ],
]

lower_header = [
    [
        ("8", "gpio"),
        ("LED", "mcu"),
    ],
    [
         ("9", "gpio"),
    ],
    [
         ("19", "gpio"),
    ],
    [
         ("18", "gpio"),
    ],
    [
         ("7", "gpio"),
    ],
    [
         ("6", "gpio"),
    ],
    [
         ("5", "gpio"),
    ],
    [
         ("4", "gpio"),
    ],
]

# Text
annotation_usb = ["Micro USB", "conn"]
annotation_reset = ["Reset", "btn"]
annotation_ch340 = ["ch340", "mcu"]
annotation_ldo = ["3.3V 800mA LDO", "pwr"]
annotation_button = ["Button", "btn"]
annotation_J7 = ["J7", "conn"]
annotation_J6 = ["J6", "conn"]
annotation_ne555 = ["NE555", "sns"]
annotation_opamp = ["Op-Amp", "sns"]
annotation_sht20 = ["SHT20", "sns"]
annotation_ws2812 = ["WS2812 LED", "mcu"]

title = "<tspan class='h1'>Plant Bot</tspan>"

description = """Automated plant care"""