from struct import *
print("place the binary file in the directory and")
print("enter the filename with the extension stl")
f=input("enter file name ")

file_object=open(f,'rb')
line=file_object.read()
index=80

temp = list(unpack('i', line[index:index+4]))#врем.пер.для расп.кол.треуг.

file_object=open('ASCII_write.stl','w')
file_object.write("solid Exported STL Binary read to ASCII write")#об. нач. запись
file_object.write("\n")#перенос на новую строку

for faces in range(0,temp[0]):#temp врем. пер. опред. кол. треугольников
    file_object.write("facet normal ")
    
    #нормали
    index=index+4
    for norm in range(3):

        pnx=unpack('f', line[index:index+4])#заносим кортеж во врем. пер.
        file_object.write(str(pnx[0]))#записываем котреж как строку 
        file_object.write(" ")
        index=index+4
        
    
    file_object.write("\n")#перенос на новую строку
    
    file_object.write("outer loop")
    file_object.write("\n")#перенос на новую строку

    for vertex in range(3):
        file_object.write("vertex ")
        # точки (vertex)  
        for vert in range(3):#меняем range с 0 на 3 и ук. индексы смещ. внутри цикла
             #print(vert)
             pvx=unpack('f', line[index:index+4])
             file_object.write(str(pvx[0]))
             file_object.write(" ")
             index=index+4
        
        file_object.write("\n")#перенос на новую строку
    index=index-2#доб. 2 байт в инд. для окончания описания лупа
        
    file_object.write("endloop")
    file_object.write("\n")#перенос на новую строку
    file_object.write("endfacet")
    file_object.write("\n")#перенос на новую строку
        
file_object.write("endsolid Exported STL Binary read to ASCII write")#финальная запись
file_object.close()

print ('done')
