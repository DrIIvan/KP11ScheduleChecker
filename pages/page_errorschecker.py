from flet_route import Params, Basket
import usefull_functions
import flet as ft 


class ErrorChecker:
    def view(self, page: ft.Page, params, basket: Basket):
        # Иницализация параметров страницы.-------------------------
        
        page.title = "Проверка ошибок в расписании"
        page.window_height = 500
        page.window_width = 400
        page.window_visible = True
        page.update()

        # ----------------------------------------------------------
        # Блок создания функций.------------------------------------
        
        # ----------------------------------------------------------
        # Создание элеменов управления.-----------------------------

        excel_dropdown_text = ft.Text(
            "Выберите файл для работы:",
            text_align=ft.TextAlign.CENTER,
            size=20
        )
        
        # Выбор .xlsm файлов
        excel_dropdown_list = ft.Container(
            content=ft.Dropdown(
                border_color="cyan", 
                hint_text="Выберите файл .xlsm"
            ), 
            alignment=ft.alignment.center
        )

        formater_button = ft.ElevatedButton(
            text="Выбрать",
            color="cyan"
        )

        # ----------------------------------------------------------
        # Возврашаем список элементов управления.-------------------

        for file in usefull_functions.files_list("./"):
            if ".xlsm" in file:
                excel_dropdown_list.content.options.append(ft.dropdown.Option(file))

        # ----------------------------------------------------------
        # Возврашаем список элементов управления.-------------------

        return ft.View(
            "/", controls=[
                excel_dropdown_text,
                excel_dropdown_list,
                formater_button,
                ]
            )
