from datetime import date, datetime
class FormatDate(object):

    def __init__(self, date):
        self.date = date

    def __str__(self):
        return self.date

    def actualDate(type = 'en'):
        data_atual = date.today()
        if type == 'en':
            return(data_atual)
        if type == 'pt-br':
            data_em_texto = data_atual.strftime('%d/%m/%Y')
            return(data_em_texto)

    def actualDateTime(type = 'en'):
        data_e_hora_atuais = datetime.now()
        if type == 'en':
            return(data_e_hora_atuais)
        if type == 'pt-br':
            return data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')

    @staticmethod
    def stringToDateTime(type = 'en', text = ''):
        date = text
        if date:
            if type == 'en':
                return datetime.strptime(date, '%Y/%m/%d %H:%M')
            if type == 'pt-br':
                return datetime.strptime(date, '%d/%m/%Y %H:%M')
        return False

    def compareTwoDates(type,date1,date2):
        date1 = FormatDate.stringToDateTime(type, date1)
        date2 = FormatDate.stringToDateTime(type, date2)
        if date1 > date2:
            return(date1)
        else:
            return(date2)
