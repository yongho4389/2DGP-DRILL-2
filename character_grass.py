from pico2d import * # pico2d에 있는 모듈을 모두 가져옴('*' 키워드로 가능)
# 캔버스의 좌표계는 1사분면에 존재한다.
open_canvas() # 캔버스 열기. 기본 크기는 800x600 (가로 800, 세로 600)
# hide_lattice() # 모눈 숨기기
# show_lattice() # 모눈 보이기

# fill here
# img = load_image('character.png') # 이미지를 불러와 img 변수에 저장
# img.draw_now(400, 300) # 캔버스 400, 300 위치에 img에 담긴 그림 그리기
grass = load_image('grass.png') # 이미지를 불러와 grass 변수에 저장 (이미지 객체)
character = load_image('character.png') # 이미지를 불러와 character 변수에 저장 (이미지 객체)
x = 800 # 캐릭터 초기 위치
while (x > 0):
    # 렌더링 부분 (그림을 표시하는 단계)
    clear_canvas_now() # 캔버스 지우기 (이를 통해 캔버스를 지우고 다시 그려 캐릭터를 새로운 위치로 갱신시킨다. 이를 반복시키면서 마치 캐릭터가 움직이는 것처럼 보이도록 함)
    grass.draw_now(400, 30)
    character.draw_now(x, 90) # 캐릭터의 x에 따른 현위치에 표시
    # 게임 로직 (객체의 상호작용)
    x -= 2 # x 좌표를 2씩 감소시켜 캐릭터가 왼쪽으로 이동하게 함
    delay(0.01) # 0.01초마다 반복
# delay(2) # 2초 대기
close_canvas() # 캔버스 닫기
