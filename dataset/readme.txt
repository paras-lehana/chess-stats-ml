This contains the datasets used for the project. Various parameters are briefly described further in the text. The descriptions for the files are as follows:

• Example.si4 - Database of 1,27,819 games from ScidBase.
• final.pgn - The PGN file exported after annotating evaluation scores for first 10,000 games in the Example.si4 database. Please note that this contains the game data of all the games in the inital file but just few of them are annotated. 
• 10kprocess3.txt - The text file generated from final.pgn. Text-processing is done for making this file easy to be processed by python. For example, by adding carriage return following a line feed to the end of each line, making each line containing no more than one half-move, appending evaluation score in the same line as of the move and removing invalid blank lines finally. The games after the 10,000th one are then deleted.
• small_move.csv - The manually created CSV dataset for 1002 moves from 183 games. Move details mention only the current move while winning scores are calculated in the respect with the parent database.
• big_all_x.csv - Where x = 10, 15, 20 and denotes the limit on the number of half-moves considered in each game. The winning score here is the proportion of games won by white and is calculated from the 10,000 games database used in this dataset. The number of rows for 10, 15 and 20-moves datasets are 1,09,152, 1,58,615 and 2,16,316 respectively.



Some of the fundamental attributes existing in anyone of the datasets are briefly described as:

• Move number: The number denotes the current sequence number of the played move by one side. When we say that we are using a 20-move dataset or that the engine is running on depth 20, we mean about the total number of half-moves or ply whereas the attribute in the dataset denotes the move sequence corresponding to a side. Note that the PGN format also doesn‟t mention half-moves. Move classification is also used in another column that appends letter 'a' for white's ply and 'b' for black's ply to the numerical move number.
• Move details: It denotes the move details with the move number in algebraic notation. The move detail can be only about the current move or can contain previous move sequences too. For the former one, we implement the Markov Decision process [37] i.e. the algorithm only considers about the current move and not the past ones. Although, this is a very general approach and can be a conflicting attribute for some cases, it is still the most optimal one. The latter one considers all of the previous moves that made it to the current move which grows sequentially with the move numbers since all of the previous moves are appended before the current move. This approach finds exact move sequences and is a more specific case for the evaluations but requires more space and time for computations.
• ECO: Chess Opening classification by Encyclopedia of Chess. The classification is based on the moves
played that correspond to one of the openings defined in the ECO.
• ELO: FIDE Elo rating of the player on one side according to the move classification.
• Result: The game outcome – 0 for black win, 1 for white win and 0.5 for draw.
• Evaluation score: Pre-computed move evaluation score by Stockfish engine running on depth 17.
• Winning score: The winning score is calculated by calculating the weighted sum of the number of games won and/or draw by playing a move divided by the total number of moves in consideration. The total number of moves can be either accounted from the whole database of ScidBase or only the considered subset.
