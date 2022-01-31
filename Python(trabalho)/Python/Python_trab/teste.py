from fpdf import FPDF
import pandas as pd
import os
import matplotlib.pyplot as plt

pdf = FPDF('p', 'mm', 'A4')
pdf.add_page()
pdf.set_font('times', '', 16)

dadosEstado = pd.read_excel(r'Dados-covid-19-estado.xlsx')
totalDeCasos = dadosEstado["Total de casos"]
casosDia = dadosEstado["Casos por dia"]

plt.plot(totalDeCasos)
plt.xlabel('Total de casos')
plt.savefig("exemplo.png")
plt.close()
pdf.multi_cell(w=0, h=8, txt="Grafico total de casos no estado de sp", ln=1, align='C')
pdf.image(x=20, y=30, w=180, h=80, name='exemplo.png')

plt.plot(casosDia)
plt.xlabel('Casos por dia')
plt.savefig("exemplo2.png")
plt.close()
pdf.multi_cell(w=0, h=230, txt="Grafico de casos por dia no estado de sp", ln=1, align='C')
pdf.image(x=20, y=140, w=180, h=80, name='exemplo2.png')


pdf.output('teste.pdf')

os.system("pause")