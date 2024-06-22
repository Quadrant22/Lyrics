import pygame
import os

pygame.init()
pygame.mixer.init()

# Constants for screen dimensions
SCREEN_WIDTH = 850
SCREEN_HEIGHT = 900

# Create the Pygame window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mariam's Lyrics Reader Don't be Scared of Halloween")

# Load your music file
song_file = 'dont-be-scared-halloween-v2.mp3'  
pygame.mixer.music.load(song_file)



lyrics = [
    {"time": 15, "text": "Dont be scared of Halloween", "image": "Images/witchespot (13).jpg"},
    {"time": 18, "text": "Or the things that go unseen", "image": "Images/witchespot (2).jpg"},
    {"time": 21, "text": "Theres no need to feed the fear", "image": "Images/CatGallery(6).jpg"},
    
    {"time": 24, "text": "When the ghosts and ghouls are awfully near", "image": "Images/witchespot (16).jpg"},
    {"time": 27, "text": "Witches love to swoop on sticks", "image": "Images/witchespot (19).jpg"},
    {"time": 29, "text": "Formation flying, stunting tricks", "image": "Images/CatGallery (24).jpg"},
    {"time": 32, "text": "Loop the loop and scoop the earth", "image": "Images/CatGallery(6).jpg"},
    {"time": 35, "text": "Flinging sweets for all theyre worth", "image": "Images/flingingsweets (2).jpg"},

    {"time": 37, "text": "People say the girls a witch", "image": "Images/witchespot (6).jpg"},
    {"time": 40, "text": "Kids are cruel and love to snitch", "image": "Images/witchespot (11).jpg"},
    {"time": 43, "text": "They say shes got a funny squint", "image": "Images/witchespot (4).jpg"},
    {"time": 45, "text": "And sucks on garlic like a mint", "image": "Images/witchespot (8).jpg"},

    {"time": 48, "text": "Katie knows a spell or two", "image": "Images/witchespot (15).jpg"},
    {"time": 51, "text": "She can make a toad of you", "image": "Images/witchespot (1).jpg"},
    {"time": 54, "text": "So dont go near or else you might", "image": "Images/CatGallery (18).jpg"},
    {"time": 56, "text": "Crouch and croak throughout the night", "image": "Images/witchespot (3).jpg"},

    {"time": 59, "text": "October thirty first is the time", "image": "Images/flingingsweets (3).jpg"},
    # The audio was at 1:02 one minute and 2 seconds, so increasing seconds to 62 seconds
    {"time": 62 , "text": "They taunt her worst and its a crime", "image": "Images/CatGallery (27).jpg"},
    {"time": 64, "text": "(chant)”Your familys fiendish and a clutch", "image": "Images/CatGallery (24).jpg"},
    {"time": 67, "text": "Of witches goblins ghouls and such", "image": "Images/kittypumpkin (1).jpg"},

    {"time": 70, "text": "Out on the streets there are sweets about", "image": "Images/flingingsweets (4).jpg"},
    {"time": 73, "text": "Katie shes at home, Katies missing out", "image": "Images/witcheshouse.jpg"},
    {"time": 75, "text": "Out in the night the kids are tricking fun", "image": "Images/witcheshouses.jpg"},
    {"time": 78, "text": "Katie, Katie shes at home and Katies feeling glum", "image": "Images/CatGallery (25).jpg"},
    {"time": 81, "text": "Katie, Katie, Katie, Katie", "image": "Images/witchespot (18).jpg"},
    {"time": 83, "text": "Shes the Witch whos scared of Halloween", "image": "Images/witchespot (17).jpg"},
]

# Initialize variables for displaying lyrics
current_lyric_index = 0
current_time = 0

# Create a font for displaying lyrics
font = pygame.font.Font("Sanctuary.ttf", 45)

# Create a function to display both text and image
def display_lyrics_and_image(current_time):
    global current_lyric_index

    # Find the next lyric to display
    while current_lyric_index < len(lyrics) - 1 and lyrics[current_lyric_index + 1]["time"] <= current_time:
        current_lyric_index += 1

    # Display the current lyric's text
    lyric_text = lyrics[current_lyric_index]["text"]
    text = font.render(lyric_text, True, (255, 0, 0))
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50))

    # Check if an image should be displayed
    image_path = lyrics[current_lyric_index].get("image", None)
    if image_path:
        image = pygame.image.load(image_path)
        image_rect = image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        
        # Display the image
        screen.fill((255, 255, 255))  # Clear the screen
        screen.blit(image, image_rect)

    # Display text
    screen.blit(text, text_rect)
    pygame.display.flip()

   
pygame.mixer.music.play()

    # Main event loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    current_time = pygame.time.get_ticks() / 1000  # Get the current time in seconds
    display_lyrics_and_image(current_time)  # Display lyrics and image

    clock.tick(35)  # Limit the frame rate to 30 FPS

     

pygame.quit()