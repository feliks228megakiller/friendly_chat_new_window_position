import customtkinter
# створюємо клас App 
class App(customtkinter.CTk):
    def __init__(self, app_width, app_height):
        super().__init__()
        # задаємо властивості, що зберігають розміри екрану додатку
        self.APP_WIDTH = app_width
        self.APP_HEIGHT = app_height
        # задаємо властивості, що зберігають розміри екрану комп'ютера
        self.PC_SCREEN_WIDTH = self.winfo_screenwidth()
        self.PC_SCREEN_HEIGHT = self.winfo_screenheight()
        # встановлюємо розмір додатку та його розташування на екрані комп'ютера
        self.geometry(f"{self.APP_WIDTH}x{self.APP_HEIGHT}+{700}+{300}") #справа сверху {1400}+{0}, слева сверху {0}+{0}, слева снизу {0}+{600}, {1400}+{600}, по центру {700}+{300}
        # задаємо назву вікну додатку
        self.title("Головне вікно додатку")
# створюємо об'єкт від класу App
app = App(app_width= 400, app_height = 300)
