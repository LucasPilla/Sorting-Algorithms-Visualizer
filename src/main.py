import pygame
from display import Window, TextBox, SlideBox, DropdownBox, ButtonBox
from algs import algorithmsDict
from random import randint
import time
import math

# Initialize pygame modules
pygame.init()

# Constants
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 500
BAR_AREA_HEIGHT = 400
WIDGET_Y = 440

# Font
baseFont = pygame.font.SysFont('Arial', 24)

# Colors
GREY = (100, 100, 100)
GREEN = (125, 240, 125)
WHITE = (250, 250, 250)
RED = (255, 50, 50)
BLACK = (0, 0, 0)
BLUE = (50, 50, 255)

# Default values
DEFAULT_ARRAY_SIZE = 100
MIN_BAR_HEIGHT = 10
MAX_BAR_HEIGHT = 400

class SortingVisualizer:
    """Main class to handle the sorting visualization"""

    def __init__(self):
        pygame.display.set_caption('Sorting Algorithms Visualizer')
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.window = Window(self.screen)
        self.clock = pygame.time.Clock()

        self._setup_widgets()
        self._reset_state()

    def _setup_widgets(self):
        """Initialize all UI widgets"""
        self.window.add_widget(
            widget_id='size_input',
            widget=TextBox((30, WIDGET_Y, 100, 50), 'Size', GREY, baseFont, str(DEFAULT_ARRAY_SIZE))
        )
        self.window.add_widget(
            widget_id='delay_slider',
            widget=SlideBox((140, WIDGET_Y, 150, 50), 'Delay', GREY, baseFont)
        )
        self.window.add_widget(
            widget_id='algorithm_input',
            widget=DropdownBox((300, WIDGET_Y, 200, 50), 'Algorithm', GREY, baseFont,
                            list(algorithmsDict.keys()), WHITE)
        )
        self.window.add_widget(
            widget_id='play_button',
            widget=ButtonBox((510, WIDGET_Y + 5, 40, 40), 'res/playButton.png', 'res/stopButton.png')
        )

    def _reset_state(self):
        """Reset the visualizer state"""
        self.numbers = []
        self.is_sorting = False
        self.sorting_iterator = None
        self.last_iteration = 0

    def _generate_random_array(self, size):
        """Generate a random array for sorting"""
        try:
            num_bars = max(1, min(int(size), SCREEN_WIDTH))  # Validate input
        except (ValueError, TypeError):
            num_bars = DEFAULT_ARRAY_SIZE

        return [randint(MIN_BAR_HEIGHT, MAX_BAR_HEIGHT) for _ in range(num_bars)]

    def _draw_bars(self, red_indices=(-1, -1), blue_indices=(-1, -1), green_indices=None):
        """
        Draw the bars with appropriate colors

        Args:
            red_indices: Tuple of indices to color red (comparison)
            blue_indices: Tuple of indices to color blue (swap)
            green_indices: Set of indices to color green (sorted)
        """
        if not self.numbers:
            return

        num_bars = len(self.numbers)
        bar_width = SCREEN_WIDTH / num_bars
        ceil_width = math.ceil(bar_width)
        green_indices = green_indices or set()

        for idx, height in enumerate(self.numbers):
            # Determine bar color based on state
            if idx in red_indices:
                color = RED
            elif idx in blue_indices:
                color = BLUE
            elif idx in green_indices:
                color = GREEN
            else:
                color = GREY

            # Draw the bar
            x_pos = idx * bar_width
            y_pos = BAR_AREA_HEIGHT - height
            pygame.draw.rect(self.screen, color, (x_pos, y_pos, ceil_width, height))

    def _start_sorting(self):
        """Initialize and start the sorting process"""
        size_input = self.window.get_widget_value('size_input')
        self.numbers = self._generate_random_array(size_input)

        algorithm_name = self.window.get_widget_value('algorithm_input')
        self.sorting_iterator = algorithmsDict[algorithm_name](
            self.numbers, 0, len(self.numbers) - 1
        )
        self.is_sorting = True
        self.last_iteration = time.time()

    def _update_sorting(self, delay):
        """Update the sorting visualization"""
        current_time = time.time()

        if current_time - self.last_iteration >= delay:
            try:
                self.numbers, red1, red2, blue1, blue2 = next(self.sorting_iterator) # type: ignore
                self.last_iteration = current_time
                self._draw_bars(red_indices=(red1, red2), blue_indices=(blue1, blue2))
            except StopIteration:
                # Sorting completed
                self.is_sorting = False
                self.window.set_widget_value('play_button', False)
                self._draw_bars(green_indices=set(range(len(self.numbers))))
        else:
            # Redraw with current state
            self._draw_bars()

    def run(self):
        """Main application loop"""
        running = True

        while running:
            self.screen.fill(WHITE)

            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                self.window.update(event)

            # Get current state
            is_playing = self.window.get_widget_value('play_button')
            delay = self.window.get_widget_value('delay_slider') / 10

            # Handle play/pause
            if is_playing and not self.is_sorting:
                self._start_sorting()
            elif not is_playing and self.is_sorting:
                self.is_sorting = False

            # Update visualization
            if self.is_sorting:
                self._update_sorting(delay)
            else:
                # Show array in final state
                green_indices = set(range(len(self.numbers))) if self.numbers else set()
                self._draw_bars(green_indices=green_indices)

            # Render UI and update display
            self.window.render()
            pygame.display.update()
            self.clock.tick(60)  # Limit to 60 FPS

        pygame.quit()


def main():
    """Entry point for the application"""
    visualizer = SortingVisualizer()
    visualizer.run()


if __name__ == '__main__':
    main()
