import time

from hand import Hand
from utils.string_utils import accomodate_list_to_character_limit





def generate_handwriting(text, style=8, bias=0.8, strokes_width=0.9, line_height=40, view_width=1000):
    print("Started generating.")
    start_time = time.time()  # start time of the loop

    hand = Hand()

    # usage demo
    
    lines = text.split(sep='\n')
    lines = [x for x in lines if len(x) > 0]
    lines = accomodate_list_to_character_limit(lines)
    biases = [bias for i in lines]
    styles = [style for i in lines]
    stroke_colors = ['black' for i in lines]
    stroke_widths = [strokes_width for i in lines]
    hand.write(
        filename='img/generiran_rukopis.svg',
        lines=lines,
        biases=biases,
        styles=styles,
        stroke_colors=stroke_colors,
        stroke_widths=stroke_widths,
        line_height=line_height,
        view_width=view_width,
        align_center=False
    )

    print("Time Taken: ", (time.time() - start_time) / 60, " Minutes")
