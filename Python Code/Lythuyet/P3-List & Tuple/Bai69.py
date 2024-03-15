#BAI 69: SANG SO NGUYEN TO ERATOSTHENES

from math import*

"""
- Thông thường ta hay sàng số nguyên tố bằng việc viết hàm rồi duyệt -> Độ phúc tạp O(N * can(N))
để tối ưu và giảm độ phúc tạp ta dùng -> Thuật toán Eratosthenes -> Độ phức tạp O(N * log(logN))
"""
#B1: Coi tất cả các số từ 0 -> N là số nguyên tố
#B2: Bội của một số nguyên tố sẽ không phải là số nguyên tố

prime=[True]*1000001

def sieve():
    prime[0]=prime[1]=False

    for i in range(2,int(sqrt(1000001))+1):
        #Kiem tra neu i laf snt => loai boi cua i
        if prime[i]==True:
          for j in range(i**2,1000001,i):
              prime[j]=False


if __name__=="__main__":
    sieve()
    for i in range(100):
        if prime[i]:
            print(i,end=" ")