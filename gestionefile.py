import string

input_file = open("prova.ll","r")
output_file = open("newfile.txt","w")

control = 0

while(True):
    tmp = input_file.readline()
    if tmp == "define i32 @main() #0 {\n":
        tmp = input_file.readline()
        while "}\n" != tmp:
            index = tmp.find("align", 0 ,len(tmp))
            index1 = tmp.find("nsw", 0 ,len(tmp))            
            if(index != -1):
                tmp = tmp[:index - 2] + '\n'
            if(index1 != -1):
                tmp = tmp[:index1 -1] + tmp[index1+3:]
            
            if(tmp != 0):
                output_file.write(tmp)
                tmp = input_file.readline()
            
        output_file.write(";;")
        break
input_file.close()
output_file.close()
        

