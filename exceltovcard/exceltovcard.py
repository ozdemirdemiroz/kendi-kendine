import pandas as pd
from vobject import vCard


df = pd.read_excel('kendi-kendine/exceltovcard/number.xlsx') 

vcards = []

for index, row in df.iterrows():
    vcard = vCard()
    vcard.add('fn').value = row['Eczane İsmi']
    # vcard.add('n').value = row['Eczane İsmi']
    # vcard.add('n').value = row['Eczacı Adı']; row['Ecz. Adı'] 
    tel=vcard.add('tel')
    tel.type_param='MOBILE'
    tel.value=row['Telefon Numarası']
    vcards.append(vcard)

with open('kendi-kendine/exceltovcard/eczaneler_4.vcf', 'w') as f:
    for vcard in vcards:
        f.write(vcard.serialize())
        f.write('\n')
