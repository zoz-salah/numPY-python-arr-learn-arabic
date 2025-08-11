import numpy as np

def arr():
    arr = np.array([1 , 2 , 3 , 4])
    # arr.ndim    # عدد الأبعاد (dimensions)
    # arr.shape   # شكل الـ array (rows, cols)
    # arr.size    # عدد العناصر الكلي
    # arr.dtype   # نوع البيانات

    # np.zeros((3, 3))       # مصفوفة 0
    # np.ones((2, 2))        # مصفوفة 1
    # np.full((2, 3), 7)     # مصفوفة مليانة رقم معين
    # np.eye(3)              # مصفوفة هوية Identity
    # np.arange(0, 10, 2)    # أرقام بمدى محدد
    # np.linspace(0, 1, 5)   # أرقام موزعة بالتساوي
    #arr[-1]    # آخر عنصر
    # arr[1:3]     # من 1 لـ 2
    # arr[:3]      # من الأول لـ 2
    # arr[::2]     # كل عنصرين


    # a = [1 , 2 , 3]
    # b = [1 , 2 , 3]
    # print(a + b)
    # print("-" * 50)
                                    # important diffrence
    # c = np.array([1 , 2 , 3])
    # d = np.array([1 , 2 , 3])
    # print(c+d)

    # np.sum(a)       # مجموع العناصر
    # np.mean(a)      # المتوسط
    # np.min(a)       # أقل قيمة
    # np.max(a)       # أكبر قيمة
    # np.sort(a)      # ترتيب


    #arr.reshape(3, 2)    # تغيير شكل المصفوفة
    #arr.flatten()        # تحويل لـ 1D
    
    #array slicing:
    #arr = np.array([10, 20, 30, 40, 50])
    #arr = np.array([10, 20, 30, 40, 50])
    # arr[1:4]   # من index 1 لحد قبل 4 → [20, 30, 40]
    # arr[:3]    # من الأول لحد قبل 3 → [10, 20, 30]
    # arr[2:]    # من index 2 للنهاية → [30, 40, 50]
    # arr[::2]   # كل عنصرين → [10, 30, 50]
    # arr[::-1]  # عكس المصفوفة → [50, 40, 30, 20, 10]

    #reshape : 
    #arr = np.array([1, 2, 3, 4, 5, 6])
    #
    #reshaped = arr.reshape(2, 3)
    #print(reshaped)
    ## [[1 2 3]
    ##  [4 5 6]]
    #ravel :
    #arr = np.array([[1, 2, 3],
    #            [4, 5, 6]])

    #flat = arr.ravel()
    #print(flat)  # [1 2 3 4 5 6]
