import math

# splitting between both the program's functions
split = input("Welcome to Spotify Wrapped but for computer science! To start, choose a prompt:\n1 - show statistics\n2 - define my taste\nInput here: ")

# choosing to show statistics
if split == "1":
    file = open("songs.txt")
    line = file.readline()

    # setting up counters that will be used later  
    counter_song = 0
    counter_artist = 0
    counter_genre = 0
    counter_artists_count = 0

    # deciding on an end goal for the user
    print("Great choice, what do you want to know?\n1 - my favourite song\n2 - my favourite artist\n3 - my favourite genre\n4 - quit")
    goal = input("Input here: ")

    # setting up all lists and dictionaries that will be used
    artists = {} # information about each artist's total plays
    artists_list = [] # all artists in the file
    genres = {} # information about each genre's total plays
    genres_list = [] # all genres in the file
    genres_Artists = {} # all artists in each individual genre

    while goal != "4": # while user doesn't quit
        while line != "": # reads through all songs
            # DEFINING VARIABLES
            song_Name = line.split(";")[0]
            song_Artist = line.split(";")[1]
            song_Album = line.split(";")[2]
            song_Genre = line.split(";")[3]
            song_Year = int(line.split(";")[4])
            song_Plays = int(line.split(";")[5])

            # TOP SONG INFO
            if song_Plays > counter_song:
                counter_song = song_Plays
                top_Song = song_Name
                # if a song read has more plays than the top song until then, those plays become the new max, and its name the top song
                # by the end of the file, the highest played song in the file will have its name and plays defined in the program

            # TOP ARTIST INFO
            if song_Artist in artists:
                artists[song_Artist] = artists[song_Artist] + song_Plays
                # if an artist has already been read before, it's previous plays will be added to the plays that were now read, becoming it's total plays
            else:
                artists[song_Artist] = song_Plays
                # if an artist hasn't been read before, it's total plays are the plays currently read
            
            if song_Artist not in artists_list:
                artists_list.append(song_Artist)
                # adds all artists in the file to a list

            for i in range(len(artists_list)):
                if artists[artists_list[i]] > counter_artist: # if an artist's total plays is bigger than the counter..
                    counter_artist = artists[artists_list[i]] # ..those plays become the new counter (highest plays so far)
                    top_Artist = artists_list[i] # ..and that artist becomes the most played artist
                    # goes through every artist's total plays, and will define the highest one

            # TOP GENRE INFO (similar to artist info)
            if song_Genre in genres:
                genres[song_Genre] = genres[song_Genre] + song_Plays
                # similar to before, if a genre has already been read before, it's previous plays will be added to the plays that were now read, becoming it's total plays
            else:
                genres[song_Genre] = song_Plays
                # if a genre hasn't been read before, it's total plays are the plays currently read
            
            if song_Genre not in genres_list:
                genres_list.append(song_Genre)
                # adds all genres in the file to a list

            for i in range(len(genres_list)): 
                if genres[genres_list[i]] > counter_genre: # if an genre's total plays is bigger than the counter..
                    counter_genre = genres[genres_list[i]] # ..those plays become the new counter (highest plays so far)
                    top_Genre = genres_list[i] # ..and that genre becomes the most played genre
                    # goes through every genre's total plays, and will define the highest one
                
            if song_Genre not in genres_Artists: # if the song artist read is the first of a particular genre..
                genres_Artists[song_Genre] = song_Artist # ..that artist becomes a value for the key of that genre (as string)

            elif song_Genre in genres_Artists and song_Artist not in genres_Artists[song_Genre]: # if the song artist read is NOT the first of a particular genre..
                genres_Artists[song_Genre] = genres_Artists[song_Genre] + ", " + song_Artist # ..that artist is added to the string for the key of that genre
                

            line = file.readline()


        if goal == "1": # favourite song
            print("Your favourite song, " + top_Song + ", was played " + str(counter_song) + " times.") # prints the top song's name and number of plays, in a tidy string

            goal = input("Input here: ") # always asks for another input after action


        if goal == "2": # favourite artist
            print("Your favourite artist was " + top_Artist + ", with " + str(counter_artist) + " plays.") # prints the top artist's name and number of plays across all its songs, in a tidy string

            goal = input("Input here: ") # always asks for another input after action


        if goal == "3": # favourite genre
            artists_String = str(genres_Artists[top_Genre])
            artists_NL = artists_String.split(", ")

            for i in range(len(artists_NL)):
                counter_artists_count = counter_artists_count + 1

            print("Your favourite genre was " + top_Genre + ", with a total of " + str(counter_artists_count) + " artists.")
            genre_goal = input("Do you want to know who your " + top_Genre + " artists were? (y/n): ")
    
            counter_artists_count = 0 #RESETS THE COUNTER  

            # here it can display, if prompted y, all the artists from the user's top genre
            if genre_goal == "y": # y, displays
                genre_artists_list = str(genres_Artists[top_Genre])[2:-2]
                genre_artists_string = str(genre_artists_list.split("', '"))

                print("Your favourite " + top_Genre + " artists were:")
                print(genres_Artists[top_Genre])
                    
                goal = input("Input here: ")
            elif genre_goal == "n": # n, gets disappointed
                print("Wow, ok.. this is awkward. ")
                goal = input("Input here (if you want I guess): ")
            else: # anything else, invalid input
                print("It's a y/n question, silly.")
                genre_goal = input("Input here (y/n): ") 

                if genre_goal == "y": # after one invalid input, y (forgives)
                    genre_artists_list = str(genres_Artists[top_Genre])[2:-2]
                    genre_artists_string = str(genre_artists_list.split("', '"))

                    print("Your favourite " + top_Genre + " artists were:")
                    print(genres_Artists[top_Genre])

                    goal = input("Input here: ")
                elif genre_goal == "n": # after one invalid input (still disappointed)
                    print("Wow, ok.. this is awkward. ")
                    goal = input("Input here (if you want I guess): ")
                else: # two invalid inputs (the program gets upset)
                    print("Stop breaking my brain! >:( Let's backtrack:")


        else: # invalid request on choosing action
            print("Invalid request!")
            goal = input("Input here: ")

# choosing to define user's taste
if split == "2":
    file = open("songs.txt")
    line = file.readline()

    # setting up counters
    counter_song = 0
    counter_artist = 0
    counter_genre_first = 0
    counter_genre_second = 0
    counter_artists_count = 0
    value_box = 0
    first_index = 0
    second_index = 0
    index_score = 0

    # setting up necessary lists and dictionaries (same as before)
    artists = {}
    artists_list = []
    genres = {}
    genres_list = []
    genres_Artists = {}
    genres_index = {} # except for this one, which will contain the indexes for all the genres 

    while line != "":
        # DEFINING VARIABLES
        song_Name = line.split(";")[0]
        song_Artist = line.split(";")[1]
        song_Album = line.split(";")[2]
        song_Genre = line.split(";")[3]
        song_Year = int(line.split(";")[4])
        song_Plays = int(line.split(";")[5])

        # dictionary of genres with values as number of plays per genre
        if song_Genre in genres:
            genres[song_Genre] = genres[song_Genre] + song_Plays
        else:
            genres[song_Genre] = song_Plays
        
        # list of all genres in the file
        if song_Genre not in genres_list:
            genres_list.append(song_Genre)
            

        line = file.readline()

    # gets the most played genre
    for i in range(len(genres_list)):
        if genres[genres_list[i]] > counter_genre_first: # if the one read is the biggest..
            counter_genre_first = genres[genres_list[i]] # ..it's replaced as such
            first_top_Genre = genres_list[i]

    # gets the second most played genre, by ignoring the value of the first most played genre
    for i in range(len(genres_list)):
        if genres[genres_list[i]] > counter_genre_second: # if the one read is bigger than the current biggest..
            counter_genre_second = genres[genres_list[i]] # ..it gets replaced by the new biggest
            second_top_Genre = genres_list[i]

        if counter_genre_second == counter_genre_first: # if the one read is equal to the already top song..
                counter_genre_second = value_box # gets the value box (explained below)
                second_top_Genre = genres_list[i-1] # skips the top genre

        value_box = counter_genre_second # keeps track of the previous value, and replaces the current one when it is equal to the most played

    # indexes for all the genres 
    genres_index = {
        'Classical':1,
        'Folk':14,
        'Country':29,'Reggae':35,'Blues':40,
        'Jazz':50,'R&B/Soul':59,'Funk':59,'Rock':70,'Metal':80,
        'Electronic':110,'Hip-Hop/Rap':130,'Pop':131
    }

    # calculates the overall index score 
    first_index = genres_index[first_top_Genre]
    second_index = genres_index[second_top_Genre]
    index_score = abs(first_index - second_index)

    # defines the taste of the user based on the index score
    if index_score <= 10:
        print("You have a very defined taste, listening to both " + first_top_Genre + " and " + second_top_Genre + ", two very similar genres!")

    elif 10 < index_score <= 20:
        print("Your taste is somewhat defined, listening to both " + first_top_Genre + " and " + second_top_Genre + ", two resembling genres.")

    elif 20 < index_score <= 30:
        print("Your taste is quite diverse, listening to both " + first_top_Genre + " and " + second_top_Genre + ", two distinctive genres.")

    elif 30 < index_score:
        print("Your taste is extremely diverse! You listen to both " + first_top_Genre + " and " + second_top_Genre + ", two polar opposite genres.")