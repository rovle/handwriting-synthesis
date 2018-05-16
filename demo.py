import time

from hand import Hand

if __name__ == '__main__':
    print("Entered main")
    start_time = time.time()  # start time of the loop

    hand = Hand()

    # usage demo
    lines = [
        "Now this is a story all about how",
        "My life got flipped turned upside down",
        "And I'd like to take a minute, just sit right there",
        "I'll tell you how I became the prince of a town called Bel-Air",
    ]
    biases = [1.0 for i in lines]
    styles = [7 for i in lines]
    stroke_colors = ['black', 'black', 'black', 'black']
    stroke_widths = [0.7, 0.7, 0.7, 0.7]
    line_height = 20
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
