
# UnifyId challenge

Generating 128*128 RDB image using Random.org

### Dependencies

python3
PIL

### Code

RANDOM.ORG API provides with random numbers in the mentioned range in our case we need (0,255) for RGB values.
The maximum number of random numbers from one API call is 10000 hence I calculated the for loop range in get_rgb method accordingly to get total required pixels i.e. 128*128*3.

Tuple is created using 3 consecutive random numbers from total pixles and appended to a list. This list is then return which generates the bitmap image.

