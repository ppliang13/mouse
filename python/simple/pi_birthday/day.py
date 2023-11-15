class Day:
  def __init__(self,day,flag,num,index):
    self.day=day
    self.flag=flag
    self.num=num
    self.index=index

  def __init__(self,day,num):
    self.day=day
    self.flag=False
    self.num=num
    self.index=-1


  def exist(self,index):
    if(self.index==-1):
      self.index=index
    if(self.index>index):
      self.index=index
    self.flag=True
    return self.index

  def __str__(self):
        return f"(day={self.day}, flag={self.flag}, num={self.num}, index={self.index})"
