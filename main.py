# python3

def parallel_processing(n, m, data):
    output = []
    thread_work = []
    for i in range(n):
        thread_work.append(0)
    
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    time = 0
    job = 0
    while True:
        for i in range(n):
            if thread_work[i] == 0:
                thread_work[i] = int(data[job]) - 1
                output.append((i, time))
                job = job + 1
            else:
                thread_work[i] = thread_work[i] - 1
        if job == m:
            break
        time = time + 1
    return output

def main():

    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    string = input().split()
    n = int(string[0])
    m = int(string[1])

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
        data = input().split()
    else:
        return
    # TODO: create the function
    assert len(data) == m
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    for i, j in result:
        print(i, j)


if __name__ == "__main__":
    main()
