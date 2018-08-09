# China-Historical-Newspaper-OCR
An OCR system that's designed to digitize "Shen Bao" -- one of the most important newspapers in China.

### Roadmap — 3 steps

##### 1 OpenCV文字切割处理

- [x] 报纸图片切割文字区块
  - [x] 二值化处理
  - [x] 框线检测、去除
  - [x] 边框定位，文字区域切割（小区域切割尚无法实现）
  - [ ] 水平、竖直投影
- [ ] 逐区块切割单个文字

##### 2 CNN文字识别

- [ ] “制造”训练数据集
- [ ] 训练识别网络

##### 3 利用语言模型进行文字处理

- [ ] 提高文字识别率
- [ ] 文段断句

### Files

可用做module的python文件：

- `showPic.py`
  - 调用cv2显示图片
  - 两种执行模式：`showPic(path, para=1)`和`showImg(img, name="image")`
  - 也可以命令行调用
- `threshold.py`
  - 传入图片地址，返回二值化的cv2 img
  - `threshold(name, reverse=False)`
  - 文件参数为name，默认格式是png
  - `reverse=True`时返回的image反色，用作cv2的直线检测
  - 命令行调用：`python threshold.py <input-pic> <output-pic>`
- `dilation.py`
  - 利用cv2的`dilation`算法得到膨胀后的图像，然后用`im2-im1`得到图像的轮廓，并检测框线
  - `getDilationLines(img, kernel=10, minlen=300, maxgap=10)`
- `segment.py`
  - 利用`dilation.py`检测得到的竖直、水平直线对图像进行切割
  - 距离不超过200px的直线将会被合并
  - 检测到的线段将会被清除
  - `getSegments(name)`，返回切割好的cv2 img

一些小实验的python文件（暂时没啥用）：

- `wipeLinesP.py`
  - 目前还只能画出图片中检测到的框线
- `findContours.py`
  - 找出图像中每个物体的轮廓，不联通的字会被分成数个部分
- `dilationHorizontal.py`
  - 利用`dilation`检测水平线