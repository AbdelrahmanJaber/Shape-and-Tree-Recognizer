
import numpy as np
import cv2 as cv

# this function is used to print the word circle above the circles shape
def circleFun(cX , cY , t):
    cv.putText(img, "Circle", (cX - 20, cY-t -15), cv.FONT_HERSHEY_SIMPLEX, 0.55, (64, 0, 128), 2)
# this function is used to print the word Rectangle above the Rectangles  shape
def rectangleFun(cX , cY , t):
    cv.putText(img, "Rectangle", (cX - 20, cY - t - 15), cv.FONT_HERSHEY_SIMPLEX, 0.55, (255, 0, 0), 2)
# this function is used to print the word Triangle above the Triangles shape
def triangleFun(cX , cY , t):
    cv.putText(img, "Triangle", (cX - 20, cY - t - 15), cv.FONT_HERSHEY_SIMPLEX, 0.55, (200, 0, 255), 2)


#this function is used to determine if the shape is Triangle or Rectangle
def is_Rectangle_Or_Triangle(l,r,t,b):
    #check if the shape is Rectangle by subtracting the right from left , and bottom from top
    #if the result less than 5 , we can say that the shape is Rectangle
    if((abs(l-r) <= 10) and (abs(t - b) <= 10) ):
        return 0
    else:
        #supposing that there are three types of shapes , the third one will be Triangle
        return 1

# this function find the types of inner shapes of the  Tree
def find_shape(array_indexes , array):
    array_Of_Types = []
    for cnt in array_indexes:
        leftmost = tuple(array[cnt][array[cnt][:, :, 0].argmin()][0])
        rightmost = tuple(array[cnt][array[cnt][:, :, 0].argmax()][0])
        topmost = tuple(array[cnt][array[cnt][:, :, 1].argmin()][0])
        bottommost = tuple(array[cnt][array[cnt][:, :, 1].argmax()][0])
        M = cv.moments(array[cnt])
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        # calculate left ,right , top , bottom of the contour
        l = cX - leftmost[0]
        r = rightmost[0] - cX
        t = cY - topmost[1]
        b = bottommost[1] - cY
        area = cv.contourArea(array[cnt])
        per = cv.arcLength(array[cnt], True)
        # Calculate the circularity of each contour
        cir = (4 * 3.14 * area) / (per * per)
        if(cir > 0.85):
           array_Of_Types.append(2)
        else :
           f1 = is_Rectangle_Or_Triangle(l, r, t, b) # 0 rectangle , 1 triangle
           array_Of_Types.append(f1)
        # print(cir)
    flag_of_circle = 0
    flag_of_rectangle = 0
    flag_of_triangle = 0
    for m in array_Of_Types:
        if m ==2 :
            flag_of_circle=1
        elif m==0 :
            flag_of_rectangle=1
        elif m==1 :
            flag_of_triangle=1

    if ( (flag_of_circle == 1) and (flag_of_rectangle == 1)):
        cv.putText(img, "Tree Class 1", (cX - 20, cY - t - 15), cv.FONT_HERSHEY_SIMPLEX, 0.55, (250, 64, 0), 2)
    elif (( flag_of_triangle==1) and (flag_of_rectangle == 1)):
        cv.putText(img, "Tree Class 2", (cX - 20, cY - t - 15), cv.FONT_HERSHEY_SIMPLEX, 0.55, (0, 255, 0), 2)


#this function is used to determine if the shape is Tree
def is_Tree(array):

    array_Of_inners = []
    array_of_three_contours_of_the_tree = []
    duplicate_Array = []
    duplicate_tmp = []

    for ii in range(len(array)):
        array_of_three_contours_of_the_tree.append(ii)
        for jj in range(len(array)) :

            if (ii != jj):
               blank1 = np.zeros(img.shape[0:2])
               image11 = cv.drawContours(blank1.copy(), array ,ii, 1 , 12)
               image22 = cv.drawContours(blank1.copy(), array,jj , 1 , 12)
               intersection = np.logical_and(image11 , image22)

               if(intersection.any()):
                   array_of_three_contours_of_the_tree.append(jj)
                   duplicate_tmp.append(jj)


        tmp = -1
        if(len(array_of_three_contours_of_the_tree) > 1):
            for index in range(len(array_of_three_contours_of_the_tree)) :
                area1 = cv.contourArea(array[array_of_three_contours_of_the_tree[index]])
                max1 = cv.contourArea(array[array_of_three_contours_of_the_tree[0]])
                if (area1 > max1):
                     tmp = array_of_three_contours_of_the_tree[index]


        for g in range (len(array_of_three_contours_of_the_tree)):
            if(tmp != array_of_three_contours_of_the_tree[g]):
                array_Of_inners.append(array_of_three_contours_of_the_tree[g])


        duplicate_flag = True
        if ((len(array_Of_inners ) > 1) and (len(duplicate_Array) > 1)):

            for ll in array_Of_inners:
                for kk in duplicate_Array:
                    if(ll == kk ):
                        duplicate_flag = False

        if(duplicate_flag == True):
               find_shape(array_Of_inners , array )

        array_of_three_contours_of_the_tree.clear()
        array_Of_inners.clear()
        for dup in duplicate_tmp:
            duplicate_Array.append(dup)
        duplicate_tmp.clear()
#-------------------------------------------------------------------------------------------------------
#Start code

#Read Image
img = cv.imread('Test4.png')
#Convert the colored image To Gray Scale
grayImg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#Apply GaussianBlur filter to reduce the noize
blurredImg = cv.GaussianBlur(grayImg, (5, 5), 0)
#convert the gray scale image to binary image using 127 as the threshold value
threshImg = cv.threshold(blurredImg,170, 255, cv.THRESH_BINARY)[1]
#using  findCountours  function to find all the contoures in the image
contours,hierarchy=cv.findContours(threshImg, 1, 2 )

# set of arrayes used as temporal for data
arrayOfContoutrs = []
arrayOfTreesContours = []
arrayOfIndexes = []
arrayOfIndexes2 = []

for i in range(len(contours) - 1) :
    MM = cv.moments(contours[i])
    cX1 = int(MM["m10"] / MM["m00"])
    cY1 = int(MM["m01"] / MM["m00"])

    flag1 = False
    c1 = 0
    while(c1 < (len(arrayOfContoutrs))):
            MMM = cv.moments(arrayOfContoutrs[c1])
            cX2 = int(MMM["m10"] / MMM["m00"])
            cY2 = int(MMM["m01"] / MMM["m00"])
            if((abs(cX1 - cX2 ) <=10) and (abs(cY1 - cY2 ) <=10)):
                flag1 = True
                arrayOfIndexes.append(c1)
                break
            c1 = c1 + 1
    if(flag1 == False):
        arrayOfContoutrs.append(contours[i])

#----------------------------------------------------------

for k in range(len(arrayOfContoutrs)):
    flag2 = -1
    for t in  arrayOfIndexes:
        if k == t :
            flag2 = 1
    if flag2 == -1:
        arrayOfIndexes2.append(k)




arrayOfContours_for_circle_triangle_rectangle =[]
arrayOfContours_for_trees = []
for v in range (len(arrayOfIndexes)):
    arrayOfContours_for_circle_triangle_rectangle.append(arrayOfContoutrs[arrayOfIndexes[v]])

for q in range (len(arrayOfIndexes2)):
    arrayOfContours_for_trees .append(arrayOfContoutrs[arrayOfIndexes2[q]])
# call isTree function
is_Tree(arrayOfContours_for_trees)


count = 0
for x in arrayOfContours_for_circle_triangle_rectangle:

  # Find the moments of each contour
  M = cv.moments(x)
  # Find the area of each contour
  area = cv.contourArea(x)
  # Find the perimeter  of each contour
  per = cv.arcLength(x, True)
  #Calculate the circularity of each contour
  cir = (4 * 3.14 * area) / (per * per)

  #Extract the left , right , top , bottom most coordinates for each contour
  leftmost = tuple(x[x[:, :, 0].argmin()][0])
  rightmost = tuple(x[x[:, :, 0].argmax()][0])
  topmost = tuple(x[x[:, :, 1].argmin()][0])
  bottommost = tuple(x[x[:, :, 1].argmax()][0])



  # calculate x,y coordinate of center from moments
  cX = int(M["m10"] / M["m00"])
  cY = int(M["m01"] / M["m00"])
  # calculate left ,right , top , bottom of the contour
  l = cX - leftmost[0]
  r = rightmost[0] - cX
  t = cY - topmost[1]
  b = bottommost[1] - cY



  #------------------------------------------------------------------------------------------
  #from the circularity descriptor we can detect the circles if it has a circularity >= 0.85
  if cir > 0.85 :
         circleFun(cX,cY,t)
  else :
             flag = is_Rectangle_Or_Triangle(l,r,t,b)
             if(flag == 0):
                 rectangleFun(cX,cY,t)
             elif(flag == 1):
                 triangleFun(cX,cY,t)

  #increment the counter
  count = count + 1

cv.imshow('Output Image', img)
cv.waitKey(0)
# closing all open windows
cv.destroyAllWindows()
