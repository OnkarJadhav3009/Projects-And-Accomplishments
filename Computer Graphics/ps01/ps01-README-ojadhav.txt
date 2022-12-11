B581 / Fall 2022, Problem Set 01, Onkar Jadhav, ojadhav

Assets I used for this project:

    Unity version: 
        2020.3.16f
    Scripts (C#): 
        DragObjects.cs - to drag the 2D sprites
        LineUtility.cs - to calculate the closest point on a single line segment and on the line segment of the polygon
        SingleSegmentsPositionLines.cs : to display the line segment and the connecting line using line renderers
        PolygonSegments.cs : to calculate the line segments of the polygon and the connecting line using line renderers
    Scenes:
        ClosestPointInteractive


What did I do?:

    TASK A:
        Created a Line Segment object that hold the identity of the whole task.
        Created 3 empty gameObjects, two for the line segment and one for the subject point, and added a sprite renderer to each of them. These srite renderers are used to give the empty objects a shape. I gave them a knob sprite.
        I added the 2D circle collider to these 3 gameObjects too. These colliders are used to drag the objects using the DragObjects.cs script.
        I added two line renderers. One colored green for the line segment and one red colored for the connecting line. 
        The Line Segment gameobject takes in the SingleSegmentsPositionLines script which has serialized fields that takes in the different components of the task A, i.e. the Start, the end and the subject point, and the line renderers.
        In the given LineUtility script, I had to add the code to get a point on the line segment. I did it using the following steps:

        1. calculate the normal vector using the formula (-(y2 - y1), (x2 - x1)) where P1 is the point on the line and P2 is the subject point
        2. Calculate the vector AC where A is the start of the segment and C is the subject point.
        3. From the above information we can calculate l as the dot product of the vector ac and the normalized vector v which is nothing but direcction vector between start and the end.
        3. From the value of l we can calculate the point P which is start + l x (unit vector v)
        4. We compare the values of P.x with the length of the segment. 
            if l < 0:
                return start
            elif l > length of the segment:
                return end
            else:
                return P

    TASK B:
        The logic is pretty similar to the above task. We have to iterate the above procedure n number of times, where n is the number of points of the polygon.

The things that I am proud of:

    I understood the given code pretty quickly as compared to other courses which give a code to start with. Perhaps its because its easy to visualize what you're coding in Unity.
    I colored the polygon/line points differently as to the subject point.

    