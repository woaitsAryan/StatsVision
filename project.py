import plotext as plt
import sys 
from tabulate import tabulate
import country_converter as coco
import wbdata 

dict2 = { "GDP" : "NY.GDP.MKTP.CD" ,
          "GDP per Capita PPP" : "NY.GNP.PCAP.PP.CD",
          "GDP Growth Rate" : "NY.GDP.MKTP.KD.ZG",
          "Inflation Rate" : "FP.CPI.TOTL.ZG",
          "Unemployment Rate" : "SL.UEM.TOTL.NE.ZS",
          "Fertility rate" : "SP.DYN.TFRT.IN",
          "CO2 Emissions per capita" : "EN.ATM.CO2E.PC",
          "Life expectancy" : "SP.DYN.LE00.IN"
           } # WorldBank official codes for respective datasets.

def main(): 
    global list_of_countries 
    list_of_countries = get_country()
    print(print_table())
    global indicator
    indicator = get_indicator()
    iso = coco.convert(names=list_of_countries, to = "ISO3") #Worldbank doesn't support country names, gotta convert it into ISO codes
    indicator_code = dict2[indicator]
    data = get_data(iso, indicator_code) 
    LIST_OF_COUNTRY = [] #make country list to titled versions of it
    for lala in list_of_countries:
        LIST_OF_COUNTRY.append(lala.title())
    plt.bar(LIST_OF_COUNTRY, data, orientation = "h", width = 0.3, marker = 'fhd') 
    plt.title(o2)
    plt.clc() # to remove colors
    plt.plotsize(100, (2 * len(list_of_countries) - 1) + 4) # 4 = (1 for x numerical ticks + 2 for x axes + 1 for title)
    plt.show()
def get_country(): #Basically get a valid country
    global countries 
    countries = ['afghanistan', 'albania', 'algeria', 'american_samoa', 'andorra', 'angola', 'anguilla', 'antigua_and_barbuda', 'argentina', 'armenia', 'aruba', 'australia', 'austria', 'azerbaijan', 'bahamas', 'bahrain', 'bangladesh', 'barbados', 'belarus', 'belgium', 'belize', 'benin', 'bermuda', 'bhutan', 'bolivia', 'bosnia_and_herzegovina', 'botswana', 'brazil', 'brunei', 'bulgaria', 'burkina_faso', 'burundi', 'cambodia', 'cameroon', 'canada', 'cape_verde', 'cayman_islands', 'central_african_republic', 'chad', 'channel_islands', 'chile', 'china', 'christmas_island', 'colombia', 'comoros', 'congo', 'cook_islands', 'costa_rica', 'croatia', 'cuba', 'cyprus', 'czech_republic', 'denmark', 'djibouti', 'dominica', 'dominican_republic', 'east_timor', 'ecuador', 'egypt', 'el_salvador', 'equatorial_guinea', 'eritrea', 'estonia', 'ethiopia', 'euro_area', 'european_union', 'falkland_islands', 'faroe_islands', 'fiji', 'finland', 'france', 'french_polynesia', 'gabon', 'gambia', 'georgia', 'germany', 'ghana', 'gibraltar', 'greece', 'greenland', 'grenada', 'guam', 'guatemala', 'guinea', 'guinea_bissau', 'guyana', 'haiti', 'honduras', 'hong_kong', 'hungary', 'iceland', 'india', 'indonesia', 'iran', 'iraq', 'ireland', 'isle_of_man', 'israel', 'italy', 'ivory_coast', 'jamaica', 'japan', 'jordan', 'kazakhstan', 'kenya', 'kiribati', 'kosovo', 'kuwait', 'kyrgyzstan', 'laos', 'latvia', 'lebanon', 'lesotho', 'liberia', 'libya', 'liechtenstein', 'lithuania', 'luxembourg', 'macau', 'macedonia', 'madagascar', 'malawi', 'malaysia', 'maldives', 'mali', 'malta', 'marshall_islands', 'mauritania', 'mauritius', 'mayotte', 'mexico', 'micronesia', 'moldova', 'monaco', 'mongolia', 'montenegro', 'montserrat', 'morocco', 'mozambique', 'myanmar', 'namibia', 'nepal', 'netherlands', 'netherlands_antilles', 'new_caledonia', 'new_zealand', 'nicaragua', 'niger', 'nigeria', 'norfolk_island', 'north_korea', 'northern_mariana_islands', 'norway', 'oman', 'pakistan', 'palau', 'palestine', 'panama', 'papua_new_guinea', 'paraguay', 'peru', 'philippines', 'pitcairn_islands', 'poland', 'portugal', 'puerto_rico', 'qatar', 'republic_of_the_congo', 'reunion', 'romania', 'russia', 'rwanda', 'samoa', 'san_marino', 'sao_tome_and_principe', 'saudi_arabia', 'senegal', 'serbia', 'seychelles', 'sierra_leone', 'singapore', 'slovakia', 'slovenia', 'solomon_islands', 'somalia', 'south_africa', 'south_korea', 'south_sudan', 'spain', 'sri_lanka', 'st_helena', 'st_kitts_and_nevis', 'st_lucia', 'st_pierre_and_miquelon', 'st_vincent_and_the_grenadines', 'sudan', 'suriname', 'swaziland', 'sweden', 'switzerland', 'syria', 'taiwan', 'tajikistan', 'tanzania', 'thailand', 'togo', 'tokelau', 'tonga', 'trinidad_and_tobago', 'tunisia', 'turkey', 'turkmenistan', 'tuvalu', 'uganda', 'ukraine', 'united_arab_emirates', 'united_kingdom', 'united_states', 'uruguay', 'uzbekistan', 'vanuatu', 'venezuela', 'vietnam', 'virgin_islands', 'wallis_and_futuna', 'west_bank_and_gaza', 'yemen', 'zambia', 'zimbabwe']

    b = [] #Add valid countries in this list and return
    b1 = 0 # count up if any are invalid(not found in that countries dict)
    b2 = 0 # count up if number of countries aren't more than 10 or just 1. Why 10? I think a graph that big will look messy with 11 elements tbh
    while True:
        a = input("Which countries data do you want graphically representated? ").lower()
        if "," in a:
            b = a.split(", ")
            for country in b:
                if country not in countries:
                    b1 = b1 + 1
                else:
                    b2 = b2 + 1
        elif a in countries:
            pass
        else:
            print("Country not found!(Kindly seperate two-worded countries with an underscore and use commas!)")
            print()
        if b1 == 0:
            if 1 < b2 < 10:
                return b
            else:
                print("Kindly input more than 1 and less than 10 countries for a more beautiful graph!")
                print()
        else:
            print("Country not found!(Kindly seperate two-worded countries with an underscore and use commas!)")
            print()

def print_table(): # print a pretty table 
    global dict
    dict = { "Choose your number!" : ['1','2','3','4','5','6','7','8'],
            "Indicator" : ['GDP','GDP per Capita PPP','GDP Growth Rate','Inflation Rate','Unemployment Rate','Fertility rate',
            'CO2 Emissions per capita','Life expectancy'] }
    table = tabulate(dict, headers="keys", tablefmt="pretty")
    return table

def get_indicator(): # get an indicator(0=9) and match it to the specific indicator name
    while True:
        y = input("Which indicator to graph? ")
        try:
            if 0 < int(y) and int(y) < 9:
                return dict['Indicator'][(int(y) - 1)]
            else:
                print("Kindly provide a valid number!")
        except ValueError:
            print("Kindly provide a valid number!")

def get_data(n1, n2): #Get data of those indicators and countries from World bank, add em up into a neat list called o
    o = []
    for iso_countries in n1:
        o1 = wbdata.get_data(n2, country=iso_countries)[0]['value']
        if o1 == None:
            o1 = wbdata.get_data(n2, country=iso_countries)[1]['value']
        if o1 == None:
            o1 = wbdata.get_data(n2, country=iso_countries)[2]['value']
        if o1 == None:
            o1 = wbdata.get_data(n2, country=iso_countries)[3]['value'] #Can't believe I need 3 contingencies checking data for as back as 2019, CMON WORLD BANK, UPDATE YOUR FREAKING DATA
        global o2
        o2 = wbdata.get_data(n2, country=iso_countries)[3]['indicator']['value']
        if o1 == None:
            sys.exit("Sorry, even the WorldBank doesn't have the data you're seeking for") #Ain't no way I'm printing data issued before 2019, this is on world bank, not me
        o.append(round(o1,1))
    return o

if __name__ == "__main__":
    main()
