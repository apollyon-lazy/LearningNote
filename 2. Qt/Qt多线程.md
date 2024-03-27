# QThread

公有槽函数
	`thread.start()` 用于启动线程
	`thread.quit()` 线程退出事件循环并等待线程结束(即运行函数执行完毕)
	`thread.terminate()` 则是一种强制终止线程的方式。
公有函数
	`thread.isRunning()` 检查线程是否正在运行
	`thread.isFinished()` 检查线程是否结束
静态公有函数
	`thread.sleep()` 使当前线程休眠指定的秒数（以秒为单位）
	`thread.msleep()` 使当前线程休眠指定的毫秒数（以毫秒为单位）
	`thread.usleep()` 使当前线程休眠指定的微秒数（以微秒为单位）
	`thread.wait()` 等待线程结束
保护函数
	`thread.run()` 虚函数，继承`QThread`类需重载 ，调用 `thread.start()` 后会执行其中逻辑

```ad-note
线程的`run()`函数执行完会进入终止状态，此时使用`isFinished()`函数判断会返回`true`
线程的`quit()`函数将线程的事件循环停止，如果线程还有事件没处理完所以线程可能仍在运行中
线程的`wait()`函数会阻塞当前线程，等待特定线程结束，如果线程没启动会直接返回
线程的`isFinished()`只能帮助判断运行函数是否执行完，无法判断线程是否开始运行
```
## 示例一

GPT: 写一个简单的Qt线程代码

```ad-summary
Qt怎么利用主线程创建子线程，并在子线程中执行特定类的函数 ？
1. 创建一个继承自`QObject`的`MyWorker`类
2. 主线程：创建一个`MyWorker`类对象`worker`，再创建一个线程`QThread`类对象`workerThread`
3. 将类对象 `worker` 移动到子线程 `workerthread`
4. 连接线程启动 **信号** `Qthread::started`到类对象 **槽** 函数`MyWorker::dowork`
5. 启动线程`QThread.start`, 此时程序主线程和子线程并发
```

```cpp
#include <QCoreApplication>
#include <QThread>
#include <QDebug>
class MyWorker : public QObject
{
    Q_OBJECT
public slots:
    void doWork() {
        for (int i = 0; i < 5; ++i) {
            qDebug() << "Working on iteration" << i;
            QThread::sleep(1);
        }
        emit workFinished(); // 发送打印完成信号
    }
    
public: 
	void normalFunction() {
		qDebug() << "This is a normal function running in the main thread."; 
	}
	
signals:
    void workFinished(); // 定义信号
};

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);
    MyWorker worker; // 定义对象
    QThread workerThread; //  定义线程
	// 连接线程启动和执行工作
    QObject::connect(&workerThread, &QThread::started, &worker, &MyWorker::doWork);
    // 连接工作结束信号和线程停止
    QObject::connect(&worker, &MyWorker::workFinished, &workerThread, &QThread::quit);
    // 连接线程停止和程序退出
    QObject::connect(&workerThread, &QThread::finished, &a, &QCoreApplication::quit);
    worker.moveToThread(&workerThread); // 对象移动到线程当中
    workerThread.start(); // 启动线程
    worker.normalFunction(); // 调用不耗时的函数
    
    return a.exec();
}
```

```ad-question
**Qt中开 两个定时器 还是 两个线程 有区别吗？**
- Qt中使用`QTimer`类实现定时器。两个定时器是在同一个线程中，并不是并发执行的。定时器事件会在事件循环中出触发，这意味着当一个定时器的槽函数执行时，另一个定时器的槽函数会等待，直到前一个槽函数执行完成才执行。
- Qt中使用`QThread`类实现多线程编程。将任务放置在不同的线程中运行，可以实现并发执行的效果，提高程序的性能和响应性。

**Qt中使用moveToThread将对象移动到子线程为什么还能调用对象的成员函数？**
- 当你使用 `moveToThread` 将对象移动到子线程中时，仅仅是该对象所连接的`信号和槽函数`会在新线程中执行，而其他成员函数仍然可以在原来的线程中被调用和执行。
- 这意味着，即使对象被移动到子线程中，仍然可以在主线程中使用对象的成员函数。这样的设计允许你将耗时操作移至单独的线程执行，同时保持在主线程中执行一些不涉及耗时操作的逻辑。
```

## 示例二

GPT: 现在存在一个数据读取设备，请用Qt单独开个线程读取其中的数据

```cpp
#include <QCoreApplication>
#include <QThread>
#include <QDebug>

// 模拟数据读取设备
class DataDevice : public QObject
{
    Q_OBJECT
public:
    void startReading() {
        // 模拟数据读取过程
        for (int i = 0; i < 5; ++i) {
            qDebug() << "Reading data" << i;
            QThread::sleep(1);
        }
        emit readingFinished();
    }

signals:
    void readingFinished();
};

// 数据读取线程
class DataReaderThread : public QThread
{
    Q_OBJECT
public:
    DataReaderThread() : m_isRunning(false) {}

    void run() override {
		// 灵活控制线程启动停止 而不是 重新创建线程
        if (!m_isRunning) {
            return;
        }
        connect(&m_device,&DataDevice::readingFinished,this, &DataReaderThread::readingFinished);
        // 在新线程中执行数据读取操作
        m_device.startReading();
    }

    void setRunning(bool running) {
        m_isRunning = running;
    }
    
signals:
    void readingFinished();
    
private:
    bool m_isRunning;
    DataDevice m_device;
};

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);
    DataReaderThread readerThread;
    readerThread.setRunning(true); // 设置为运行状态
    QObject::connect(&readerThread, &DataReaderThread::readingFinished, &a, &QCoreApplication::quit);
    // 启动数据读取线程
    readerThread.start();
    
    return a.exec();
}
```

## 示例三

Qt创建多线程接收惯导UDP数据(代码有问题)

```ad-note
1. 技巧：示例二和示例三都用到了一个`bool`量来管理线程的运行启动和停止
2. 子线程构造：标记运行状态(线程可以运行但未运行)；初始化UDP套接字
3. 线程运行：不断接收UDP数据；每隔固定时间将数据写入文件
4. 线程结束：标记运行状态(线程对象并未析构)
```

gnss.h
```cpp
#ifndef GNSS_H
#define GNSS_H
#include <QThread>
#include <QtCore>
#include <QObject>
#include <QMutex>
#include <iostream>
#include <QtNetwork>
 
class GNSS: public QThread
{
public:    
    Q_OBJECT
public:
    GNSS(); // 构造函数
    void stop(); // 
private slots:
    void run(); // 运行函数
    void processPendingDatagram();
private:
    bool stopped; // 停止标志
    QMutex m_lock; // 互斥锁
    QUdpSocket *receiver; // UDP通讯
    QFile f();
};
 
#endif // GNSS_H
```

gnss.cpp
```cpp
#include "gnss.h"
#include <QTimer>
#include <QMutexLocker>
#include "mainwindow.h"
 
GNSS::GNSS()
{
 
    stopped = false;//标记可以运行
    //创建一个QUdpSocket类对象，该类提供了Udp的许多相关操作
    receiver = new QUdpSocket(this);
    int port =3000;//设置UDP的端口号参数，指定在此端口上监听数据
    //此处的bind是个重载函数，连接本机的port端口，采用ShareAddress模式(即允许其它的服务连接到相同的地址和端口，特别是
    //用在多客户端监听同一个服务器端口等时特别有效)，和ReuseAddressHint模式(重新连接服务器)
    int receive = receiver->bind(QHostAddress("195.0.0.230"),port);
    qDebug() << "receive: " <<receive << endl;
    if(receive == 0)
    {
        qDebug() << "UDP Connected Succeed ! " << endl;
    }
    else
    {
        qDebug() << "UDP Connected Faild ! " << endl;
    }
}
void GNSS::stop()
{
    QMutexLocker locker(&m_lock);
    stopped = true;
    receiver->close();
    delete receiver;
 
}
 
void GNSS::run()
{
    //获得系统时间并输出
    QString min = QDateTime::currentDateTime().toString("yyyyMMddhhmm");
    //打开文本 以时间命名文件名字
    QString fileName = "C:\\SensorsData\\BASLER\\code\\build-opencv-Desktop_Qt_5_8_0_MSVC2015_64bit-Debug\\GNSS_" + min + ".txt";//假设指定文件夹路径为D盘根目录
    QFile f(fileName);
    LONGLONG time_now=0;
    QString s = QDateTime::currentDateTime().toString("yyyy-MM-dd hh:mm:ss.zzz");
    QString a = QDateTime::currentDateTime().toString("yyyyMMddhhmm");
    QString b = QDateTime::currentDateTime().toString("mmss");
	 
	// 判别线程运行 进入不断地循环
    while(!stopped)
    {
        while(receiver->hasPendingDatagrams())  //拥有等待的数据报
        {
           //qDebug() << "receive succeed ! " << endl;
            QByteArray datagram; //拥于存放接收的数据报
           //pendingDatagramSize为返回第一个在等待读取报文的size，
           //resize函数是把datagram的size归一化到参数size的大小一样
           datagram.resize(receiver->pendingDatagramSize());
           //接收数据报，将其存放到datagram中
           //将读取到的不大于datagram.size()大小数据输入到datagram.data()中，
           //datagram.data()返回的是一个字节数组中存储数据位置的指针
           receiver->readDatagram(datagram.data(),datagram.size());
           //将数据报内容显示出来
           QString HexData = datagram.toHex();
           //判断数据是否完整
           if(HexData.length() == 144)
           {
               //解析Hex数据
               QString Status = HexData.mid(42,2);
               qDebug() << "Status :" << Status  << endl;
               QString Latitude = HexData.mid(46,16);
               qDebug() << "Latitude :" << Latitude  << endl;
               QString Longitude = HexData.mid(62,16);
               qDebug() << "Longitude :" << Longitude  << endl;
               QString Altitude = HexData.mid(78,8);
               qDebug() << "Altitude :" << Altitude  << endl;
               QString North_Velocity = HexData.mid(86,6);
               qDebug() << "North_Velocity :" << North_Velocity  << endl;
               QString East_Velocity = HexData.mid(92,6);
               qDebug() << "East_Velocity :" << East_Velocity  << endl;
               QString Down_Velocity = HexData.mid(98,6);
               qDebug() << "Down_Velocity :" << Down_Velocity  << endl;
               QString Heading = HexData.mid(104,6);
               qDebug() << "Heading :" << Heading  << endl;
               QString Pitch = HexData.mid(110,6);
               qDebug() << "Pitch :" << Pitch  << endl;
               QString Roll = HexData.mid(116,6);
               qDebug() << "Roll :" << Roll  << endl;
 
               //获得系统时间并输出
               s = QDateTime::currentDateTime().toString("yyyy-MM-dd hh:mm:ss.zzz");
               a = QDateTime::currentDateTime().toString("yyyyMMddhhmm");
               b = QDateTime::currentDateTime().toString("mmss");
               qDebug() << "min : " <<min<< endl;
               time_now = b.toLongLong();
               qDebug() << "time_now: " <<time_now<< endl;
               //每10分钟保存一次
               if(time_now % 1000 == 0)
               {
                   qDebug() << "write again ! " <<time_now<< endl;
                   f.fileName() = "C:\\SensorsData\\BASLER\\code\\build-opencv-Desktop_Qt_5_8_0_MSVC2015_64bit-Debug\\GNSS_" + a + ".txt";
               }
 
               qDebug() << "time" << s;
 
               if(!f.open( QIODevice::Append))
               {
                   cout << "Open failed." << endl;
               }
               QTextStream txtOutput(&f);
               txtOutput << s <<"$$"<< HexData<< "&&" << endl;
 
               f.close();
 
           }
           else
           {
               qDebug() << "The data is not complete !" << endl;
           }
        }
    }
 
 
}
/***********GNSS数据处理***********/
void GNSS::processPendingDatagram()
{
 
}
```

mainwindow.cpp
```cpp
void MainWindow::on_StartGNSSBtn_clicked()
{
    if(!gnss.isRunning())
    {
        gnss.start();
        ui->StartGNSSBtn->setEnabled(false);
        ui->StopGNSSBtn->setEnabled(true);
    }
    else
    {
        qDebug() << "GNSS receive has started !!!" << endl;
 
    }
 
}
 
/***********停止GNSS数据接收***********/
void MainWindow::on_StopGNSSBtn_clicked()
{
    if(gnss.isRunning())
    {
        gnss.stop();
    }
    ui->StartGNSSBtn->setEnabled(true);
    ui->StopGNSSBtn->setEnabled(false);
}
```

```ad-question
**重写`QThread`的`run`函数和自定义`run`函数的区别？**
- 
```

# 互斥量

QMutex
	`mutex.lock() mutex.unlock()`  需要显式的锁定和解锁`QMutex`对象，忘记解锁可能导致死锁
QMutexLocker	
	`QMutexLocker locker(&mutex)`  便捷类，离开作用域后会自动解锁`QMutex`对象

# 消息队列

## 示例一

简单的多线程消息队列例程

messagequeue.h
```cpp
#include <QThread>
#include <QMutex>
#include <QWaitCondition>
#include <QQueue>

class MessageQueue : public QObject
{
	Q_OBJECT
	public:
	    MessageQueue(QObject *parent = 0); // 构造函数
	    ~MessageQueue(); // 析构函数
	
	    void sendMessage(const QString &message); // 发送消息
	    QString getMessage(); // 接受消息
	
	signals:
	    void messageReceived(); // 消息接收信号
	
	private:
	    QMutex m_mutex;
	    QWaitCondition m_cond;
	    QQueue<QString> m_messages;
};

class ProducerThread : public QThread
{
	Q_OBJECT
	public:
	    ProducerThread(MessageQueue *queue, QObject *parent = 0);
	    ~ProducerThread();
	
	protected:
	    void run();
	
	private:
	    MessageQueue *m_queue;
};

class ConsumerThread : public QThread
{
	Q_OBJECT
	public:
	    ConsumerThread(MessageQueue *queue, QObject *parent = 0);
	    ~ConsumerThread();
	
	protected:
	    void run();
	
	private:
	    MessageQueue *m_queue;
};
```

```ad-note
1. 消息队列类 `MessageQueue`
	- 临界区资源 消息队列 <成员对象> `m_messages` 
	- 互斥锁 <成员对象> `m_mutex`
	- 发送消息函数 触及临界区 需要上互斥锁 <成员函数> `sendMessage()`
		- 上锁-消息填充到队列-唤醒所有等待线程-解锁
	- 接受消息函数 触及临界区 需要上互斥锁 <成员函数> `getMessage()`
		- 上锁-队列为空临时解锁等待消息进入队列-出队-解锁
2. 生产者线程类 `ProducerThread`
	- 运行函数 `run()` 
		- 发送消息到队列-触发消息发送完成信号-线程延时
	- 指向消息队列类对象的指针 访问消息队列 `m_queue`
3. 消费者线程类 `ConsumerThread`
	- 运行函数 `run()`
		- 读取信息从队列-如果消息为空退出运行函数
	- 指向消息队列类对象的指针 访问消息队列 `m_queue`
```

messagequeue.cpp
```cpp
MessageQueue::MessageQueue(QObject *parent)
    : QObject(parent)
{
}

MessageQueue::~MessageQueue()
{
    m_mutex.lock();
    m_cond.wakeAll();
    m_mutex.unlock();
}

void MessageQueue::sendMessage(const QString &message)
{
    m_mutex.lock();
    m_messages.enqueue(message);
    m_cond.wakeAll();
    m_mutex.unlock();
}

QString MessageQueue::getMessage()
{
    m_mutex.lock();
    while (m_messages.isEmpty()) {
        m_cond.wait(&m_mutex);
    }
    QString message = m_messages.dequeue();
    m_mutex.unlock();
    return message;
}

ProducerThread::ProducerThread(MessageQueue *queue, QObject *parent)
    : QThread(parent),
      m_queue(queue)
{
}

ProducerThread::~ProducerThread()
{
}

void ProducerThread::run()
{
    for (int i = 0; i < 10; ++i) {
        m_queue->sendMessage(QString("Message %1").arg(i));
        emit m_queue->messageReceived();
        msleep(200);
    }
}

ConsumerThread::ConsumerThread(MessageQueue *queue, QObject *parent)
    : QThread(parent),
      m_queue(queue)
{
}

ConsumerThread::~ConsumerThread()
{
}

void ConsumerThread::run()
{
    while (true) {
        QString message = m_queue->getMessage();
        qDebug() << message;
        if (message.isNull()) {
            break;
        }
    }
}

int main(int argc, char *argv[])
{
    QCoreApplication app(argc, argv);

    MessageQueue queue;
    ProducerThread producer(&queue);
    ConsumerThread consumer(&queue);

    QObject::connect(&queue, &MessageQueue::messageReceived, &consumer, &ConsumerThread::start);

    producer.start(); // 启动生产者线程
    producer.wait(); // 生产者只要生产一个消息到队列，就会使得消费者线程启动(先生产后消费)
    queue.sendMessage(QString()); // 空字符用来停止消费者线程运行
    consumer.wait(); // 等待消费者线程停止(run函数停止)

    return app.exec();
}

#include "main.moc"

```


