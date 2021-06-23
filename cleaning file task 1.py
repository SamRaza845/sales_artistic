#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from csv import reader


# In[251]:


data=list(reader(open('Sales1.csv')))
data


# In[252]:


data[0].index('COUNTRY')


# In[253]:


name={}
for i in data[1:]:
#     print(i[4])
    if i[3]:
        name[i[4]]=i[3]
    else:
        pass
print(name)


# In[254]:


for i in data[1:]:
    if not i[3]:
        if i[4] in name:
            i[3]= name[i[4]]
        else:
            pass
    else: 
        pass


# In[255]:


k= []
for i in data[1:]:
    a11=i[1].split()
    k.append(a11)
#     else:
#         pas
print(len(k))
print(k[76711])


# In[256]:


count=0
for ii,i in enumerate(data[1:]):
    if i[23]:
        pass
    else:
        if len(k[ii])>0:
            coun= k[ii]
#             print(coun,ii)
            for h in coun:
                h=h.replace('.','')
                h=h.replace('POLAIND.', 'POLAND' )
                h=h.replace('Lanka', 'SRI LANKA' )
                print(h)
                if h.upper() in countries:
    #                 print(h)
                    i[23] = h
                    print('y')
                else: 
                    print('no')
            
        else:
            pass
# #         print(coun)
        


# In[257]:


data


# In[116]:


coun=['T', 'GRANTI','TURKEY', 'BANKASI', 'A.S', 'ISTANBUL']
for h in coun:
    if h.upper() in countries:
        print('y', h)
    else: 
        print('no')

jjj='TAIWAN.'
jjj.replace('.','')


# In[258]:


for i in data[1:]:
    if i[1] == 'MEGA INTERNATIONAL COMMERCIAL BANK CO LTD':
        i[23]= 'TAIWAN'
    else:
        pass


# In[259]:


for i in data[1:]:
    ab= i[3]
    idd= i[5]
    
    if not i[23]:
        if ab == 'NIEN HSING TEXTILE CO. LTD.':
            i[23]='Taiwan'
        elif ab=='Ananta Apparel':
            i[23]='Bangladesh'
        elif ab=='UNIVERSAL JEANS LIMITED':
            i[23]='Bangladesh'
        elif ab=='PHONG PHU INTERNATIONAL JSC':
            i[23]='Veit Nam'
        elif ab=='JEANS COMPANY (PVT) LTD.':
            i[23]='Pakistan'
        elif ab=='GRUPPO TESSILE CASMIK SRL':
            i[23]='Italy'
        elif ab=='CONTO BENE JEANS':
            i[23]='Serbia'
        elif ab=='KENPARK BANGLADESH APPAREL (PVT) LTD':
            i[23]= 'Bangladesh'
        elif idd== 5357 :
            i[23]= 'Bangladesh'
        elif ab== 'SAI TEXTILE INTERNATIONAL LTD' :
            i[23]= 'Veit Nam'
        elif ab== 'ORIT TRADING LANKA' :
            i[23]= 'Sri Lanka'
        else:
            pass
    else:
        pass


# In[ ]:





# In[114]:


print(len(k))
ajj= "Peru"
if ajj in countries:
    print('k')


# In[9]:


name['5230']


# In[260]:


a=pd.DataFrame(data)
a.head(10)


# In[27]:


# a.rename(columns=a.iloc[0])


# In[261]:


header= a.iloc[0]
a=a[1:]
# a.reset_index(drop=True)
# a.columns = header
a=a.rename(columns= header )


# In[ ]:





# In[107]:


# a.rename(columns= header)


# In[262]:


a.sort_index()
a.head(10)
a.to_csv('mid_cleaned2.csv')


# In[131]:


a['CUSTOMER_NAME'].isnull().sum()
a['COUNTRY'].isnull().sum()


# In[155]:


count=0
for i in data1[1:]:
    if i[24]== "" or i[24]== ' ':
        count +=1
    else:
        pass
count


# In[93]:


value = [
    ('US', 'United States'),
    ('AF', 'Afghanistan'),
    ('AL', 'Albania'),
    ('DZ', 'Algeria'),
    ('AS', 'American Samoa'),
    ('AD', 'Andorra'),
    ('AO', 'Angola'),
    ('AI', 'Anguilla'),
    ('AQ', 'Antarctica'),
    ('AG', 'Antigua And Barbuda'),
    ('AR', 'Argentina'),
    ('AM', 'Armenia'),
    ('AW', 'Aruba'),
    ('AU', 'Australia'),
    ('AT', 'Austria'),
    ('AZ', 'Azerbaijan'),
    ('BS', 'Bahamas'),
    ('BH', 'Bahrain'),
    ('BD', 'Bangladesh'),
    ('BB', 'Barbados'),
    ('BY', 'Belarus'),
    ('BE', 'Belgium'),
    ('BZ', 'Belize'),
    ('BJ', 'Benin'),
    ('BM', 'Bermuda'),
    ('BT', 'Bhutan'),
    ('BO', 'Bolivia'),
    ('BA', 'Bosnia And Herzegowina'),
    ('BW', 'Botswana'),
    ('BV', 'Bouvet Island'),
    ('BR', 'Brazil'),
    ('BN', 'Brunei Darussalam'),
    ('BG', 'Bulgaria'),
    ('BF', 'Burkina Faso'),
    ('BI', 'Burundi'),
    ('KH', 'Cambodia'),
    ('CM', 'Cameroon'),
    ('CA', 'Canada'),
    ('CV', 'Cape Verde'),
    ('KY', 'Cayman Islands'),
    ('CF', 'Central African Rep'),
    ('TD', 'Chad'),
    ('CL', 'Chile'),
    ('CN', 'China'),
    ('CX', 'Christmas Island'),
    ('CC', 'Cocos Islands'),
    ('CO', 'Colombia'),
    ('KM', 'Comoros'),
    ('CG', 'Congo'),
    ('CK', 'Cook Islands'),
    ('CR', 'Costa Rica'),
    ('CI', 'Cote D`ivoire'),
    ('HR', 'Croatia'),
    ('CU', 'Cuba'),
    ('CY', 'Cyprus'),
    ('CZ', 'Czech Republic'),
    ('DK', 'Denmark'),
    ('DJ', 'Djibouti'),
    ('DM', 'Dominica'),
    ('DO', 'Dominican Republic'),
    ('TP', 'East Timor'),
    ('EC', 'Ecuador'),
    ('EG', 'Egypt'),
    ('SV', 'El Salvador'),
    ('GQ', 'Equatorial Guinea'),
    ('ER', 'Eritrea'),
    ('EE', 'Estonia'),
    ('ET', 'Ethiopia'),
    ('FK', 'Falkland Islands (Malvinas)'),
    ('FO', 'Faroe Islands'),
    ('FJ', 'Fiji'),
    ('FI', 'Finland'),
    ('FR', 'France'),
    ('GF', 'French Guiana'),
    ('PF', 'French Polynesia'),
    ('TF', 'French S. Territories'),
    ('GA', 'Gabon'),
    ('GM', 'Gambia'),
    ('GE', 'Georgia'),
    ('DE', 'Germany'),
    ('GH', 'Ghana'),
    ('GI', 'Gibraltar'),
    ('GR', 'Greece'),
    ('GL', 'Greenland'),
    ('GD', 'Grenada'),
    ('GP', 'Guadeloupe'),
    ('GU', 'Guam'),
    ('GT', 'Guatemala'),
    ('GN', 'Guinea'),
    ('GW', 'Guinea-bissau'),
    ('GY', 'Guyana'),
    ('HT', 'Haiti'),
    ('HN', 'Honduras'),
    ('HK', 'Hong Kong'),
    ('HU', 'Hungary'),
    ('IS', 'Iceland'),
    ('IN', 'India'),
    ('ID', 'Indonesia'),
    ('IR', 'Iran'),
    ('IQ', 'Iraq'),
    ('IE', 'Ireland'),
    ('IL', 'Israel'),
    ('IT', 'Italy'),
    ('JM', 'Jamaica'),
    ('JP', 'Japan'),
    ('JO', 'Jordan'),
    ('KZ', 'Kazakhstan'),
    ('KE', 'Kenya'),
    ('KI', 'Kiribati'),
    ('KP', 'Korea (North)'),
    ('KR', 'Korea (South)'),
    ('KW', 'Kuwait'),
    ('KG', 'Kyrgyzstan'),
    ('LA', 'Laos'),
    ('LV', 'Latvia'),
    ('LB', 'Lebanon'),
    ('LS', 'Lesotho'),
    ('LR', 'Liberia'),
    ('LY', 'Libya'),
    ('LI', 'Liechtenstein'),
    ('LT', 'Lithuania'),
    ('LU', 'Luxembourg'),
    ('MO', 'Macau'),
    ('MK', 'Macedonia'),
    ('MG', 'Madagascar'),
    ('MW', 'Malawi'),
    ('MY', 'Malaysia'),
    ('MV', 'Maldives'),
    ('ML', 'Mali'),
    ('MT', 'Malta'),
    ('MH', 'Marshall Islands'),
    ('MQ', 'Martinique'),
    ('MR', 'Mauritania'),
    ('MU', 'Mauritius'),
    ('YT', 'Mayotte'),
    ('MX', 'Mexico'),
    ('FM', 'Micronesia'),
    ('MD', 'Moldova'),
    ('MC', 'Monaco'),
    ('MN', 'Mongolia'),
    ('MS', 'Montserrat'),
    ('MA', 'Morocco'),
    ('MZ', 'Mozambique'),
    ('MM', 'Myanmar'),
    ('NA', 'Namibia'),
    ('NR', 'Nauru'),
    ('NP', 'Nepal'),
    ('NL', 'Netherlands'),
    ('AN', 'Netherlands Antilles'),
    ('NC', 'New Caledonia'),
    ('NZ', 'New Zealand'),
    ('NI', 'Nicaragua'),
    ('NE', 'Niger'),
    ('NG', 'Nigeria'),
    ('NU', 'Niue'),
    ('NF', 'Norfolk Island'),
    ('MP', 'Northern Mariana Islands'),
    ('NO', 'Norway'),
    ('OM', 'Oman'),
    ('PK', 'Pakistan'),
    ('PW', 'Palau'),
    ('PA', 'Panama'),
    ('PG', 'Papua New Guinea'),
    ('PY', 'Paraguay'),
    ('PE', 'Peru'),
    ('PH', 'Philippines'),
    ('PN', 'Pitcairn'),
    ('PL', 'Poland'),
    ('PT', 'Portugal'),
    ('PR', 'Puerto Rico'),
    ('QA', 'Qatar'),
    ('RE', 'Reunion'),
    ('RO', 'Romania'),
    ('RU', 'Russian Federation'),
    ('RW', 'Rwanda'),
    ('KN', 'Saint Kitts And Nevis'),
    ('LC', 'Saint Lucia'),
    ('VC', 'St Vincent/Grenadines'),
    ('WS', 'Samoa'),
    ('SM', 'San Marino'),
    ('ST', 'Sao Tome'),
    ('SA', 'Saudi Arabia'),
    ('SN', 'Senegal'),
    ('SC', 'Seychelles'),
    ('SL', 'Sierra Leone'),
    ('SG', 'Singapore'),
    ('SK', 'Slovakia'),
    ('SI', 'Slovenia'),
    ('SB', 'Solomon Islands'),
    ('SO', 'Somalia'),
    ('ZA', 'South Africa'),
    ('ES', 'Spain'),
    ('LK', 'Sri Lanka'),
    ('SH', 'St. Helena'),
    ('PM', 'St.Pierre'),
    ('SD', 'Sudan'),
    ('SR', 'Suriname'),
    ('SZ', 'Swaziland'),
    ('SE', 'Sweden'),
    ('CH', 'Switzerland'),
    ('SY', 'Syrian Arab Republic'),
    ('TW', 'Taiwan'),
    ('TJ', 'Tajikistan'),
    ('TZ', 'Tanzania'),
    ('TH', 'Thailand'),
    ('TG', 'Togo'),
    ('TK', 'Tokelau'),
    ('TO', 'Tonga'),
    ('TT', 'Trinidad And Tobago'),
    ('TN', 'Tunisia'),
    ('TR', 'Turkey'),
    ('TM', 'Turkmenistan'),
    ('TV', 'Tuvalu'),
    ('UG', 'Uganda'),
    ('UA', 'Ukraine'),
    ('AE', 'United Arab Emirates'),
    ('UK', 'United Kingdom'),
    ('UY', 'Uruguay'),
    ('UZ', 'Uzbekistan'),
    ('VU', 'Vanuatu'),
    ('VA', 'Vatican City State'),
    ('VE', 'Venezuela'),
    ('VN', 'Viet Nam'),
    ('VG', 'Virgin Islands (British)'),
    ('VI', 'Virgin Islands (U.S.)'),
    ('EH', 'Western Sahara'),
    ('YE', 'Yemen'),
    ('YU', 'Yugoslavia'),
    ('ZR', 'Zaire'),
    ('ZM', 'Zambia'),
    ('ZW', 'Zimbabwe')
]
countries= []
for i in value:
#     print(i[1])
    countries.append(i[1].upper())


# In[239]:


countries


# In[238]:


countries.append('TURKIYE')
countries.append('KONG')
countries.append("LANKA")


# In[179]:


data1=list(reader(open('mid_cleaned.csv' , encoding="utf8")))
data1


# In[180]:


count=0
for ii,i in enumerate(data1[1:]):
    if i[23]:
        pass
    else:
        if len(k[ii])>0:
            coun= k[ii]
#             print(coun)
            
        else:
            pass
#         print(coun)
        for h in coun:
            h=h.replace('.','')
            h=h.replace('Lanka', 'SRI LANKA' )
#             print(h)
            if h.upper() == 'LANKA':
#                 print(h)
                i[23] = h
                print('y')
            else: 
                pass


# In[189]:


m=pd.DataFrame(data1)
m.head(185)


# In[190]:


header= m.iloc[0]
m=m[1:]
# m.reset_index(drop=True)
# a.columns = header
m=m.rename(columns= header )


# In[183]:


m['COUNTRY' == "SRI LANKA"]


# In[184]:


m.columns


# In[187]:


count=0
for i in data1[1:]:
    if i[23]== "" or i[23]== ' ':
        count +=1
    else:
        pass
count


# In[176]:


data1[0].index('COUNTRY')


# In[186]:


for i in data1[1:]:
    if i[1] == 'MEGA INTERNATIONAL COMMERCIAL BANK CO LTD':
        i[23]= 'TAIWAN'
    else:
        pass


# In[191]:


# m.to_csv('new_clean.csv')


# In[196]:


data11=list(reader(open('new_clean.csv' , encoding="utf8")))
data11


# In[201]:


for i in data11[1:]:
    ab= i[3]
    idd= i[5]
    
    if not i[23]:
        if ab == 'NIEN HSING TEXTILE CO. LTD.':
            i[23]='Taiwan'
        elif ab=='Ananta Apparel':
            i[23]='Bangladesh'
        elif ab=='UNIVERSAL JEANS LIMITED':
            i[23]='Bangladesh'
        elif ab=='PHONG PHU INTERNATIONAL JSC':
            i[23]='Veit Nam'
        elif ab=='JEANS COMPANY (PVT) LTD.':
            i[23]='Pakistan'
        elif ab=='GRUPPO TESSILE CASMIK SRL':
            i[23]='Italy'
        elif ab=='CONTO BENE JEANS':
            i[23]='Serbia'
        elif ab=='KENPARK BANGLADESH APPAREL (PVT) LTD':
            i[23]= 'Bangladesh'
        elif idd== 5357 :
            i[23]= 'Bangladesh'
        elif ab== 'SAI TEXTILE INTERNATIONAL LTD' :
            i[23]= 'Veit Nam'
        elif ab== 'ORIT TRADING LANKA' :
            i[23]= 'Sri Lanka'
        else:
            pass
    else:
        pass


# In[198]:


data11[0].index('PARTYID')


# In[207]:


data11[0].index('COUNTRY')


# In[200]:


data11[0].index('CUSTOMER_TYPE')


# In[264]:


for i in data11[1:]:
    abc= i[23]
    if abc != 'Pakistan' or abc !='PAKISTAN':
        i[7]= 'Export'
        print('aa')
    elif ((abc == 'PAKISTAN' or abc== 'Pakistan') and i[3]== 'ARTISTIC MILLINERS (AMG)'):
        i[7]= 'INTER UNIT'
        print('yes')
    else:
        i[7]= 'INDIRECT EXPORT'
    


# In[208]:


c=pd.DataFrame(data11)
c.head(65)


# In[209]:


header= c.iloc[0]
c=c[1:]
# m.reset_index(drop=True)
# a.columns = header
c=c.rename(columns= header )


# In[215]:


c.head(10)
c.iloc[60:65,23]


# In[206]:


# c.to_csv('new_clean_data.csv')


# In[222]:


print(c['COUNTRY'].value_counts())


# In[4]:


data1=list(reader(open('final_sales.csv', encoding='utf-8')))
data1


# In[ ]:




