# class ListNode:
#     def __init__(self, x):
#         self.val = x     #val
#         self.next = None
# class ReverseKGroup:
#     def reverse(self, head, k):
#         dummy = ListNode(0)
#         p = dummy
#         while True:
#             count = k
#             stack = []
#             tmp = head
#             while count and tmp:
#                 stack.append(tmp)
#                 tmp = tmp.next
#                 count -= 1
#             if count:
#                 p.next = head
#                 break
#             while stack:
#                 p.next = stack.pop()
#                 p = p.next
#             p.next = tmp
#             head = tmp
#         return dummy.next     #dummy.next
# if __name__ == '__main__':
#     reverseKGroup = ReverseKGroup()
#     node = ListNode(0)
#     head = eval(input("head="))
#     k = eval(input("k="))
#     r = node
#     for i in head[:-1]:
#         r.val = i
#         r.next = ListNode(0)
#         r = r.next
#     r.val = head[-1]
#     ss = []
#     tmp = reverseKGroup.reverse(node, k)
#     while tmp.next and tmp.val:
#         ss.append(tmp.val)
#         tmp = tmp.next
#     ss.append(tmp.val)
#     print(ss)
"""#val   #dummy.next"""
"""_______________________________"""
# class StuInfo:
#     def __init__(self):
#         self.name = input("请输入5名学生的姓名：").split("，")    #.split("，")
#         self.score = []
#         for i in self.name:
#             self.score.append(eval(input("请输入{}的英语成绩：".format(i))))
#     def count(self):    #count
#         print("5名同学中英语成绩最高分为：", max(self.score))
#         print("5名同学中英语成绩最低分为：", min(self.score))
#         print("5名同学中英语成绩平均分为：", sum(self.score) / len(self.score))    #sum(self.score) / len(self.score)
# if __name__ == '__main__':
#     stuInfo = StuInfo()
#     stuInfo.count()     #stuInfo.count()
"""#.split("，")  #count   #count    #sum(self.score) / len(self.score)    #stuInfo.count()"""
"""_______________________________"""
#
# import random
# class TestSort:
#     def __init__(self):
#         self.array = []
#         for i in range(10):                                 #for i in range(10):
#             self.array.append(random.randint(0, 1000))      #self.array.append(random.randint(0, 1000))
#     def sort(self):
#         a = len(self.array)
#         for i in range(1, a):
#             for j in range(0, a - 1):
#                 if self.array[j] > self.array[j + 1]:                                    #self.array[j + 1]
#                     self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]  #self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
#         return self.array
# if __name__ == '__main__':
#     testSort = TestSort()
#     print(testSort.array)
#     print(testSort.sort())
"""#for i in range(10):
   #self.array.append(random.randint(0, 1000))
   #self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]"""
"""_______________________________"""
# class FindMedianSortedArrays:
#     def __init__(self):
#         self.array1 = eval(input("array1="))
#         self.array2 = eval(input("array2="))
#     def find(self):
#         array = self.array1 + self.array2
#         array.sort()                                           #array.sort()
#         tmp = len(array)
#         if not tmp:
#             return
#         if tmp % 2 == 0:
#             return (array[tmp // 2] + array[tmp // 2 - 1]) / 2  #(array[tmp // 2] + array[tmp // 2 - 1]) / 2
#         else:
#             return array[tmp // 2]
# if __name__ == '__main__':
#     findMedianSortedArrays = FindMedianSortedArrays()
#     print(findMedianSortedArrays.find())
""" #array.sort()  
    #(array[tmp // 2] + array[tmp // 2 - 1]) / 2"""
"""_____________________________________"""
"""
（1） create database EMPDB; #database
（2） use  EMPDB;
create table employee(
  Emp_Id int primary key ,  #primary key
  Emp_Name varchar(50) unique ,
  gender varchar(2),
  birthday date
);
（3）insert into employee(emp_id, emp_name, gender, birthday)  #emp_id, emp_name, gender, birthday
values (10, '张三 ', '男', '2000-11-11'),
       (11, '李四 ', '女', '2002-04-02'),
       (12, '王五 ', '女', '1999-12-12');
（4）select * from employee;
（5）insert into employee(emp_id, emp_name, gender, birthday)  #insert into
values (13, '小明 ', '男', '2001-6-15');
（6）update  employee  set gender='女' where Emp_Name='张三';
（7）delete from employee where Emp_Name='王五'; #delete
"""
#总共：该错 database
#     填空 primary key
#     填空 emp_id, emp_name, gender, birthday
#     该错 insert into
#     填空 update  employee  set gender='女' where Emp_Name='张三';
#     该错 delete
