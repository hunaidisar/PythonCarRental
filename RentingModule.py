import sys
options = ["Brows " , "Rent car(s) ", "Return car(s) ", "Exit program "]

choice = ""
in_message = "please select a choice \n"
for i , e in enumerate(options):
    in_message += f" {i+1} {e} \n"
    
in_message += "I choose _"

while choice not in map(str,range(1,len(options)+1)):
    choice = input(in_message)

choice_out =  options[int(choice)-1]  
print ("you chose : " + choice_out )

for i in range(1,len(options)+1):
        
    if choice_out == options[i]:
        print (i)
sys.stop()

    
    
    