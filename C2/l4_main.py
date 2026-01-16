def get_follower_prediction(follower_count, influencer_type, num_months):
    multiplier = 2

    if influencer_type == "fitness":
        multiplier = 4
    elif influencer_type == "cosmetic":
        multiplier = 3

    return follower_count * multiplier ** num_months
