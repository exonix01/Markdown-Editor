def header(x):
    while True:
        level = int(input('Level:'))
        if level < 1 or level > 6:
            print('The level should be within the range of 1 to 6')
            continue
        else:
            break
    text = input('Text:')
    head = level * '#'
    text = x + f'{head} {text}\n'
    print(text)
    return text

def bold(x):
    text = input('Text:')
    text = x + f'**{text}**'
    print(text)
    return text

def italic(x):
    text = input('Text:')
    text = x + f'*{text}*'
    print(text)
    return text

def plain(x):
    text = x + input('Text:')
    print(text)
    return text

def link(x):
    label = input('Label:')
    url = input('URL:')
    text = x + f'[{label}]({url})'
    print(text)
    return text

def inline_code(x):
    text = input('Text:')
    text = x + f'`{text}`'
    print(text)
    return text

def new_line(x):
    text = x + '\n'
    print(text)
    return text

def list_create(x, type_):
    while True:
        NO_rows = int(input('Number of rows:'))
        list_ = []
        if NO_rows < 1:
            print('The number of rows should be greater than zero')
        else:
            break
    for i in range(1, NO_rows + 1):
        t = input(f'Row #{i}')
        list_.append(t)
    if type_ == 'unordered-list':
        result = list(map(lambda x: '* ' + str(x) + '\n', list_))
    else:
        n = range(1, NO_rows + 1)
        result = list(map(lambda x, y: str(y) + '. ' + str(x) + '\n', list_, n))
    text = x + ''.join(result)
    print(text)
    return text

lst = ['plain', 'bold', 'italic', 'header', 'link', 'inline-code', 'ordered-list', 'unordered-list', 'new-line']
txt = ''
while True:
    answer = input('Choose a formatter: ')
    if answer == '!help':
        print('Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line')
        print('Special commands: !help !done')
        continue
    elif answer == '!done':
        output = open('output.md', 'w')
        output.writelines(txt)
        output.close()
        break
    else:
        if not lst.count(answer):
            print('Unknown formatting type or command')
            continue

    if answer == 'plain':
        txt = plain(txt)
    elif answer == 'header':
        txt = header(txt)
    elif answer == 'bold':
        txt = bold(txt)
    elif answer == 'italic':
        txt = italic(txt)
    elif answer == 'link':
        txt = link(txt)
    elif answer == 'inline-code':
        txt = inline_code(txt)
    elif answer == 'new-line':
        txt = new_line(txt)
    else:
        txt = list_create(txt, answer)
