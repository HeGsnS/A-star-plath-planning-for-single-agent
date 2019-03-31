#!/usr/bin/env python
#__*__ coding: utf-8 __*__

manhattan_dis = lambda x, y: abs(x[0] - y[0]) + abs(x[1] - y[1])

class Astar:

    def __init__(self, tabu_table):
        self.open_list = []
        self.G_dict = dict()
        self.H_dict = dict()
        self.F_dict = dict()
        self.father_point = dict()
        self.close_list = []
        self.tabu_table = tabu_table
        return

    def clear_history(self):
        self.open_list.clear()
        self.G_dict.clear()
        self.H_dict.clear()
        self.F_dict.clear()
        self.father_point.clear()
        self.close_list.clear()
        self.tabu_table.clear()
        return

    def recall_route(self, strt_position, terminal_position):
        route = [terminal_position]
        point_tmp = tuple(terminal_position)
        while point_tmp != tuple(strt_position):
            point_tmp = self.father_point[point_tmp]
            route.insert(0, list(point_tmp))

        return route

    def A_star_search(self, strt_position, terminal_position):
        self.open_list.append(tuple(strt_position))
        self.G_dict[tuple(strt_position)] = 0
        while True:
            choose_point = self.open_list.pop(0) # self.open_list[0]
            self.close_list.append(choose_point)
            if choose_point == tuple(terminal_position):
                return

            x, y = choose_point[0], choose_point[1]
            neighbour = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]

            for unit in neighbour:
                if list(unit) in self.tabu_table or unit in self.close_list:
                    continue
                elif unit[0] > 31 or unit[0] < 0 or unit[1] > 23 or unit[1] < 0:
                    continue
                elif unit in self.open_list:
                    new_G_value = manhattan_dis(unit, choose_point) + self.G_dict[choose_point]
                    if new_G_value < self.G_dict[unit]:
                        self.G_dict[unit] = new_G_value
                        self.F_dict[unit] = new_G_value + self.H_dict[unit]
                        self.father_point[unit] = choose_point
                        self.open_list.remove(unit)
                        self.open_list_insert(unit)
                else:
                    # print(unit, choose_point)
                    G_value = manhattan_dis(unit, choose_point) + self.G_dict[choose_point]
                    H_value = manhattan_dis(unit, terminal_position)
                    F_value = G_value + H_value
                    self.G_dict[unit] = G_value
                    self.H_dict[unit] = H_value
                    self.F_dict[unit] = F_value
                    self.father_point[unit] = choose_point
                    self.open_list_insert(unit)

    def open_list_insert(self, new_unit):
        idx = 0
        for idx in range(len(self.open_list)):
            unit = self.open_list[idx]
            if self.F_dict[new_unit] < self.F_dict[unit]:
                break
        self.open_list.insert(idx, new_unit)








        return
