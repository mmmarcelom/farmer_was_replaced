while True:
	if can_harvest():
		harvest()
		if(get_ground_type() != Grounds.Soil):
			till()
		plant(Entities.Carrot)
	if get_pos_y() == get_world_size()-1:
		move(East)
	move(North)