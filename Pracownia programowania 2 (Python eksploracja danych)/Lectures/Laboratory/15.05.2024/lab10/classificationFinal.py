import os
import numpy as np
from PIL import Image
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score
import joblib


def load_images_from_folder(folder, label):
    images = []
    labels = []
    for filename in os.listdir(folder):
        if filename.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif')):
            img_path = os.path.join(folder, filename)
            try:
                img = Image.open(img_path).convert('L')  # Konwersja do skali szarości
                img = img.resize((64, 64))  # Zmiana rozmiaru do 64x64
                img_array = np.array(img).flatten()  # Spłaszczenie obrazu
                images.append(img_array)
                labels.append(label)
            except Exception as e:
                print(f"Nie udało się załadować obrazu {img_path}: {e}")
    return images, labels


def prepare_data(yes_folder, no_folder):
    yes_images, yes_labels = load_images_from_folder(yes_folder, 1)
    no_images, no_labels = load_images_from_folder(no_folder, 0)
    
    X = np.array(yes_images + no_images)
    y = np.array(yes_labels + no_labels)
    
    return X, y


def train_svm(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    scaler = StandardScaler().fit(X_train)
    X_train_scaled = scaler.transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    svm = SVC(kernel='linear', random_state=42)
    svm.fit(X_train_scaled, y_train)
    
    y_pred = svm.predict(X_test_scaled)
    
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Classification Report:")
    print(classification_report(y_test, y_pred))
    
    return svm, scaler


def save_model(model, scaler, model_path, scaler_path):
    joblib.dump(model, model_path)
    joblib.dump(scaler, scaler_path)


def main():
    yes_folder = r'D:\sub\Pracownia programowania 2 (Python eksploracja danych)\Lectures\Laboratory\15.05.2024\lab10\photosParrot\yes'  # Podaj ścieżkę do folderu "yes"
    no_folder = r'D:\sub\Pracownia programowania 2 (Python eksploracja danych)\Lectures\Laboratory\15.05.2024\lab10\photosParrot\no'    # Podaj ścieżkę do folderu "no"
    
    X, y = prepare_data(yes_folder, no_folder)
    model, scaler = train_svm(X, y)
    
    save_model(model, scaler, 'svm_model.pkl', 'scaler.pkl')
    print("Model i skaler zostały zapisane.")


if __name__ == "__main__":
    main()
