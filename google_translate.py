from pyfiglet import Figlet
f=Figlet(font='standard')
print(f.renderText('Google Translate')) 
def show_menu():
    print('1- Add new word')
    print('2- Translation english2persian')
    print('3- Translation persian2english')
    print('4- Exit')
words=[]
def load():
    print('Loading...')
    file=open('dictionary.txt','r')
    data=file.read()
    rows=data.split('\n')
    for i in range(len(rows)):
        info=rows[i].split(',')
        words.append({'english':info[0],'persian':info[1]})
    file.close()
    print('Welcome to google translate')
def add_words():
    english=input("Please english word: ")
    persian=input('Please persian word: ')
    words.append({'english':english,'persian':persian})
    print("New Words are successfully ")
def save_and_exit():
    file=open('dictionary.txt','w')
    for i in range(len(words)):
        row=words[i]['english'] + ',' + words[i]['persian'] + '\n'
        file.write(row)
    print('save words to dictionary.txt')
    file.close()
    exit()
def search_English_to_Persian_translation():
    wordList=[]
    list=[]
    sentences=input('enter english sentences: ')
    sentence=sentences.split('.')
    for s in range(len(sentence)):
        wordList.append(sentence[s].split(' '))
    for i in range(len(wordList)):
        for j in range(len(wordList[i])):
            for w in words:
                if wordList[i][j]==w['english']:
                    list.append((w['persian']))
                    break
    print(list)
def search_Persian_to_English_translation():
    wordList=[]
    list=[]
    sentences=input('enter persian sentences: ')
    sentence=sentences.split('.')
    for s in range(len(sentence)):
        wordList.append(sentence[s].split(' '))
    for i in range(len(wordList)):
        for j in range(len(wordList[i])):
            for w in words:
                if wordList[i][j]==w['persian']:
                    list.append(w['english'])
                    break
    print(list)
load()
while True:
        show_menu()
        choice=int(input('Please select from menu: '))
        if choice==1:
                add_words()
        elif choice==2:
                search_English_to_Persian_translation()
        elif choice==3:
                search_Persian_to_English_translation()
        elif choice==4:
                save_and_exit()