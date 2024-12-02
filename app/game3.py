from rembg import remove
from PIL import Image

def remove_background(input_path, output_path):
    input_path = Image.open(input_path)
    output_path = remove(input_path)
    output_image.save(output_path)

if __name__ == "__main__":
    input_path = 'input_image.png'
    output_path = 'output_image.png'
    remove_background(input_path, output_path)
    print(f'Изображение с удаленным фоном сохранена в {output_path}')