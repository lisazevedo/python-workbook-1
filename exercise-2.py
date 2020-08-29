song = [ "On the first day of Christmas", "my true love sent to me:", "A partridge in a pear tree.", "On the second day of Christmas", "my true love sent to me:", "Two turtle doves,", "And a partridge in a pear tree.", "On the third day of Christmas", "my true love sent to me:", "Three French hens,", "Two turtle doves,", "And a partridge in a pear tree." ]
def print_song(verse): print(song[verse])
def main(): [print_song(i) for i in range(12)]
if __name__ == "__main__": main()