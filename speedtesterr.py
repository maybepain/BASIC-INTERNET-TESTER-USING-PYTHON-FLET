import flet as ft
import speedtest
from time import sleep


def main(page: ft.Page):
    page.title="INTERNET SPEED TEST"
    page.theme_mode="dark"
    page.window_color="black"
    page.bgcolor="black"
    page.vertical_alignment="center"
    page.horizontal_alignment = "center"
    page.padding=30
    
    page.fonts={
        "dion" : "/home/shenz/Desktop/indoor map/flet study/assets/dion.otf",
        "glorius" : "/home/shenz/Desktop/indoor map/flet study/assets/the-glorious.otf",
        "perfoma" :"/home/shenz/Desktop/indoor map/flet study/assets/nk57monospacecdrg-bold.otf",
        "tche":"/home/shenz/Desktop/indoor map/flet study/assets/calasans04soliddemo-04solid.otf",
        "tchee":"/home/shenz/Desktop/indoor map/flet study/assets/tcheadlinerprint-bold.otf"
    }
    
    st=speedtest.Speedtest()
    
    apptitle=ft.Row(
        controls=[
            ft.Text(value="INTERNET SPEED",color="#FFFFFF",style="displayLarge"),
            ft.Text(value="TESTER",color="#00FF40",style="displayLarge")
        
        ],alignment="center"
    )
    
    t1=(ft.Text(value="PRESS START ",font_family="tche",size=25))
    t2=(ft.Text(value="",font_family="tche",size=20))
    p1=ft.ProgressBar(width=400,color="#00FF40",bgcolor="white",opacity=0)
    t3=(ft.Text(value="",font_family="tche",size=20))
    t4=(ft.Text(value="",color="#00FF40",font_family="perfoma",size=30))
    t5=(ft.Text(value="",font_family="tche",size=20))
    p2=ft.ProgressBar(width=400,color="#00FF40",bgcolor="white",opacity=0)
    
    t6=(ft.Text(value="",color="#00FF40",font_family="perfoma",size=30))
    t7=(ft.Text(value="",font_family="tche",size=20))
    t8=(ft.Text(value="",font_family="tche",color="red",size=20))
   
    column1=ft.Column(
        controls=[
            t1,
            t2,
            
            t3,
            p1,
            t4,
            t5,
            p2,
            t6,
            t7,
            t8
            
        ]
    ) 
   
    
    containerr=ft.Container(
        content=column1,
        width=200,
        height=50,
        bgcolor="#555753",  
        border_radius=30,
        padding=20,
        animate=ft.Animation(500,"bounceOut")
    )
    
    
    
    def animator(e):
        containerr.width=600
        containerr.height=400
        containerr.colour="#C17D11"
        button1.icon_color="green"
        button1.update()
        
        containerr.update() 
        
        t1.size=20
        t1.value=">>searching for the nearest server, please wait..."
        t1.update()
        
        
        ideal_server=st.get_best_server()
        city=ideal_server["name"]
        country=ideal_server["country"]
        cc=ideal_server["cc"]
        
        t2.value=f">>connection established into {city} , {country} , {cc}"
        t2.update()
        sleep(2)
           
        t3.value=">>everything is fine , checking download speed...."
        t3.update()
        
        p1.opacity=1
        p1.update()
        
        download=st.download()/1024/1024
        t4.value=f">>your download speed is {download:.2f} mbps"
        t4.update()
        
        p1.bgcolor="#00FF40"
        p1.update()
        
        t5.value=">>begin to checking upload speed....."
        t5.update()
        
        p2.opacity=1
        p2.update()
        
        upload=st.upload()/1024/1024
        t6.value=f">>your upload speed is {upload:.2f} mpbs"
        t6.update()
        
        p2.bgcolor="#00FF40"
        p2.update()
        
        t7.value=f"test completed successfully"
        t7.update()
        
        t8.value=f"APP DEVOLEPED BY MAYBEPAIN"
        t8.update()
        
        
        
    button1=ft.IconButton(ft.Icons.PLAY_CIRCLE_FILLED_OUTLINED,icon_color="white",icon_size=50,on_click=animator)
    
    page.add(
        apptitle,
        button1,
        containerr,
        
    )
    
    


ft.app(target=main,assets_dir="/home/shenz/Desktop/indoor map/flet study/assets",view=ft.WEB_BROWSER, port=8550)