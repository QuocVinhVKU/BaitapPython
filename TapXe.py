# Cô giáo trường tiểu học X đang dạy n học sinh tập xe đạp, các học sinh được đánh số từ 1 tới n, học sinh thứ j có trọng lượng là aj. Có một xe đạp duy nhất với tải trọng là m, hai học sinh chỉ có thể cùng lên xe nếu tổng trọng lượng của hai học sinh không vượt quá m.

# Cô giáo tự hỏi có bao nhiêu cách chọn hai học sinh khác nhau cho cùng lên xe, sau nhiều giờ tính toán không có kết quả, cô quyết định hỏi các chuyên gia lập trình giải bài toán Counting Student Pairs (CSP)

# Yêu cầu: Đếm số cặp chỉ số i,j trong đó i<j và ai+aj≤m
# Dữ liệu vào

# Dòng 1 chứa hai số nguyên dương n,m (m≤106)
# Dòng 2 chứa n số nguyên dương a1,a2,…an (∀i:ai≤106)
# Kết quả

# Ghi một số nguyên duy nhất là đáp số
a = input().split()
n = input().split()
dem = 0
for i in range(len(n)):
    for j in range(len(n)):
        if(i<j and (int(n[i])+int(n[j]))<=(int(a[1]))):
            dem +=1
print(dem)
