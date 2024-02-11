
from PIL import Image, ImageDraw, ImageFont
import random
import string

def generate_captcha():
    # Set the size of the image
    image_size = (300, 100)

    # Create an image with a white background
    image = Image.new('RGB', image_size, 'white')
    draw = ImageDraw.Draw(image)

    # Define fonts
    fonts = ["arial.ttf", "calibri.ttf", "times.ttf"]  # Add more fonts if needed

    # Ask the user to choose a font
    print("Choose a font:")
    for i, font in enumerate(fonts):
        print(f"{i + 1}. {font}")

    selected_font_index = int(input("Enter the number corresponding to the desired font: ")) - 1
    selected_font = fonts[selected_font_index]

    # Load the selected font
    font_size = 40
    font = ImageFont.truetype(selected_font, font_size)

    # Generate a random 6-character code
    captcha_code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))

    # Save the code to a text file
    with open("captcha_code.txt", "w") as file:
        file.write(captcha_code)

    # Draw random shapes and colors in the background
    for _ in range(30):
        shape = random.choice(["rectangle", "ellipse"])
        color = tuple(random.randint(0, 255) for _ in range(3))
        position = (random.randint(0, image_size[0]), random.randint(0, image_size[1]))
        size = (random.randint(20, 80), random.randint(20, 80))

        if shape == "rectangle":
            draw.rectangle([position, (position[0] + size[0], position[1] + size[1])], fill=color)
        elif shape == "ellipse":
            draw.ellipse([position, (position[0] + size[0], position[1] + size[1])], fill=color)

    # Draw the captcha code on the image
    text_position = ((image_size[0] - font_size * len(captcha_code)) // 4, (image_size[1] - font_size) // 4)
    draw.text(text_position, captcha_code, font=font, fill=(0, 0, 0))

    # Save the image
    image.save("captcha_image.jpeg")
    img = Image.open("captcha_image.jpeg")
    img.show()
if __name__ == "__main__":
    generate_captcha()
