arn1 = "arn:aws:iam::1578:user/pro/film1"
arn2 = "arn:aws:iam::92945500:user/pro/film2"
arn3 = "arn:aws:iam::5534551:user/pro/film3"

# splitted_arn1 = arn1.split(":")
# print(splitted_arn1[4])

def get_account_id(arn: str) -> str:
    """"
    This function is to take an arn and return its account_id
    """
    splitted_arn = arn.split(":")
    return splitted_arn[4]

account_id1 = get_account_id(arn1)
print(f"account_id1 is {account_id1}")

account_id2 = get_account_id(arn2)
print(f"account_id2 is {account_id2}")

account_id3 = get_account_id(arn3)
print(f"account_id3 is {account_id3}")




def get_movie_name(arn: str) -> str:
    """"
    This function is to take an arn and return its movie_name
    """
    splitted_arn = arn.split(":")  # ['arn', 'aws', 'iam', '', '1578', 'user/pro/film1']
    movie_url = splitted_arn[5]  # 'user/pro/film1'
    splitted_movie_url = movie_url.split("/")  # ['user', 'pro', 'film1']
    movie_name = splitted_movie_url[2]  # 'film1'
    return movie_name

movie1 = get_movie_name(arn=arn1)
print()
    




