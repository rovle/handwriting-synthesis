import time

from hand import Hand
from utils.string_utils import accomodate_list_to_character_limit

if __name__ == '__main__':
    print("Entered main")
    start_time = time.time()  # start time of the loop

    hand = Hand()

    # usage demo
    lines = [
        "What is Lorem Ipsum",
        "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
        "Where does it come from?",
        "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. ",
        "What is Lorem Ipsum",
        "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
        "Where does it come from?",
        "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. ",
        "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. ",
    ]
    lines = accomodate_list_to_character_limit(lines)
    biases = [0.80 for i in lines]
    styles = [8 for i in lines]
    stroke_colors = ['black' for i in lines]
    stroke_widths = [0.9 for i in lines]
    line_height = 40
    view_width = 1000

    hand.write(
        filename='img/usage_demo.svg',
        lines=lines,
        biases=biases,
        styles=styles,
        stroke_colors=stroke_colors,
        stroke_widths=stroke_widths,
        line_height=line_height,
        view_width=view_width,
        align_center=False
    )

    # # demo number 1 - fixed bias, fixed style
    # lines = lyrics.all_star.split("\n")
    # biases = [.75 for i in lines]
    # styles = [12 for i in lines]
    #
    # hand.write(
    #     filename='img/all_star.svg',
    #     lines=lines,
    #     biases=biases,
    #     styles=styles,
    # )
    #
    # # demo number 2 - fixed bias, varying style
    # lines = lyrics.downtown.split("\n")
    # biases = [.75 for i in lines]
    # styles = np.cumsum(np.array([len(i) for i in lines]) == 0).astype(int)
    #
    # hand.write(
    #     filename='img/downtown.svg',
    #     lines=lines,
    #     biases=biases,
    #     styles=styles,
    # )
    #
    # # demo number 3 - varying bias, fixed style
    # lines = lyrics.give_up.split("\n")
    # biases = .2 * np.flip(np.cumsum([len(i) == 0 for i in lines]), 0)
    # styles = [7 for i in lines]
    #
    # hand.write(
    #     filename='img/give_up.svg',
    #     lines=lines,
    #     biases=biases,
    #     styles=styles,
    # )
    print("Time Taken: ", (time.time() - start_time) / 60, " Minutes")
