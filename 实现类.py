from pip._vendor.distlib.database import new_dist_class


class person(object):
    """"人的类"""

    def __init__(self, name):
        super(person, self).__init__()
        self.name = name
        self.gun=None
        self.hp=100
        self.shoushang=False
        self.dazhong=False
    def anzhuang_zidan(self,dan_temp_jia,zi_temp_dan):
        dan_temp_jia.an_zhuang(zi_temp_dan)
    def anzhuang_danjia(self,Gun_temp, dan_temp_jia):
        Gun_temp.an_zhuang(dan_temp_jia)
    def na_qiang(self,Gun_temp):
        self.gun=Gun_temp
    def kai_qiang(self,enemy):
        if self.gun.da_zhong(enemy):
            self.yicidazhong=True;
        else:
            self.yicidazhong = False;
        self.dazhong = self.yicidazhong
    def beijizhong(self,shanghai):
        self.hp-=shanghai
        self.shoushang = True
    def __str__(self):
        if self.gun:
            return ("%s的血量为%s,%s有枪，%s，此次是否打中：%s"%(self.name,self.hp,self.name,self.gun,self.dazhong))
        else:
            if self.hp>0:
                return ("%s的血量为%s,%s没枪,此次有无受伤：%s" % (self.name, self.hp,self.name,self.shoushang))
            else:
                return ("%s已挂" % (self.name))
class Gun(object):
    """枪的类"""
    def __init__(self,name):
        super(Gun, self).__init__()
        self.name = name
        self.dan_jia=None
    def an_zhuang(self,dan_temp_jia):
        self.dan_jia = dan_temp_jia

    def __str__(self):
        if self.dan_jia:
            return ("枪为%s,%s"%(self.name,self.dan_jia))
        else:
            return ("枪为%s" % (self.name))
    def da_zhong(self,enemy):
        if self.dan_jia.shangtang(enemy):
            return True
        else:
            return False

class Danjia(object):
    """弹夹容量"""
    def __init__(self,max_num):
        super(Danjia, self).__init__()
        self.max_num = max_num
        self.zidan_lists=[]
    def an_zhuang(self,zi_temp_dan):
        self.zidan_lists.append(zi_temp_dan)
    def shangtang(self,enemy):
        if self.zidan_lists:
            zidan_temp=self.zidan_lists.pop()
            if zidan_temp:
                zidan_temp.da_ren(enemy)
            return True
        else:
            return False
    def __str__(self):

        return("弹夹子弹数量：%d/%d"%(len(self.zidan_lists),self.max_num))



class Zidan(object):
    """弹夹容量"""
    def __init__(self,shanghai):
        super(Zidan,self ).__init__()
        self.shanghai = shanghai
    def da_ren(self,enemy):
        enemy.beijizhong(self.shanghai)
def main():
    """用来控制程序流程"""
    # 1.创建老王对象
    laowang = person("老王")
    # 2.创建枪对象
    ak47=Gun("AK47")
    # 3.创建弹夹对象
    dan_jia=Danjia(20)
    # 4.创建子弹对象
    for i in range(10):

        zi_dan=Zidan(10)

        # 5.老王把子弹装到弹夹
        #老王.把子弹安装到弹夹
        laowang.anzhuang_zidan(dan_jia,zi_dan)
    # 6.把弹夹装到枪
    laowang.anzhuang_danjia(ak47,dan_jia)
    # 7.老王拿枪
    laowang.na_qiang(ak47)
    # 8.创建敌人对象
    enemy=person("老宋")

    # test弹夹
    print (dan_jia)
    # test枪
    print (ak47)
    # test老王拿枪
    print (laowang)
    # test老宋
    print (enemy)
    # 9.老王打敌人
    if laowang.gun:
        for i in range(20):
            laowang.kai_qiang(enemy)
            # test弹夹
            print (dan_jia)
            # test枪
            print (ak47)
            # test老王拿枪
            print (laowang)
            # test老宋
            print (enemy)


if __name__ == '__main__':
    main()
