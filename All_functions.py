

def convert_str_float_2(df,column):
    df[column]=df[column].astype('string')
    df[column]=df[column].apply(lambda x: x[1:] if x[0]=='₹' else x )
    df[column]=df[column].replace('[^0-9,.]','0',regex=True)
    df[column]=df[column].apply(lambda x:x.split(',')[0]+'.'+x.split(',')[1][0:2] if(x.find(',')!=-1) else x)
    df[column]=df[column].astype(float)

    
def convert_str_float(column):
    column.astype('string')
    column.apply(lambda x: x[1:] if x[0]=='₹' else x )
    column.replace('[^0-9,.]','0',regex=True)
    column.apply(lambda x:x.split(',')[0]+'.'+x.split(',')[1][0:2] if(x.find(',')!=-1) else x)
    column.astype(float)

