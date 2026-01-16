def get_avg_brand_followers(all_handles, brand_name):
    total_followers = 0
    for handles in all_handles:
        for follower in handles:
            if brand_name in follower:
                total_followers += 1
    return total_followers / len(all_handles)

