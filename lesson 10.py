from fpdf import FPDF

pdf = FPDF('P', 'cm', (10, 15))
pdf.add_page()
pdf.set_font('courier', size = 16)
pdf.set_text_color(0, 255, 0)
pdf.set_fill_color(56, 0, 255)
pdf.set_draw_color(255, 0, 0)
pdf.cell(w = 5, h = 5, txt = 'HelloWorld', border = 1, align = 'C', fill = True)
pdf.image('happy.png', h = 0, w = 10, x = 0, y = 5)

pdf.output('test_fpdf.pdf')