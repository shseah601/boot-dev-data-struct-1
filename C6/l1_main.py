def count_marketers(job_titles: list[str]):
    count = 0
    for job_title in job_titles:
        if job_title.lower() == "marketer":
            count += 1

    return count
