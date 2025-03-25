import time
import os

printers_and_colours = {
    "FDM (Regular printer)": [
        [230, 250, 350]
        ["PLA", 0.5, 0.02, 1.25],
        ["ABS", 0.6, 0.03, 1.04],
        ["PETG", 0.7, 0.025, 1.27],
        ["TPU", 1.0, 0.035, 1.20]
    ],
    "SLA (Resin Printer)": [
        [150, 90, 175]
        ["Standard Resin", 1.2, 0.08, 1.10],
        ["Tough Resin", 1.5, 0.12, 1.15],
        ["Flexible Resin", 1.8, 0.15, 1.05]
    ],
    "SLS (Metal Printer)": [
        [400, 400, 400]
        ["Nylon 12", 1.0, 0.06, 1.01],
        ["TPU Powder", 1.3, 0.09, 1.12]
    ],
    "colours": [
        "Red", "Blue", "Black", "White", "Green", "Yellow", "Purple", "Orange"
    ]
}

"""
This dictionary holds three 3d printers and their usable filaments.
The structure is [build volume], [Name, cost per mm, ]
"""
