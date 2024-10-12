def maximalSquare(matrix):
    if not matrix or not matrix[0]:
        return 0, []
    rows = len(matrix)
    cols = len(matrix[0])
    dp = [[0] * cols for _ in range(rows)]
    max_side = 0
    squares = []  # Lưu các hình vuông lớn nhất
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                if i == 0 or j == 0:
                    dp[i][j] = 1  # Đối với hàng đầu tiên và cột đầu tiên
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                
                if dp[i][j] > max_side:
                    max_side = dp[i][j]
                    squares = [((i - max_side + 1, j - max_side + 1), (i, j))]  # Xóa danh sách cũ và lưu hình vuông mới
                elif dp[i][j] == max_side:
                    squares.append(((i - max_side + 1, j - max_side + 1), (i, j)))  # Thêm hình vuông cùng kích thước
    return max_side ** 2, squares


def maximalRectangle(matrix):
    if not matrix:
        return 0, []
    n = len(matrix[0])
    heights = [0] * n
    max_area = 0
    rectangles = []  # Danh sách lưu tất cả các hình chữ nhật có diện tích lớn nhất
    for i in range(len(matrix)):
        for j in range(n):
            heights[j] = heights[j] + 1 if matrix[i][j] == 1 else 0
        
        area, rects = largestRectangleArea(heights, i)
        if area > max_area:
            max_area = area
            rectangles = rects  # Cập nhật danh sách các hình chữ nhật lớn nhất
        elif area == max_area:
            rectangles.extend(rects)  # Thêm các hình chữ nhật có diện tích bằng max_area
    return max_area, rectangles

def largestRectangleArea(heights, row):
    stack = []
    max_area = 0
    rectangles = []  # Danh sách lưu các hình chữ nhật có cùng diện tích lớn nhất
    heights.append(0)  # Thêm phần tử 0 để xử lý hết stack
    for i in range(len(heights)):
        while stack and heights[i] < heights[stack[-1]]:
            h = heights[stack.pop()]
            w = i if not stack else i - stack[-1] - 1
            area = h * w
            top_left = (row - h + 1, stack[-1] + 1 if stack else 0)
            bottom_right = (row, i - 1)

            if area > max_area:
                max_area = area
                rectangles = [(top_left, bottom_right)]  # Reset và lưu hình chữ nhật mới
            elif area == max_area:
                rectangles.append((top_left, bottom_right))  # Thêm hình chữ nhật có diện tích bằng max_area
        stack.append(i)
    heights.pop()  # Bỏ phần tử 0 đã thêm
    return max_area, rectangles

matrix = [
    [1, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 0, 1, 1, 1, 1]
]
area, squares = maximalSquare(matrix)
print(f"OUTPUT_1 = {area}")
for square in squares:
    print(f"[[{square[0][1]+1}, {square[0][0]+1}], [{square[1][1]+1}, {square[1][0]+1}]]")
area, rectangles = maximalRectangle(matrix)
print(f"OUTPUT_2 = {area}")
for rect in rectangles:
    print(f"[[{rect[0][1]+1}, {rect[0][0]+1}], [{rect[1][1]+1}, {rect[1][0]+1}]]")
