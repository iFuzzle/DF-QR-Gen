import csv
import qrcode
from PIL import Image, ImageDraw, ImageFont


def generate_qr_code(data, filename):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)


def add_text_to_image(input_image_path, output_image_path, text):
    image = Image.open(input_image_path)

    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    font = font.font_variant(size=25)
    draw.text((50, image.height - 30), text, "black", font=font)
    image.save(output_image_path)


def main():
    csv_file = 'data.csv'  # Change this to the path of your CSV file
    with open(csv_file, newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            name = row[0]  # Assuming the first column contains names
            code = row[1]  # Assuming the second column contains codes
            qr_filename = f'{name}_qr.png'  # Adjust filename format if needed
            generate_qr_code(code, qr_filename)
            add_text_to_image(input_image_path=qr_filename, output_image_path=qr_filename, text=code)
            print(f'Generated QR code for {name}')


if __name__ == "__main__":
    main()
