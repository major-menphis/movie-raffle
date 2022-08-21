from random import choices

def raffle():
    try:
        movie_list = []
        txt = './movies.txt'
        f = open(txt, 'r')
        for line in f.readlines():
            name = line.replace('\n', '')
            movie_list.append(name)
            print(f'Add to raffle: {name}')
        f.close
        return print(f'Movie raffled: {choices(movie_list)[0]}')
    except:
        print(f'File {txt.replace("./", "")} not found.')

raffle()
