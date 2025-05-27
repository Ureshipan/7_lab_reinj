import tkinter as tk
from tkinter import ttk
import threading
import time
from PIL import Image, ImageTk
import os
import subprocess
import shutil

class NozzleCalculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Расчет сопла Лаваля")
        self.root.geometry("1200x800")
        
        # Настройка масштабирования
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        
        # Переменные для хранения значений
        self.p_input = tk.StringVar(value="200000")
        self.t_input = tk.StringVar(value="1000")
        self.p_output = tk.StringVar(value="8000")
        self.g = tk.StringVar(value="2.0")
        self.alpha = tk.StringVar(value="14")
        self.betta = tk.StringVar(value="22")
        
        # Флаг для отслеживания состояния расчета
        self.calculation_running = False
        
        # Путь к папке с OpenFOAM
        self.nozzle_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "nozzle_1")
        
        self.create_widgets()
        
    def create_widgets(self):
        # Создаем основной контейнер для разделения на левую и правую части
        self.main_container = ttk.Frame(self.root)
        self.main_container.grid(row=0, column=0, sticky="nsew")
        self.main_container.grid_rowconfigure(0, weight=1)
        self.main_container.grid_columnconfigure(0, weight=1)
        self.main_container.grid_columnconfigure(1, weight=1)
        
        # Левая часть с формой ввода
        self.left_frame = ttk.Frame(self.main_container)
        self.left_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
        self.left_frame.grid_rowconfigure(0, weight=1)
        self.left_frame.grid_columnconfigure(0, weight=1)
        
        # Создаем фрейм для формы ввода
        self.input_frame = ttk.LabelFrame(self.left_frame, text="Входные параметры", padding="20")
        self.input_frame.grid(row=0, column=0, sticky="nsew")
        self.input_frame.grid_rowconfigure(6, weight=1)
        self.input_frame.grid_columnconfigure(1, weight=1)
        
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
        self.right_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
        self.right_frame.grid_rowconfigure(0, weight=1)
        self.right_frame.grid_columnconfigure(0, weight=1)
        
        # Загрузка и отображение изображения
        try:
            image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "soplo.png")
            self.image = Image.open(image_path)
            # Изменяем размер изображения, сохраняя пропорции
            self.image.thumbnail((400, 400))
            self.photo = ImageTk.PhotoImage(self.image)
            self.image_label = ttk.Label(self.right_frame, image=self.photo)
            self.image_label.grid(row=0, column=0, pady=20)
        except Exception as e:
            print(f"Ошибка загрузки изображения: {e}")
        
        # Создаем фрейм для результатов
        self.result_frame = ttk.LabelFrame(self.root, text="Прогресс расчета", padding="20")
        self.result_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)
        self.result_frame.grid_rowconfigure(0, weight=1)
        self.result_frame.grid_columnconfigure(0, weight=1)
        
        # Текстовое поле для вывода результатов
        self.result_text = tk.Text(self.result_frame, height=10, width=50)
        self.result_text.grid(row=0, column=0, sticky="nsew")
        
        # Прогресс-бар
        self.progress = ttk.Progressbar(self.result_frame, mode='determinate')
        self.progress.grid(row=1, column=0, sticky="ew", pady=10)
        
        # Кнопки управления
        self.control_frame = ttk.Frame(self.result_frame)
        self.control_frame.grid(row=2, column=0, sticky="ew", pady=10)
        self.control_frame.grid_columnconfigure(0, weight=1)
        self.control_frame.grid_columnconfigure(1, weight=1)
        self.control_frame.grid_columnconfigure(2, weight=1)
        
        self.stop_button = ttk.Button(self.control_frame, text="Остановить расчет", 
                                    command=self.stop_calculation, state="disabled")
        self.stop_button.grid(row=0, column=0, padx=5)
        
        self.paraview_button = ttk.Button(self.control_frame, text="Открыть ParaView", 
                                        command=self.open_paraview, state="disabled")
        self.paraview_button.grid(row=0, column=1, padx=5)
        
        self.log_button = ttk.Button(self.control_frame, text="Открыть лог", 
                                   command=self.open_log, state="disabled")
        self.log_button.grid(row=0, column=2, padx=5)
        
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
            
    def update_params_file(self):
        """Обновляет файл params.txt с новыми значениями"""
        params_content = f"""p_input
{self.p_input.get()}

t_input
{self.t_input.get()}

p_output
{self.p_output.get()}

G
{self.g.get()}

alpha
{self.alpha.get()}

betta
{self.betta.get()}
width
"""
        with open(os.path.join(self.nozzle_path, "params.txt"), "w") as f:
            f.write(params_content)
            
    def run_command(self, command, shell=True):
        """Выполняет команду и возвращает результат"""
        try:
            result = subprocess.run(command, shell=shell, capture_output=True, text=True)
            return result.stdout, result.stderr
        except Exception as e:
            return "", str(e)
            
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
        try:
            # Этап 1: Обновление параметров
            self.result_text.insert(tk.END, "Этап 1/5: Обновление параметров...\n")
            self.progress["value"] = 1
            self.update_params_file()
            
            if not self.calculation_running:
                return
                
            # Этап 2: Запуск ChangeParams.sh
            self.result_text.insert(tk.END, "Этап 2/5: Применение параметров...\n")
            self.progress["value"] = 2
            stdout, stderr = self.run_command(f"cd {self.nozzle_path} && ./ChangeParams.sh")
            if stderr:
                self.result_text.insert(tk.END, f"Ошибка при применении параметров: {stderr}\n")
                return
                
            if not self.calculation_running:
                return
                
            # Этап 3: Запуск Run.sh
            self.result_text.insert(tk.END, "Этап 3/5: Запуск расчета...\n")
            self.progress["value"] = 3
            stdout, stderr = self.run_command(f"cd {self.nozzle_path} && ./Run.sh")
            if stderr:
                self.result_text.insert(tk.END, f"Ошибка при запуске расчета: {stderr}\n")
                return
                
            if not self.calculation_running:
                return
                
            # Этап 4: Ожидание завершения расчета
            self.result_text.insert(tk.END, "Этап 4/5: Ожидание завершения расчета...\n")
            self.progress["value"] = 4
            
            # Проверяем наличие файла log
            log_file = os.path.join(self.nozzle_path, "log")
            while self.calculation_running:
                if os.path.exists(log_file):
                    with open(log_file, "r") as f:
                        log_content = f.read()
                        if "Finalising parallel run" in log_content:
                            break
                time.sleep(5)
                
            if not self.calculation_running:
                return
                
            # Этап 5: Завершение
            self.result_text.insert(tk.END, "Этап 5/5: Расчет завершен!\n")
            self.progress["value"] = 5
            
            # Активируем кнопки для просмотра результатов
            self.paraview_button.configure(state="normal")
            self.log_button.configure(state="normal")
            
        except Exception as e:
            self.result_text.insert(tk.END, f"Ошибка: {str(e)}\n")
        finally:
            self.calc_button.configure(state="normal")
            self.stop_button.configure(state="disabled")
            self.calculation_running = False
        
    def stop_calculation(self):
        self.calculation_running = False
        self.result_text.insert(tk.END, "\nРасчет остановлен пользователем")
        
    def open_paraview(self):
        try:
            subprocess.Popen(["paraFoam", "-case", self.nozzle_path])
            self.result_text.insert(tk.END, "\nОткрытие ParaView...")
        except Exception as e:
            self.result_text.insert(tk.END, f"\nОшибка при открытии ParaView: {str(e)}")
        
    def open_log(self):
        try:
            log_file = os.path.join(self.nozzle_path, "log")
            if os.path.exists(log_file):
                if os.name == 'nt':  # Windows
                    os.startfile(log_file)
                else:  # Linux/Mac
                    subprocess.Popen(["xdg-open", log_file])
                self.result_text.insert(tk.END, "\nОткрытие лог-файла...")
            else:
                self.result_text.insert(tk.END, "\nЛог-файл не найден")
        except Exception as e:
            self.result_text.insert(tk.END, f"\nОшибка при открытии лог-файла: {str(e)}")
        
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = NozzleCalculator()
    app.run() 