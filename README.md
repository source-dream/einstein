# 小梦-爱恩斯坦棋

## 介绍

这是一个用python实现的爱恩斯坦棋项目

## 安装运行指南

本项目在python3.10.8环境下测试运行，理论上也支持其他版本

命令行输入以下命令安装所需模块(现在你可以看见文件时空的, 因为没有使用其他任何模块, 所以理论上可以跳过这一步, 直接运行)

```python
pip install -r requirements.txt
```

确定安装好所需库并且配置好配置信息后，手动运行start.bat，或者执行下面命令都可

```python
python main.py
```

## 使用说明

项目配置

## 项目结构

>本项目结构由源梦重构，一方面是以前的代码写的实在是太烂了，另一方面是想做的更好

├──&emsp;README.md&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;//&emsp;帮助文档    
├──&emsp;main.py&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;//&emsp;程序运行主程序    
├──&emsp;Config&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;//&emsp;配置文件夹    
│&emsp;&emsp;&emsp;├──ai.ini&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;//&emsp;算法配置文件    
│&emsp;&emsp;&emsp;└──game.ini&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;//&emsp;游戏运行配置文件    
├──&emsp;Data&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;//&emsp;数据文件夹    
│&emsp;&emsp;&emsp;├──&emsp;ChessManual&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;//&emsp;比赛棋谱存储    
│&emsp;&emsp;&emsp;└──&emsp;TrianData&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;//&emsp;训练数据存储    
├──&emsp;Resource&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;//&emsp;资源文件夹    
├──&emsp;Game&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;//&emsp;游戏实现模块    
├──&emsp;AI&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;//&emsp;算法实现模块     
├──&emsp;Doc&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;//&emsp;文档    
├──&emsp;License&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;//&emsp;许可说明文件    
└──&emsp;requirements.txt&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;//&emsp;第3方依赖库列表    

## 团队介绍

本项目由曾经的绊爱团队根据前年参加计算机博弈大赛的代码改进而来，现在我们的队名也正式更名为小梦。

本项目一共5人。

团队分工

在大一的时候我们团队就一起参加了计算机博弈大赛，那个时候我们拿到了学长写的一份代码，当时就连运行代码也运行不起来，后面很荣幸可以去我们学校的本部参加集训，在集训中我们慢慢理解代码，每天准时到达集训地点参加培训，并且对代码进行了一些自己的改进和优化，最后在正式比赛的时候我们也获得了全国二等奖。
