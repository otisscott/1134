def two_sum(srt_lst, target):
    for num in range(len(srt_lst)//2):
        for num2 in range(len(srt_lst)//2, len(srt_lst)):
            if srt_lst[num] + srt_lst[num2] == target:
                return (num, num2)
    return None
