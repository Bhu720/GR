import cv2
from pyzbar.pyzbar import decode

def scan_qr_code(image_path):
    image = cv2.imread(image_path)
    decoded_objects = decode(image)

    for obj in decoded_objects:
        print(f"Type: {obj.type}, Data: {obj.data.decode('utf-8')}")

    cv2.imshow('QR Code Scanner', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

image_path = 'path/to/your/image_with_qr_code.png'
scan_qr_code(image_path)
