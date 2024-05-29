def solution(keyinput, board):
    answer = [0, 0]
    dic = {'left': -1, 'right': 1, 'up': 1, 'down': -1}

    limit_x = abs(board[0] // 2)  # 최대로 움직일 수 있는 값
    limit_y = abs(board[1] // 2)

    for i in keyinput:
        if i in ['left', 'right']:
            if not (-(limit_x) <= answer[0] + dic[i] <= abs(limit_x)):
                continue

            answer[0] += dic[i]

        else:
            if not (-(limit_y) <= (answer[1] + dic[i]) <= abs(limit_y)):
                continue

            answer[1] += dic[i]

    if abs(answer[0]) > limit_x:
        if answer[0] < 0:
            answer[0] = -(limit_x)
        else:
            answer[0] = limit_x

    elif abs(answer[1]) > limit_y:
        if answer[1] < 0:
            answer[1] = -(limit_y)
        else:
            answer[1] = limit_y
    return answer


"""
another
"""

def solution(keyinput, board):
    x_lim, y_lim = board[0] // 2, board[1]  // 2
    move = {'left':(-1,0),'right':(1,0),'up':(0,1),'down':(0,-1)}
    x, y = 0, 0

    for k in keyinput:
        dx, dy = move[k]
        if abs(x + dx) > x_lim or abs(y + dy) > y_lim:
            continue

        else:
            x, y = x + dx, y + dy

    return [x, y]
