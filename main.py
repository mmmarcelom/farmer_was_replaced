clear()
size = get_world_size() * get_world_size()
direction = North
crop = Entities.Carrot

while True:
	# Necessário adicionar 1 porque o range é não inclusivo
	for i in range(1, size+1):
		if(crop == Entities.Carrot and get_ground_type() != Grounds.Soil):
			till()
			plant(crop)
		# Voltar ao início
		if(i == size):
			while get_pos_x() != 0:
				move(West)
			while get_pos_y() != 0:
				move(South)
			harvest()
			if(crop != Entities.Grass):
				plant(crop)
			
		else:
			if(i % get_world_size() == 0):
				move(East)
				# Inverte a direção
				if(direction == North):
					direction = South
				else:
					direction = North
			else:	
				move(direction)
			harvest()
			if(crop != Entities.Grass):
				plant(crop)