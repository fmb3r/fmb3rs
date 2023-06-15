from fpdf import FPDF
from datetime import datetime

pdf = FPDF('P', 'mm', 'A4')
pdf.add_page()
pdf.image('b_day.jpg', h = 297, w = 210, x = 0, y = 0)
pdf.add_font('arial', '', 'C:\Windows\Fonts\Arial.ttf', uni = True)
pdf.set_font('Arial', size = 26)
pdf.set_text_color(0, 0, 0)

friend_name = input('Введите имя того, кого вы хотите поздравить:\n ')
pdf.cell(0, 95, ln = 1)
pdf.cell(0, 20, txt = 'Дорогая, ' +friend_name+'!', align = 'C', ln = 1)

pdf.set_font('Arial', size = 18)
pdf.set_text_color(0, 0, 0)
message = input('Введите текст поздравления:\n ')
pdf.set_right_margin(50)
pdf.set_left_margin(50)
pdf.multi_cell(0, 20, txt = message, align = 'С')

today = datetime.today().strftime('%d.%m.%Y')
pdf.set_text_color(124, 30, 150)
pdf.cell(0, 10, txt = today, align = 'C', ln = 1)

author_name = input('Введите свое имя:\n ')
pdf.cell(0, 10, txt = author_name, align = 'R', ln = 1)

pdf.output('bday_card.pdf')