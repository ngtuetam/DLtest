'''
Prob: https://www.hackerrank.com/challenges/find-a-string/problem?isFullScreen=true
'''
def count_substring(string, sub_string):
    l = len(string)
    l_s = len(sub_string)
    cnt = 0
    for i in range(l-2):
        if string[i:i+l_s] == sub_string:
            cnt += 1
    return cnt        

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)