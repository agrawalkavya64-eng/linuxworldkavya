import pygame

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("X/O Game")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SIZE = 200A

board = [["", "", ""],
         ["", "", ""],
         ["", "", ""]]

player = "X"
font = pygame.font.Font(None, 100)
winner_font = pygame.font.Font(None, 60)
run = True
winner = None

while run:
    screen.fill(WHITE)

    
    pygame.draw.line(screen, BLACK, (200, 0), (200, 600), 5)
    pygame.draw.line(screen, BLACK, (400, 0), (400, 600), 5)
    pygame.draw.line(screen, BLACK, (0, 200), (600, 200), 5)
    pygame.draw.line(screen, BLACK, (0, 400), (600, 400), 5)

    
    for row in range(3):
        for col in range(3):
            if board[row][col] != "":
                text = font.render(board[row][col], True, BLACK)
                screen.blit(text, (col * SIZE + 70, row * SIZE + 50))

   
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != "":
            winner = board[row][0]
    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != "":
            winner = board[0][col]
   
    if board[0][0] == board[1][1] == board[2][2] != "":
        winner = board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        winner = board[0][2]

    if winner:
        text = winner_font.render(winner + " wins!", True, (255, 0, 0))
        screen.blit(text, (180, 260))
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not winner: 
                mouse_x, mouse_y = pygame.mouse.get_pos()
                row = mouse_y // SIZE
                col = mouse_x // SIZE
                if board[row][col] == "":
                    board[row][col] = player
                    player = "O" if player == "X" else "X"

    pygame.display.update()

pygame.quit()
