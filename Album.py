def make_album(artistname, albumtitle , nofsongs = None):
    if nofsongs :
        album = {'a_name' : artistname , 'a_title' : albumtitle}
        album['n_songs'] = nofsongs
    else:
        album = {'a_name': artistname, 'a_title': albumtitle}
    return album
print(make_album('ahmed','wara el shasha'))
print(make_album('azab','elela de'))
print(make_album('mohamed','3as3os qaser el genah'))
print(make_album('essam','qset hob', 22))