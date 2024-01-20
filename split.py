import cv2
import numpy as np
from PIL import Image
import os
import logging

def extract_and_save_objects(input_folder, output_folder, min_area, output_format='gif'):
    logging.basicConfig(level=logging.DEBUG)
    logging.info(f"Starting: {input_folder}")


    for image_file in os.listdir(input_folder):
        logging.info(f"Picture found: {image_file}")
        if image_file.endswith('.png'):
            image_path = os.path.join(input_folder, image_file)
            logging.info(f"Picture processing: {image_path}")

            # Picture loading
            image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
            if image is None:
                logging.warning(f"Cannot load picture: {image_path}")
                continue

            # Search for contours
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            _, thresh = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)
            contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            if not contours:
                logging.info(f"Контуры не найдены в: {image_path}")
                continue

            object_number = 0
            for contour in contours:
                # Check area of contour
                area = cv2.contourArea(contour)
                if area > min_area:
                    # Create mask
                    # Mask must be single-channel for grayscale image
                    mask = np.zeros(image.shape[:2], dtype=np.uint8)
                    cv2.drawContours(mask, [contour], -1, color=255, thickness=cv2.FILLED)

                    # Apply mask
                    result = cv2.bitwise_and(image, image, mask=mask)

                    # Search for bounding box
                    x, y, w, h = cv2.boundingRect(contour)
                    cropped_result = result[y:y+h, x:x+w]

                    # Convert cropped result to PIL format for saving
                    obj_pil = Image.fromarray(cv2.cvtColor(cropped_result, cv2.COLOR_BGRA2RGBA))

                    # Save object
                    output_path = os.path.join(output_folder, f'object_{object_number}.{output_format}')
                    obj_pil.save(output_path, format=output_format)
                    logging.info(f"Object saved: {output_path}")
                    object_number += 1


extract_and_save_objects('/workspace/input', '/workspace/output', min_area=400)
