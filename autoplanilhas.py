# ler dados da planilha
# inserir cada celula de cada linha em um campo do sistema
import openpyxl
import pyautogui

workbook = openpyxl.load_workbook('caminho ate aonde a documento està')
vendas_sheet = workbook['vendas']

for linha in vendas_sheet.iter_rows(min_row=numero da linha que começa):
    # [luis] [computador] [444] [hacking]

    # nome
pyautogui.click(coordenadas da tela, duration=3)
pyautogui.write(linha[0].value)
# produto
pyautogui.click(coordenadas da tela, duration=3)
pyautogui.write(linha[1].value)
# numero
pyautogui.click(coordenadas da tela, duration=3)
pyautogui.write(str(linha[2].value))
# serviço
pyautogui.click(coordenadas da tela, duration=3)
pyautogui.write(linha[3].value)
pyautogui.click(coordenadas da tela, duration=3)

# clicando para salvar os dados
pyautogui.click(coordenadas da tela, duration=3)
