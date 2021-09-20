import boto3
from pathlib import Path

client = boto3.client('comprehend')

temp_txt = Path('temp.txt').read_text()
hof_txt = Path('GREEN HILLS OF AFRICA_DF.txt').read_text()
atr_txt = Path('ACROSS THE RIVER  AND  INTO THE TREES_DF.txt').read_text()
sar_txt = Path('THE SUN ALSO RISES_DF.txt').read_text()
oms_txt = Path('THE OLD MAN  AND  THE SEA_DF.txt').read_text()
mww_txt = Path('MEN WITHOUT WOMEN_DF.txt').read_text()
temp_all = hof_txt + atr_txt + sar_txt + oms_txt + mww_txt 
lst_total = []
for i in range(len(temp_all)//5000):
    temp = temp_all[4992*i:4992*(i+1)]
    response = client.batch_detect_entities(TextList=[temp,],LanguageCode='en')
    list_of_loc = [i['Text'] for i in response['ResultList'][0]['Entities'] if i['Type'] == 'ANIMAL' and i['Score'] > 0.6]
    lst_total.extend(list_of_loc )
print(lst_total)
#print(response['ResultList'][0]['Entities'][0]['Type'])