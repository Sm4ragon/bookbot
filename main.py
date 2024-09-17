book = "books/frankenstein.txt"

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        #print(file_contents)

def number_of_words():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        word_count = 0
        for i in words:
            word_count+=1
        #print(word_count)

def print_report(list):
    word_count = str(number_of_words())
    print("--- Begin report of " + book + " ---")
    print(word_count + " words found in the document.")
    for k in list:
        print("The '" + str(k[0]) + "' charcter was found " +  str(k[1]) + " times.")        
    print("--- End report ---")

def sort_on(dict):
    return dict[1]

def character_count():
    with open(book) as f:
        file_contents = f.read()
        lowered_string = file_contents.lower()

        count_of_characters = {'a': 00}
        list_of_character_count = []
        for i in lowered_string:
            if i.isalpha():
                count_of_characters[i] = count_of_characters.get(i, 0) + 1
        #print(count_of_characters)
        #list_of_character_count.append(count_of_characters.items())
        for key, value in count_of_characters.items():
            temp = [key,value]
            list_of_character_count.append(temp)
        list_of_character_count.sort(reverse=True, key=sort_on)
        print_report(list_of_character_count)


    
# main()
# number_of_words()
character_count()
#print_report()