# Импортируем модули для создания GUI и работы со случайными числами
from tkinter import *
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
    """
    Генерирует два случайных числа от 1 до 6,
    загружает соответствующие изображения и отображает их в окне.
    Предыдущие изображения удаляются для избежания наложения.
    """
    global images
    images.clear()  # Очищаем список изображений

    # Удаляем все старые изображения из фрейма
    for widget in image_frame.winfo_children():
        widget.destroy()

    # Генерируем случайные значения для двух кубиков
    x = random.randint(1, 6)
    y = random.randint(1, 6)

    # Обновляем текстовый результат
    result_label.config(text=f"🎲 Выпало: {x} и {y}")

    try:
        # Загружаем изображение для первого кубика
        img1 = PhotoImage(file=f"{x}.png")
        lbl1 = Label(image_frame, image=img1, bg="#f0f0f0")
        lbl1.image = img1  # Сохраняем ссылку — важно для Tkinter!
        lbl1.pack(side=LEFT, padx=10)
        images.append(img1)  # Добавляем в список, чтобы изображение не удалилось

        # Загружаем изображение для второго кубика
        img2 = PhotoImage(file=f"{y}.png")
        lbl2 = Label(image_frame, image=img2, bg="#f0f0f0")
        lbl2.image = img2
        lbl2.pack(side=LEFT, padx=10)
        images.append(img2)

    except Exception as e:
        # Если файлы не найдены — выводим сообщение об ошибке
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