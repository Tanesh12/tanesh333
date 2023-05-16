def solution(A):
    total_sum = sum(A)
    left_sum = 0

    for i in range(len(A)):
        total_sum -= A[i]  
        if left_sum == total_sum:
            return i
        left_sum += A[i]  

    return 1  
