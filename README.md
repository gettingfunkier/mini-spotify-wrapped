# Mini Spotify Wrapped
FPP Report – Software Engineering G430

## What is it? A spotify wrapped alternative
The program can read a file, which should contain information about songs the user listens to. With
which information, it can: read out the user’s most played song; most played artist (across all the
artist’s songs); and most played genre (and print all the user’s artists from said genre), as well as
define the user’s musical taste (if they listen to similar or distinct genres of music).

## What motivated me to choose this project?
I have a passion for music and aspire to be a producer/artist myself. Software Engineering, and by
extension CS, will give me the freedom I’ll need to pursue such a career. And since I’m also an avid
critical listener, who recently switched from Spotify to Apple Music, and by consequence lost the
Spotify Wrapped... I decided to simply make my own.

## Brief user instructions
1. There needs to be a separate text file, called “songs.txt” and in the same directory as the python
file.
2. The input requirements may vary. When choosing an action, there will be a number before the
action (e.g. 1 – show favourites), and only that number must be typed out, but there is an instance
of yes/no, that will be indicated by a “(y/n)” and should only receive a “y” or a “n”. (it can receive
anything else, but the program might not react very well, try at your own risk!)
3. The genre for any song in the file must be one of any in the following list: Classical, Folk, Country,
Reggae, Blues, Jazz, R&B/Soul, Funk, Rock, Metal, Electronic, Hip-Hop/Rap, Pop.

## How does it work?
The project has two main functions: showing statistics and defining the user’s music taste. And will
firstly prompt to pick one of the two. If they choose to show statistics, it will ask for which specific
information they want, these being either their favourite song, artist or genre. For the favourite
song, it prints the name of the song with the most plays. For the favourite artist, it counts all plays
any individual artist has across all their songs and prints the name of highest. For the genre it does
the same as for the artist, but it can also print, if prompted, all the artists that belong to the user’s
favourite genre. Keep in mind that if the user doesn’t want that extra information, the program may
get upset. If an input by the user isn’t any of the prompts, the program will say so with “invalid
request”. If they choose to define their music taste, the program will have ready a dictionary that
assigns every possible genre (out of the ones listed) an index value. With this, the program will read
the file, determine which are the user’s top two genres. With this information, it will calculate how
similar the two genres are based on the difference of their indexes. The smaller the difference, the
more defined the taste. The bigger the difference, the more diverse the taste.

## Data structures
All lists and dictionaries’ purposes are commented in the python file.
For the number of plays, the program works with integers, while for every other data gathered from
the file, it works with strings.
Program starts with a split by two if statements. Either showing statistics or defining taste.
Inside showing statistics, a while loop keeps the program running until user decides to quit.
Chosen action has a corresponding if statement, where the results are given.
If the user inputs something that’s invalid (e.g. ”sjd5hs.6,ajhkd”), the program simply runs the loop
again, asking for another input.
In the defining taste section, a dictionary with all indexes for the accepted genres is created, to
calculate the overall index for each user.

## Interesting / tricky / subtle aspects of the code meriting further explanation
1. The file “songs.txt” must follow this layout:
Song name;Artist;Album;Genre;Release year;# of plays
…
Example: (there’s an example file on the repository)
Outro;Vulfpeck;Vollmilch;Funk;2012;58
can you please take tim out?;Woody Goss;High Loon!;R&B/Soul;2023;60
I'm Still Standing;Elton John;2Low4Zero;Rock;1985;38

3. The one and only aspect of the code that wasn’t covered in lectures, but required for the program
to function, is the presence of the math library. Its only use is, in line 229, to calculate the absolute
value of the difference of the two genre indexes. This was put in place because the order in which
genres appear is defined by the user themselves, and therefore this number can come out positive
or negative depending on if they write their higher indexed genres first or not. (eg. For two genres
Jazz and Classical, if Classical appears in the file first, the number will be negative, but if Jazz appears
first the number will be positive, but both their absolute values are the same, and that’s the value
we need.)

4. There is one circumstance under which the defining taste section of the program will not work.
This happens when the file only contains two songs, from different genres, and with the same
number of plays. The explanation for this is, when calculating the second top genre, because the
number of plays will be the same, it will simply replace the current genre with the previous, thus
ending up with two identical top genres. However, I could not figure out a way to solve this.

## Particular challenges I overcame
1. To accurately distinguish between different genres, based on how similar they might be, involves
a lot of variables, and it’s practically impossible to get an accurate answer every single time. To
overcome this, I split them into categories, determined by how long ago they came by. This allowed
me to sort of distinguish between the different waves of music culture, particularly in the last
century. The values are carefully given, such that similar genres can still be considered as such, but
not in the way that if a is similar to b and b is similar to c, then a is similar to c, because this isn’t
always the case.
2. Given that the program involves a tree of actions, where one choice can lead to another choice,
and so on, it was particularly interesting to figure out the ideal structure for the file. Especially,
taking into account that I wanted the program to keep running until the user decides to quit.
3. I noticed that after two invalid inputs in the “genre artists” section, the program would simply
backtrack a few loops. Thus, I decided to go along with it, and give it a bit of personality.

## Acknowledgements

This was my first coding project, built during the first semester of Year 1 Software Engineering for the course Computing Science 1CT. It represents the beginning of my journey into programming, where I combined my passion for music with the skills I was just starting to learn. The project achieved full marks, and I’m keeping it here unchanged as an archive of my early work. I won’t be updating or maintaining it beyond this version.

Made by [gettingfunkier](https://github.com/gettingfunkier) . 2024 🤍
