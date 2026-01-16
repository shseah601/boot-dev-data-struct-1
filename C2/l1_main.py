def get_estimated_spread(audiences_followers):
    if len(audiences_followers) == 0:
        return 0

    total_audiences_followers = sum(audiences_followers)
    total_followers = len(audiences_followers)

    avg = total_audiences_followers / total_followers

    return avg * (total_followers ** 1.2)

