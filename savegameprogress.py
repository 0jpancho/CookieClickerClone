import shelve

shelfFile = shelve.open('saved_game_filename')

mainBoard = shelfFile ['mainBoardVariable']

playerTile = shelfFile ['playerTileVariable']

computerTile = shelfFile ['computerTileVariable']

showHints = shelfFile ['showHintsVariable']

shelfFile.close()
