def is_ok(arg):
    pass

def meguru_bisect(ng, ok):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

def bisect(key, L):
    left = 0
    right = len(L)-1
    while right - left >= 0:
        mid = left + (right - left) // 2
        if L[mid] == key:
            return mid
        if L[mid] > key:
            right = mid - 1
        else:
            left = mid +1
    return -1