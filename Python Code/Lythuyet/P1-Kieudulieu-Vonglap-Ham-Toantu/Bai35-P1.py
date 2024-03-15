#BAI 35: SO THUAN NGHICH - PALINDROME

"""
- Một số được gọi là "thuận nghịch" nếu bạn có thể đọc chúng từ trái sang phải hoặc từ phải sang trái mà vẫn thu được cùng một giá trị. 
Điều này có nghĩa là thứ tự của các chữ số không ảnh hưởng đến giá trị của số đó. 
Để đạt được tính thuận nghịch, số phải có dạng đối xứng hoặc có một cấu trúc đặc biệt.

- Ví dụ, số nguyên dương 121 là một số thuận nghịch.
Nếu bạn đọc nó từ trái sang phải hoặc từ phải sang trái, bạn vẫn thu được 121.
Tương tự, số 1331 cũng là một số thuận nghịch vì nó vẫn giữ nguyên khi bạn đảo ngược các chữ số.
"""

def palindrome(n):
    temp=n
    rev=0
    while(n!=0):
        rev=rev*10+n%10
        n//=10

    return temp==rev      

if __name__=="__main__":
    n=int(input())
    if(palindrome(n)):
        print("YES")
    else:
        print("NO")