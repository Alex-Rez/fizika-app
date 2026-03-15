import flet as ft
import time

# === БАЗА ЗНАНИЙ: ТЕОРИЯ И ЗАДАЧИ ===
TOPICS = {
    "heat": {
        "title": "🌡️ Количество теплоты",
        "icon": "🌡️",
        "theory": """
КОЛИЧЕСТВО ТЕПЛОТЫ (Q)

Что это такое?
Теплота — это форма энергии, которая передаётся между телами вследствие разности их температур.

Простыми словами:
Когда вы нагреваете воду в чайнике, вы передаёте ей энергию. Эта энергия и называется количеством теплоты.

Единица измерения: Джоуль (Дж)

Основная формула:
Q = c · m · (t₂ - t₁)

Что означает каждая буква:
• Q — количество теплоты [Дж]
• c — удельная теплоёмкость [Дж/(кг·°C)] — показывает, сколько энергии нужно для нагрева 1 кг вещества на 1°C
• m — масса тела [кг]
• t₁ — начальная температура [°C]
• t₂ — конечная температура [°C]

Важно запомнить:
✅ При нагревании: t₂ > t₁ → Q > 0 (тело получает тепло)
✅ При охлаждении: t₂ < t₁ → Q < 0 (тело отдаёт тепло)

Удельные теплоёмкости некоторых веществ:
• Вода: 4200 Дж/(кг·°C)
• Лёд: 2100 Дж/(кг·°C)
• Алюминий: 880 Дж/(кг·°C)
• Железо: 460 Дж/(кг·°C)
• Медь: 380 Дж/(кг·°C)
""",
        "tasks": [
            {"level": 1, "condition": "Какое количество теплоты потребуется для нагревания 2 кг воды от 20°C до 70°C? (c = 4200 Дж/(кг·°C))", "given": "m = 2 кг, t₁ = 20°C, t₂ = 70°C, c = 4200 Дж/(кг·°C)", "formula": "Q = c · m · (t₂ - t₁)", "answer": 420000, "unit": "Дж", "hint": "Найди разность температур: Δt = 70 - 20 = 50°C. Затем Q = 4200 · 2 · 50"},
            {"level": 2, "condition": "Сколько теплоты выделится при остывании 3 кг алюминия от 100°C до 20°C? (c = 880 Дж/(кг·°C))", "given": "m = 3 кг, t₁ = 100°C, t₂ = 20°C, c = 880 Дж/(кг·°C)", "formula": "Q = c · m · (t₁ - t₂)", "answer": 211200, "unit": "Дж", "hint": "При остывании: Q = c · m · (t₁ - t₂) = 880 · 3 · 80"},
            {"level": 3, "condition": "Нагревание 5 кг вещества от 15°C до 65°C потребовало 1 050 000 Дж. Найдите удельную теплоёмкость.", "given": "m = 5 кг, t₁ = 15°C, t₂ = 65°C, Q = 1 050 000 Дж", "formula": "c = Q / (m · (t₂ - t₁))", "answer": 4200, "unit": "Дж/(кг·°C)", "hint": "Вырази c: c = Q / (m · Δt) = 1050000 / (5 · 50)"},
            {"level": 4, "condition": "Смешали 2 кг воды при 30°C и 3 кг воды при 80°C. Какая установится температура? (c одинаковая)", "given": "m₁ = 2 кг, t₁ = 30°C, m₂ = 3 кг, t₂ = 80°C", "formula": "t = (m₁·t₁ + m₂·t₂) / (m₁ + m₂)", "answer": 60, "unit": "°C", "hint": "Уравнение теплового баланса: t = (2·30 + 3·80) / 5"},
            {"level": 5, "condition": "Сколько теплоты нужно для нагревания 1.5 кг меди от 25°C до 125°C? (c = 380 Дж/(кг·°C))", "given": "m = 1.5 кг, t₁ = 25°C, t₂ = 125°C, c = 380 Дж/(кг·°C)", "formula": "Q = c · m · (t₂ - t₁)", "answer": 57000, "unit": "Дж", "hint": "Q = 380 · 1.5 · (125 - 25) = 380 · 1.5 · 100"}
        ]
    },
    "combustion": {
        "title": "🔥 Теплота сгорания",
        "icon": "🔥",
        "theory": """
ТЕПЛОТА СГОРАНИЯ (Q)

Что это такое?
Топливо — вещество, при сгорании которого выделяется некоторое количество теплоты.

Простыми словами:
Когда вы зажигаете костёр или включаете газовую плиту, топливо сгорает и выделяет тепло. Это тепло и называется теплотой сгорания.

Единица измерения: Джоуль (Дж)

Основная формула:
Q = q · m

Что означает каждая буква:
• Q — количество теплоты [Дж]
• q — удельная теплота сгорания [Дж/кг] — показывает, сколько энергии выделится при сгорании 1 кг топлива
• m — масса топлива [кг]

Важно запомнить:
✅ При сгорании тепло ВСЕГДА выделяется (Q > 0)
✅ Чем больше q, тем больше энергии даёт топливо

Удельная теплота сгорания некоторых видов топлива:
• Бензин: 46 000 000 Дж/кг
• Природный газ: 44 000 000 Дж/кг
• Уголь: 30 000 000 Дж/кг
• Дрова: 10 000 000 Дж/кг
• Порох: 3 800 000 Дж/кг
""",
        "tasks": [
            {"level": 1, "condition": "Сколько теплоты выделится при полном сгорании 2 кг бензина? (q = 46 000 000 Дж/кг)", "given": "m = 2 кг, q = 46 000 000 Дж/кг", "formula": "Q = q · m", "answer": 92000000, "unit": "Дж", "hint": "Q = 46 000 000 · 2 = 92 000 000 Дж"},
            {"level": 2, "condition": "Какое количество теплоты выделится при сгорании 5 кг дров? (q = 10 000 000 Дж/кг)", "given": "m = 5 кг, q = 10 000 000 Дж/кг", "formula": "Q = q · m", "answer": 50000000, "unit": "Дж", "hint": "Q = 10 000 000 · 5 = 50 000 000 Дж"},
            {"level": 3, "condition": "При сгорании угля выделилось 90 000 000 Дж. Найдите массу сгоревшего угля. (q = 30 000 000 Дж/кг)", "given": "Q = 90 000 000 Дж, q = 30 000 000 Дж/кг", "formula": "m = Q / q", "answer": 3, "unit": "кг", "hint": "m = Q / q = 90 000 000 / 30 000 000"},
            {"level": 4, "condition": "Для обогрева помещения требуется 220 000 000 Дж. Сколько кг природного газа нужно сжечь? (q = 44 000 000 Дж/кг)", "given": "Q = 220 000 000 Дж, q = 44 000 000 Дж/кг", "formula": "m = Q / q", "answer": 5, "unit": "кг", "hint": "m = 220 000 000 / 44 000 000 = 5 кг"},
            {"level": 5, "condition": "Найдите удельную теплоту сгорания топлива, если при сгорании 4 кг выделилось 184 000 000 Дж.", "given": "m = 4 кг, Q = 184 000 000 Дж", "formula": "q = Q / m", "answer": 46000000, "unit": "Дж/кг", "hint": "q = Q / m = 184 000 000 / 4"}
        ]
    },
    "melting": {
        "title": "🧊 Теплота плавления",
        "icon": "🧊",
        "theory": """
ТЕПЛОТА ПЛАВЛЕНИЯ И КРИСТАЛЛИЗАЦИИ (Q)

Что это такое?
Фазовый переход — процесс перехода вещества из одного агрегатного состояния в другое.

Простыми словами:
Когда лёд тает и превращается в воду, или вода замерзает и превращается в лёд — происходит фазовый переход. Для этого нужна энергия (при плавлении) или выделяется энергия (при кристаллизации).

Единица измерения: Джоуль (Дж)

Основная формула:
Q = λ · m

Что означает каждая буква:
• Q — количество теплоты [Дж]
• λ (лямбда) — удельная теплота плавления [Дж/кг] — показывает, сколько энергии нужно для плавления 1 кг вещества
• m — масса вещества [кг]

Важно запомнить:
✅ При плавлении: тело ПОЛУЧАЕТ тепло (Q > 0)
✅ При кристаллизации: тело ОТДАЁТ тепло (Q < 0)
✅ Температура НЕ меняется во время фазового перехода!
✅ Плавление начинается только при достижении температуры плавления

Удельная теплота плавления некоторых веществ:
• Лёд/вода: 330 000 Дж/кг
• Алюминий: 390 000 Дж/кг
• Железо: 270 000 Дж/кг
• Свинец: 25 000 Дж/кг
""",
        "tasks": [
            {"level": 1, "condition": "Сколько теплоты нужно для плавления 2 кг льда при 0°C? (λ = 330 000 Дж/кг)", "given": "m = 2 кг, λ = 330 000 Дж/кг", "formula": "Q = λ · m", "answer": 660000, "unit": "Дж", "hint": "Q = 330 000 · 2 = 660 000 Дж"},
            {"level": 2, "condition": "Какое количество теплоты выделится при кристаллизации 5 кг воды? (λ = 330 000 Дж/кг)", "given": "m = 5 кг, λ = 330 000 Дж/кг", "formula": "Q = λ · m", "answer": 1650000, "unit": "Дж", "hint": "При кристаллизации Q = λ · m = 330 000 · 5"},
            {"level": 3, "condition": "Для плавления металла потребовалось 780 000 Дж. Найдите массу металла. (λ = 390 000 Дж/кг)", "given": "Q = 780 000 Дж, λ = 390 000 Дж/кг", "formula": "m = Q / λ", "answer": 2, "unit": "кг", "hint": "m = Q / λ = 780 000 / 390 000"},
            {"level": 4, "condition": "Найдите удельную теплоту плавления, если для плавления 4 кг вещества потребовалось 1 080 000 Дж.", "given": "m = 4 кг, Q = 1 080 000 Дж", "formula": "λ = Q / m", "answer": 270000, "unit": "Дж/кг", "hint": "λ = Q / m = 1 080 000 / 4"},
            {"level": 5, "condition": "Сколько теплоты нужно, чтобы нагреть 1 кг льда от -10°C до 0°C и расплавить его? (c льда = 2100 Дж/(кг·°C), λ = 330 000 Дж/кг)", "given": "m = 1 кг, t₁ = -10°C, t₂ = 0°C, c = 2100 Дж/(кг·°C), λ = 330 000 Дж/кг", "formula": "Q = c·m·Δt + λ·m", "answer": 351000, "unit": "Дж", "hint": "Q = Q₁ (нагрев) + Q₂ (плавление) = 2100·1·10 + 330 000·1"}
        ]
    },
    "vaporization": {
        "title": "💨 Теплота парообразования",
        "icon": "☁️",
        "theory": """
ТЕПЛОТА ПАРООБРАЗОВАНИЯ И КОНДЕНСАЦИИ (Q)

Что это такое?
Когда вода кипит и превращается в пар, или пар охлаждается и превращается в воду — происходит фазовый переход.

Простыми словами:
Для превращения воды в пар нужна энергия (парообразование). При превращении пара в воду энергия выделяется (конденсация).

Единица измерения: Джоуль (Дж)

Основная формула:
Q = L · m

Что означает каждая буква:
• Q — количество теплоты [Дж]
• L — удельная теплота парообразования [Дж/кг] — показывает, сколько энергии нужно для превращения 1 кг жидкости в пар
• m — масса вещества [кг]

Важно запомнить:
✅ При парообразовании: тело ПОЛУЧАЕТ тепло (Q > 0)
✅ При конденсации: тело ОТДАЁТ тепло (Q < 0)
✅ Температура НЕ меняется во время фазового перехода!
✅ Кипение начинается только при достижении температуры кипения

Удельная теплота парообразования некоторых веществ:
• Вода: 2 300 000 Дж/кг
• Спирт: 900 000 Дж/кг
• Ртуть: 290 000 Дж/кг

Интересный факт:
L воды очень большая! Поэтому пар обжигает сильнее, чем кипяток — при конденсации на коже пар отдаёт много энергии.
""",
        "tasks": [
            {"level": 1, "condition": "Сколько теплоты нужно для превращения 2 кг воды в пар при 100°C? (L = 2 300 000 Дж/кг)", "given": "m = 2 кг, L = 2 300 000 Дж/кг", "formula": "Q = L · m", "answer": 4600000, "unit": "Дж", "hint": "Q = 2 300 000 · 2 = 4 600 000 Дж"},
            {"level": 2, "condition": "Какое количество теплоты выделится при конденсации 3 кг пара? (L = 2 300 000 Дж/кг)", "given": "m = 3 кг, L = 2 300 000 Дж/кг", "formula": "Q = L · m", "answer": 6900000, "unit": "Дж", "hint": "При конденсации Q = L · m = 2 300 000 · 3"},
            {"level": 3, "condition": "Для испарения жидкости потребовалось 4 500 000 Дж. Найдите массу жидкости. (L = 900 000 Дж/кг)", "given": "Q = 4 500 000 Дж, L = 900 000 Дж/кг", "formula": "m = Q / L", "answer": 5, "unit": "кг", "hint": "m = Q / L = 4 500 000 / 900 000"},
            {"level": 4, "condition": "Найдите удельную теплоту парообразования, если для испарения 2 кг потребовалось 1 800 000 Дж.", "given": "m = 2 кг, Q = 1 800 000 Дж", "formula": "L = Q / m", "answer": 900000, "unit": "Дж/кг", "hint": "L = Q / m = 1 800 000 / 2"},
            {"level": 5, "condition": "Сколько теплоты нужно, чтобы нагреть 1 кг воды от 20°C до 100°C и превратить в пар? (c = 4200 Дж/(кг·°C), L = 2 300 000 Дж/кг)", "given": "m = 1 кг, t₁ = 20°C, t₂ = 100°C, c = 4200 Дж/(кг·°C), L = 2 300 000 Дж/кг", "formula": "Q = c·m·Δt + L·m", "answer": 2636000, "unit": "Дж", "hint": "Q = Q₁ (нагрев) + Q₂ (пар) = 4200·1·80 + 2 300 000·1"}
        ]
    }
}

# === ГЛАВНОЕ ПРИЛОЖЕНИЕ ===
def main(page: ft.Page):
    page.title = "Физика: Тепловые явления"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 10
    page.bgcolor = "#E3F2FD"
    page.window_width = 700
    page.window_height = 900
    page.scroll = ft.ScrollMode.AUTO
    
    # Переменные состояния
    current_topic = ft.Text(value="", visible=False)
    current_task_index = ft.Text(value="0", visible=False)
    attempt_count = ft.Text(value="0", visible=False)
    
    # === ФУНКЦИИ ===
    
    def show_topic_theory(topic_key):
        """Показать теорию для выбранной темы"""
        current_topic.value = topic_key
        theory_title.value = f"{TOPICS[topic_key]['icon']} {TOPICS[topic_key]['title']}"
        theory_text.value = TOPICS[topic_key]["theory"]
        
        page.controls.clear()
        page.add(header, theory_container)
        theory_container.visible = True
        topic_menu.visible = False
        task_section.visible = False
        page.update()
    
    def go_to_practice_from_theory(e):
        """Перейти от теории к задачам"""
        topic_key = current_topic.value
        current_task_index.value = "0"
        attempt_count.value = "0"
        
        page.controls.clear()
        page.add(header, task_section)
        theory_container.visible = False
        topic_menu.visible = False
        task_section.visible = True
        load_task(0)
    
    def go_to_tasks_direct(topic_key):
        """Перейти сразу к задачам (без теории)"""
        current_topic.value = topic_key
        current_task_index.value = "0"
        attempt_count.value = "0"
        
        page.controls.clear()
        page.add(header, task_section)
        theory_container.visible = False
        topic_menu.visible = False
        task_section.visible = True
        load_task(0)
    
    def load_task(index):
        topic_key = current_topic.value
        if index >= len(TOPICS[topic_key]["tasks"]):
            show_topic_complete()
            return
        
        task = TOPICS[topic_key]["tasks"][index]
        attempt_count.value = "0"
        
        topic_info.value = f"{TOPICS[topic_key]['icon']} {TOPICS[topic_key]['title']}"
        condition_text.value = f"📝 ЗАДАЧА {task['level']}\n{task['condition']}"
        given_info.value = f"💡 Дано: {task['given']}"
        unit_label.value = f"⚠️ Ответ введите в {task['unit']}"
        input_given.value = ""
        input_formula.value = ""
        input_answer.value = ""
        result_message.value = ""
        hint_text_display.value = ""
        btn_retry.visible = False
        btn_show_solution.visible = False
        progress_bar.value = index / len(TOPICS[topic_key]["tasks"])
        progress_text.value = f"Задача {index + 1} из {len(TOPICS[topic_key]['tasks'])}"
        page.update()
    
    def show_topic_complete():
        topic_key = current_topic.value
        task_section.visible = False
        
        complete_screen = ft.Container(
            content=ft.Column([
                ft.Text("🎉", size=60),
                ft.Text("Тема завершена!", size=28, weight=ft.FontWeight.BOLD, color="#2E7D32"),
                ft.Text(f"Вы решили все {len(TOPICS[topic_key]['tasks'])} задач!", size=16),
                ft.Text("🔥 Отличная работа!", size=16, color="#4CAF50"),
                ft.ElevatedButton("Выбрать другую тему", on_click=lambda _: show_main_menu(), bgcolor="#1565C0", color="white", width=300, height=50),
                ft.ElevatedButton("Начать заново", on_click=lambda _: restart_topic(), bgcolor="#4CAF50", color="white", width=300, height=50)
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=15),
            padding=40, bgcolor="white", border_radius=15, shadow=ft.BoxShadow(blur_radius=10, color="#0000001A")
        )
        
        page.controls.clear()
        page.add(header, complete_screen)
        page.update()
    
    def show_main_menu():
        """Показать главное меню"""
        page.controls.clear()
        page.add(header, topic_menu)
        topic_menu.visible = True
        theory_container.visible = False
        task_section.visible = False
        page.update()
    
    def restart_topic():
        """Начать тему заново"""
        current_task_index.value = "0"
        attempt_count.value = "0"
        page.controls.clear()
        page.add(header, task_section)
        load_task(0)
    
    def check_answer(e):
        topic_key = current_topic.value
        task_index = int(current_task_index.value)
        task = TOPICS[topic_key]["tasks"][task_index]
        attempts = int(attempt_count.value)
        
        try:
            user_answer = float(input_answer.value.replace(" ", "").replace(",", "."))
            
            # Проверка с погрешностью 5%
            tolerance = task["answer"] * 0.05
            if abs(user_answer - task["answer"]) <= tolerance:
                result_message.value = "✅ ПРАВИЛЬНО! Молодец!"
                result_message.color = "#2E7D32"
                hint_text_display.value = ""
                btn_retry.visible = False
                btn_show_solution.visible = False
                page.update()
                
                # Переход к следующей задаче
                time.sleep(1.5)
                current_task_index.value = str(task_index + 1)
                load_task(task_index + 1)
            else:
                attempts += 1
                attempt_count.value = str(attempts)
                
                if attempts >= 3:
                    result_message.value = "❌ После 3 попыток показываем решение"
                    result_message.color = "#C62828"
                    hint_text_display.value = f"📖 Формула: {task['formula']}\n✅ Правильный ответ: {task['answer']} {task['unit']}\n💭 Подсказка: {task['hint']}"
                    btn_retry.visible = True
                    btn_show_solution.visible = True
                else:
                    result_message.value = f"❌ Неверно! Попытка {attempts} из 3"
                    result_message.color = "#FF9800"
                    hint_text_display.value = f"💭 Подсказка: {task['hint']}"
                    btn_retry.visible = True
                    btn_show_solution.visible = False
                
                page.update()
                
        except ValueError:
            result_message.value = f"⚠️ Введите число в {task['unit']}!"
            result_message.color = "#FF9800"
            hint_text_display.value = ""
            btn_retry.visible = False
            btn_show_solution.visible = False
            page.update()
    
    def retry_task(e):
        input_answer.value = ""
        result_message.value = ""
        hint_text_display.value = ""
        btn_retry.visible = False
        btn_show_solution.visible = False
        page.update()
    
    def show_solution(e):
        topic_key = current_topic.value
        task_index = int(current_task_index.value)
        task = TOPICS[topic_key]["tasks"][task_index]
        
        hint_text_display.value = f"📖 РЕШЕНИЕ:\n\n1) Формула: {task['formula']}\n2) Подставляем: {task['hint']}\n3) Ответ: {task['answer']} {task['unit']}"
        btn_show_solution.visible = False
        page.update()
    
    def back_to_menu(e):
        show_main_menu()
    
    # === ИНТЕРФЕЙС ===
    
    header = ft.Container(
        content=ft.Column([
            ft.Text("📚", size=50),
            ft.Text("Физика: Тепловые явления", size=24, weight=ft.FontWeight.BOLD, color="#1565C0"),
            ft.Text("Подготовка к экзамену", size=13, color="#546E7A")
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
        padding=15, bgcolor="#BBDEFB", border_radius=10
    )
    
    # Меню выбора тем
    topic_menu = ft.Container(
        content=ft.Column([
            ft.Text("📖 ВЫБЕРИТЕ ТЕМУ:", size=20, weight=ft.FontWeight.BOLD, color="#1565C0"),
            ft.Divider(),
            
            # Тема 1: Количество теплоты
            ft.Column([
                ft.Text(f"{TOPICS['heat']['icon']} {TOPICS['heat']['title']}", size=16, weight=ft.FontWeight.BOLD),
                ft.Row([
                    ft.ElevatedButton("📖 Изучить теорию", on_click=lambda _: show_topic_theory("heat"), bgcolor="#2196F3", color="white", width=220),
                    ft.ElevatedButton("📝 Решать задачи", on_click=lambda _: go_to_tasks_direct("heat"), bgcolor="#4CAF50", color="white", width=220),
                ], alignment=ft.MainAxisAlignment.CENTER)
            ], spacing=5, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            
            # Тема 2: Теплота сгорания
            ft.Column([
                ft.Text(f"{TOPICS['combustion']['icon']} {TOPICS['combustion']['title']}", size=16, weight=ft.FontWeight.BOLD),
                ft.Row([
                    ft.ElevatedButton("📖 Изучить теорию", on_click=lambda _: show_topic_theory("combustion"), bgcolor="#FF5722", color="white", width=220),
                    ft.ElevatedButton("📝 Решать задачи", on_click=lambda _: go_to_tasks_direct("combustion"), bgcolor="#4CAF50", color="white", width=220),
                ], alignment=ft.MainAxisAlignment.CENTER)
            ], spacing=5, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            
            # Тема 3: Теплота плавления
            ft.Column([
                ft.Text(f"{TOPICS['melting']['icon']} {TOPICS['melting']['title']}", size=16, weight=ft.FontWeight.BOLD),
                ft.Row([
                    ft.ElevatedButton("📖 Изучить теорию", on_click=lambda _: show_topic_theory("melting"), bgcolor="#00BCD4", color="white", width=220),
                    ft.ElevatedButton("📝 Решать задачи", on_click=lambda _: go_to_tasks_direct("melting"), bgcolor="#4CAF50", color="white", width=220),
                ], alignment=ft.MainAxisAlignment.CENTER)
            ], spacing=5, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            
            # Тема 4: Теплота парообразования
            ft.Column([
                ft.Text(f"{TOPICS['vaporization']['icon']} {TOPICS['vaporization']['title']}", size=16, weight=ft.FontWeight.BOLD),
                ft.Row([
                    ft.ElevatedButton("📖 Изучить теорию", on_click=lambda _: show_topic_theory("vaporization"), bgcolor="#9C27B0", color="white", width=220),
                    ft.ElevatedButton("📝 Решать задачи", on_click=lambda _: go_to_tasks_direct("vaporization"), bgcolor="#4CAF50", color="white", width=220),
                ], alignment=ft.MainAxisAlignment.CENTER)
            ], spacing=5, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            
            ft.Divider(),
            ft.Text("💡 Рекомендуется сначала изучить теорию, затем решать задачи!", size=13, color="#546E7A", italic=True, text_align=ft.TextAlign.CENTER),
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=20),
        padding=20, bgcolor="white", border_radius=10, shadow=ft.BoxShadow(blur_radius=10, color="#0000001A"),
        visible=True
    )
    
    # Теория
    theory_title = ft.Text("", size=22, weight=ft.FontWeight.BOLD, color="#1565C0")
    theory_text = ft.Text("", size=14, weight=ft.FontWeight.W_500)
    
    theory_container = ft.Container(
        content=ft.Column([
            theory_title,
            ft.Divider(),
            theory_text,
            ft.Divider(),
            ft.ElevatedButton("📝 ПЕРЕЙТИ К ЗАДАЧАМ", on_click=go_to_practice_from_theory, bgcolor="#4CAF50", color="white", width=450, height=55),
            ft.TextButton("← Вернуться к меню", on_click=back_to_menu)
        ], spacing=10, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        padding=20, bgcolor="white", border_radius=10, shadow=ft.BoxShadow(blur_radius=10, color="#0000001A"),
        visible=False
    )
    
    # Задачи
    topic_info = ft.Text("", size=18, weight=ft.FontWeight.BOLD, color="#1565C0")
    condition_text = ft.Text("", size=15, weight=ft.FontWeight.W_500, color="#37474F")
    given_info = ft.Text("", size=13, color="#546E7A", italic=True)
    unit_label = ft.Text("", size=14, weight=ft.FontWeight.BOLD, color="#D84315")
    
    input_given = ft.TextField(label="✏️ Дано", hint_text="Запишите данные из условия...", width=550, multiline=True, min_lines=2)
    input_formula = ft.TextField(label="✏️ Формула", hint_text="Запишите формулу для решения...", width=550, multiline=True, min_lines=1)
    input_answer = ft.TextField(label="✏️ Ответ", hint_text="Только число...", width=550, keyboard_type=ft.KeyboardType.NUMBER)
    
    result_message = ft.Text("", size=15, weight=ft.FontWeight.BOLD)
    hint_text_display = ft.Text("", size=13, color="#FF9800", italic=True)
    
    progress_bar = ft.ProgressBar(width=550, value=0, color="#4CAF50")
    progress_text = ft.Text("Задача 0 из 5", size=13, color="#546E7A")
    
    btn_check = ft.ElevatedButton(
        "✅ ПРОВЕРИТЬ ОТВЕТ",
        on_click=check_answer,
        bgcolor="#4CAF50",
        color="white",
        width=450,
        height=55
    )
    
    btn_retry = ft.ElevatedButton(
        "🔄 ПОПРОБОВАТЬ ЗАНОВО",
        on_click=retry_task,
        bgcolor="#FF9800",
        color="white",
        width=450,
        height=55,
        visible=False
    )
    
    btn_show_solution = ft.ElevatedButton(
        "📖 ПОКАЗАТЬ РЕШЕНИЕ",
        on_click=show_solution,
        bgcolor="#2196F3",
        color="white",
        width=450,
        height=55,
        visible=False
    )
    
    task_section = ft.Container(
        content=ft.Column([
            topic_info,
            progress_bar,
            progress_text,
            ft.Divider(),
            condition_text,
            given_info,
            ft.Divider(),
            unit_label,
            input_given,
            input_formula,
            input_answer,
            result_message,
            hint_text_display,
            btn_check,
            btn_retry,
            btn_show_solution,
            ft.Divider(),
            ft.TextButton("← Вернуться к меню", on_click=back_to_menu),
        ], spacing=10, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        padding=20,
        bgcolor="white",
        border_radius=10,
        shadow=ft.BoxShadow(blur_radius=10, color="#0000001A"),
        visible=False
    )
    
    # Добавляем всё на страницу
    page.add(header, topic_menu, theory_container, task_section)

ft.run(main)