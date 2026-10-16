import qrcode

def generate_qr_code(data, filename="output_qr.png"):
    """
    Generates a QR code image from the provided text or URL and saves it to disk.
    """
    try:
        # Configure QR code properties
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        
        # Add data to the QR code
        qr.add_data(data)
        qr.make(fit=True)

        # Create an image from the QR Code instance
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Save the image
        img.save(filename)
        print(f"Success! QR code saved successfully as '{filename}'.")

    except Exception as e:
        print(f"An error occurred while generating the QR code: {e}")

if __name__ == "__main__":
    print("========================================")
    print("      QR CODE GENERATOR UTILITY         ")
    print("========================================")
    
    user_input = input("Enter the text or URL to encode into a QR code: ")
    custom_filename = input("Enter output filename (default: output_qr.png): ").strip()
    
    if not custom_filename:
        custom_filename = "output_qr.png"
    elif not custom_filename.endswith(".png"):
        custom_filename += ".png"

    generate_qr_code(user_input, custom_filename)
