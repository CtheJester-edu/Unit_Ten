# By Caleb Grusendorf
# this code counts how many times each word is used in a document. does struggle minorly with formating.



from pathlib import Path
import docx2txt

def wordFreq(file):
    
    if file.suffix != ".txt":
        temp1 = docx2txt.process(file)
    else:
        temp1 = Path.read_text(file)   
    
    punctChars = (",",".",":",";","<",">","/","?","`","\"","\\","(",")","*","&","^","%","$","#","@","!","+","=","~","}","{","'",)
    for c in punctChars:
        temp1 = temp1.replace(c,"")

    temp3 = [temp1.split(" ")]
    return(temp3)

def wordcount(data):
    freq = {}
    for list in data:
        for word in list:
            word = word.lower()
            freq[word] = freq.get(word, 0) + 1
    return(freq)




def printWds(data):
    # for x in sorted(data.keys()):
    #     print()
    for key, value in sorted(data.items()):
        print(f"{str(key):<15} {str(value):<15}")
    return

def main():
    sentinel = False
    path = ""
    while sentinel == False:
    #     filename = input("please enter the filename for the file you would like to analyse.")
    #     path = Path(filename)
    #     if path.exists == True:
    #         sentinel = True
    #     else:
    #         sentinel = False
    #     if path.is_file == True:
    #         sentinel = True
    #     else:
    #         sentinel = False
        path = Path.cwd() / "Text_Assets" / input("please enter the filename for the file you would like to analyse.")
        sentinel = Path.exists(path)
    list = wordFreq(path)
    final = wordcount(list)
    printWds(final)


main()

