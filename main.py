import openpyxl
from PIL import Image, ImageDraw, ImageFont

workbook_alunos = openpyxl.load_workbook('filename.xlsx')
sheet_alunos = workbook_alunos['Sheet1']

for indice, linha in enumerate(sheet_alunos.iter_rows(min_row=2)):
    treco_nome = linha[0].value

    fonte_nome = ImageFont.truetype('./SUSE-Medium.ttf')

    image = Image.open('certificado.png')
    desenhar = ImageDraw.Draw(image)

    desenhar.text((200,600), treco_nome, fill='black', font='fonte_nome')

    image.save(f'./{indice}{treco_nome}.png')