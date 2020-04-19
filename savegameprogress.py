import shelve

shelfFile = shelve.open('saved_game_filename')

shelfFile.close()
