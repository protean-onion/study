# coding: utf-8
def draw_line(line_count):
    print("-" * line_count)
    
def draw_interval(center_count):
    if center_count > 1:
        draw_interval(center_count - 1)
    draw_line(center_count)
    if center_count > 1:
        draw_interval(center_count - 1)
        
