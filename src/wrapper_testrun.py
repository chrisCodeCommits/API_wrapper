

from __future__ import print_function
from tmdbwrapper import TV





popular = TV.popular()

for number, show in enumerate(popular['results'], start=1):

        print(

            f"{num   = number}. "\
            f"{name  = show['name']} - "\
            f"{pop   = show['popularity']}"

            )
