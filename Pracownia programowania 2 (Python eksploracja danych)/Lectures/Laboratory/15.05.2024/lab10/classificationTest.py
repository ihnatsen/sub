import os
import random
import numpy as np
from PIL import Image, ImageTk
import joblib
import tkinter as tk


def load_and_prepare_image(image_path):
    img = Image.open(image_path).convert('L')  # Konwersja do skali szarości
    img = img.resize((64, 64))  # Zmiana rozmiaru do 64x64
    img_array = np.array(img).flatten()  # Spłaszczenie obrazu
    return img_array


def classify_images(model, scaler, image_paths):
    classifications = []
    for image_path in image_paths:
        img_array = load_and_prepare_image(image_path)
        img_array_scaled = scaler.transform([img_array])
        prediction = model.predict(img_array_scaled)
        label = "TAK" if prediction == 1 else "NIE"
        classifications.append((image_path, label))
    return classifications


def display_images_with_classifications(classifications):
    root = tk.Tk()
    root.title("Image Classifier Results")
    
    for i, (image_path, label) in enumerate(classifications):
        frame = tk.Frame(root)
        frame.pack(side=tk.TOP, pady=10)
        
        img = Image.open(image_path)
        img = img.resize((200, 200))  # Zmiana rozmiaru do wyświetlenia
        img_tk = ImageTk.PhotoImage(img)
        
        img_label = tk.Label(frame, image=img_tk)
        img_label.image = img_tk  # Zachowanie odniesienia do obrazka
        img_label.pack(side=tk.TOP)
        
        label_label = tk.Label(frame, text=label, font=("Helvetica", 16))
        label_label.pack(side=tk.BOTTOM)
    
    root.mainloop()


def main():
    model_path = 'svm_model.pkl'
    scaler_path = 'scaler.pkl'
    
    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)
    
    test_folder = r'D:\sub\Pracownia programowania 2 (Python eksploracja danych)\Lectures\Laboratory\15.05.2024\lab10\pthotosSomthing'  # Podaj ścieżkę do folderu z testowymi obrazami
    image_files = [os.path.join(test_folder, f) for f in os.listdir(test_folder) if f.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif'))]
    
    if len(image_files) < 5:
        print("Za mało obrazów w folderze testowym. Potrzebne są przynajmniej 3 obrazy.")
        return
    
    random_images = random.sample(image_files, 5)
    classifications = classify_images(model, scaler, random_images)
    display_images_with_classifications(classifications)


if __name__ == "__main__":
    main()
