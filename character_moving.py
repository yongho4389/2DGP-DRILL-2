from pico2d import *
import math
open_canvas()
grass = load_image('grass.png')
character = load_image('character.png')


mode = True
# 원 중심 좌표
cx = 400
cy = 320
while True:
    x = 400  # 캐릭터 초기 위치
    y = 90 # 캐릭터 초기 위치
    if mode == True:
        while(x < 780):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            x += 2
            delay(0.001)
        while(y < 560):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            y += 2
            delay(0.001)
        while(x > 20):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            x -= 2
            delay(0.001)
        while(y > 90):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            y -= 2
            delay(0.001)
        while(x < 400):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            x += 2
            delay(0.001)
        mode = False
    else:
        cycle = 1.5 # 2가 360도이므로 1.5는 270도
        for i in range(20):
            radian = cycle * math.pi  # 270도를 라디안 각도로 바꾸어 저장. 2파이가 360도를 나타내는 라디안이기 때문
            clear_canvas_now()
            grass.draw_now(400, 30)
            # cx, cy는 원의 중심 좌표, 220은 반지름
            x = cx + 220 * math.cos(radian)
            y = cy + 220 * math.sin(radian)
            character.draw_now(x, y)
            cycle -= 0.1
            delay(0.1)
        mode = True

close_canvas()