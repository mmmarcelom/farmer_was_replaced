while True:
	if can_harvest():
		harvest()
		plant(Entities.Bush)
	if get_pos_y() == get_world_size()-1:
		move(East)
	move(North)