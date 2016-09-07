

def song(num_beers):
   if num_beers >= 1:
        print(num_beers),
        print(" bottles of beer on the wall,"),
        print(num_beers),
        print( " bottles of beer.")
        print("Take one down and pass it around,"),
        if num_beers == 1:
            print(" no more bottles of beer on the wall.\n")
            song(num_beers-1)
        else:
            print(num_beers-1),
            print(" bottles of beer on the wall.\n")
            song(num_beers-1)
   else:
        print('No more bottles of beer on the wall, no more bottles of beer.')
        print("Go to the store and buy some more, 99 bottles of beer on the wall!\n")


num_beers = 99
song(num_beers)

print("Now our song is done, let's drink!")
