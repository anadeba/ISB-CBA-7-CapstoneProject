# 1 - Categories shopped from last time
# 2 - Last time user experience rating
# 3 - Reasons for not shopping in a long time from Flipkart
# 4 - Likelihood for using Flipkart in future
# 5 - Most popular categories of Flipkart
# 6 - Other portals shopped from in the past 6 months
# 7 - Amazon shopping experience
# 8 - Flipkart vs Amazon - Price, Selection, Product-Quality, Navigation, Payment Options, Delivery Quality, Delivery Time, Returns, Discoverability, Recommendation
# 9 - Most preferred shopping portal
# 10 - City
# 11 - Age
# 12 - Gender
# 13 - Lifestage
# 14 - Education
# 15 - Occupation


import csv


input_file = '/Users/anurag/Documents/Work/Customer_Care/data_csv.csv'
output_file = '/Users/anurag/Documents/Work/Customer_Care/data_processed_csv.csv'

input_raw_data = []
with open(input_file, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        #print(row)
        input_raw_data.append(row)


input_processed_data = []
for iter, row in enumerate(input_raw_data):
    if iter > 1:
        start_dt = row[2]
        end_dt = row[3]

        # Single option checked
        last_cat = None
        if len(row[9].strip()) > 0: last_cat = 1
        if len(row[10].strip()) > 0: last_cat = 2
        if len(row[11].strip()) > 0: last_cat = 3
        if len(row[12].strip()) > 0: last_cat = 4
        if len(row[13].strip()) > 0: last_cat = 5
        if len(row[14].strip()) > 0: last_cat = 6
        if len(row[15].strip()) > 0: last_cat = 7
        if len(row[16].strip()) > 0: last_cat = 8
        if len(row[17].strip()) > 0: last_cat = 9
        if len(row[18].strip()) > 0: last_cat = 10
        if len(row[19].strip()) > 0: last_cat = 11
        if len(row[20].strip()) > 0: last_cat = 12
        if len(row[21].strip()) > 0: last_cat = 13

        # Single option checked
        last_flipkart_rating = None
        if len(row[22].strip()) > 0: last_flipkart_rating = 1
        if len(row[23].strip()) > 0: last_flipkart_rating = 2
        if len(row[24].strip()) > 0: last_flipkart_rating = 3
        if len(row[25].strip()) > 0: last_flipkart_rating = 4
        if len(row[26].strip()) > 0: last_flipkart_rating = 5

        # Multiple options checked
        if len(row[27].strip()) > 0: last_bad_exp1 = 1
        else: last_bad_exp1 = 0
        if len(row[28].strip()) > 0: last_bad_exp2 = 1
        else: last_bad_exp2 = 0
        if len(row[29].strip()) > 0: last_bad_exp3 = 1
        else: last_bad_exp3 = 0
        if len(row[30].strip()) > 0: last_bad_exp4 = 1
        else: last_bad_exp4 = 0
        if len(row[31].strip()) > 0: last_bad_exp5 = 1
        else: last_bad_exp5 = 0
        if len(row[32].strip()) > 0: last_bad_exp6 = 1
        else: last_bad_exp6 = 0
        if len(row[33].strip()) > 0: last_bad_exp7 = 1
        else: last_bad_exp7 = 0
        if len(row[34].strip()) > 0: last_bad_exp8 = 1
        else: last_bad_exp8 = 0
        if len(row[35].strip()) > 0: last_bad_exp9 = 1
        else: last_bad_exp9 = 0
        if len(row[36].strip()) > 0: last_bad_exp10 = 1
        else: last_bad_exp10 = 0
        if len(row[37].strip()) > 0: last_bad_exp11 = 1
        else: last_bad_exp11 = 0
        if len(row[38].strip()) > 0: last_bad_exp12 = 1
        else: last_bad_exp12 = 0

        # Single option checked
        flipkart_rating = None
        if len(row[39].strip()) > 0: flipkart_rating = 1
        if len(row[40].strip()) > 0: flipkart_rating = 2
        if len(row[41].strip()) > 0: flipkart_rating = 3
        if len(row[42].strip()) > 0: flipkart_rating = 4
        if len(row[43].strip()) > 0: flipkart_rating = 5

        # Single option checked
        popular_cat = None
        if len(row[44].strip()) > 0: popular_cat = 1
        if len(row[45].strip()) > 0: popular_cat = 2
        if len(row[46].strip()) > 0: popular_cat = 3
        if len(row[47].strip()) > 0: popular_cat = 4
        if len(row[48].strip()) > 0: popular_cat = 5
        if len(row[49].strip()) > 0: popular_cat = 6
        if len(row[50].strip()) > 0: popular_cat = 7
        if len(row[51].strip()) > 0: popular_cat = 8
        if len(row[52].strip()) > 0: popular_cat = 9
        if len(row[53].strip()) > 0: popular_cat = 10
        if len(row[54].strip()) > 0: popular_cat = 11
        if len(row[55].strip()) > 0: popular_cat = 12
        if len(row[56].strip()) > 0: popular_cat = 13

        # Multiple options checked
        if len(row[57].strip()) > 0: last_portal_used1 = 1
        else: last_portal_used1 = 0
        if len(row[58].strip()) > 0: last_portal_used2 = 1
        else: last_portal_used2 = 0
        if len(row[59].strip()) > 0: last_portal_used3 = 1
        else: last_portal_used3 = 0
        if len(row[60].strip()) > 0: last_portal_used4 = 1
        else: last_portal_used4 = 0
        if len(row[61].strip()) > 0: last_portal_used5 = 1
        else: last_portal_used5 = 0
        if len(row[62].strip()) > 0: last_portal_used6 = 1
        else: last_portal_used6 = 0
        if len(row[63].strip()) > 0: last_portal_used7 = 1
        else: last_portal_used7 = 0
        if len(row[64].strip()) > 0: last_portal_used8 = 1
        else: last_portal_used8 = 0

        # Single option checked
        last_amazon_rating = None
        if len(row[65].strip()) > 0: last_amazon_rating = 1
        if len(row[66].strip()) > 0: last_amazon_rating = 2
        if len(row[67].strip()) > 0: last_amazon_rating = 3
        if len(row[68].strip()) > 0: last_amazon_rating = 4
        if len(row[69].strip()) > 0: last_amazon_rating = 5

        # Single option checked
        flipkart_pricing = None
        if len(row[70].strip()) > 0: flipkart_pricing = 1
        if len(row[71].strip()) > 0: flipkart_pricing = 2
        if len(row[72].strip()) > 0: flipkart_pricing = 3
        if len(row[73].strip()) > 0: flipkart_pricing = 4
        if len(row[74].strip()) > 0: flipkart_pricing = 5

        # Single option checked
        amazon_pricing = None
        if len(row[75].strip()) > 0: amazon_pricing = 1
        if len(row[76].strip()) > 0: amazon_pricing = 2
        if len(row[77].strip()) > 0: amazon_pricing = 3
        if len(row[78].strip()) > 0: amazon_pricing = 4
        if len(row[79].strip()) > 0: amazon_pricing = 5

        # Single option checked
        none_pricing = 0
        if len(row[80].strip()) > 0: none_pricing = 1

        # Single option checked
        flipkart_selection = None
        if len(row[81].strip()) > 0: flipkart_selection = 1
        if len(row[82].strip()) > 0: flipkart_selection = 2
        if len(row[83].strip()) > 0: flipkart_selection = 3
        if len(row[84].strip()) > 0: flipkart_selection = 4
        if len(row[85].strip()) > 0: flipkart_selection = 5

        # Single option checked
        amazon_selection = None
        if len(row[86].strip()) > 0: amazon_selection = 1
        if len(row[87].strip()) > 0: amazon_selection = 2
        if len(row[88].strip()) > 0: amazon_selection = 3
        if len(row[89].strip()) > 0: amazon_selection = 4
        if len(row[90].strip()) > 0: amazon_selection = 5

        # Single option checked
        none_selection = 0
        if len(row[91].strip()) > 0: none_selection = 1

        # Single option checked
        flipkart_product_quality = None
        if len(row[92].strip()) > 0: flipkart_product_quality = 1
        if len(row[93].strip()) > 0: flipkart_product_quality = 2
        if len(row[94].strip()) > 0: flipkart_product_quality = 3
        if len(row[95].strip()) > 0: flipkart_product_quality = 4
        if len(row[96].strip()) > 0: flipkart_product_quality = 5

        # Single option checked
        amazon_product_quality = None
        if len(row[97].strip()) > 0: amazon_product_quality = 1
        if len(row[98].strip()) > 0: amazon_product_quality = 2
        if len(row[99].strip()) > 0: amazon_product_quality = 3
        if len(row[100].strip()) > 0: amazon_product_quality = 4
        if len(row[101].strip()) > 0: amazon_product_quality = 5

        # Single option checked
        none_product_quality = 0
        if len(row[102].strip()) > 0: none_product_quality = 1

        # Single option checked
        flipkart_navigation = None
        if len(row[103].strip()) > 0: flipkart_navigation = 1
        if len(row[104].strip()) > 0: flipkart_navigation = 2
        if len(row[105].strip()) > 0: flipkart_navigation = 3
        if len(row[106].strip()) > 0: flipkart_navigation = 4
        if len(row[107].strip()) > 0: flipkart_navigation = 5

        # Single option checked
        amazon_navigation = None
        if len(row[108].strip()) > 0: amazon_navigation = 1
        if len(row[109].strip()) > 0: amazon_navigation = 2
        if len(row[110].strip()) > 0: amazon_navigation = 3
        if len(row[111].strip()) > 0: amazon_navigation = 4
        if len(row[112].strip()) > 0: amazon_navigation = 5

        # Single option checked
        none_navigation = 0
        if len(row[113].strip()) > 0: none_navigation = 1

        # Single option checked
        flipkart_payment = None
        if len(row[114].strip()) > 0: flipkart_payment = 1
        if len(row[115].strip()) > 0: flipkart_payment = 2
        if len(row[116].strip()) > 0: flipkart_payment = 3
        if len(row[117].strip()) > 0: flipkart_payment = 4
        if len(row[118].strip()) > 0: flipkart_payment = 5

        # Single option checked
        amazon_payment = None
        if len(row[119].strip()) > 0: amazon_payment = 1
        if len(row[120].strip()) > 0: amazon_payment = 2
        if len(row[121].strip()) > 0: amazon_payment = 3
        if len(row[122].strip()) > 0: amazon_payment = 4
        if len(row[123].strip()) > 0: amazon_payment = 5

        # Single option checked
        none_payment = 0
        if len(row[124].strip()) > 0: none_payment = 1

        # Single option checked
        flipkart_delivery_quality = None
        if len(row[125].strip()) > 0: flipkart_delivery_quality = 1
        if len(row[126].strip()) > 0: flipkart_delivery_quality = 2
        if len(row[127].strip()) > 0: flipkart_delivery_quality = 3
        if len(row[128].strip()) > 0: flipkart_delivery_quality = 4
        if len(row[129].strip()) > 0: flipkart_delivery_quality = 5

        # Single option checked
        amazon_delivery_quality = None
        if len(row[130].strip()) > 0: amazon_delivery_quality = 1
        if len(row[131].strip()) > 0: amazon_delivery_quality = 2
        if len(row[132].strip()) > 0: amazon_delivery_quality = 3
        if len(row[133].strip()) > 0: amazon_delivery_quality = 4
        if len(row[134].strip()) > 0: amazon_delivery_quality = 5

        # Single option checked
        none_delivery_quality = 0
        if len(row[135].strip()) > 0: none_delivery_quality = 1

        # Single option checked
        flipkart_delivery_speed = None
        if len(row[136].strip()) > 0: flipkart_delivery_speed = 1
        if len(row[137].strip()) > 0: flipkart_delivery_speed = 2
        if len(row[138].strip()) > 0: flipkart_delivery_speed = 3
        if len(row[139].strip()) > 0: flipkart_delivery_speed = 4
        if len(row[140].strip()) > 0: flipkart_delivery_speed = 5

        # Single option checked
        amazon_delivery_speed = None
        if len(row[141].strip()) > 0: amazon_delivery_speed = 1
        if len(row[142].strip()) > 0: amazon_delivery_speed = 2
        if len(row[143].strip()) > 0: amazon_delivery_speed = 3
        if len(row[144].strip()) > 0: amazon_delivery_speed = 4
        if len(row[145].strip()) > 0: amazon_delivery_speed = 5

        # Single option checked
        none_delivery_speed = 0
        if len(row[146].strip()) > 0: none_delivery_speed = 1

        # Single option checked
        flipkart_returns = None
        if len(row[147].strip()) > 0: flipkart_returns = 1
        if len(row[148].strip()) > 0: flipkart_returns = 2
        if len(row[149].strip()) > 0: flipkart_returns = 3
        if len(row[150].strip()) > 0: flipkart_returns = 4
        if len(row[151].strip()) > 0: flipkart_returns = 5

        # Single option checked
        amazon_returns = None
        if len(row[152].strip()) > 0: amazon_returns = 1
        if len(row[153].strip()) > 0: amazon_returns = 2
        if len(row[154].strip()) > 0: amazon_returns = 3
        if len(row[155].strip()) > 0: amazon_returns = 4
        if len(row[156].strip()) > 0: amazon_returns = 5

        # Single option checked
        none_returns = 0
        if len(row[157].strip()) > 0: none_returns = 1

        # Single option checked
        flipkart_discoverability = None
        if len(row[158].strip()) > 0: flipkart_discoverability = 1
        if len(row[159].strip()) > 0: flipkart_discoverability = 2
        if len(row[160].strip()) > 0: flipkart_discoverability = 3
        if len(row[161].strip()) > 0: flipkart_discoverability = 4
        if len(row[162].strip()) > 0: flipkart_discoverability = 5

        # Single option checked
        amazon_discoverability = None
        if len(row[163].strip()) > 0: amazon_discoverability = 1
        if len(row[164].strip()) > 0: amazon_discoverability = 2
        if len(row[165].strip()) > 0: amazon_discoverability = 3
        if len(row[166].strip()) > 0: amazon_discoverability = 4
        if len(row[167].strip()) > 0: amazon_discoverability = 5

        # Single option checked
        none_discoverability = 0
        if len(row[168].strip()) > 0: none_discoverability = 1

        # Single option checked
        flipkart_recommend = None
        if len(row[169].strip()) > 0: flipkart_recommend = 1
        if len(row[170].strip()) > 0: flipkart_recommend = 2
        if len(row[171].strip()) > 0: flipkart_recommend = 3
        if len(row[172].strip()) > 0: flipkart_recommend = 4
        if len(row[173].strip()) > 0: flipkart_recommend = 5

        # Single option checked
        amazon_recommend = None
        if len(row[174].strip()) > 0: amazon_recommend = 1
        if len(row[175].strip()) > 0: amazon_recommend = 2
        if len(row[176].strip()) > 0: amazon_recommend = 3
        if len(row[177].strip()) > 0: amazon_recommend = 4
        if len(row[178].strip()) > 0: amazon_recommend = 5

        # Single option checked
        none_recommend = 0
        if len(row[179].strip()) > 0: none_recommend = 1

        # Single option checked
        preferred_portal = None
        if len(row[180].strip()) > 0: preferred_portal = 'Flipkart'
        if len(row[181].strip()) > 0: preferred_portal = 'Amazon'
        if len(row[182].strip()) > 0: preferred_portal = 'Snapdeal'
        if len(row[183].strip()) > 0: preferred_portal = 'Paytm'
        if len(row[184].strip()) > 0: preferred_portal = 'Ebay'
        if len(row[185].strip()) > 0: preferred_portal = 'Myntra'
        if len(row[186].strip()) > 0: preferred_portal = 'Jabong'
        if len(row[187].strip()) > 0: preferred_portal = 'Others'

        # Single option checked
        city = None
        if len(row[188].strip()) > 0: city = 'Delhi'
        if len(row[189].strip()) > 0: city = 'Mumbai'
        if len(row[190].strip()) > 0: city = 'Bangalore'
        if len(row[191].strip()) > 0: city = 'Kolkata'
        if len(row[192].strip()) > 0: city = 'Chennai'
        if len(row[193].strip()) > 0: city = 'Hyderabad'
        if len(row[194].strip()) > 0: city = 'Agartala'
        if len(row[195].strip()) > 0: city = 'Agra'
        if len(row[196].strip()) > 0: city = 'Ahmedabad'
        if len(row[197].strip()) > 0: city = 'Ahmednagar'
        if len(row[198].strip()) > 0: city = 'Aizawl'
        if len(row[199].strip()) > 0: city = 'Ajmer'
        if len(row[200].strip()) > 0: city = 'Akola'
        if len(row[201].strip()) > 0: city = 'Aligarh'
        if len(row[202].strip()) > 0: city = 'Allahabad'
        if len(row[203].strip()) > 0: city = 'Alwar'
        if len(row[204].strip()) > 0: city = 'Amravati'
        if len(row[205].strip()) > 0: city = 'Amritsar'
        if len(row[206].strip()) > 0: city = 'Anantapur'
        if len(row[207].strip()) > 0: city = 'Asansol'
        if len(row[208].strip()) > 0: city = 'Aurangabad'
        if len(row[209].strip()) > 0: city = 'Bardhaman'
        if len(row[210].strip()) > 0: city = 'Bareilly'
        if len(row[211].strip()) > 0: city = 'Bathinda'
        if len(row[212].strip()) > 0: city = 'Belgaum'
        if len(row[213].strip()) > 0: city = 'Bhagalpur'
        if len(row[214].strip()) > 0: city = 'Bharatpur'
        if len(row[215].strip()) > 0: city = 'Bhilai'
        if len(row[216].strip()) > 0: city = 'Bhopal'
        if len(row[217].strip()) > 0: city = 'Bhubaneswar'
        if len(row[218].strip()) > 0: city = 'Bijapur'
        if len(row[219].strip()) > 0: city = 'Bikaner'
        if len(row[220].strip()) > 0: city = 'Bilaspur'
        if len(row[221].strip()) > 0: city = 'Bokaro'
        if len(row[222].strip()) > 0: city = 'Brahmapur'
        if len(row[223].strip()) > 0: city = 'Chandigarh'
        if len(row[224].strip()) > 0: city = 'Coimbatore'
        if len(row[225].strip()) > 0: city = 'Cuttack'
        if len(row[226].strip()) > 0: city = 'Daman'
        if len(row[227].strip()) > 0: city = 'Dehradun'
        if len(row[228].strip()) > 0: city = 'Dewas'
        if len(row[229].strip()) > 0: city = 'Dhanbad'
        if len(row[230].strip()) > 0: city = 'Dispur'
        if len(row[231].strip()) > 0: city = 'Durgapur'
        if len(row[232].strip()) > 0: city = 'Faridabad'
        if len(row[233].strip()) > 0: city = 'Farrukhabad'
        if len(row[234].strip()) > 0: city = 'Firozabad'
        if len(row[235].strip()) > 0: city = 'Gandhinagar'
        if len(row[236].strip()) > 0: city = 'Gangtok'
        if len(row[237].strip()) > 0: city = 'Gaya'
        if len(row[238].strip()) > 0: city = 'Ghaziabad'
        if len(row[239].strip()) > 0: city = 'Gopalpur'
        if len(row[240].strip()) > 0: city = 'Gorakhpur'
        if len(row[241].strip()) > 0: city = 'Gulbarga'
        if len(row[242].strip()) > 0: city = 'Guntur'
        if len(row[243].strip()) > 0: city = 'Guwahati'
        if len(row[244].strip()) > 0: city = 'Gwalior'
        if len(row[245].strip()) > 0: city = 'Hisar'
        if len(row[246].strip()) > 0: city = 'Howrah'
        if len(row[247].strip()) > 0: city = 'Imphal'
        if len(row[248].strip()) > 0: city = 'Indore'
        if len(row[249].strip()) > 0: city = 'Itanagar'
        if len(row[250].strip()) > 0: city = 'Jabalpur'
        if len(row[251].strip()) > 0: city = 'Jaipur'
        if len(row[252].strip()) > 0: city = 'Jalandhar'
        if len(row[253].strip()) > 0: city = 'Jamnagar'
        if len(row[254].strip()) > 0: city = 'Jamshedpur'

        input_processed_data.append([start_dt, end_dt, last_cat, last_flipkart_rating,
                                     last_bad_exp1, last_bad_exp2, last_bad_exp3, last_bad_exp4, last_bad_exp5, last_bad_exp6,
                                     last_bad_exp7, last_bad_exp8, last_bad_exp9, last_bad_exp10, last_bad_exp11, last_bad_exp12,
                                     flipkart_rating, popular_cat,
                                     last_portal_used1, last_portal_used2, last_portal_used3, last_portal_used4,
                                     last_portal_used5,last_portal_used6, last_portal_used7, last_portal_used8,
                                     last_amazon_rating,
                                     flipkart_pricing, amazon_pricing, none_pricing,
                                     flipkart_selection, amazon_selection, none_selection,
                                     flipkart_product_quality, amazon_product_quality, none_product_quality,
                                     flipkart_navigation, amazon_navigation, none_navigation,
                                     flipkart_payment, amazon_payment, none_payment,
                                     flipkart_delivery_quality, amazon_delivery_quality, none_delivery_quality,
                                     flipkart_delivery_speed, amazon_delivery_speed, none_delivery_speed,
                                     flipkart_returns, amazon_returns, none_returns,
                                     flipkart_discoverability, amazon_discoverability, none_discoverability,
                                     flipkart_recommend, amazon_recommend, none_recommend,
                                     preferred_portal, city
                                     ])



#for row in input_raw_data[5:10]:
#    print(row)

#for row in input_processed_data[5:10]:
#    print(row)

header = ['start_dt','end_dt','last_cat','last_flipkart_rating','last_bad_exp1','last_bad_exp2','last_bad_exp3','last_bad_exp4','last_bad_exp5','last_bad_exp6','last_bad_exp7','last_bad_exp8','last_bad_exp9','last_bad_exp10','last_bad_exp11','last_bad_exp12','flipkart_rating','popular_cat','last_portal_used1','last_portal_used2','last_portal_used3','last_portal_used4','last_portal_used5','last_portal_used6','last_portal_used7','last_portal_used8','last_amazon_rating','flipkart_pricing','amazon_pricing','none_pricing','flipkart_selection','amazon_selection','none_selection','flipkart_product_quality','amazon_product_quality','none_product_quality','flipkart_navigation','amazon_navigation','none_navigation','flipkart_payment','amazon_payment','none_payment','flipkart_delivery_quality','amazon_delivery_quality','none_delivery_quality','flipkart_delivery_speed','amazon_delivery_speed','none_delivery_speed','flipkart_returns','amazon_returns','none_returns','flipkart_discoverability','amazon_discoverability','none_discoverability','flipkart_recommend','amazon_recommend','none_recommend','preferred_portal','city']
with open(output_file, 'w') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(header)
    for row in input_processed_data:
        csv_writer.writerow(row)

