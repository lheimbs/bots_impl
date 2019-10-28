#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Coordinates Class """

class Coordinates():
    """ Handle the coordinates of current player position.
        Move the player and display the map """
    def __init__(self, size, fov):
        # use top-left coordinate for view tracking
        self._x = size-fov
        self._y = size-fov

        self._fov = fov
        self._size = size

    def move_north(self):
        """ Move the players x coordinate up one field (-> north).
            If it is out of bounds, put x at the bottom of the field """
        self._x -= 1
        if self._x < 1 - self._fov:
            self._x = self._size - self._fov

    def move_south(self):
        """ Move the players x coordinate down one field (-> south).
            If it is out of bounds, put x at the top of the field """
        self._x += 1
        if self._x > self._size - self._fov:
            self._x = 1-self._fov

    def move_west(self):
        """ Move the players y coordinate to the left (-> west).
            If it is out of bounds, put y at the right side of the field """
        self._y -= 1
        if self._y < 1 - self._fov:
            self._y = self._size - self._fov

    def move_east(self):
        """ Move the players y coordinate to the right (-> east).
            If it is out of bounds, put y at the left side of the field """
        self._y += 1
        if self._y > self._size - self._fov:
            self._y = 1-self._fov

    def set_map(self, view, actual_map):
        """ Print players view on map, based on where he moved."""
        if self.is_out_of_bounds_hori() and self.is_out_of_bounds_vert():
            # Player is out of bound horizontally AND vertically.
            # Split view into 4 rectangles and put them individually into the map.
            slice_map_h_a = slice(0, self._fov + self._x)
            slice_map_h_b = slice(self._size + self._x, self._size)

            slice_map_v_a = slice(0, self._fov + self._y)
            slice_map_v_b = slice(self._size + self._y, self._size)

            slice_view_h_a = slice(self._x*-1, self._fov)
            slice_view_h_b = slice(0, self._x*-1)

            slice_view_v_a = slice(self._y*-1, self._fov)
            slice_view_v_b = slice(0, self._y*-1)

            actual_map[slice_map_h_a, slice_map_v_a] = view[slice_view_h_a, slice_view_v_a]
            actual_map[slice_map_h_a, slice_map_v_b] = view[slice_view_h_a, slice_view_v_b]
            actual_map[slice_map_h_b, slice_map_v_b] = view[slice_view_h_b, slice_view_v_b]
            actual_map[slice_map_h_b, slice_map_v_a] = view[slice_view_h_b, slice_view_v_a]

        elif self.is_out_of_bounds_hori() and not self.is_out_of_bounds_vert():
            # Player is only out of bounds horizontally.
            # Split view in two rectangles and insert both into map.
            slice_map_h_a = slice(0, self._fov + self._x)
            slice_map_h_b = slice(self._size + self._x, self._size)

            slice_map_v_a = slice(self._y, self._fov + self._y)

            slice_view_h_a = slice(self._x*-1, self._fov)
            slice_view_h_b = slice(0, self._x*-1)

            slice_view_v_a = slice(0, self._fov)

            actual_map[slice_map_h_a, slice_map_v_a] = view[slice_view_h_a, slice_view_v_a]
            actual_map[slice_map_h_b, slice_map_v_a] = view[slice_view_h_b, slice_view_v_a]

        elif not self.is_out_of_bounds_hori() and self.is_out_of_bounds_vert():
            # Player is only out of bounds vertically.
            # Split view in two rectangles and insert both into map.
            slice_map_v_a = slice(0, self._fov + self._y)
            slice_map_v_b = slice(self._size + self._y, self._size)

            slice_map_h_a = slice(self._x, self._fov + self._x)

            slice_view_v_a = slice(self._y*-1, self._fov)
            slice_view_v_b = slice(0, self._y*-1)

            slice_view_h_a = slice(0, self._fov)

            actual_map[slice_map_h_a, slice_map_v_a] = view[slice_view_h_a, slice_view_v_a]
            actual_map[slice_map_h_a, slice_map_v_b] = view[slice_view_h_a, slice_view_v_b]
        else:
            # Player is not out of bounds. Insert complete view in map.
            slice_h = slice(self._x, self._x + self._fov)
            slice_v = slice(self._y, self._y + self._fov)
            actual_map[slice_h, slice_v] = view
        return actual_map


    def is_out_of_bounds_hori(self):
        """ view coord has overlap horizontally:
             - top of view in lower map
             - bottom of view in upper map """
        return bool(self._x in range(1-self._fov, 0))

    def is_out_of_bounds_vert(self):
        """ view coord has overlap vertically:
             - right of view in left map
             - left of view in right map """
        return bool(self._y in range(1-self._fov, 0))
