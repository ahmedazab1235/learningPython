def make_album(artistname, albumtitle , nofsongs = None):
    if nofsongs :
        album = {'a_name' : artistname , 'a_title' : albumtitle}
        album['n_songs'] = nofsongs
    else:
        album = {'a_name': artistname, 'a_title': albumtitle}
    return album

active = True

while active :
    a_name = input("enter artist name\nenter 'q' if you want to en prog\n")
    if a_name == 'q':
        break
    a_title = input("enter alboum title\nenter 'q' if you want to en prog\n")
    if a_title == 'q':
        break
    print(make_album(a_name,a_title))