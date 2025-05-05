import pygame

# Size gamewindow
rows = 20
colums = 10
cells = 40
gamewindow_width, gamewindow_height = colums * cells, rows * cells

# Sidebar

sidebar_width = 200
preview_height_fraction = 0.7
score_height_fraction = 1 - preview_height_fraction

# Window

padding = 20
window_width = gamewindow_width + sidebar_width + padding * 3
window_height = gamewindow_height + padding * 2

# Game Settings

block_Offset = pygame.Vector2(colums // 2, -1)
update_start_speed = 800
move_wait_time = 200
rotate_wait_time = 200

# Colors

linecolor = 255,0,255
purple4 = 85,26,139
purple2 = 145,44,238
plum1 = 255,187,255
orchid1 = 255,131,250
maroon3 = 205,41,144
mediumpurple1 = 171,130,255
plum4 = 139,102,139
thistle2 = 238,210,238

# shapes

Tetrominos = {
    'T': {'shape': [(0,0), (-1,0), (1,0), (0,-1)], 'color': purple4},
    'O': {'shape': [(0,0), (0,-1), (1,0), (1,-1)], 'color': purple2},
    'J': {'shape': [(0,0), (0,-1), (0,1), (-1,1)], 'color': plum1},
    'L': {'shape': [(0,0), (0,-1), (0,1), (1,1)], 'color': orchid1},
    'I': {'shape': [(0,0), (0,-1), (0,-2), (0,1)], 'color': maroon3},
    'S': {'shape': [(0,0), (-1,0), (0,-1), (1,-1)], 'color': mediumpurple1},
    'Z': {'shape': [(0,0), (1,0), (0,-1), (-1,-1)], 'color': thistle2}
}

Scoredata = {1: 25, 2: 50, 3: 100, 4: 250}


