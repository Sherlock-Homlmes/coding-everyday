nguoi_mot=[[10,12],[13,14],[15,18]]
nguoi_hai=[[9,10],[11,11.75],[12,12.5],[13,13.5],[14,14.25],[15,19]]

gapnhau=[]
arr=[]

for i in range(len(nguoi_mot)):
    #thoi gian bat dau ranh
    if(nguoi_mot[i][0]<nguoi_hai[i][1]):
         arr.append(nguoi_mot[i][0])
    else:
         arr.append(nguoi_hai[i][0])

    #thoi gian ket thuc
    if(nguoi_mot[i][1]<nguoi_hai[i][1]):
         arr.append(nguoi_mot[i][1])
    else:
         arr.append(nguoi_hai[i][1])
    gapnhau.append(arr)
    arr=[]

print(gapnhau)