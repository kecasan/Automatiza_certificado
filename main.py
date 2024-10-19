import openpyxl
from PIL import Image, ImageDraw, ImageFont

workbook_alunos = openpyxl.load_workbook('./dados.xlsx')
sheet_alunos = workbook_alunos['Planilha1']

for indice, linha in enumerate(sheet_alunos.iter_rows(min_row=2)):
    pessoa_nome = linha[0].value
    curso_nome = linha[1].value
    cnpj_numero = linha[2].value
    carga_horaria = linha[3].value

    fonte_nome = ImageFont.truetype('./SUSE-Medium.ttf',90)

    image = Image.open('./certificado.png')
    desenhar = ImageDraw.Draw(image)

    desenhar.text((200,600), pessoa_nome, fill='black', font=fonte_nome)
    desenhar.text((202,600), curso_nome, fill='royalblue', font=fonte_nome)
    desenhar.text((204,600), cnpj_numero, fill='red', font=fonte_nome)
    desenhar.text((206,600), carga_horaria, fill='green', font=fonte_nome)




    image.save(f'./{indice}{pessoa_nome}.png')