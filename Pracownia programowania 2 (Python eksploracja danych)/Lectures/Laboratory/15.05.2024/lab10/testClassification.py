import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


class ImageClassifierApp:
    def __init__(self, master, image_folder):
        self.master = master
        self.master.title("Image Classifier")
        self.image_folder = image_folder
        self.image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif'))]
        self.current_image_index = 0
        self.yes_folder = os.path.join(image_folder, 'yes')
        self.no_folder = os.path.join(image_folder, 'no')
        os.makedirs(self.yes_folder, exist_ok=True)
        os.makedirs(self.no_folder, exist_ok=True)
        
        self.image_label = tk.Label(master)
        self.image_label.pack()
        
        self.yes_button = tk.Button(master, text="TAK", command=self.yes_action, width=10)
        self.yes_button.pack(side=tk.LEFT, padx=20, pady=20)
        
        self.no_button = tk.Button(master, text="NIE", command=self.no_action, width=10)
        self.no_button.pack(side=tk.RIGHT, padx=20, pady=20)
        
        self.load_image()

    def load_image(self):
        if self.current_image_index < len(self.image_files):
            image_path = os.path.join(self.image_folder, self.image_files[self.current_image_index])
            image = Image.open(image_path)
            image.thumbnail((800, 600))  # Resize to fit into the window
            self.photo = ImageTk.PhotoImage(image)
            self.image_label.config(image=self.photo)
        else:
            messagebox.showinfo("Koniec", "Wszystkie obrazy zostały skategoryzowane.")
            self.master.quit()

    def yes_action(self):
        self.move_image(self.yes_folder)
        self.next_image()

    def no_action(self):
        self.move_image(self.no_folder)
        self.next_image()

    def move_image(self, target_folder):
        image_path = os.path.join(self.image_folder, self.image_files[self.current_image_index])
        target_path = os.path.join(target_folder, self.image_files[self.current_image_index])
        os.rename(image_path, target_path)

    def next_image(self):
        self.current_image_index += 1
        self.load_image()


def main():
    root = tk.Tk()
    image_folder = r'D:\sub\Pracownia programowania 2 (Python eksploracja danych)\Lectures\Laboratory\15.05.2024\lab10\photosParrot'  # Replace with the path to your image folder
    app = ImageClassifierApp(root, image_folder)
    root.mainloop()


if __name__ == "__main__":
    main()
