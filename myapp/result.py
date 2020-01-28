def get_data(room_dict):
    import numpy as np
    array1=[]
    array2=[]
    for i in range(1,101):
        if i<=40:
            array1.append('abcdef')
        array2.append('abcdef')
    for i in room_dict:
        if i=='2p7':
            array=np.array(array2)
            array.shape=(10,10)
            room_dict[i]=array
        else:
            array=np.array(array1)
            array.shape=(8,5)
            room_dict[i]=array
    return room_dict
def result1(cls_name,cls_value,room_dict):
  room_dict=get_data(room_dict)
  x,y,a=0,0,0
  b=1
  ind=len(cls_name)-1
  
  for i in room_dict:
    if i=="2p7" :
        for j in range(0,10):
            
            for k in range(0,10):
                if j%2==0 and cls_value[a] !=0:
                    x=x+1
                    room_dict[i][k,j]=cls_name[a]+str(x)
                    cls_value[a]-=1
                    
                if j%2 !=0 and cls_value[b] !=0:
                    y=y+1
                    room_dict[i][k,j]=cls_name[b]+str(y)
                    cls_value[b]-=1
            
                if cls_value[a]==0 and ind>=(a+2):
                    a+=2
                    x=0
                
                if cls_value[b]==0 and  ind>=(b+2):
                    b+=2
                    y=0
    else:
        for j in range(0,5):
            
            for k in range(0,8):
                if j%2==0 and cls_value[a] !=0:
                    x=x+1
                    room_dict[i][k,j]=cls_name[a]+str(x)
                    cls_value[a]-=1
                if ind !=0:
                    if j%2 !=0 and cls_value[b] !=0:
                        y=y+1
                        room_dict[i][k,j]=cls_name[b]+str(y)
                        cls_value[b]-=1
            
                if cls_value[a]==0 and ind>=(a+2):
                    a+=2
                    x=0
                if ind!=0:
                    if cls_value[b]==0  and  ind>=(b+2):
                        b+=2
                        y=0
  return room_dict

    


