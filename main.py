import cv2 as cv

image_arr = cv.imread('./photos/anime.png')

gray = cv.cvtColor(image_arr,cv.COLOR_BGR2GRAY)

# Tính độ nổi khối Scharr (Scharr Gradient theo tùy chọn ksize = -1)
gX = cv.Sobel(gray,ddepth=cv.CV_32F,dx=1,dy=0,ksize=-1)
gY = cv.Sobel(gray,ddepth=cv.CV_32F,dx=0,dy=1,ksize=-1)

# Chuyển từ IEE754 8 bit float sang int
gX = cv.convertScaleAbs(gX)
gY = cv.convertScaleAbs(gY)

# trộn 2 kết quả với nhau
result = cv.addWeighted(gX,0.5,gY,0.5,0)
cv.imshow("Win",result)
cv.waitKey(0)
# print(gX)

