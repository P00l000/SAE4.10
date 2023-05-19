
import datetime
def foundDatesFromOption(typeDecoupage,date) :
    '''
    donne la date de depart et la date de fin selon les paramèetres
    :param typeDecoupage: a: année , m : mois,  s: saison
    :param date: année, mois/année en nombre  ou saison-année avec saison =h,a,p,e
    :return: date_debut
    :return: date_fin
    '''
    if ( typeDecoupage == 's'):
        date = date.split('-')
        if date[0] == 'h' :
            date_debut = datetime.datetime.strptime('01/09/'+ date[1],'%d/%m/%Y')
            date_fin = datetime.datetime.strptime('01/03/'+ str(int(date[1])+1),'%d/%m/%Y')
        elif date[0] == 'a':
            date_debut = datetime.datetime.strptime('01/09/' + date[1], '%d/%m/%Y')
            date_fin = datetime.datetime.strptime('01/12/' + date[1], '%d/%m/%Y')
        elif date[0] =='p':
            date_debut = datetime.datetime.strptime('01/03/' + date[1], '%d/%m/%Y')
            date_fin = datetime.datetime.strptime('01/06/' + date[1], '%d/%m/%Y')
        else :
            date_debut = datetime.datetime.strptime('01/06/' + date[1], '%d/%m/%Y')
            date_fin = datetime.datetime.strptime('01/09/' + date[1], '%d/%m/%Y')
    if (typeDecoupage == 'm'):
            date_debut = datetime.datetime.strptime('01/'+date,'%d/%m/%Y')
            date=date.split('/')
            if date[0] == '12' :
                date_fin =datetime.datetime.strptime('01/01/'+str(int(date[1])+1),'%d/%m/%Y')
            else:
                if int(date[0]) >=9:
                    date_fin = datetime.datetime.strptime('01/'+str(int(date[0])+1)+'/'+date[1],'%d/%m/%Y')
                else :
                    date_fin = datetime.datetime.strptime('01/' +'0'+ str(int(date[0])+1) + '/' + date[1], '%d/%m/%Y')
    if (typeDecoupage == 'a'):
        date_debut = datetime.datetime.strptime('01/01/' + str(date), '%d/%m/%Y')
        date_fin = datetime.datetime.strptime('01/01/' + str(int(date)+1), '%d/%m/%Y')

    return date_debut,date_fin

def SplitDataFromDate(df,typeDecoupage,date):

    start_date,end_date = foundDatesFromOption(typeDecoupage,date)
    print(start_date)
    print(end_date)
    date_condition = (df['report_date'] >= start_date) & (df['report_date'] <= end_date)
    df_filtered = df.loc[date_condition]
    return df_filtered
