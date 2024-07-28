from datetime import datetime
from dateutil.relativedelta import relativedelta

sexo = input('Informe o sexo (masculino/feminino): ').lower()
data_nascimento = input('Informe a data de nascimento (DD/MM/AAAA): ')
data_inicio_contribuicao = input('Informe a data de início da contribuição previdenciária (DD/MM/AAAA): ')

data_nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y')
data_inicio_contribuicao = datetime.strptime(data_inicio_contribuicao, '%d/%m/%Y')

hoje = datetime.now()
idade = hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))

anos_contribuicao = hoje.year - data_inicio_contribuicao.year - ((hoje.month, hoje.day) < (data_inicio_contribuicao.month, data_inicio_contribuicao.day))

if sexo == 'masculino':
    idade_aposentadoria = 65
    anos_minimos_contribuicao = 15
else:
    idade_aposentadoria = 62
    anos_minimos_contribuicao = 15

if idade >= idade_aposentadoria:
    print('Parabéns! Você pode se aposentar por idade.')
    data_aposentadoria_idade = data_nascimento + relativedelta(years=idade_aposentadoria)
    print('Data de aposentadoria por idade : ', data_aposentadoria_idade.strftime('%d/%m/%Y'))
elif anos_contribuicao >= anos_minimos_contribuicao:
    print('Parabéns! Você pode se aposentar por tempo de contribuição.')
    data_aposentadoria_contribuicao = data_nascimento + relativedelta(years=idade_aposentadoria)
    print('Data de aposentadoria por tempo de contribuição : ', data_aposentadoria_contribuicao.strftime('%d/%m/%Y'))
else:
    data_prevista_aposentadoria = data_nascimento + relativedelta(years=idade_aposentadoria)
    print('A pessoa ainda não possui os requisitos necessários para aposentadoria.')
    print('Data prevista para aposentadoria : ', data_prevista_aposentadoria.strftime('%d/%m/%Y'))
