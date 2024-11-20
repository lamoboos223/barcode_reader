from PIL import Image
from pyzbar.pyzbar import decode

def read_barcode_from_id(image_path):
    """
    Read barcode from citizen ID card image using only pyzbar
    """
    # Read image using PIL instead of OpenCV
    try:
        image = Image.open(image_path)
        barcodes = decode(image)
        
        if barcodes:
            return barcodes[0].data.decode('utf-8')
            
    except Exception as e:
        print(f"Error decoding barcode: {str(e)}")
    
    return None

def main():
    # Example usage
    image_path = "./image.jpeg"  # Replace with your image path
    barcode_data = read_barcode_from_id(image_path)
    
    if barcode_data:
        print(f"Barcode data: {barcode_data}")
    else:
        print("No barcode detected")

if __name__ == "__main__":
    main()
