def match_flight_length_and_movie_lengths(flight_length, movie_lengths):

    movie_lengths_equaling_flight_length = set()

    for movie_length in movie_lengths:

        complementary_movie_length = flight_length - movie_length

        if movie_length in movie_lengths_equaling_flight_length:
            return True

        else:
            movie_lengths_equaling_flight_length.add(complementary_movie_length)
    
    return False


    
print(match_flight_length_and_movie_lengths(60, [50, 200, 100]))

