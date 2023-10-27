from django.contrib.auth.decorators import login_required
from mypage.models import UserProfile, Article, ClickCount,House
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render, redirect
from mypage.forms import Form
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.shortcuts import render
from .models import ClickCount
@login_required
def ranking_kr(request, username):
    user = User.objects.get(username=username)
    top_click_counts = ClickCount.objects.order_by('-click_count')[:30]
    click_count_obj, created = ClickCount.objects.get_or_create(user=user)
    click_count = click_count_obj.click_count
    context = {
        'username': username,
        'click_count': click_count,
        'top_click_counts': top_click_counts,
    }
    return render(request, 'mypage/kr/ranking.html', context)
def increase_click_count(email):
    if email.endswith("@stpaulhanoi.com"):
        try:
            house_name_dict ={
                "Poseidon":"seungwoo.choi@stpaulhanoi.com", "Poseidon":"doyoon.kim@stpaulhanoi.com", "Poseidon":"minwoo.kim@stpaulhanoi.com", "Poseidon":"nakyeong.kwak@stpaulhanoi.com", "Poseidon":"huuphuocminh.nguyen@stpaulhanoi.com", "Poseidon":"egor.nekhai@stpaulhanoi.com", "Poseidon":"hayoun.kim@stpaulhanoi.com", "Poseidon":"huisang.han@stpaulhanoi.com", "Poseidon":"jinuc.jung@stpaulhanoi.com", "Poseidon":"juwon.seo@stpaulhanoi.com", "Poseidon":"annayiyeon.kim@stpaulhanoi.com", "Poseidon":"vankhanh.mai@stpaulhanoi.com", "Poseidon":"donghyeon.kim@stpaulhanoi.com", "Poseidon":"suho.lee@stpaulhanoi.com", "Poseidon":"subin.jeon@stpaulhanoi.com", "Poseidon":"celso.boene@stpaulhanoi.com", "Poseidon":"hongseo.kang@stpaulhanoi.com", "Poseidon":"soomin.lee@stpaulhanoi.com", "Poseidon":"jia.kim@stpaulhanoi.com", "Poseidon":"ducminh.cao@stpaulhanoi.com", "Poseidon":"thaitueminh.nguyen@stpaulhanoi.com", "Poseidon":"minhtri.nguyen@stpaulhanoi.com", "Poseidon":"hyeryeong.kim@stpaulhanoi.com", "Poseidon":"anhmn.pham@stpaulhanoi.com", "Poseidon":"sohyun.kim@stpaulhanoi.com", "Poseidon":"sein.kim@stpaulhanoi.com", "Poseidon":"minseop.kim@stpaulhanoi.com", "Poseidon":"jonas.kletzing@stpaulhanoi.com", "Poseidon":"giadai.pham@stpaulhanoi.com", "Poseidon":"yoonseok.cha@stpaulhanoi.com", "Poseidon":"joohyeon.kwak@stpaulhanoi.com", "Poseidon":"leo.moric@stpaulhanoi.com", "Poseidon":"talia.marantos@stpaulhanoi.com", "Poseidon":"hyeseo.cho@stpaulhanoi.com", "Poseidon":"seungbeom.son@stpaulhanoi.com", "Poseidon":"yeonwoo.jeong@stpaulhanoi.com", "Poseidon":"jun.kim@stpaulhanoi.com", "Poseidon":"joejun.tan@stpaulhanoi.com", "Poseidon":"hienmy.nguyen@stpaulhanoi.com", "Poseidon":"giakhang.ly@stpaulhanoi.com", "Poseidon":"jisung.lee@stpaulhanoi.com", "Poseidon":"yuwon.park@stpaulhanoi.com", "Poseidon":"youngdo.park@stpaulhanoi.com", "Poseidon":"khanhchi.ha@stpaulhanoi.com", "Poseidon":"namphong.nguyen@stpaulhanoi.com", "Poseidon":"gyueun.kim@stpaulhanoi.com", "Poseidon":"dana.kim@stpaulhanoi.com", "Poseidon":"baoanh.tran@stpaulhanoi.com", "Poseidon":"bogeun.jung@stpaulhanoi.com", "Poseidon":"khoaan.bach@stpaulhanoi.com", "Poseidon":"minseo.chae@stpaulhanoi.com", 
                "Poseidon":"yun-gu.kang@stpaulhanoi.com", "Poseidon":"sojin.park@stpaulhanoi.com", "Poseidon":"jooha.park@stpaulhanoi.com", "Poseidon":"seohyeon.hwang@stpaulhanoi.com", "Poseidon":"hyoryeong.choi@stpaulhanoi.com", "Poseidon":"jaehyeok.choi@stpaulhanoi.com", "Poseidon":"zisung.choi@stpaulhanoi.com", "Poseidon":"phuonglinh.nguyen@stpaulhanoi.com", "Poseidon":"hyunchan.cho@stpaulhanoi.com", "Poseidon":"junseo.park@stpaulhanoi.com", "Poseidon":"quanganh.nguyen@stpaulhanoi.com", "Poseidon":"minhngan.nguyen@stpaulhanoi.com", "Poseidon":"thieunhu.hoang@stpaulhanoi.com", "Poseidon":"thianhtho.tran@stpaulhanoi.com", "Poseidon":"kyungmin.lee@stpaulhanoi.com", "Poseidon":"luongkhanhvan.nguyen@stpaulhanoi.com", "Poseidon":"anna.lee@stpaulhanoi.com", "Poseidon":"ngoclam.pham@stpaulhanoi.com", "Poseidon":"yanxi.jin@stpaulhanoi.com", "Poseidon":"quoctoan.trinh@stpaulhanoi.com", "Poseidon":"nayeon.kim@stpaulhanoi.com", "Poseidon":"mingyeong.park@stpaulhanoi.com", "Poseidon":"sehyeon.jang@stpaulhanoi.com", "Poseidon":"vanan.luong@stpaulhanoi.com", "Poseidon":"minseo.choi@stpaulhanoi.com", "Poseidon":"jinseo.kim@stpaulhanoi.com", "Poseidon":"boosung.kwak@stpaulhanoi.com", "Poseidon":"chaeyeon.shin.25@stpaulhanoi.com", "Poseidon":"hyunjae.chang@stpaulhanoi.com", "Poseidon":"jonghyuk.ko@stpaulhanoi.com", "Poseidon":"sua.choi.24@stpaulhanoi.com", "Poseidon":"khueanh.nguyen@stpaulhanoi.com", "Poseidon":"bachyen.bui@stpaulhanoi.com", "Poseidon":"nguyen.nghia@stpaulhanoi.com", "Poseidon":"seyeon.chung@stpaulhanoi.com", "Poseidon":"xiaoxian.tan@stpaulhanoi.com", "Poseidon":"hyunsol.han@stpaulhanoi.com", "Poseidon":"hyewon.kim@stpaulhanoi.com", "Poseidon":"christina.cooper@stpaulhanoi.com", "Poseidon":"minhanh.cao@stpaulhanoi.com", "Poseidon":"bohyun.jang@stpaulhanoi.com", 
                "Poseidon":"p.duwon@stpaulhanoi.com", "Poseidon":"hannah.stewart@stpaulhanoi.com", "Poseidon":"michael.popovich@stpaulhanoi.com", "Poseidon":"collin.dwyer@stpaulhanoi.com", "Poseidon":"julie.kesti@stpaulhanoi.com", "Poseidon":"callie.rundhammer@stpaulhanoi.com", "Poseidon":"trang.le@stpaulhanoi.com", "Poseidon":"philip.massaro@stpaulhanoi.com", "Poseidon":"fiona.mccarthy@stpaulhanoi.com", "Poseidon":"alan.vanpatter@stpaulhanoi.com", "Poseidon":"robert.bowley@stpaulhanoi.com", "Poseidon":"joanne.park@stpaulhanoi.com", "Artemis":"milan.vu@stpaulhanoi.com", "Artemis":"minhquan.pham@stpaulhanoi.com", "Artemis":"jungwon.lee@stpaulhanoi.com", "Artemis":"lucy.kletzing@stpaulhanoi.com", "Artemis":"eunseo.kwon@stpaulhanoi.com", "Artemis":"yun.sehoon@stpaulhanoi.com", "Artemis":"inu.park@stpaulhanoi.com", "Artemis":"thailam.le@stpaulhanoi.com", "Artemis":"seoin.kim@stpaulhanoi.com", "Artemis":"yewon.bae@stpaulhanoi.com", "Artemis":"lam.nguyen@stpaulhanoi.com", "Artemis":"sieon.jeon@stpaulhanoi.com", "Artemis":"cheolhyeon.hwang@stpaulhanoi.com", "Artemis":"hanyul.lee@stpaulhanoi.com", "Artemis":"yerim.kang@stpaulhanoi.com", "Artemis":"baoan.nguyen@stpaulhanoi.com", "Artemis":"conghung.thiem@stpaulhanoi.com", "Artemis":"gayun.lee@stpaulhanoi.com", "Artemis":"minseo.park@stpaulhanoi.com", "Artemis":"ngocminh.tran@stpaulhanoi.com", "Artemis":"geonwoo.lee@stpaulhanoi.com", "Artemis":"won.kim@stpaulhanoi.com", "Artemis":"huynsu.jang@stpaulhanoi.com", "Artemis":"yewon.bae@stpaulhanoi.com", "Artemis":"junyoung.jeong@stpaulhanoi.com", "Artemis":"quy.tranthiminh@stpaulhanoi.com", "Artemis":"dinhquan.ha@stpaulhanoi.com", "Artemis":"gitae.park@stpaulhanoi.com", "Artemis":"jiyun.oh@stpaulhanoi.com", "Artemis":"nguyenangelina.bui@stpaulhanoi.com", "Artemis":"santiago.cortizasfontan@stpaulhanoi.com", "Artemis":"supin.kim@stpaulhanoi.com", "Artemis":"darsh.agarwal@stpaulhanoi.com", "Artemis":"manhcuong.nguyen@stpaulhanoi.com", "Artemis":"gyueun1.kim@stpaulhanoi.com", "Artemis":"quanghiep.tran@stpaulhanoi.com", "Artemis":"junghyeok.lee@stpaulhanoi.com", "Artemis":"jaemin.lim@stpaulhanoi.com", "Artemis":"yebin.kim@stpaulhanoi.com", "Artemis":"woojeong.kwak@stpaulhanoi.com", "Artemis":"khuenn.nguyen@stpaulhanoi.com", "Artemis":"gyeongmin.yang@stpaulhanoi.com", "Artemis":"juhwan.lee@stpaulhanoi.com", "Artemis":"lamgiang.nguyen@stpaulhanoi.com", "Artemis":"jeonghyeon.kim@stpaulhanoi.com", "Artemis":"yeeun.song@stpaulhanoi.com", "Artemis":"huije.yun@stpaulhanoi.com", "Artemis":"yuji.choi@stpaulhanoi.com", "Artemis":"junhyeok.jeon@stpaulhanoi.com", "Artemis":"jeongyun.kim@stpaulhanoi.com", "Artemis":"hyemin.kang@stpaulhanoi.com", "Artemis":"sonyul.lee@stpaulhanoi.com", "Artemis":"nguyen.vinhhien@stpaulhanoi.com", "Artemis":"geonwoo.kim@stpaulhanoi.com", "Artemis":"czeczuga.honor@stpaulhanoi.com", "Artemis":"yoonjin.lee@stpaulhanoi.com", "Artemis":"vu.minhhieu@stpaulhanoi.com", "Artemis":"khueanh.nguyen@stpaulhanoi.com", "Artemis":"hyunjun.an@stpaulhanoi.com", "Artemis":"song.jieun@stpaulhanoi.com", "Artemis":"eunchae.lee@stpaulhanoi.com", "Artemis":"hongnhi.nguyen@stpaulhanoi.com", "Artemis":"doducduy.nguyen@stpaulhanoi.com", "Artemis":"tranxuanan.nguyen@stpaulhanoi.com", "Artemis":"uichan.jeon@stpaulhanoi.com", "Artemis":"jaehoon.soh@stpaulhanoi.com", "Artemis":"chae-eun.seol@stpaulhanoi.com", "Artemis":"mji.kim@stpaulhanoi.com", "Artemis":"seoyeon.lee@stpaulhanoi.com", "Artemis":"jangho.kim@stpaulhanoi.com", "Artemis":"quockhanh.duong@stpaulhanoi.com", "Artemis":"hanmin.ryu@stpaulhanoi.com", "Artemis":"nhatanh.nguyen@stpaulhanoi.com", "Artemis":"jacqueline.huh@stpaulhanoi.com", "Artemis":"sumin.lim@stpaulhanoi.com", "Artemis":"daewook.kim@stpaulhanoi.com", "Artemis":"yan.pham@stpaulhanoi.com", "Artemis":"yoonyoung.jeong@stpaulhanoi.com", "Artemis":"tueminh.nguyen@stpaulhanoi.com", "Artemis":"j.junseo@stpaulhanoi.com", "Artemis":"kimkhanh.le@stpaulhanoi.com", "Artemis":"younghun.jung@stpaulhanoi.com", "Artemis":"khanhlinh.nguyen@stpaulhanoi.com", "Artemis":"minhngoc.truong@stpaulhanoi.com", "Artemis":"dinhminhquang.luong@stpaulhanoi.com", "Artemis":"l.hyunsong@stpaulhanoi.com", "Artemis":"tuekhue.vu@stpaulhanoi.com", "Artemis":"hyewon.park@stpaulhanoi.com", "Artemis":"jisol.park@stpaulhanoi.com", "Artemis":"hoangduong.nguyen@stpaulhanoi.com", "Artemis":"park.dahoe@stpaulhanoi.com", "Artemis":"justin.garza@stpaulhanoi.com", "Artemis":"ethan.blonder@stpaulhanoi.com", "Artemis":"macara.oshida@stpaulhanoi.com", "Artemis":"jesse.aguilar@stpaulhanoi.com", "Artemis":"stephen.volz@stpaulhanoi.com", "Artemis":"alicia.drapkin@stpaulhanoi.com", "Artemis":"xu.dan@stpaulhanoi.com", "Artemis":"bradley.weeder@stpaulhanoi.com", "Artemis":"toby.walker@stpaulhanoi.com", "Artemis":"derek.vanpatter@stpaulhanoi.com", "Artemis":"keith.vanpatter@stpaulhanoi.com",
                "Apollo":"quocdung.khuc@stpaulhanoi.com", "Apollo":"joonsung.chung@stpaulhanoi.com", "Apollo":"thaochi.nguyen@stpaulhanoi.com", "Apollo":"jiwon.lee@stpaulhanoi.com", "Apollo":"jiyu.lee.30@stpaulhanoi.com", "Apollo":"youngmin.park@stpaulhanoi.com", "Apollo":"nhaminh.tran@stpaulhanoi.com", "Apollo":"minhtrang.do@stpaulhanoi.com", "Apollo":"baohan.pham@stpaulhanoi.com", "Apollo":"museong.kim@stpaulhanoi.com", "Apollo":"anthy.ly@stpaulhanoi.com", "Apollo":"gahyeon.jung@stpaulhanoi.com", "Apollo":"seogil.choi@stpaulhanoi.com", "Apollo":"minchae.kim@stpaulhanoi.com", "Apollo":"jiyeul.kim@stpaulhanoi.com", "Apollo":"minhngoc.doan@stpaulhanoi.com", "Apollo":"ryul.kim@stpaulhanoi.com", "Apollo":"gyumin.kim@stpaulhanoi.com", "Apollo":"yejin.na@stpaulhanoi.com", 
                "Apollo":"uigyun.jo@stpaulhanoi.com", "Apollo":"hazel.jenkins@stpaulhanoi.com", "Apollo":"yeojin.jung@stpaulhanoi.com", "Apollo":"minkyeong.kim@stpaulhanoi.com", "Apollo":"truongan.le@stpaulhanoi.com", "Apollo":"jiyoo.kim@stpaulhanoi.com", "Apollo":"junseo.lee1@stpaulhanoi.com", "Apollo":"minjei.lee@stpaulhanoi.com", "Apollo":"taehyun.oh@stpaulhanoi.com", "Apollo":"hyojeong.kim@stpaulhanoi.com", "Apollo":"seoyun.lim@stpaulhanoi.com", "Apollo":"woojin.kang@stpaulhanoi.com", "Apollo":"zhaoan.tan@stpaulhanoi.com", "Apollo":"narae.lee@stpaulhanoi.com", "Apollo":"hyewon.so@stpaulhanoi.com", "Apollo":"jihoo.park1@stpaulhanoi.com", "Apollo":"seunghyun.lim@stpaulhanoi.com", "Apollo":"seeun.park@stpaulhanoi.com", "Apollo":"taeyou.kim@stpaulhanoi.com", "Apollo":"seojun.park@stpaulhanoi.com", "Apollo":"donghyun.kim@stpaulhanoi.com", "Apollo":"giyeol.park@stpaulhanoi.com", "Apollo":"haeri.shin@stpaulhanoi.com", "Apollo":"chaehwan.lim@stpaulhanoi.com", "Apollo":"tueanh.pham@stpaulhanoi.com", "Apollo":"minji.lee@stpaulhanoi.com", "Apollo":"jeong.hayul@stpaulhanoi.com", "Apollo":"viethung.nguyen@stpaulhanoi.com", "Apollo":"giatue.le@stpaulhanoi.com", "Apollo":"oliver.marantos@stpaulhanoi.com", "Apollo":"jinyoung.choi@stpaulhanoi.com", "Apollo":"yunji.lee@stpaulhanoi.com", "Apollo":"yeju.lee@stpaulhanoi.com", "Apollo":"yejoon.cho@stpaulhanoi.com", "Apollo":"hoyeun.lee@stpaulhanoi.com", "Apollo":"lee.geonho@stpaulhanoi.com", "Apollo":"juyeon.hyun@stpaulhanoi.com", "Apollo":"minhtri.tran@stpaulhanoi.com", "Apollo":"haanh.nguyen@stpaulhanoi.com", "Apollo":"hienphuong.nguyen@stpaulhanoi.com", "Apollo":"seokhyeon.son@stpaulhanoi.com", "Apollo":"mingyun.kim@stpaulhanoi.com", "Apollo":"minjae.kim@stpaulhanoi.com", "Apollo":"nguyen.khaiminh@stpaulhanoi.com", "Apollo":"koun.choi@stpaulhanoi.com", "Apollo":"seoyeong.kim@stpaulhanoi.com", "Apollo":"sehee.ham@stpaulhanoi.com", "Apollo":"kyuwon.shim@stpaulhanoi.com", "Apollo":"bowei.tseng@stpaulhanoi.com", "Apollo":"jiwon.you@stpaulhanoi.com", "Apollo":"hainam.nguyen@stpaulhanoi.com", "Apollo":"jioh.ryu@stpaulhanoi.com", "Apollo":"mkduong@stpaulhanoi.com", "Apollo":"yejun.kwon@stpaulhanoi.com", "Apollo":"lamgiang.ngo@stpaulhanoi.com", "Apollo":"junseok.park@stpaulhanoi.com", "Apollo":"seolin.yoo@stpaulhanoi.com", "Apollo":"minhthang.nguyen@stpaulhanoi.com", "Apollo":"shnguyen@stpaulhanoi.com", "Apollo":"tueanh.vu@stpaulhanoi.com", "Apollo":"park.daun@stpaulhanoi.com", "Apollo":"duyanh.nguyen@stpaulhanoi.com", "Apollo":"duha.lee@stpaulhanoi.com", "Apollo":"minhkhue.doan@stpaulhanoi.com", "Apollo":"sookyung.moon@stpaulhanoi.com", "Apollo":"minjeong.jeon@stpaulhanoi.com", "Apollo":"hoanglinhdan.phan@stpaulhanoi.com", "Apollo":"subeen.woo@stpaulhanoi.com", "Apollo":"aeun.cho@stpaulhanoi.com", "Apollo":"shannon.mccartha@stpaulhanoi.com", "Apollo":"steven.jenkins@stpaulhanoi.com", "Apollo":"lorraine.purzycki@stpaulhanoi.com", "Apollo":"stacey.perez@stpaulhanoi.com", "Apollo":"carly.kessler@stpaulhanoi.com", "Apollo":"patricia.bravo@stpaulhanoi.com", "Apollo":"brian.murray@stpaulhanoi.com", "Apollo":"scott.cooper@stpaulhanoi.com", "Apollo":"cody.showalter@stpaulhanoi.com", "Apollo":"lauren.thomson@stpaulhanoi.com", "Apollo":"tony.nguyen@stpaulhanoi.com","Athena":"nhatanh.nguyen@stpaulhanoi.com", "Athena":"junseo.yang@stpaulhanoi.com", "Athena":"nathan.huh@stpaulhanoi.com", "Athena":"hyunmin.lee@stpaulhanoi.com", "Athena":"ducminh.bui@stpaulhanoi.com", "Athena":"khanhngoc.phi@stpaulhanoi.com", "Athena":"riyu.han@stpaulhanoi.com", "Athena":"yupin.kim@stpaulhanoi.com", "Athena":"xuananh.hoang@stpaulhanoi.com", "Athena":"sihoo.park@stpaulhanoi.com", "Athena":"jyule.jang@stpaulhanoi.com", "Athena":"xuankhanh.nguyen@stpaulhanoi.com", "Athena":"minwoong.choi@stpaulhanoi.com", "Athena":"huiji.hwang@stpaulhanoi.com", "Athena":"juhee.park@stpaulhanoi.com", "Athena":"eunjun.choi@stpaulhanoi.com", "Athena":"yoonho.jung@stpaulhanoi.com", "Athena":"sea.jang@stpaulhanoi.com", "Athena":"hyeonjoon.cho@stpaulhanoi.com", "Athena":"haeun.shin@stpaulhanoi.com", "Athena":"yena.shin@stpaulhanoi.com", "Athena":"duyducdung.khuat@stpaulhanoi.com", "Athena":"jueun.lim@stpaulhanoi.com", "Athena":"yeonsu.kim@stpaulhanoi.com", "Athena":"nayeon.lee@stpaulhanoi.com", "Athena":"yoonseo.an@stpaulhanoi.com", "Athena":"thachphong.nguyen@stpaulhanoi.com", "Athena":"seunghyun.kim@stpaulhanoi.com", "Athena":"trinhnamanh.pham@stpaulhanoi.com", "Athena":"ain.kim.28@stpaulhanoi.com", "Athena":"choi.sua.28@stpaulhanoi.com", "Athena":"minhyuk.oh@stpaulhanoi.com", "Athena":"hoangkhoi.le@stpaulhanoi.com", "Athena":"truongan.le@stpaulhanoi.com", "Athena":"hyunsoo.cho@stpaulhanoi.com", "Athena":"yeji.suh@stpaulhanoi.com", "Athena":"hyeongjun.lim@stpaulhanoi.com", "Athena":"hayeon.jung@stpaulhanoi.com", "Athena":"jiwon.kang@stpaulhanoi.com", "Athena":"hyeokju.kwon@stpaulhanoi.com", "Athena":"geonhee.kim@stpaulhanoi.com,", "Athena":"sungyoon.kim@stpaulhanoi.com", "Athena":"woong.kim@stpaulhanoi.com", "Athena":"donggyu.han@stpaulhanoi.com", "Athena":"soyul.jun@stpaulhanoi.com", "Athena":"jinrui.xuan@stpaulhanoi.com", "Athena":"siwoo.choi@stpaulhanoi.com", "Athena":"ahhyeon.kim@stpaulhanoi.com", "Athena":"seungyoo.kim@stpaulhanoi.com", "Athena":"soohyun.lee@stpaulhanoi.com", "Athena":"youbin.bae@stpaulhanoi.com", "Athena":"chaeyeon.shin.26@stpaulhanoi.com", "Athena":"haram.park@stpaulhanoi.com", "Athena":"minseok.yoo@stpaulhanoi.com", "Athena":"eunyeong.choi@stpaulhanoi.com", "Athena":"nguyen.catnhi@stpaulhanoi.com", "Athena":"hangyeol.kim@stpaulhanoi.com", "Athena":"jeongyeon.lee@stpaulhanoi.com", "Athena":"minji.park@stpaulhanoi.com", "Athena":"heechan.kwon@stpaulhanoi.com", "Athena":"namkhanh.nguyen@stpaulhanoi.com", "Athena":"dangkhoi.nguyen@stpaulhanoi.com", "Athena":"songyeon.kim@stpaulhanoi.com", "Athena":"quanganh.bui@stpaulhanoi.com", "Athena":"seungtae.kim@stpaulhanoi.com", "Athena":"anhnhatquang.pham@stpaulhanoi.com", "Athena":"haan.pham@stpaulhanoi.com", "Athena":"yeonjoo.cho@stpaulhanoi.com", "Athena":"fangyu.liu@stpaulhanoi.com", 
                "Athena":"seungmin.ji@stpaulhanoi.com", "Athena":"juhyeok.kim@stpaulhanoi.com", "Athena":"ain.kim.25@stpaulhanoi.com", "Athena":"catthy.hoang@stpaulhanoi.com", "Athena":"jeongrak.song@stpaulhanoi.com", "Athena":"junheum.jee@stpaulhanoi.com", "Athena":"vinhdd.nguyen@stpaulhanoi.com", "Athena":"seobin.lim@stpaulhanoi.com", "Athena":"yejun.kwon@stpaulhanoi.com", "Athena":"vuongle@stpaulhanoi.com", "Athena":"jiwoo1.lee@stpaulhanoi.com", "Athena":"jinsung.yang@stpaulhanoi.com", "Athena":"baodiep.phung@stpaulhanoi.com", "Athena":"k.minhhoitran@stpaulhanoi.com", "Athena":"linh.bach@stpaulhanoi.com", "Athena":"bomi.lee@stpaulhanoi.com", "Athena":"tansang.do@stpaulhanoi.com", "Athena":"eunho.lee@stpaulhanoi.com", "Athena":"gyujoon.kim@stpaulhanoi.com", "Athena":"nayeong.koh@stpaulhanoi.com", "Athena":"jungho.hwang@stpaulhanoi.com", "Athena":"ahyoung.kim@stpaulhanoi.com", "Athena":"vu.baolinh@stpaulhanoi.com", "Athena":"sharmila.majumdar@stpaulhanoi.com", "Athena":"sean.costello@stpaulhanoi.com", "Athena":"laroi.williams@stpaulhanoi.com", "Athena":"kevin.saxton@stpaulhanoi.com", "Athena":"alex.maldonado@stpaulhanoi.com", "Athena":"stephanie.shiers@stpaulhanoi.com", "Athena":"larissa.davignon@stpaulhanoi.com", "Athena":"patrick.doverspike@stpaulhanoi.com", "Athena":"josh.langenbach@stpaulhanoi.com", "Athena":"lindsay.vaughan@stpaulhanoi.com", "Athena":"russell.kay@stpaulhanoi.com"
            }
            house_name = house_name_dict.get(email)
            if house_name:
                house = House.objects.get(name=house_name)
                click_count = ClickCount.objects.get(house=house)
                click_count.click_count += 1
                click_count.save()
        except House.DoesNotExist:

            pass
        except ClickCount.DoesNotExist:

            pass
def get_click_count(request, username):
    user = User.objects.get(username=username)
    click_count_obj, created = ClickCount.objects.get_or_create(user=user)
    click_count = click_count_obj.click_count
    return render(request, 'mypage/kr/click_count.html', {'click_count': click_count})
@login_required
def update_click_count(request, username):
    if request.method == 'POST':
        user = request.user
        click_count_obj, created = ClickCount.objects.get_or_create(user=user)
        click_count_obj.click_count += 1
        click_count_obj.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})
@login_required
def mainpage(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return redirect('user_view')
    users = User.objects.get(username=username)
    article_list = Article.objects.filter(user=users)
    
    context = {
        'user': user,
        'username' : username,
        'candy' : len(article_list)
    }
    return render(request, 'mypage/kr/mainpage.html', context)

@login_required
def mypage_eg(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return redirect('user_view')

    context = {
        'user': user,
        'username' : username,
    }
    return render(request, 'mypage/eg/mainpage_eg.html', context)
@login_required
def inside_pumpkin_eg(request, username,page_num):
    user = request.user
    users = User.objects.get(username=username)
    article_list = Article.objects.filter(user=users)
    articles_per_page = 4
    start_index = (page_num - 1) * articles_per_page
    end_index = start_index + articles_per_page
    paginated_article_list = article_list[start_index:end_index]
    max_pages = (len(article_list) + articles_per_page - 1) // articles_per_page
    max_pages_minus_one = max_pages - 1
    if request.user.username == username:

        
        
        context = {
            'user': user,
            'username': username,
            'article_list': paginated_article_list,
            'max_pages': max_pages,
            'max_pages_minus_one': max_pages_minus_one,
            'range' : range(1,max_pages+1)
        }
        return render(request, 'mypage/eg/inside_pumpkin_eg.html', context)
    else:
        japp_context = {
            'user': user,
            'username': username,
            'article_list': paginated_article_list,
            'max_pages': max_pages,
            'max_pages_minus_one': max_pages_minus_one,
            'range' : range(1,max_pages+1)
        }
        return render(request, 'mypage/eg/inside_pumpkin_notme_eg.html', japp_context)
@login_required
def inside_pumpkin(request, username, page_num):
    user = request.user
    users = User.objects.get(username=username)
    article_list = Article.objects.filter(user=users)
    articles_per_page = 4
    start_index = (page_num - 1) * articles_per_page
    end_index = start_index + articles_per_page
    paginated_article_list = article_list[start_index:end_index]
    max_pages = (len(article_list) + articles_per_page - 1) // articles_per_page
    max_pages_minus_one = max_pages - 1
    if request.user.username == username:

        context = {
            'user': user,
            'username': username,
            'article_list': paginated_article_list,
            'max_pages': max_pages,
            'max_pages_minus_one': max_pages_minus_one,
            'range' : range(1,max_pages+1)
        }
        return render(request, 'mypage/kr/inside_pumpkin.html', context)
    else:
        japp_context = {
            'user': user,
            'username': username,
            'article_list': paginated_article_list,
            'max_pages': max_pages,
            'max_pages_minus_one': max_pages_minus_one,
            'range' : range(1,max_pages+1)
        }
        return render(request, 'mypage/kr/inside_pumpkin_notme.html', japp_context)
@login_required
def write(request, username):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = User.objects.get(username=username)
            article.save()
            user = request.user
            profile = UserProfile.objects.get(user=user)
            language = profile.language
            if language == 'ko':
                return redirect('mypage_kr', username)
            else:
                return redirect('mypage_eg', username)
    else:
        form = Form()
                                                                                                                                                        
    return render(request, 'write.html', {'form': form})

@login_required
def user_list(request, username):
    user = User.objects.get(username=username)
    article_list = Article.objects.filter(user=user)
    return render(request, 'list.html', {'article_list': article_list})

@login_required
def user_view(request, username, num):
    try:
        article = Article.objects.get(id=num, user=User.objects.get(username=username))
        return render(request, 'view.html', {'article': article})
    except Article.DoesNotExist:
        return redirect('user_list', username=username)