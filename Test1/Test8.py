import clr
#import sys
#x12Req = sys.argv[1]
#print(x12Req)

x12Req = """ISA*00*          *00*          *ZZ*BPR21GRACEZI   *ZZ*00773          *010806*1200*^*00501*000000003*0*T*:~
            GS*HS*PROFSERV*DEVELOPMENT*20010101*120000*1*X*005010X279A1~
            ST*270*0001*005010X279A1~
            BHT*0022*13*10001234*19990501*1319~
            HL*1**20*1~
            NM1*PR*2*UHC COMPANY*****PI*00773~
            HL*2*1*21*1~
            NM1*1P*1*OUTLAND*CHERYL****XX*1123456789~
            HL*3*2*22*0~
            TRN*1*93175-012547*9877281234~
            NM1*IL*1*VATTAKATTE*KEVIN*F***MI*00629276176~
            REF*6P*0742431~
            DMG*D8*19840307~
            DTP*291*RD8*20170801-20171120~
            EQ*AL~
            SE*14*0001~
            GE*1*1~
            IEA*1*000000003~"""



#
def xmlParser(x12Req):
    print(type(x12Req))
    clr.AddReference("Optum.X12")	
    from Optum.X12.Parsing import X12Parser	
    xpar = X12Parser()	
    xmlObj = xpar.ParseMultiple(x12Req)
    xmlStr = []	
    for x in xmlObj:
        x.SerializeToX12(True)
        xmlStr.append(x.Serialize()) 
    return(xmlStr[0])
#   return xmlStr[0]


#test1 = xmlParser(x12Req)
#print(test1)
    
if __name__== "__main__":
    test1 = xmlParser(x12Req)
    print(test1)
            

