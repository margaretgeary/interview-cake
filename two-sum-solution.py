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


# See if there's a matching_second_movie_length we've seen already (stored in our 
# movie_lengths_seen set) that is equal to flight_length - first_movie_length. 
# If there is, we short-circuit and return True.
# Keep our movie_lengths_seen set up to date by throwing in the current 
# first_movie_length.

def two_sum_solution(nums):
    complementary_nums = set()

    for num in nums:
        complement = 2020-num
        if num in complementary_nums:
            return True
        else:
            complementary_nums.add(complement)

    return False