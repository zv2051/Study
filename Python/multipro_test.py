from multiprocessing import Process,Queue
def func(q):
    q.put([42,None,"hello"])    #把一个列表放入一个队列中

if __name__=="__main__":
    q1=Queue()        #定义一个队列
    p1=Process(target=func,args=(q1,))		#实例化一个进程
    p1.start()	#启动进程 
    print(q1.get())		#从队列中取出一个项目，并打印 
    p1.join()	#阻塞进程
