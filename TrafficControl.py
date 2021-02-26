


'''
    Traffic Control


    +--------------+      1     +-------------------+
    |    timetable |    ---->   |  drive_schematic  |
    +--------------+            +-------------------+
            ^                    | 3             ^ 
             \                   v               |2
              \        +---------+    4      +------------+
               \       |  trains | <-------  | dispatcher |
                \      +---------+           +------------+
                 \         ^     ^               ^  
                  \        |7        \\6         |5
                   \       |            \\       |
                    v      v                v    v
    +---------+    +-------------------+   +----------+
    | signals | <--|  traffic control  |   | switches |
    +---------+    +-------------------+   +----------+
                            ^              ^   
                            |           //
                            v          v
                    +-------------------+
                    |     blocks        |
                    +-------------------+
                            ^
                            |
                            v
                    +-------------------+
                    |      queue        |
                    +-------------------+

    1.  A drive-instruction is copied to the drive-schematic with a property that it is originated from the time-table
    2.  The dispatcher (human controlled) sends a copy of a drive-instruction to drive-schematic with a property that it
        is originated from the dispatcher
    3.  The drive-instruction is presented to the train.
    4.  The dispatcher can directly operate a train when the train has no drive-instruction, or canceling a drive-instruction
    5.  The dispachter (human controlled) can operate not locked switches.
    6.  Trains do not operate the switches
    7.  The train operates on its own, requesting blocks at traffic control. Traffic control sets switches and signals and locks them 
        for this train or places the request in the queue when blocks or switches were locked. When the block is free then it signals
        the train that the route is clear. 


    A drive-instruction contains route and times.

    A train that has requested a block and it has been assigned, 'owns' all switches in that block

'''
