def last_work_experience(work_experiences: list[str]):
    if len(work_experiences) == 0:
        return None

    return work_experiences.pop()
