import pygame as pg
import sys

# Initialize Pygame
pg.init()

# Define screen size and grid
SCREEN_SIZE = (800, 600)
CELL_SIZE = 20
GRID_WIDTH = SCREEN_SIZE[0] // CELL_SIZE
GRID_HEIGHT = SCREEN_SIZE[1] // CELL_SIZE

# Set up the display
screen = pg.display.set_mode(SCREEN_SIZE)
pg.display.set_caption("Map Editor")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
RED = (255, 0, 0)

# Define the map grid
grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

def draw_grid():
    """Draw the grid and walls on the screen."""
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            rect = pg.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            if grid[y][x] == 1:
                pg.draw.rect(screen, BLACK, rect)
            pg.draw.rect(screen, GRAY, rect, 1)

def draw_save_button():
    """Draw the 'Save Map' button on the screen."""
    button_rect = pg.Rect(SCREEN_SIZE[0] - 120, SCREEN_SIZE[1] - 50, 100, 40)
    pg.draw.rect(screen, RED, button_rect)
    font = pg.font.Font(None, 36)
    text_surf = font.render("Save Map", True, WHITE)
    screen.blit(text_surf, (button_rect.x + 10, button_rect.y + 5))
    return button_rect

def save_map(filename="map.txt"):
    """Save the current grid to a text file."""
    with open(filename, 'w') as file:
        for row in grid:
            file.write(''.join(map(str, row)) + '\n')

def main():
    clock = pg.time.Clock()
    placing_wall = True  # Toggle between placing and removing walls

    while True:
        screen.fill(WHITE)
        draw_grid()

        # Draw the Save Map button and store its rectangle
        save_button_rect = draw_save_button()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_p:
                    placing_wall = True  # Set to place walls
                elif event.key == pg.K_d:
                    placing_wall = False  # Set to delete walls
            elif event.type == pg.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pg.mouse.get_pos()
                grid_x = mouse_x // CELL_SIZE
                grid_y = mouse_y // CELL_SIZE

                # Check if the Save Map button is clicked
                if save_button_rect.collidepoint(mouse_x, mouse_y):
                    save_map()  # Save the map to a file
                    print("Map saved!")  # Debug message
                else:
                    # Modify the grid based on the current mode
                    if placing_wall:
                        grid[grid_y][grid_x] = 1  # Place a wall
                    else:
                        grid[grid_y][grid_x] = 0  # Remove a wall

        # Update the display
        pg.display.flip()
        clock.tick(30)  # Limit to 30 frames per second

if __name__ == "__main__":
    main()
