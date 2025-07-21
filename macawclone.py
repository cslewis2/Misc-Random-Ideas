##simple text sequence membership comparison
##add input user sequence,
##find list of restriction enzymes csv or txt
##run comparison
##ideal output" there are x number of y restriction sites"
##stretch: complimentary sequence output. hmmm.....
seq=('accggtagtatc')
ecor1=('ccatgg')
if ecor1 in seq:
    print ('found')
else:
    print ('not found')