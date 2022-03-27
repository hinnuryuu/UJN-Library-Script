# UJN-Library-Script

之前写的预约工具的脚本式执行

感谢学长提供的[API](https://github.com/Hephyr/UJN-Lib-Seat-API)

---

[使用方法](https://github.com/hinnuryuu/UJN-Library-Script/issues/1)

---

@hinnuryuu

就目前的测试看来预约功能是能够正常使用的，但是[API](https://github.com/Hephyr/UJN-Lib-Seat-API)里面的签到功能现在无法调用了。

具体的使用步骤如下：

Step 1: 运行 **settings_file_generator.py** ，这个脚本会在你的当前目录产生一个名为settings的JSON文件，这个文件呢是用于保存你即将预约的座位的信息，里面包含着如下信息：

你的学号username，预约系统密码password(初始密码为你的身份证后6位)，UJN座位唯一标识seat_id，开始时间start_time和结束时间end_time(它们都接受一个24进制的整数)，预约日期date

Step 2: 用记事本或者其他编辑器的方式打开该JSON文件，然后将你的学号，密码两项信息填入(如果是多用户预约，也只用先填上第一个用户的就行了)，注意不能删去两端的引号，然后保存。

Step 3: 运行 **get_seat_id.py** ，这个文件是用于获取UJN图书馆的全局唯一标识的，在脚本里面选择完你要预约的校区，楼层，图书室后，程序将会反馈一个seat_id，对其复制后即可关闭 **get_seat_id.py**。

Step 4:打开JSON文件，将刚才获取到的 **seat_id** 填入，并完善其余信息(初始化的JSON文件都有完善的注释)，同样需要注意两段引号不能删去。

Step 5:运行 **book_seat.py** ，等待提示成功即可结束程序。

其实这个仓库的项目是打算自己使用的，因为身边会Python的同学并且想折腾的同学实在不多，所以这份代码没有写具体注释，逻辑交互也是凭直觉写的，阅读起来难免混乱，这个执行脚本我之前写的预约程序的精简版，之前的还有取消预约和查看历史预约记录的功能，考虑到我也不怎么去图书馆了，于是就把这个脚本精简了。

这个脚本最好搭配apschedule库，这是用于定时自动执行的。

---

@QinMoMeak

基于多任务，在json配置文件中增加多个座位id

seat.xlsx 储存座位号（默认14号第六阅览室）

seat_id.py 获得seats中座位号并请求对应座位id输出到result.txt（可修改阅览室号）

start.py 设置定时任务，定时开启脚本依次尝试json配置文件中目标座位

使用过程：

+ 使用settings_file_generator生成新的配置文件（初次使用），在生成的settings.json中填入username与password（填入此两项后即可使用get_seat_id查询目标座位id）
+ 若有多个目标座位（用于备用），可在填入用户密码后，在seats.xlsx中填入座位号（默认使用第一列），在seat_id中修改目标阅览室、用户名、密码，最后运行seat_id.py。将result.txt中的结果粘贴进配置文件settings.json中。
+ 配置好后，修改start.py中启动时间（7点），运行后最小化即可。设定时间后会自动尝试预约配置文件中的座位。
