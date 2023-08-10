from vector import Vector

def get_steps(tile_map,entity,target):
    '''Returns a list of steps to get from the entity to the target entity as a list with the position vector and direction vector
    Parameters:
        tile_map: The tile map the entities are on
        entity: the entity the path is guiding
        target: the entity the entity needs to get to'''
    possible_steps,path_map = path(tile_map,entity,target)
    path_point = target.get_tile_pos()
    steps = [[target.get_tile_pos(),Vector(0,0)]]
    for i in range(len(possible_steps)-1,0,-1):
        for point in possible_steps[i]:
            differencex = abs(path_point[0] - point[0])
            differencey = abs(path_point[1] - point[1])
            if differencex + differencey == 1:
                steps.insert(0,[Vector(tuple=point), Vector(tuple=path_point) - Vector(tuple=point)])
                path_point = Vector(tuple=point)
                break
    return steps



def get_next_step(tile_map,entity,target):
    '''Returns a vector which is the next step for the entity to get to its target.
    Parameters:
        tile_map: The tile map the entities are on
        entity: the entity the path is guiding
        target: the entity the entity needs to get to'''
    steps = get_steps(tile_map,entity,target)
    if len(steps) > 0:
        return (steps[0][0] - entity.get_tile_pos()) * Vector(tile_map.tile_size,tile_map.tile_size)
    else:
        return Vector(0,0)

def display_path_map(tile_map,entity,target):
    '''Prints out a representation of the path that the entity can take to get to the target.
    Parameters:
        tile_map: The tile map the entities are on
        entity: the entity the path is guiding
        target: the entity the entity needs to get to'''
    possible_steps,path_map = path(tile_map,entity,target)
    rows = []
    for i in range(tile_map.rows):
        row = []
        for column in path_map:
            row.append(column[i])
        rows.append(row)
    for row in rows:
        for item in row:
            if item >= 0:
                print(" " + str(item),end='|')
            else:
                print(item,end='|')
        print()
    print()


def path(tile_map,entity,target):
    '''INNER FUNCTION: Calculates all paths up until it finds the target. Returns that raw data and a path map 
    Parameters:
        tile_map: The tile map the entities are on
        entity: the entity the path is guiding
        target: the entity the entity needs to get to'''
    target_pos = target.get_tile_pos().tuple()
    start_x,start_y = entity.get_tile_pos().tuple()
    steps = [[(start_x,start_y)]]
    path_map =  [[-1 for _ in range(tile_map.rows)] for _ in range(tile_map.columns)]
    path_map[start_x][start_y] = 0
    step = 0
    while True:
        if target_pos in steps[step]:
            return steps,path_map
        steps.append([])
        found = False
        for x,y in steps[step]:
            options = [(-1,0),(1,0),(0,-1),(0,1)]                
            for option in options:
                new_x,new_y = x+option[0],y+option[1]
                if new_x < 0 or new_x >= tile_map.columns or new_y < 0 or new_y >= tile_map.rows:
                    continue
                elif tile_map.tiles[new_x][new_y].material.collides:
                    path_map[new_x][new_y] = -5
                    continue
                elif path_map[new_x][new_y] != -1:
                    continue
                else:
                    steps[step+1].append((new_x,new_y))
                    path_map[new_x][new_y] = step+1
                    found = True
        # If there is no moves past a point, give up
        if not found:
            return steps,path_map
        
        step += 1

def test_path(tile_map,entity,target):
    display_path_map(tile_map,entity,target)
    steps = get_steps(tile_map,entity,target)
    for step in steps:
        print(step[0],step[1])