
'''simple Rx SIG quiz'''


#data_sets={}

#admin_routes={po,os,od,ou,as,ad,au,pr,pv,sq,im,iv,top-tpcl}
#med_frequency={qd,bid,tid,qod,wk,qmn,}
#mass_volume={'mg':'milligrams','g':'grams','u':'unit','ml':'millliliter','mcg':'microgram'}
#verbs={t,g,adm,inj,app,ins,}
#print(mass_volume)

#def ad_rout(*ad_keys,**ad_values):
 #   '''trying to produce a dict of adkeys advalues--this works#'''
#    ad_keys=('mg','g','u','mcg')
#    ad_values=('milligrams','grams','units','micrograms')
#    combo=dict(zip (ad_keys,ad_values))
#    #print (combo)
#    return (combo)
   



#print(ad_rout())

#funct for user choice as to which quiz they would like, eg 1=admin_routes,2=med_frequency,etc
#guts of user lookup use case/switch

user_input= input('input your unit...' )
match user_input:
    case ('mg'):
        print ('milligram')
    case(' '):
        print ('need an input')
        