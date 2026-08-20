def job_sequencing(jobs):
    """
    jobs: list of tuples (job_id, deadline, profit)
    returns: (total_profit, sequence of job_ids scheduled)
    """
    # Step 1: sort by profit, descending
    jobs = sorted(jobs, key=lambda x: x[2], reverse=True)

    max_deadline = max(job[1] for job in jobs)
    slots = [None] * (max_deadline + 1)  # index 0 unused

    total_profit = 0
    sequence = []

    for job_id, deadline, profit in jobs:
        # try to place job in the latest free slot <= its deadline
        for t in range(deadline, 0, -1):
            if slots[t] is None:
                slots[t] = job_id
                total_profit += profit
                sequence.append(job_id)
                break

    return total_profit, sequence


# Example usage
jobs = [
    ("J1", 4, 20),
    ("J2", 1, 10),
    ("J3", 1, 40),
    ("J4", 1, 30),
]

profit, seq = job_sequencing(jobs)
print(f"Total profit: {profit}")
print(f"Job sequence: {seq}")