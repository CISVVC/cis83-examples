#!/usr/bin/env python3

import line
import point

'''
6+---+ (1,6) -> (5,6)                                                                    
5|   |                                                                                   
4|   | Left (1,1) -> (1,6)                                                               
3|   | Right (5,1) -> (5,6)                                                              
2|   |                                                                                   
1+---+ (1,1) -> (5,1)                                                                   
012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789
'''
def main():
    rect = [ line.Line(point.Point(1,6),point.Point(6,6)),
             line.Line(point.Point(5,6),point.Point(5,1)),
             line.Line(point.Point(6,1),point.Point(1,1)),
             line.Line(point.Point(1,1),point.Point(1,6))
            ]
    print(rect)
    

if __name__ == '__main__':
    main()

