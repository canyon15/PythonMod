"""
CSE310 Python Workshop - Example 3

This example will explore classes and inheritance
in Python.
"""

class Job:

    def __init__(self, title, work):
        """
        Constructor for a Job object
        """
        self.title = title
        self.work = work
        pass

    def __str__(self):
        """
        Used to print out the object.  Returns a 
        string representation of the object.
        """
        text = "{} : {} work".format(self.title, self.work)
        return text

    def do_work(self, ammount):
        """
        Do work (don't let it go negative)
        """
        if self.work < ammount:
            self.work = 0
        else:
            self.work -= ammount

    def add_work(self, ammount):
        """
        Increase the work load in the Job
        """
        self.work += ammount
        pass



def print_jobs(job_list):
    for job in job_list:
        print("{}\t".format(job),end="")
    print()

def main():
    job1 = Job("job1", 20)
    job2 = Job("job2", 10)
    job3 = Job("job3", 15)

    jobs = [job1, job2, job3]
    print_jobs(jobs)

    # Do 5 units of work for all jobs
    for job in jobs:
        job.do_work(8)
    print_jobs(jobs)

    # Do 4 units of work for all jobs
    for job in jobs:
        job.do_work(4)
    print_jobs(jobs)

    # Add 10 units of work to all jobs
    for job in jobs:
        job.add_work(10)
    print_jobs(jobs)

if __name__ == "__main__":
    main()