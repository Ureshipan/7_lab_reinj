import tkinter as tk
from tkinter import ttk
import threading
import time
from PIL import Image, ImageTk

class NozzleCalculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Расчет сопла Лаваля")
        self.root.geometry("1200x800")
        
        # Переменные для хранения значений
        self.p_input = tk.StringVar(value="200000")
        self.t_input = tk.StringVar(value="1000")
        self.p_output = tk.StringVar(value="8000")
        self.g = tk.StringVar(value="2.0")
        self.alpha = tk.StringVar(value="14")
        self.betta = tk.StringVar(value="22")
        
        # Флаг для отслеживания состояния расчета
        self.calculation_running = False
        
        self.create_widgets()
        
    def create_widgets(self):
        # Создаем основной контейнер для разделения на левую и правую части
        self.main_container = ttk.Frame(self.root)
        self.main_container.pack(fill="both", expand=True)
        
        # Левая часть с формой ввода
        self.left_frame = ttk.Frame(self.main_container)
        self.left_frame.pack(side="left", fill="both", expand=True, padx=20, pady=20)
        
        # Создаем фрейм для формы ввода
        self.input_frame = ttk.LabelFrame(self.left_frame, text="Входные параметры", padding="20")
        self.input_frame.pack(fill="both", expand=True)
        
        # Создаем и размещаем поля ввода
        self.create_input_field("Давление воздуха Pe на входе в сопло (Па):", self.p_input, 0)
        self.create_input_field("Температура воздуха Te на входе в сопло (K):", self.t_input, 1)
        self.create_input_field("Давление воздуха P1 на выходе из сопла (Па):", self.p_output, 2)
        self.create_input_field("Расход воздуха G через сопло (Кг/с):", self.g, 3)
        self.create_input_field("Угол раскрытия сопла a - входная часть (°):", self.alpha, 4)
        self.create_input_field("Угол раскрытия сопла b - выходная часть (°):", self.betta, 5)
        
        # Кнопка расчета
        self.calc_button = ttk.Button(self.input_frame, text="Расчет", command=self.start_calculation)
        self.calc_button.grid(row=6, column=0, columnspan=2, pady=20)
        
        # Правая часть с изображением
        self.right_frame = ttk.Frame(self.main_container)
        self.right_frame.pack(side="right", fill="both", expand=True, padx=20, pady=20)
        
        # Загрузка и отображение изображения
        try:
            self.image = Image.open("soplo.png")
            # Изменяем размер изображения, сохраняя пропорции
            self.image.thumbnail((400, 400))
            self.photo = ImageTk.PhotoImage(self.image)
            self.image_label = ttk.Label(self.right_frame, image=self.photo)
            self.image_label.pack(pady=20)
        except Exception as e:
            print(f"Ошибка загрузки изображения: {e}")
        
        # Создаем фрейм для результатов
        self.result_frame = ttk.LabelFrame(self.root, text="Результаты расчета", padding="20")
        self.result_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Текстовое поле для вывода результатов
        self.result_text = tk.Text(self.result_frame, height=10, width=50)
        self.result_text.pack(fill="both", expand=True)
        
        # Прогресс-бар
        self.progress = ttk.Progressbar(self.result_frame, mode='determinate')
        self.progress.pack(fill="x", pady=10)
        
        # Кнопки управления
        self.control_frame = ttk.Frame(self.result_frame)
        self.control_frame.pack(fill="x", pady=10)
        
        self.stop_button = ttk.Button(self.control_frame, text="Остановить расчет", 
                                    command=self.stop_calculation, state="disabled")
        self.stop_button.pack(side="left", padx=5)
        
        self.paraview_button = ttk.Button(self.control_frame, text="Открыть ParaView", 
                                        command=self.open_paraview, state="disabled")
        self.paraview_button.pack(side="left", padx=5)
        
        self.log_button = ttk.Button(self.control_frame, text="Открыть лог", 
                                   command=self.open_log, state="disabled")
        self.log_button.pack(side="left", padx=5)
        
    def create_input_field(self, label_text, variable, row):
        ttk.Label(self.input_frame, text=label_text).grid(row=row, column=0, sticky="w", pady=5)
        entry = ttk.Entry(self.input_frame, textvariable=variable)
        entry.grid(row=row, column=1, sticky="ew", pady=5)
        
    def validate_input(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False
            
    def start_calculation(self):
        # Проверяем все входные значения
        values = [self.p_input.get(), self.t_input.get(), self.p_output.get(),
                 self.g.get(), self.alpha.get(), self.betta.get()]
        
        if not all(self.validate_input(v) for v in values):
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, "Ошибка: все поля должны содержать числовые значения")
            return
            
        # Отключаем кнопку расчета и включаем кнопку остановки
        self.calc_button.configure(state="disabled")
        self.stop_button.configure(state="normal")
        self.calculation_running = True
        
        # Очищаем поле вывода перед началом нового расчета
        self.result_text.delete(1.0, tk.END)
        
        # Запускаем расчет в отдельном потоке
        self.calculation_thread = threading.Thread(target=self.run_calculation)
        self.calculation_thread.start()
        
    def run_calculation(self):
        # Имитация этапов расчета
        stages = [
            "Инициализация расчета...",
            "Подготовка геометрии...",
            "Расчет сетки...",
            "Решение уравнений...",
            "Постобработка результатов..."
        ]
        
        self.progress["maximum"] = len(stages)
        self.progress["value"] = 0
        
        for i, stage in enumerate(stages):
            if not self.calculation_running:
                break
                
            # Добавляем новый этап в конец текста
            self.result_text.insert(tk.END, f"Этап {i+1}/{len(stages)}: {stage}\n")
            self.result_text.see(tk.END)  # Прокручиваем к последней строке
            self.progress["value"] = i + 1
            
            # Имитация работы
            time.sleep(2)
            
        if self.calculation_running:
            self.result_text.insert(tk.END, "\nРасчет успешно завершен!")
            self.paraview_button.configure(state="normal")
            self.log_button.configure(state="normal")
            
        self.calc_button.configure(state="normal")
        self.stop_button.configure(state="disabled")
        self.calculation_running = False
        
    def stop_calculation(self):
        self.calculation_running = False
        self.result_text.insert(tk.END, "\nРасчет остановлен пользователем")
        
    def open_paraview(self):
        self.result_text.insert(tk.END, "\nОткрытие ParaView...")
        # Здесь будет код для открытия ParaView
        
    def open_log(self):
        self.result_text.insert(tk.END, "\nОткрытие лог-файла...")
        # Здесь будет код для открытия лог-файла
        
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = NozzleCalculator()
    app.run() 