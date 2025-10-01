# Импортируем модули для создания GUI и работы со случайными числами
from tkinter import *
from PIL import Image, ImageTk
import random


# Создаём главное окно приложения
window = Tk()
window.title("🎲 Cube Random Game")  # Заголовок окна
window.geometry("300x350")           # Размер окна
window.resizable(False, False)       # Запрещаем изменение размера
window.configure(bg="#f0f0f0")       # Устанавливаем светлый фон

# Глобальный список для хранения ссылок на изображения (чтобы сборщик мусора их не удалил)
images = []

# Фрейм для размещения изображений кубиков
image_frame = Frame(window, bg="#f0f0f0")
image_frame.pack(pady=20)

# Метка для отображения текстового результата броска
result_label = Label(window, text="", font=("Arial", 12), bg="#f0f0f0")
result_label.pack(pady=10)


# 🎯 Основная функция игры — бросок кубиков
def Game():
    global images
    images.clear()

    for widget in image_frame.winfo_children():
        widget.destroy()

    x = random.randint(1, 6)
    y = random.randint(1, 6)

    result_label.config(text=f"🎲 Выпало: {x} и {y}")

    try:
        # Размер, до которого будем масштабировать кубики (например, 80x80 пикселей)
        target_size = (80, 80)

        # Загружаем и масштабируем первое изображение
        img_path1 = f"CubeGame/image/{x}.png"
        pil_img1 = Image.open(img_path1).resize(target_size, Image.LANCZOS)
        tk_img1 = ImageTk.PhotoImage(pil_img1)
        lbl1 = Label(image_frame, image=tk_img1, bg="#f0f0f0")
        lbl1.image = tk_img1
        lbl1.pack(side=LEFT, padx=10)
        images.append(tk_img1)

        # Загружаем и масштабируем второе изображение
        img_path2 = f"CubeGame/image/{y}.png"
        pil_img2 = Image.open(img_path2).resize(target_size, Image.LANCZOS)
        tk_img2 = ImageTk.PhotoImage(pil_img2)
        lbl2 = Label(image_frame, image=tk_img2, bg="#f0f0f0")
        lbl2.image = tk_img2
        lbl2.pack(side=LEFT, padx=10)
        images.append(tk_img2)

    except Exception as e:
        result_label.config(text="❌ Ошибка: файлы 1-6.png не найдены!")
        print(f"[ОШИБКА ЗАГРУЗКИ] {e}")

# 🎨 Интерфейс: размещаем элементы управления
Label(window, text="🎲 Кубик: Брось два кубика!", font=("Arial", 14, "bold"), bg="#f0f0f0").pack(pady=20)

# Кнопка для броска кубиков
Button(
    window,
    text="Бросить кубики!",
    command=Game,
    font=("Arial", 12),
    bg="#4CAF50",   # Цвет фона кнопки
    fg="white",     # Цвет текста
    padx=10,        # Внутренние отступы
    pady=5
).pack(pady=10)

# Устанавливаем начальный текст
result_label.config(text="Нажмите кнопку, чтобы бросить кубики")

# Запуск главного цикла обработки событий Tkinter
window.mainloop()